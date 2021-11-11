metros = float(input('Digite uma distância em metros: '))

print('A medida de {:.1f}m corresponde a: '.format(metros))
print('{}km'.format(metros/1000))
print('{}hm'.format(metros/100))
print('{}am'.format(metros/10))
print('{}dm'.format(round(metros*10)))
print('{}cm'.format(round(metros*100)))
print('{}mm'.format(round(metros*1000)))