#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wap

server = 'http://api.wolframalpha.com/v2/query.jsp'
appid = 'EEKVX9-HGPX4GPUWY'
input = 'running'

waeo = wap.WolframAlphaEngine(appid, server)

queryStr = waeo.CreateQuery(input)
queryStr = queryStr+'&assumption=*FS-_**Running.t--&assumption=*FVarOpt-_**Running.v-.*Running.age-.*Running.H--&assumption=*FVarOpt-_**Running.incline-.*Running.v-.*Running.age-.*Running.H-.*Running.HRResting--'
#&assumption=*FVarOpt-_**Running.HRResting-.*Running.p--&assumption=*FVarOpt-_**Running.age-.*Running.H-.*Running.p--
wap.WolframAlphaQuery(queryStr, appid)
result = waeo.PerformQuery(queryStr)

waeqr = wap.WolframAlphaQueryResult(result)


assumptions = waeqr.Assumptions()
print(assumptions)

results = wap.WolframAlphaQueryResult(result)
#print(queryStr)

j = results.JsonResult()

#print(j)
for pod in results.Pods():
	waPod = wap.Pod(pod)
	title = "Pod.title: " + waPod.Title()[0]
	print title
	for subpod in waPod.Subpods():
		waSubpod = wap.Subpod(subpod)
		plaintext = waSubpod.Plaintext()[0]
		img = waSubpod.Img()
		src = wap.scanbranches(img[0], 'src')[0]
		alt = wap.scanbranches(img[0], 'alt')[0]
		print "-------------"
		# print "img.src: " + src
		# print "img.alt: " + alt
	# print "\n"

outer_assumption_list = []
def give_value_for_assumption(value,assumption_dict):
  for in_list in value:
    for tuples in in_list:
      if str(tuples[0]) == 'input':
        assumption_dict['value'].append(tuples[1])
  return(assumption_dict)



for assumption in assumptions:
  assumption_dict = {'type':'',"value":[]}
  waea = wap.Assumption(assumption)

  atype = waea.Type()
  print '\n', type(atype), 'assumptions type=', atype
  assumption_dict['type'] = atype
  word = waea.Word()
  print '\n', type(word), 'word=', word
  count = waea.Count()
  print '\n', type(count), 'count=', count
  value = waea.Value()
  assumption_dict = give_value_for_assumption(value,assumption_dict)
  outer_assumption_list.append(assumption_dict)

print(outer_assumption_list)


