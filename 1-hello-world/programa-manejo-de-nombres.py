primerPariente = 'Benjamin'
segundoPariente = 'Olivia'
tercerPariente = 'Rambo'

primerNombreModificado = ((primerPariente[1:2]).upper()
                          + '.'
                          + primerPariente[-2::1])
segundoNombreModificado = ((segundoPariente[1:2]).upper()
                           + '.'
                           + segundoPariente[-2::1])
tercerNombreModificado = ((tercerPariente[1:2]).upper()
                          + '.'
                          + tercerPariente[-2::1])

variableFinal = (primerNombreModificado + '_'
                 + segundoNombreModificado + '_'
                 + tercerNombreModificado)

print(variableFinal)

