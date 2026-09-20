import re

with open('out/work/decoded/smali/rg3.smali', 'r') as f:
    content = f.read()

with open('new_clinit.smali', 'r') as f:
    new_clinit_body = f.read()

new_clinit = ".method static constructor <clinit>()V\n    .locals 8\n" + new_clinit_body + ".end method"

patched = re.sub(r'\.method static constructor <clinit>\(\)V.*?^\.end method', new_clinit, content, flags=re.DOTALL | re.MULTILINE)

with open('out/work/decoded/smali/rg3.smali', 'w') as f:
    f.write(patched)
