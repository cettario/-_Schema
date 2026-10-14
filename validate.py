from pathlib import Path
from lxml import etree

folder=Path(__file__).resolve().parent
schema=etree.XMLSchema(etree.parse(str(folder/'notebook.xsd')))
expected={'valid.xml':True,**{f'no-valid-{i}.xml':False for i in range(1,6)}}
failures=0
for filename,should_pass in expected.items():
    document=etree.parse(str(folder/filename))
    passed=schema.validate(document)
    status='валидный' if passed else 'невалидный'
    correct=passed==should_pass
    print(f'{filename}: {status} | {"OK" if correct else "ОШИБКА"}')
    if not correct:
        failures+=1
    if not passed:
        for error in schema.error_log:
            print(' ',error.message)
raise SystemExit(1 if failures else 0)
