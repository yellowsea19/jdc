from mitmproxy import ctx
import json
# 所有发出的请求数据包都会被这个方法所处理
# 所谓的处理，我们这里只是打印一下一些项；当然可以修改这些项的值直接给这些项赋值即可
def request(flow):

    # 获取请求对象
    request = flow.request
    # 实例化输出类
    info = ctx.log.info
    headers=request.headers
    # info('*************')
    info('---------------------------------')

    if 'web-api' in request.url:
        with open('mit.log','a+',encoding='utf-8') as f :
            f.write(str(request.method)+'    ')
            f.write(str(request.url))
            f.write('\n')
            f.write(str(headers))
            # f.write('\n')
            # f.write(str(headers['Im-Agent']))
            # f.write('\n')
            # f.write(str(headers['Content-Type']))
            f.write('\n')
            # f.write('aaaaaaaa')
            # f.write(str(request.headers))
            # f.close()
        # 打印请求的url
        # info(request.url)
        # info('************************')
        # # 打印请求方法
        # info(request.method)
        # # 打印host头
        # info(request.host)
        # # 打印请求端口
        # info(str(request.port))
        # # 打印所有请求头部
        # info(str(request.headers))
        # # 打印cookie头
        # info(str(request.cookies))

# 所有服务器响应的数据包都会被这个方法处理
# 所谓的处理，我们这里只是打印一下一些项
def response(flow):
    # 获取响应对象
    response = flow.response
    # 实例化输出类
    info = ctx.log.info
    # # 打印响应码
    # info(str(response.status_code))
    info(str(response.text))
    # response.text=str({"id": "6006a702e74b5","action": "feedSquareSlip","code": 0,"message": "操作成功","request_id": "49069577-a948-4679-9171-3588d1a25541","type": "2","payload": {"has_next_page": 1,"data": []}})

    data={"id": "6006a702e174b5","action": "feedSquareSlip","code": 0,"message": "操作成功","request_id": "490619577-a948-4679-9171-3588d1a25541","type": "2","payload": {"has_next_page": 1,"data": []}}
    # data={"id":"6006aa5c9af224","action":"feedSquareSlip","code":0,"message":"\u64cd\u4f5c\u6210\u529f","request_id":"f7e27f26f-f043-4afb-b798-b8fd6053e421","type":"2","payload":{"has_next_page":1,"data":[{"feed_id":2348,"type":1,"content":"mitmdump--test3","extend":[],"longitude":"0.000000000","latitude":"0.000000000","position":"","address":"","city":"","comment_count":1,"favour_count":3,"created_at":"2020-09-16 16:47:40","is_top":1,"favoured":1,"user":{"user_id":"576100218","nickname":"\u5ba2\u670d4","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200915\/5f60969914483.jpg","is_dream_guard":44},"comments":[{"reply_id":9637,"feed_id":2348,"content":"\u5174\u6c11","created_at":"2020-09-22 15:01:40","user":{"user_id":"631855499","nickname":"\u80d6\u864e","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200729\/5f20eabebf678.jpg"},"reply_count":0}],"favours":[{"created_at":"2020-11-25 10:39:50","user":{"user_id":"425251791","nickname":"\u5475\u5475","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/user\/avatar\/e3\/fa\/38\/e3fa38576655285a60d4e156cdfdf7fb.png"}},{"created_at":"2020-09-22 11:56:51","user":{"user_id":"383359323","nickname":"\u72d7\u86cb---\u6d4b\u8bd5\u73af\u5883","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/user\/avatar\/04\/b1\/0e\/04b10ec1835a72e85a8764eeb9ce07c2.jpg"}},{"created_at":"2020-09-16 16:47:43","user":{"user_id":"576100218","nickname":"\u5ba2\u670d4","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200915\/5f60969914483.jpg"}}]},{"feed_id":"2345","type":1,"content":"\u6d4b","extend":[],"longitude":"0.000000000","latitude":"0.000000000","position":"","address":"","city":"","comment_count":2,"favour_count":1,"created_at":"2020-09-16 10:31:51","is_top":0,"favoured":0,"user":{"user_id":"296913292","nickname":"Hao","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/user\/avatar\/78\/ae\/49\/78ae49e12297103e2e5453b5a1647d4c.png","is_dream_guard":27},"comments":[{"reply_id":9650,"feed_id":2345,"content":"momo","created_at":"2020-09-24 14:07:37","user":{"user_id":"169257242","nickname":"\u9e21\u817f","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200730\/5f22810f4f7c3.jpg"},"reply_count":0},{"reply_id":9649,"feed_id":2345,"content":"\u554a\u554a\u554a","created_at":"2020-09-23 18:17:47","user":{"user_id":"433554354","nickname":"\u6d4b\u8bd5\u73af\u5883:\u5566\u5566\u5566\u5566\u5566\u5566","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/user\/avatar\/63\/f6\/51\/63f651708ac56db4fc220f32bf19c6ea.png"},"reply_count":0}],"favours":[{"created_at":"2020-11-25 10:39:53","user":{"user_id":"425251791","nickname":"\u5475\u5475","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/user\/avatar\/e3\/fa\/38\/e3fa38576655285a60d4e156cdfdf7fb.png"}}]},{"feed_id":"2346","type":1,"content":"\u5154\u5154\u5c31","extend":[],"longitude":"0.000000000","latitude":"0.000000000","position":"","address":"","city":"","comment_count":0,"favour_count":0,"created_at":"2020-09-16 10:42:20","is_top":0,"favoured":0,"user":{"user_id":"296913292","nickname":"Hao","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/user\/avatar\/78\/ae\/49\/78ae49e12297103e2e5453b5a1647d4c.png","is_dream_guard":27},"comments":[],"favours":[]},{"feed_id":"2352","type":2,"content":"\u9686\u57fa","extend":["{\"url\":\"http:\\\/\\\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\\\/chat\\\/user\\\/20200922\\\/token1\\\/gif\\\/5a\\\/8d\\\/f2\\\/5a8df2dbe090ff549e2afbc45dba7859.png\",\"img_width\":\"255\",\"img_height\":\"255\"}"],"longitude":"0.000000000","latitude":"0.000000000","position":"","address":"","city":"","comment_count":1,"favour_count":1,"created_at":"2020-08-01 16:12:05","is_top":0,"favoured":0,"user":{"user_id":"token1","nickname":"zr0yuyjt\u72d7\u5269kk\u2299\u03c9\u2299","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200623\/5ef1aa7dcda52.jpg","is_dream_guard":9999},"comments":[{"reply_id":9647,"feed_id":2352,"content":"\u54e6","created_at":"2020-09-22 18:15:33","user":{"user_id":"425251791","nickname":"\u5475\u5475","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/user\/avatar\/e3\/fa\/38\/e3fa38576655285a60d4e156cdfdf7fb.png"},"reply_count":0}],"favours":[{"created_at":"2020-09-22 18:15:26","user":{"user_id":"425251791","nickname":"\u5475\u5475","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/user\/avatar\/e3\/fa\/38\/e3fa38576655285a60d4e156cdfdf7fb.png"}}]},{"feed_id":"2351","type":2,"content":"\u7ecf\u7406","extend":["{\"url\":\"http:\\\/\\\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\\\/chat\\\/user\\\/20200922\\\/token1\\\/gif\\\/b9\\\/bf\\\/07\\\/b9bf0785d0980392fcd5efa076c1bffd.png\",\"img_width\":\"234\",\"img_height\":\"278\"}"],"longitude":"0.000000000","latitude":"0.000000000","position":"","address":"","city":"","comment_count":0,"favour_count":1,"created_at":"2020-08-01 16:01:26","is_top":0,"favoured":0,"user":{"user_id":"token1","nickname":"zr0yuyjt\u72d7\u5269kk\u2299\u03c9\u2299","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200623\/5ef1aa7dcda52.jpg","is_dream_guard":9999},"comments":[],"favours":[{"created_at":"2020-09-22 16:14:26","user":{"user_id":"token1","nickname":"zr0yuyjt\u72d7\u5269kk\u2299\u03c9\u2299","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200623\/5ef1aa7dcda52.jpg"}}]},{"type":7},{"feed_id":"2350","type":2,"content":"\u54af\u5973hi","extend":["{\"url\":\"http:\\\/\\\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\\\/chat\\\/user\\\/20200922\\\/token1\\\/gif\\\/2f\\\/cb\\\/97\\\/2fcb97dbee9c2dd31c9de07294d99fb6.png\",\"img_width\":\"258\",\"img_height\":\"253\"}"],"longitude":"0.000000000","latitude":"0.000000000","position":"","address":"","city":"","comment_count":0,"favour_count":2,"created_at":"2020-08-01 15:26:00","is_top":0,"favoured":1,"user":{"user_id":"token1","nickname":"zr0yuyjt\u72d7\u5269kk\u2299\u03c9\u2299","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200623\/5ef1aa7dcda52.jpg","is_dream_guard":9999},"comments":[],"favours":[{"created_at":"2020-09-22 15:47:04","user":{"user_id":"383359323","nickname":"\u72d7\u86cb---\u6d4b\u8bd5\u73af\u5883","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/user\/avatar\/04\/b1\/0e\/04b10ec1835a72e85a8764eeb9ce07c2.jpg"}},{"created_at":"2020-09-22 15:26:02","user":{"user_id":"token1","nickname":"zr0yuyjt\u72d7\u5269kk\u2299\u03c9\u2299","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200623\/5ef1aa7dcda52.jpg"}}]},{"feed_id":"2349","type":2,"content":"\u660e\u660e\u4e70","extend":["{\"url\":\"http:\\\/\\\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\\\/chat\\\/user\\\/20200922\\\/token1\\\/gif\\\/ad\\\/f4\\\/2a\\\/adf42a8198db17286e48146fdb183422.png\",\"img_width\":\"255\",\"img_height\":\"255\"}"],"longitude":"0.000000000","latitude":"0.000000000","position":"","address":"","city":"","comment_count":7,"favour_count":2,"created_at":"2020-07-15 14:43:23","is_top":0,"favoured":0,"user":{"user_id":"token1","nickname":"zr0yuyjt\u72d7\u5269kk\u2299\u03c9\u2299","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200623\/5ef1aa7dcda52.jpg","is_dream_guard":9999},"comments":[{"reply_id":9645,"feed_id":2349,"content":"123456","created_at":"2020-09-22 15:05:30","user":{"user_id":"631855499","nickname":"\u80d6\u864e","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200729\/5f20eabebf678.jpg"},"reply_count":0},{"reply_id":9644,"feed_id":2349,"content":"12345","created_at":"2020-09-22 15:04:58","user":{"user_id":"631855499","nickname":"\u80d6\u864e","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200729\/5f20eabebf678.jpg"},"reply_count":0},{"reply_id":9643,"feed_id":2349,"content":"\u554a\u554a\u554a","created_at":"2020-09-22 15:04:47","user":{"user_id":"631855499","nickname":"\u80d6\u864e","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200729\/5f20eabebf678.jpg"},"reply_count":0}],"favours":[{"created_at":"2020-09-22 14:48:47","user":{"user_id":"631855499","nickname":"\u80d6\u864e","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200729\/5f20eabebf678.jpg"}},{"created_at":"2020-09-22 14:43:24","user":{"user_id":"token1","nickname":"zr0yuyjt\u72d7\u5269kk\u2299\u03c9\u2299","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200623\/5ef1aa7dcda52.jpg"}}]},{"feed_id":"2313","type":1,"content":"dgdhdbd","extend":[],"longitude":"0.000000000","latitude":"0.000000000","position":"","address":"","city":"","comment_count":10,"favour_count":3,"created_at":"2020-08-18 17:44:43","is_top":0,"favoured":1,"user":{"user_id":"576100218","nickname":"\u5ba2\u670d4","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200915\/5f60969914483.jpg","is_dream_guard":44},"comments":[{"reply_id":9636,"feed_id":2313,"content":"\u660e\u654f","created_at":"2020-09-22 15:01:33","user":{"user_id":"631855499","nickname":"\u80d6\u864e","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200729\/5f20eabebf678.jpg"},"reply_count":0},{"reply_id":9623,"feed_id":2313,"content":"\u6539\u6210","created_at":"2020-08-18 17:54:37","user":{"user_id":"token1","nickname":"zr0yuyjt\u72d7\u5269kk\u2299\u03c9\u2299","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200623\/5ef1aa7dcda52.jpg"},"reply_count":0},{"reply_id":9622,"feed_id":2313,"content":"\u54c8\u54c8","created_at":"2020-08-18 17:54:32","user":{"user_id":"token1","nickname":"zr0yuyjt\u72d7\u5269kk\u2299\u03c9\u2299","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200623\/5ef1aa7dcda52.jpg"},"reply_count":0}],"favours":[{"created_at":"2020-09-22 11:56:44","user":{"user_id":"383359323","nickname":"\u72d7\u86cb---\u6d4b\u8bd5\u73af\u5883","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/user\/avatar\/04\/b1\/0e\/04b10ec1835a72e85a8764eeb9ce07c2.jpg"}},{"created_at":"2020-09-16 16:47:44","user":{"user_id":"576100218","nickname":"\u5ba2\u670d4","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200915\/5f60969914483.jpg"}},{"created_at":"2020-08-18 17:44:55","user":{"user_id":"token1","nickname":"zr0yuyjt\u72d7\u5269kk\u2299\u03c9\u2299","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200623\/5ef1aa7dcda52.jpg"}}]},{"feed_id":"2342","type":1,"content":"\u4eca","extend":[],"longitude":"0.000000000","latitude":"0.000000000","position":"","address":"","city":"","comment_count":1,"favour_count":1,"created_at":"2020-09-16 09:56:42","is_top":0,"favoured":0,"user":{"user_id":"631855499","nickname":"\u80d6\u864e","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200729\/5f20eabebf678.jpg","is_dream_guard":8888},"comments":[{"reply_id":9638,"feed_id":2342,"content":"\u660e\u654f","created_at":"2020-09-22 15:02:35","user":{"user_id":"631855499","nickname":"\u80d6\u864e","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200729\/5f20eabebf678.jpg"},"reply_count":0}],"favours":[{"created_at":"2020-09-16 09:59:08","user":{"user_id":"631855499","nickname":"\u80d6\u864e","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200729\/5f20eabebf678.jpg"}}]},{"feed_id":"2343","type":1,"content":"\u4e86","extend":[],"longitude":"0.000000000","latitude":"0.000000000","position":"","address":"","city":"","comment_count":0,"favour_count":1,"created_at":"2020-09-16 09:56:57","is_top":0,"favoured":0,"user":{"user_id":"631855499","nickname":"\u80d6\u864e","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200729\/5f20eabebf678.jpg","is_dream_guard":8888},"comments":[],"favours":[{"created_at":"2020-09-16 09:59:04","user":{"user_id":"631855499","nickname":"\u80d6\u864e","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200729\/5f20eabebf678.jpg"}}]},{"type":7},{"feed_id":"2340","type":1,"content":"\u94b1\u94b1\u94b1","extend":[],"longitude":"0.000000000","latitude":"0.000000000","position":"","address":"","city":"","comment_count":0,"favour_count":1,"created_at":"2020-09-15 18:42:56","is_top":0,"favoured":0,"user":{"user_id":"257828297","nickname":"gg","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200915\/5f606e42b7d4c.jpg","is_dream_guard":7777},"comments":[],"favours":[{"created_at":"2020-09-16 09:48:10","user":{"user_id":"257828297","nickname":"gg","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200915\/5f606e42b7d4c.jpg"}}]},{"feed_id":"2341","type":1,"content":"\u4f60\u7684","extend":[],"longitude":"0.000000000","latitude":"0.000000000","position":"","address":"","city":"","comment_count":0,"favour_count":1,"created_at":"2020-09-16 09:48:06","is_top":0,"favoured":0,"user":{"user_id":"257828297","nickname":"gg","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200915\/5f606e42b7d4c.jpg","is_dream_guard":7777},"comments":[],"favours":[{"created_at":"2020-09-16 09:48:09","user":{"user_id":"257828297","nickname":"gg","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200915\/5f606e42b7d4c.jpg"}}]},{"feed_id":"2339","type":1,"content":"b\u2006sh\u2006sh","extend":[],"longitude":"0.000000000","latitude":"0.000000000","position":"","address":"","city":"","comment_count":0,"favour_count":1,"created_at":"2020-09-15 18:27:55","is_top":0,"favoured":0,"user":{"user_id":"257828297","nickname":"gg","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200915\/5f606e42b7d4c.jpg","is_dream_guard":7777},"comments":[],"favours":[{"created_at":"2020-09-15 18:33:18","user":{"user_id":"257828297","nickname":"gg","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200915\/5f606e42b7d4c.jpg"}}]},{"feed_id":"2337","type":1,"content":"\u54e6\u54e6\u54e6","extend":[],"longitude":"0.000000000","latitude":"0.000000000","position":"","address":"","city":"","comment_count":1,"favour_count":2,"created_at":"2020-09-15 15:13:42","is_top":0,"favoured":0,"user":{"user_id":"169257242","nickname":"\u9e21\u817f","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200730\/5f22810f4f7c3.jpg","is_dream_guard":31},"comments":[{"reply_id":9634,"feed_id":2337,"content":"\u5443\u5443\u5443\u5443","created_at":"2020-09-15 15:14:04","user":{"user_id":"169257242","nickname":"\u9e21\u817f","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200730\/5f22810f4f7c3.jpg"},"reply_count":0}],"favours":[{"created_at":"2020-09-15 15:41:09","user":{"user_id":"169257242","nickname":"\u9e21\u817f","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200730\/5f22810f4f7c3.jpg"}},{"created_at":"2020-09-15 15:13:53","user":{"user_id":"502060808","nickname":"\u9759\u9999","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/user\/avatar\/d5\/69\/ce\/d569ce4aa4af58a36583005e36ae14db.png"}}]},{"feed_id":"2331","type":3,"content":"","extend":["{\"url\":\"http:\\\/\\\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\\\/user\\\/feed\\\/20200902\\\/4b\\\/be\\\/f3\\\/4bbef3a2fb2ede6267f701eb433a1610.jpg\",\"img_height\":192,\"img_width\":144}"],"longitude":"0.000000000","latitude":"0.000000000","position":"","address":"","city":"","comment_count":0,"favour_count":1,"created_at":"2020-09-02 18:14:14","is_top":0,"favoured":0,"user":{"user_id":"59488791","nickname":"\u76ae\u5361\u4e18\u6d4b\u8bd5\u7ad9","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200731\/5f23ba524cae0.jpg","is_dream_guard":0},"comments":[],"favours":[{"created_at":"2020-09-15 15:12:52","user":{"user_id":"169257242","nickname":"\u9e21\u817f","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200730\/5f22810f4f7c3.jpg"}}]},{"type":7},{"feed_id":"2323","type":1,"content":"111","extend":[],"longitude":"0.000000000","latitude":"0.000000000","position":"","address":"","city":"","comment_count":0,"favour_count":3,"created_at":"2020-08-27 11:34:10","is_top":0,"favoured":0,"user":{"user_id":"36330158","nickname":"%@$","avatar":"http:\/\/im-res-test.oss-cn-shenzhen.aliyuncs.com\/user\/avatar\/cf\/69\/6a\/cf696a9e6bb7ed5d847dfdda5aced283.jpg","is_dream_guard":0},"comments":[],"favours":[{"created_at":"2020-09-15 14:57:23","user":{"user_id":"36330158","nickname":"%@$","avatar":"http:\/\/im-res-test.oss-cn-shenzhen.aliyuncs.com\/user\/avatar\/cf\/69\/6a\/cf696a9e6bb7ed5d847dfdda5aced283.jpg"}},{"created_at":"2020-09-02 10:23:38","user":{"user_id":"169257242","nickname":"\u9e21\u817f","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200730\/5f22810f4f7c3.jpg"}},{"created_at":"2020-08-27 16:01:48","user":{"user_id":"044000699","nickname":"\u6b63\u80fd\u91cf\u6536\u85cf\u5bb6","avatar":"http:\/\/im-res-test.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200526\/5ecc7ef634b55.jpg"}}]},{"feed_id":"2334","type":3,"content":"","extend":["{\"url\":\"http:\\\/\\\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\\\/user\\\/feed\\\/20200915\\\/28\\\/e2\\\/4f\\\/28e24fe638af369e6a0f42ae77b8a67e.jpg\",\"img_height\":450,\"img_width\":800}","{\"url\":\"http:\\\/\\\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\\\/user\\\/feed\\\/20200915\\\/35\\\/f3\\\/fc\\\/35f3fc226b25efff059d04b915fe70c8.jpg\",\"img_height\":466,\"img_width\":800}"],"longitude":"0.000000000","latitude":"0.000000000","position":"","address":"","city":"","comment_count":0,"favour_count":2,"created_at":"2020-09-15 14:45:05","is_top":0,"favoured":0,"user":{"user_id":"257828297","nickname":"gg","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200915\/5f606e42b7d4c.jpg","is_dream_guard":7777},"comments":[],"favours":[{"created_at":"2020-09-15 14:48:30","user":{"user_id":"257828297","nickname":"gg","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200915\/5f606e42b7d4c.jpg"}},{"created_at":"2020-09-15 14:48:28","user":{"user_id":"631855499","nickname":"\u80d6\u864e","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200729\/5f20eabebf678.jpg"}}]},{"feed_id":"2335","type":3,"content":"","extend":["{\"url\":\"http:\\\/\\\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\\\/user\\\/feed\\\/20200915\\\/e0\\\/42\\\/7e\\\/e0427e1fef8d3dc0d75a99ff58abc296.png\",\"img_width\":\"500\",\"img_height\":\"500\"}"],"longitude":"0.000000000","latitude":"0.000000000","position":"","address":"","city":"","comment_count":0,"favour_count":2,"created_at":"2020-09-15 14:45:25","is_top":0,"favoured":0,"user":{"user_id":"631855499","nickname":"\u80d6\u864e","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200729\/5f20eabebf678.jpg","is_dream_guard":8888},"comments":[],"favours":[{"created_at":"2020-09-15 14:48:27","user":{"user_id":"631855499","nickname":"\u80d6\u864e","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200729\/5f20eabebf678.jpg"}},{"created_at":"2020-09-15 14:48:24","user":{"user_id":"257828297","nickname":"gg","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200915\/5f606e42b7d4c.jpg"}}]},{"feed_id":"2272","type":2,"content":"\u545c\u545c\u545c\u545c\u545c\u545c\u545c\u545c\u545c\u545c\u545c\u545c\u545c\u545c\u545c\u545c\u545c\u545c\u545c\u545c\u545c\u738b\u4e07\u738b\u4e07\u738b\u4e07\u738b\u4e07\u738b\u4e07\u738b\u4e07\u738b\u4e07\u7cbd\u7cbd\u7cbd\u7cbd\u7cbd\u7cbd\u7cbd\u6700\u6700\u6700\u6700\u6700\u6700\u6700\u6700\u6700\u6700\u5440\u5440\u5440\u5440\u5440\u5440\u5728\u771f\u5b66\u5728\u771f\u5b66\u5728\u771f\u5b66\u5728\u771f\u5728\u771f\u5b66\u5728\u771f\u5b66\u5728\u771f\u5b66\u5728\u771f\u5b66\u5728\u771f\u8f6c\u5582\u5582\u5582\u5582\u5582\u5582\u5582\u5582\u5582\u5582\u6211\u6211\u6211\u6211\u6211\u6211\u6211\u6211\u5582\u5582\u5582\u5582\u5582\u5582\u5582\u5582\u5582\u5582\u5728\u771f\u5b66\u5728\u771f\u5b66\u5728\u771f\u5b66\u5728\u771f","extend":["{\"url\":\"http:\\\/\\\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\\\/user\\\/feed\\\/20200730\\\/12\\\/ae\\\/d6\\\/12aed68839da7ce5e073235d1467f72f.gif\",\"img_height\":241,\"img_width\":247.5}","{\"url\":\"http:\\\/\\\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\\\/user\\\/feed\\\/20200730\\\/bb\\\/64\\\/71\\\/bb647151dfc83bf36087a650fd150857.gif\",\"img_height\":118,\"img_width\":120}","{\"url\":\"http:\\\/\\\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\\\/user\\\/feed\\\/20200730\\\/42\\\/70\\\/48\\\/427048200cf1cec8a369a24b99c195f2.gif\",\"img_height\":120,\"img_width\":120}","{\"url\":\"http:\\\/\\\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\\\/user\\\/feed\\\/20200730\\\/ed\\\/a6\\\/c8\\\/eda6c89019c00c7599759ed47802c389.gif\",\"img_height\":150,\"img_width\":150}","{\"url\":\"http:\\\/\\\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\\\/user\\\/feed\\\/20200730\\\/7e\\\/3a\\\/7c\\\/7e3a7c39d866a76079f3886aab76876f.jpg\",\"img_height\":516,\"img_width\":750}","{\"url\":\"http:\\\/\\\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\\\/user\\\/feed\\\/20200730\\\/e0\\\/2a\\\/89\\\/e02a890b1b44784073d9539dc23de70c.jpg\",\"img_height\":500,\"img_width\":750}","{\"url\":\"http:\\\/\\\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\\\/user\\\/feed\\\/20200730\\\/36\\\/a6\\\/9a\\\/36a69a3cf8f702bddec90a0a5b391336.jpg\",\"img_height\":924,\"img_width\":750}","{\"url\":\"http:\\\/\\\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\\\/user\\\/feed\\\/20200730\\\/06\\\/25\\\/64\\\/062564665380a9ece43c83f094169e6d.jpg\",\"img_height\":866,\"img_width\":750}"],"longitude":"113.907128000","latitude":"22.509753000","position":"\u592a\u5b50\u5c71\u5e84","address":"\u524d\u6d77\u8def0308\u53f7","city":"\u6df1\u5733\u5e02","comment_count":0,"favour_count":1,"created_at":"2020-07-30 16:17:00","is_top":0,"favoured":0,"user":{"user_id":"169257242","nickname":"\u9e21\u817f","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200730\/5f22810f4f7c3.jpg","is_dream_guard":31},"comments":[],"favours":[{"created_at":"2020-09-04 18:33:15","user":{"user_id":"169257242","nickname":"\u9e21\u817f","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200730\/5f22810f4f7c3.jpg"}}]},{"feed_id":"2273","type":1,"content":"\u545c\u545c\u545c\u545c\u545c\u545c\u545c\u545c\u545c\u545c\u545c\u545c\u545c\u545c\u545c\u545c\u545c\u545c\u545c\u545c\u545c\u738b\u4e07\u738b\u4e07\u738b\u4e07\u738b\u4e07\u738b\u4e07\u738b\u4e07\u738b\u4e07\u7cbd\u7cbd\u7cbd\u7cbd\u7cbd\u7cbd\u7cbd\u6700\u6700\u6700\u6700\u6700\u6700\u6700\u6700\u6700\u6700\u5440\u5440\u5440\u5440\u5440\u5440\u5728\u771f\u5b66\u5728\u771f\u5b66\u5728\u771f\u5b66\u5728\u771f\u5728\u771f\u5b66\u5728\u771f\u5b66\u5728\u771f\u5b66\u5728\u771f\u5b66\u5728\u771f\u8f6c\u5582\u5582\u5582\u5582\u5582\u5582\u5582\u5582\u5582\u5582\u6211\u6211\u6211\u6211\u6211\u6211\u6211\u6211\u5582\u5582\u5582\u5582\u5582\u5582\u5582\u5582\u5582\u5582\u5728\u771f\u5b66\u5728\u771f\u5b66\u5728\u771f\u5b66\u5728\u771f","extend":[],"longitude":"113.907128000","latitude":"22.509753000","position":"\u592a\u5b50\u5c71\u5e84","address":"\u524d\u6d77\u8def0308\u53f7","city":"\u6df1\u5733\u5e02","comment_count":0,"favour_count":1,"created_at":"2020-07-30 16:17:14","is_top":0,"favoured":0,"user":{"user_id":"169257242","nickname":"\u9e21\u817f","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200730\/5f22810f4f7c3.jpg","is_dream_guard":31},"comments":[],"favours":[{"created_at":"2020-09-04 18:33:14","user":{"user_id":"169257242","nickname":"\u9e21\u817f","avatar":"http:\/\/yaoxin-test-res.oss-cn-shenzhen.aliyuncs.com\/head_portrait\/20200730\/5f22810f4f7c3.jpg"}}]},{"type":7}]}}
    data=json.dumps(data)
    response.text=data
    info('---------------------------------------------------------------------')
    info('\n')
    info('\n')
    info('\n')
    info('\n')
    info('\n')
    with open('mit.log','a+',encoding='utf-8') as f :
        f.write(str(response.text))
    # if response.json()['code'] == 0:
    #     # # 打印响应报文内容
    #     info('---------------------------------------------------------------------')
        # info(str(response.text))

        # # 打印所有头部
        # info(str(response.headers))
        # # 打印cookie头部
        # info(str(response.cookies))
    # else:
    #     pass
