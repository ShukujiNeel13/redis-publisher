import redis

R = redis.StrictRedis(decode_responses=True)

CHANNEL = 'shukuji'


def publish_messages_to_channel(channel: str):

    no_of_msgs_to_publish = 100

    print(f'Publishing {100} messages in a loop...')

    for i in range(no_of_msgs_to_publish):
        msg = f'Message: {i}'
        no_of_subscribers_consumed = R.publish(channel, msg)

        if no_of_subscribers_consumed == 0:
            print('No subscribers consumed this message - Missed')
        else:
            print(f'This msg was received by {no_of_subscribers_consumed} subscribers.')


if __name__ == '__main__':
    publish_messages_to_channel(CHANNEL)
