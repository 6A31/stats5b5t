from stats5b5t import api, tools

stats = api.Statistics()

tests = tools.Debugging()

r = stats.request("4205f31069a84e42bff88d4b07e09253")


print(stats.kills(r))

r = stats.request("asdfasd")

print(tests.isvalid(r))

print(tests.errmsg(r))