import wap
import time



start = time.clock()

outer_assumption_list = []
def give_value_for_assumption(value,assumption_dict):
  for in_list in value:
    for tuples in in_list:
      if str(tuples[0]) == 'input':
        assumption_dict['value'].append(tuples[1])
  return(assumption_dict)

server = 'http://api.wolframalpha.com/v1/query.jsp'
appid = 'EEKVX9-HGPX4GPUWY'
input = 'running'
scantimeout = '3.0'
podtimeout = '4.0'
formattimeout = '8.0'
async = 'False'

waeo = wap.WolframAlphaEngine(appid, server)

waeo.ScanTimeout = scantimeout
waeo.PodTimeout = podtimeout
waeo.FormatTimeout = formattimeout
waeo.Async = async

query = waeo.CreateQuery(input)




waeq = wap.WolframAlphaQuery(input, appid)
waeq.ScanTimeout = scantimeout
waeq.PodTimeout = podtimeout
waeq.FormatTimeout = formattimeout
waeq.Async = async
waeq.ToURL()
waeq.AddPodTitle('')
waeq.AddPodIndex('')
waeq.AddPodScanner('')
waeq.AddPodState('')
waeq.AddAssumption('')

query = waeq.Query

print '***wapex output***', '\n', 'server=' + server + '\n', query

result = waeo.PerformQuery(query+'&assumption=*FS-_**Running.t--&assumption=*FVarOpt-_**Running.v-.*Running.age-.*Running.H--&assumption=*FVarOpt-_**Running.incline-.*Running.v-.*Running.age-.*Running.H-.*Running.HRResting--')

waeqr = wap.WolframAlphaQueryResult(result)


assumptions = waeqr.Assumptions()
print(assumptions)

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


  


stop = time.clock()
print '\n', 'time=', stop - start
