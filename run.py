from GFWeather import gfweather
import argparse


def run(scheduled = True):
    '''
    主程序入口
    :return:
    '''
    gfweather().run(scheduled = scheduled)


def test_run():
    '''
    运行前的测试
    :return:
    '''
    gfweather().start_today_info(is_test=True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,description=" Everyday wechat with girl friend\n see: https://github.com/weiyx16/EverydayWechat")
    parser.add_argument("-a", "--action", action="store_true", help=" -a test: test information fetching\n -a send: send message without scheduled time\n -a schedule : send message in scheduled time")
    args = parser.parse_args()
    if args.action == r'test':
        test_run()
    elif args.action == r'send':
        run(scheduled=False)
    elif args.action == r'schedule':
        run(scheduled=True)
    else:
        run(scheduled=True)



