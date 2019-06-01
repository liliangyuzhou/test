import dubbo_telnet
def coondoubble_data(Host,Port,interface,method,param):
    try:
        # 初始化dubbo对象
        conn = dubbo_telnet.connect(Host, Port)
        # 设置telnet连接超时时间
        conn.set_connect_timeout(3000)
        # 设置dubbo服务返回响应的编码
        conn.set_encoding('gbk')
        conn.invoke(interface, method, param)
        command = 'invoke %s.%s(%s)'%(interface,method,param)
        return  conn.do(command)
    except:
        return  Exception
if __name__=="__main__":
    Host = '172.17.45.14'  # Doubble服务器IP
    Port = 2181  # Doubble服务端口
    interface = 'com.bestpay.bigdata.actual.api.IDubboQueryApi'  # 接口
    method = 'iDubboQueryApi'  # 方法
    param = '{"pageCount": "20"}'  # 参数
    data=coondoubble_data(Host,Port,interface,method,param)