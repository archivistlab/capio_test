import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../capio'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))


from capio import extract_time_transcript, write_to_file, convert_time_format, \
    get_time_and_transcript, read_transcript_data, make_tid_url, make_headers
from capio_web_config import API_KEY, BASE_URL, web_config
import unittest
import requests

class TestCapio(unittest.TestCase):
    def setUp(self):
        filename = 'test_download'
        f = open(filename)
        lines = f.readlines()
        self.transcript_data = lines[0]
        f.close()

    def test_check_api(self):
        tid = '591a61ff1452a00012013deb'
        tid_url = make_tid_url(tid,web_config)
        headers = make_headers(web_config)

        http_reply = requests.get(tid_url, headers=headers)

        self.assertEqual(http_reply.status_code, 200)


    def test_get_time_and_transcript(self):
        tdata1 = [('result', [[('alternative', [[('confidence', 1), ('transcript', 'well i have two children how about you'), ('words', [[('confidence', 1), ('from', 0.26999998092651367), ('to', 0.8700000047683716), ('word', 'well')], [('confidence', 1), ('from', 0.8999999761581421), ('to', 1.1100000143051147), ('word', 'i')], [('confidence', 1), ('from', 1.1100000143051147), ('to', 1.350000023841858), ('word', 'have')], [('confidence', 0.987975537776947), ('from', 1.350000023841858), ('to', 1.559999942779541), ('word', 'two')], [('confidence', 1), ('from', 1.559999942779541), ('to', 2.129999876022339), ('word', 'children')], [('confidence', 1), ('from', 2.1599998474121094), ('to', 2.309999942779541), ('word', 'how')], [('confidence', 0.8564475774765015), ('from', 2.309999942779541), ('to', 2.5799999237060547), ('word', 'about')], [('confidence', 1), ('from', 2.5799999237060547), ('to', 2.9099998474121094), ('word', 'you')]])]]), ('final', True)]]), ('result_index', 0)]
        tdata2 = [('result', [[('alternative', [[('confidence', 1), ('transcript', "i don't either my wife gets to stay home and uh i think it's a good thing so she gets to spend well most of the day you know there's all those things that come up but"), ('words', [[('confidence', 1), ('from', 26.630001068115234), ('to', 26.720001220703125), ('word', 'i')], [('confidence', 1), ('from', 26.720001220703125), ('to', 26.900001525878906), ('word', "don't")], [('confidence', 1), ('from', 26.900001525878906), ('to', 27.260000228881836), ('word', 'either')], [('confidence', 1), ('from', 27.31999969482422), ('to', 27.5), ('word', 'my')], [('confidence', 1), ('from', 27.5), ('to', 27.770000457763672), ('word', 'wife')], [('confidence', 1), ('from', 27.80000114440918), ('to', 28.040000915527344), ('word', 'gets')], [('confidence', 1), ('from', 28.040000915527344), ('to', 28.130001068115234), ('word', 'to')], [('confidence', 1), ('from', 28.130001068115234), ('to', 28.34000015258789), ('word', 'stay')], [('confidence', 1), ('from', 28.34000015258789), ('to', 28.64000129699707), ('word', 'home')], [('confidence', 1), ('from', 28.81999969482422), ('to', 29.30000114440918), ('word', 'and')], [('confidence', 1), ('from', 29.30000114440918), ('to', 29.510000228881836), ('word', 'uh')], [('confidence', 1), ('from', 29.56999969482422), ('to', 29.65999984741211), ('word', 'i')], [('confidence', 1), ('from', 29.65999984741211), ('to', 29.8700008392334), ('word', 'think')], [('confidence', 1), ('from', 29.8700008392334), ('to', 29.989999771118164), ('word', "it's")], [('confidence', 1), ('from', 29.989999771118164), ('to', 30.05000114440918), ('word', 'a')], [('confidence', 1), ('from', 30.05000114440918), ('to', 30.260000228881836), ('word', 'good')], [('confidence', 1), ('from', 30.290000915527344), ('to', 30.6200008392334), ('word', 'thing')], [('confidence', 1), ('from', 30.650001525878906), ('to', 31.06999969482422), ('word', 'so')], [('confidence', 1), ('from', 32.029998779296875), ('to', 32.2400016784668), ('word', 'she')], [('confidence', 1), ('from', 32.2400016784668), ('to', 32.45000076293945), ('word', 'gets')], [('confidence', 1), ('from', 32.45000076293945), ('to', 32.56999969482422), ('word', 'to')], [('confidence', 1), ('from', 32.56999969482422), ('to', 33.31999969482422), ('word', 'spend')], [('confidence', 1), ('from', 33.97999954223633), ('to', 34.4900016784668), ('word', 'well')], [('confidence', 1), ('from', 34.94000244140625), ('to', 35.2400016784668), ('word', 'most')], [('confidence', 1), ('from', 35.2400016784668), ('to', 35.29999923706055), ('word', 'of')], [('confidence', 1), ('from', 35.29999923706055), ('to', 35.36000061035156), ('word', 'the')], [('confidence', 1), ('from', 35.36000061035156), ('to', 35.65999984741211), ('word', 'day')], [('confidence', 1), ('from', 35.69000244140625), ('to', 35.75), ('word', 'you')], [('confidence', 1), ('from', 35.75), ('to', 35.84000015258789), ('word', 'know')], [('confidence', 1), ('from', 35.84000015258789), ('to', 36.04999923706055), ('word', "there's")], [('confidence', 0.7285801768302917), ('from', 36.07185745239258), ('to', 36.18114471435547), ('word', 'all')], [('confidence', 0.45726966857910156), ('from', 36.18928909301758), ('to', 36.34619140625), ('word', 'those')], [('confidence', 1), ('from', 36.349998474121094), ('to', 36.560001373291016), ('word', 'things')], [('confidence', 1), ('from', 36.560001373291016), ('to', 36.68000030517578), ('word', 'that')], [('confidence', 1), ('from', 36.68000030517578), ('to', 36.88999938964844), ('word', 'come')], [('confidence', 1), ('from', 36.88999938964844), ('to', 37.099998474121094), ('word', 'up')], [('confidence', 1), ('from', 37.130001068115234), ('to', 37.34000015258789), ('word', 'but')]])]]), ('final', True)]]), ('result_index', 3)]
        test_data = [(tdata1, "well i have two children how about you"),
                     (tdata2,"i don't either my wife gets to stay home and uh i think it's a good thing so she gets to spend well most of the day you know there's all those things that come up but"),]
        #data_list = read_transcript_data(self.transcript_data)
        for one_data in test_data:
            raw_data = one_data[0]
            print(raw_data)
            timestamp, transcript = get_time_and_transcript(raw_data)
            self.assertEqual(transcript, one_data[1])

            #print(convert_time_format(timestamp), transcript)


    def test_convert_time_format(self):
        test_data = [( '124.9000015258789', '00:02:04.90'),
                     ('0.05999999865889549', '00:00:00.06'),
                     ('3.9600000381469727' , '00:00:03.96')]

        for one_data in test_data:
            self.assertEqual(one_data[1], convert_time_format(one_data[0]))


if __name__ == '__main__':
    unittest.main()




