
#--------------------------------------------------------------------------
#                     与conftest.py的获取token重复了，企业里主要用@pytest封装的
# 这两段代码是两种不同的实现方式，虽然都在获取 token，但适用场景和写法不同，不算完全重复：
# 第一段（conftest.py 里的 auth_token fixture）
# 它是 pytest 的 fixture，用 scope="session" 修饰，作用是整个测试会话只执行一次，所有用例都可以直接依赖它来拿到 token。
# 它依赖了 base_url fixture，和 pytest 的执行流程深度绑定，专门给测试用例用。
# 第二段（token_util.py 里的 get_token 函数）
# 它是一个独立的工具函数，带全局变量缓存，作用是任何地方调用都只请求一次登录接口，不管是不是 pytest 用例。
# 它直接依赖 get_base_url()，不依赖 pytest 框架，通用性更强，比如在脚本里、非 pytest 场景也能调用。
#-------------------------------------------------------------------------------------------


# from testcases.common_tool.request_util import request_way
#
#
# _token = None
#
#
# def get_token(caseinfo):
#
#     global _token
#
#     if _token:
#         return _token
#
#     rep = request_way(caseinfo['request']['method'], caseinfo)
#     if rep.status_code == 200:
#         _token = rep.json()['data']['token']
#     return _token
#
# def get_header():
#     token = get_token()
#     return {
#         'Content-Type': 'application/json',
#         'Authorization': f'Bearer {token}'
#     }
#
# def clear_token():
#     global _token
#     _token = None