s = int(input('Введите количество секунд '))
hours = s // 3600
minutes = (s-(hours*3600))//60
seconds = (s-(hours*3600+minutes*60))
print(f"{hours:02d}",f"{minutes:02d}",f"{seconds:02d}",sep=':')