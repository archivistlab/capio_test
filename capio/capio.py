import argparse
import sys
from json import JSONDecoder
import requests
import docx
import time
import http.server
from capio_web_config import API_KEY, BASE_URL, GOOD_RESPONSE, SYSTEM_ERROR_CODE, web_config
#from http.server.BaseHTTPRequestHandler import responses as response_table

def make_headers(web_config):
    headers = {API_KEY: web_config[API_KEY]}

    return headers


def make_tid_url(tid, web_config):
    tid_url = web_config[BASE_URL] + tid

    return tid_url


def download_transcript_data(tid, web_config):
    """
    :param tid(str): the transaction ID
    :param web_config(dict): web parameters
    :return:
    """
    tid_url = make_tid_url(tid, web_config)
    headers = make_headers()
    response_table = http.server.BaseHTTPRequestHandler.responses

    try:
        http_reply = requests.get(tid_url, headers=headers)
    except Exception as inst:
        print(type(inst))
        print(inst.args)

    if http_reply.status_code != GOOD_RESPONSE:
        print(response_table[http_reply.status_code])
        sys.exit(SYSTEM_ERROR_CODE)

    return http_reply.text


def parse_results(pairs):
    return pairs


def read_transcript_data(transcript_data):
    decoder = JSONDecoder(object_pairs_hook=parse_results)
    data_list = decoder.decode(transcript_data)

    return data_list

#constants for traversing internal structures of the data
FROM = 'from'
DATA_IDX = 1
ALTERNATIVE = 0
FROM_IDX = 1
FROM_DATA_IDX = 1
RESULT_TOP = 0
RESULT_DATA = 1
RESULT_DATA_DICT = 0
DETAIL_DATA_VALUE = 0
DETAIL_DATA_TRANSCRIPTS = 1
DETAIL_DATA_WORDS = 2
DETAIL_WORD = 1
STARTS_WITH = '{"result"'
ENDS_WITH = 'result_index'


def get_time_and_transcript(result):
    """
    :param result(list): a list of transcribed words
                         and time signature for a single transcription.
    :return (tuple): a tuple of starting time and a single
                     complete transcript. Time is the time of the first word.
    """
    result_data = result[RESULT_TOP][RESULT_DATA]
    result_data = result_data[0]
    result_data_detail = result_data[0][1][0]
    transcript = result_data_detail[DETAIL_DATA_TRANSCRIPTS]
    words = result_data_detail[DETAIL_DATA_WORDS][DETAIL_WORD]
    all_time = []
    for word_pair in words:
        if (word_pair[FROM_IDX][0] == 'from'):
            all_time.append(word_pair[FROM_IDX][1])
    #print(all_time[0], transcript[1])
    return (sorted(all_time)[0], transcript[1])


def extract_time_transcript(transcript_data):
    """

    :param transcript_data(list): a list of transcribed data. Each element
                                  consists a complete setence or continuous utterance"
    :return all_time_transcript(list): a list of timestamp(float) and transcribed text
    """
    data_list = read_transcript_data(transcript_data)
    all_time_transcript = []
    for one_data in data_list:
        one_time_transcript = get_time_and_transcript(one_data)
        #print(one_time_transcript)
        all_time_transcript.append(one_time_transcript)

    return all_time_transcript


def print_help():
    help_text = "<COMMAND> --transcription-id <id> --output <filename>"
    print("Usage:: ")
    print(help_text)


# command --transcription-id xxxx --output xxxx.docx
def process_commandline_arg():
    parser = argparse.ArgumentParser(description="timestamp transcription")
    parser.add_argument('-tid', '--transcription-id',
                        type=str, help='transaction id')
    parser.add_argument('-o', '--output', type=str, help='output_filename')

    args = parser.parse_args()
    if not args.transcription_id or not args.output:
        print_help()
        sys.exit(SYSTEM_ERROR_CODE)

    return (args.transcription_id, args.output)


def process_data():
    filename = 'output'
    extract_time_transcript(filename)


def convert_time_format(timestamp):
    """

    :param timestamp(float): seconds and fractions in float
    :return formatted_time(str): seconds translated to %H:%M:%S with milliseconds
                                 appended to seconds up to two decimal
    time.gmtime is used but this should be reevaluated based on requirement changes
    """
    timestamp = float(timestamp)
    before_dec = int(timestamp)
    after_dec = timestamp - int(timestamp)
    after_dec_str = str(round(after_dec, 2))
    if (len(after_dec_str) == 3):
        after_dec_str += '0'
    before_dec_str = time.strftime("%H:%M:%S", time.gmtime(before_dec))

    formated_time = before_dec_str + after_dec_str[1:]
    return formated_time


def write_to_file(just_time_transcript, out_filename):
    document = docx.Document()

    for timestamp, *transcript in just_time_transcript:
        converted_time = convert_time_format(timestamp)
        write_str = '{:20}{}'.format(converted_time, transcript)
        document.add_paragraph(write_str)
    document.save(out_filename)

def main():
    """
    :return:
    """
    (tid, out_filename) = process_commandline_arg()
    transcript_data = download_transcript_data(tid, web_config)
    all_time_transcript = extract_time_transcript(transcript_data)
    write_to_file(all_time_transcript, out_filename)


if __name__ == '__main__':
    main()

