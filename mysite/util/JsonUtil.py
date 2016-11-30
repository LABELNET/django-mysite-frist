# json 数据包装
def params_data(code=120, msg='', data=[]):
    resp = {
        "code": code,
        "msg": msg,
        "data": data
    }
    return resp
