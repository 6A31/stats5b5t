from stats5b5t import api, tools
#File in work. this is just me debugging
stats = api.Statistics()

tests = tools.Debugging()

r = stats.request("4205f31069a84e42bff88d4b07e09253")

print(stats.raw(r))

print(stats.ratio(r))
print(tests.errmsg(r))

print(tests.missmatch(r,"4205f31069a84e42bb07e09253"))

print("------------------")
r = stats.request("427e09253")
print(stats.ratio(r))
print(tests.isvalid(r))
print(tests.errmsg(r))
