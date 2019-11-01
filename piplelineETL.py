from ExtractAndFilter import extractAndFilter as EAF
from ValidateAndClean import validateAndClean as VAC
from Aggregate import aggregateUserInfoBQs as AGG_USR_INFO
from InsertColumnFamilyIntoCassandra import insertUserInfoCF as INSRT_USR_INFO
from CreateColumnFamily import createUserInfoCF as USR_INFO_CF
import os
import subprocess

def runETLPipeline(domain):
    '''

    Runs the ETL Pipeline -
        1) Transforming acquired data (archived) into unarchived XML files for every domain
        2) Filter out the XML files needed for every domain
        3) Extract necessary fields and filter out corrupt rows
        4) Validate required fields and clean duplicate data if any
        5) Aggregate values according to the business Question
        6) Insert/Dump the data into respective column family for efficient query of Business Questions

    :param domain:
    :return:
    '''

    domainName = domain.split(".")[0]

    # 1) Unarchive the source data
    unarchive_script = '/Users/avneet/Documents/Fall-19/unarchive7z.sh'
    subprocess.call([unarchive_script])

    # 2) Filter out the needed XML files
    filter_script = '/Users/avneet/Documents/Fall-19/filterXML.sh'
    subprocess.call([filter_script])

    # 3) Extract And Filter Stage
    inputPath = '/Users/avneet/Documents/Fall-19/SE_FilterXML/' + domainName + '.stackexchange.com/'
    outputPath = '/Users/avneet/Documents/Fall-19/SE_Extract_Clean/' + domainName + '.stackexchange.com/'
    EAF.extractAndFilter(outputPath, inputPath)

    # 4) Validation And Clean Stage
    inputPath = '/Users/avneet/Documents/Fall-19/SE_Extract_Clean/' + domainName + '.stackexchange.com/'
    outputPath = '/Users/avneet/Documents/Fall-19/SE_Validate_Clean/' + domainName + '.stackexchange.com/'
    #VAC.validateAndClean(outputPath, inputPath)

    # 5) Aggregation
    inputPath1 = '/Users/avneet/Documents/Fall-19/SE_Validate_Clean/' + domainName + '.stackexchange.com/'
    inputPath2 = '/Users/avneet/Documents/Fall-19/SE_FilterXML/' + domainName + '.stackexchange.com/'
    user_info_map = AGG_USR_INFO.aggregate(inputPath1, inputPath2)

    # 6) Insert the column families into Cassandra
    INSRT_USR_INFO.insertInUserInfoCF(domainName, user_info_map)

if __name__ == '__main__':
    directoryPath = '/Users/avneet/Documents/Fall-19/SE_7zFiles/'
    list_of_all_domains = os.listdir(directoryPath)
    if '.DS_Store' in list_of_all_domains:
        list_of_all_domains.remove('.DS_Store')

    #Create Column Familes User_Info And Post_Info if not exists
    USR_INFO_CF.createUserInfoCF()

    #run the ETL pipeline for every domain (around 174 domains in total in Stack Exchange Data Dump
    for domain in list_of_all_domains:
        runETLPipeline(domain)



