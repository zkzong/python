from http import HTTPStatus

from dashscope import ImageSynthesis

# todo
def simple_call():
    prompt = '雄鹰自由的飞翔在蓝色的天空'
    rsp = ImageSynthesis.call(model=ImageSynthesis.Models.wanx_v1,
                              prompt=prompt,
                              n=4,
                              size='1024*1024')
    print(rsp)
    if rsp.status_code == HTTPStatus.OK:
        print(rsp.output)
        print(rsp.usage)
    else:
        print('Failed, status_code: %s, code: %s, message: %s' %
              (rsp.status_code, rsp.code, rsp.message))
if __name__ == '__main__':
    simple_call()