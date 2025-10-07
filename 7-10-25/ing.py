add_suffix = lambda s: (s + 'ly') if s[-3:] == 'ing' else (s + 'ing')
print(add_suffix("run"))     
print(add_suffix("running")) 
