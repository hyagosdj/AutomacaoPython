import openpyxl

meus_computadores = openpyxl.Workbook()

meus_computadores.create_sheet('Computadores')

computadores_page = meus_computadores['Computadores']

computadores_page.append(['MARCA', 'MEMORIA', 'VALOR'])
computadores_page.append(['ALIENWARE', '32 GB RAM', 'R$ 8500'])
computadores_page.append(['DELL', '16 GB RAM', 'R$ 5500'])
computadores_page.append(['ASUS', '8 GB RAM', 'R$ 2500'])

meus_computadores.save('Meus computadores.xlsx')