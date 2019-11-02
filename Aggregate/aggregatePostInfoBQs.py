import numpy as np
import datetime

def aggregate(inputPath1):
    '''
    Aggregates for each BQ {Business Question} in answered by UserInfo Column Family
    :param inputPath1:
    :param inputPath2:
    :return A map with:
            Key = name of column for the BQ as in Cassandra Column Family
            Value = the answer for the BQ:
    '''

    map_solutions_BQs = extract_posts_aggregate_info_from_source(source_path = inputPath1)
    return map_solutions_BQs

def extract_posts_aggregate_info_from_source(source_path):
        unanswered_questions = 0
        total_questions = 0
        answered_questions = 0
        questions_with_answers_count = 0
        answers_count = 0
        all_accepted_answers_ids = {} #{answer_id -> question_timestamp}
        all_accepted_answers_duration = []
        most_viewed_posts = {}
        most_scored_posts = {}
        all_tags = {}

        posts_loc_list = np.load(source_path + 'Posts.npy', allow_pickle=True).tolist()

        # iterate over each post
        for post in posts_loc_list:
            if post['PostTypeId'] and post['PostTypeId'] == '1':
                total_questions += 1
                # if a question doesn't have AcceptedAnswerId, increment unanswered count 
                if not post['AcceptedAnswerId']:
                    unanswered_questions += 1
                else:
                    # if it is answered populate answerid -> questionCreationDate map
                    all_accepted_answers_ids[post['AcceptedAnswerId']] = post['CreationDate']
                if post['AnswerCount']:
                    questions_with_answers_count += 1
                    answers_count += int(post['AnswerCount'])
            # create maps for viewCount, score and tags
            if post['Id'] and post['ViewCount']:
                most_viewed_posts[post['Id']] = int(post['ViewCount'])
            if post['Id'] and post['Score']:
                most_scored_posts[post['Id']] = int(post['Score'])
            if post['Tags']:
                post_tags = post['Tags'][1:-1].split('><')
                for tag in post_tags:
                    if all_tags.has_key(tag):
                        all_tags[tag] += 1
                    else:
                        all_tags[tag] = 1

        # second iteration to calculate average time to answer a question
        for post in posts_loc_list:
            # if the element is an answer, calculate difference answer creation date - question creation creation date
            if post['Id'] in all_accepted_answers_ids.keys():
                question_date_time = datetime.strptime(all_accepted_answers_ids[post['Id']], '%Y-%m-%dT%H:%M:%S.%f')
                answer_date_time = datetime.strptime(post['CreationDate'], '%Y-%m-%dT%H:%M:%S.%f')
                time_to_answer = answer_date_time - question_date_time
                all_accepted_answers_duration.append(time_to_answer.days)
                del all_accepted_answers_ids[post['Id']]

        # sort the maps to get ids with maximum votes
        sorted_tags = sorted(all_tags.items() ,  key=lambda x: x[1] )
        sorted_tags.reverse()
        trending_tags = [i[0] for i in sorted_tags][0:10]
        trending_tags = ",".join(trending_tags)
        most_scored_posts = sorted(most_scored_posts.items() ,  key=lambda x: x[1] )
        most_scored_posts.reverse()
        most_scored_posts = [i[0] for i in most_scored_posts][0:10]
        most_scored_posts = ",".join(most_scored_posts)
        most_viewed_posts = sorted(most_viewed_posts.items() ,  key=lambda x: x[1] )
        most_viewed_posts.reverse()
        most_viewed_posts = [i[0] for i in most_viewed_posts][0:10]
        most_viewed_posts = ",".join(most_viewed_posts)
        average_answers_count = int(answers_count/questions_with_answers_count)
        # caculate average time to answer
        average_time_to_answer = int(sum(all_accepted_answers_duration)/len(all_accepted_answers_duration))

        del sorted_tags
        del all_accepted_answers_duration
        del all_accepted_answers_ids

        postinfo_map = {}
        postinfo_map['totalQuestions'] = total_questions
        postinfo_map['unansweredQuestions'] = unanswered_questions
        postinfo_map['trendingTags'] = trending_tags.split(',')
        postinfo_map['averageAnswersCount'] = average_answers_count
        postinfo_map['mostViewedPosts'] = list(map(int, most_viewed_posts.split(',')))
        postinfo_map['mostScoredPosts'] = list(map(int, most_scored_posts.split(',')))
        postinfo_map['averageTimeToAnswer'] = average_answers_count

        return postinfo_map