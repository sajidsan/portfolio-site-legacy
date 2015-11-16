import os
for x in os.listdir('.'):
    if x.endswith('.php'):
      cmd = 'php "%s" > "%s" ' % (x, x.replace('.php', '.html'))
      print cmd
      os.system(cmd)
