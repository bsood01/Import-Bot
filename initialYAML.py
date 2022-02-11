import yaml
import pprint
import ruamel.yaml



with open('demo.yaml') as f:
  yaml= ruamel.yaml.safe_load(f)
print(ruamel.yaml.dump(yaml, Dumper=ruamel.yaml.RoundTripDumper), end='')

#with open('demo_v1-0.yaml') as f:
#dataMap = yaml.safe_load(f)
#print(yaml.dump(dataMap, allow_unicode=True, default_flow_style=False))
#pretty(dataMap)

#def pretty(d, indent=0):
   #for key, value in d.items():
      #print('  '*indent  + str(key)+':',end='')
     # if isinstance(value, dict):
    #    print('')
   #     pretty(value, indent++1)
  #    else:
 #        print( str(value))


