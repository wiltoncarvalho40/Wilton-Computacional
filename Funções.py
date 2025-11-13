def Regra_Extremidade_Esquerda (a = 0, b = 0, c= 0, d = 0, e = 0, f = 0,
                                x_i = 0, x_f = 0, passo = 0,
                                plot = False, Salvar_png = False, dpi = 1200, Salvar_pdf = False, Diretorio = '\content\'):

  """
  Aqui você calculará a Integral Definida de uma função afim polinomial de até 5º grau, correspondente a uma função do tipo: f(x) = a*x**5 + b*x**4 + c*x**3 + d*x**2 + e*x + f,
  onde será calculada a Integral com Elementos Infinitos (Integral Analítica), e a Integral com Elementos Finitos (Somatória) e a regra utilizada para a Integral com Elementos Finitos
  é altura de retângulos calculados pelo ponto Esquerdo. 

  Os resultados serão retornados através de um dicionário, e também poderá ser plotado a figura com os retângulos ou não, e caso tenha a figura ela poderá ser salva ou não de forma automática,
  tanto no formato .png como no formato .pdf
  """
                                
  intervalo = []
  for i in range(int((x_f - x_i)/passo)):
    intervalo.append(x_i + i*passo)

  fxi = []
  ci_fxi = []
  for i in range(len(intervalo)):
    x = intervalo[i]
    f_x_i = a*x**5 + b*x**4 + c*x**3 + d*x**2 + e*x + f
    ci_fxi.append(f_x_i*passo)
    fxi.append(f_x_i)

  somatoria = sum(ci_fxi)

  integral_xi = (a/6)*x_i**6 + (b/5)*x_i**5 + (c/4)*x_i**4 + (d/3)*x_i**3 + (e/2)*x_i**2 + f*x_i
  integral_xf = (a/6)*x_f**6 + (b/5)*x_f**5 + (c/4)*x_f**4 + (d/3)*x_f**3 + (e/2)*x_f**2 + f*x_f
  integral_analitica = integral_xf - integral_xi

  dicionario = {
      'Intervalo': intervalo,
      'f(x)': fxi,
      'Integral Numérica': somatoria,
      'Integral Analítica': integral_analitica}

  if plot == True:
    # Plotando
    plt.figure(figsize=(10,6))
    plt.plot(intervalo, fxi, 'b',
             label = rf'$f (x) = {a}x^5 + {b}x^4 + {c}x^3 + {d}x^2 + {e}x + {f}$')  # curva da função

    # Desenhando os retângulos
    for i in range(len(intervalo)):
        x0 = intervalo[i]
        plt.bar(x0, fxi[i], width=passo, align='edge', color='orange', edgecolor='black', alpha=0.5)

    plt.text(0.3, 0.15, rf'$\int_{{{x_i}}}^{{{x_f}}} f(x)\,
    dx = \int_{{{x_i}}}^{{{x_f}}} {a}x^5 + {b}x^4 + {c}x^3 + {d}x^2 + {e}x + {f}\,
    dx = {somatoria:.2f}$',
             transform=plt.gca().transAxes,
             fontsize=12,
             verticalalignment='top',
             bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.7))

    # Detalhes do gráfico
    plt.title('Integração Numérica - Regra da Extremidade Esquerda')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$f(x)$')
    plt.legend()
    if Salvar_png == True:
      plt.savefig(Diretorio + 'integracao_extremidade_esquerda.png', dpi = dpi)
    elif Salvar_pdf == True:
      plt.savefig(Diretorio + 'integracao_extremidade_esquerda.pdf')
    plt.show()

  return dicionario
