'''
raise 예외('에러메시지')
'''


def Multiple():
    try:
        x = int(input('3의 배수를 입력하세요:'))
        if x%3 != 0:
            raise Exception('3의 배수가 아닙니다.')
        print(x)
    except Exception as e:
        print('예외가 발생했습니다.', e)
        raise

try:
    Multiple()
except Exception as e:
    print('스크립트에서 예외 발생했습니다.', e)