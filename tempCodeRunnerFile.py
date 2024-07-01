# Jarak Solusi Ideal Positif (D+)
    jarak_positif = [
        {
            'no': i+1,
            'merek': row[1],
            'd_plus': math.sqrt(
                sum(pow(float(row[j+2]) - float(positif[j]), 2) for j in range(5))
            )
        }
        for i, row in enumerate(matriks_terbobot)
    ]

    # Jarak Solusi Ideal Negatif (D-)
    jarak_negatif = [
        {
            'no': i+1,
            'merek': row[1],
            'd_minus': math.sqrt(
                sum(pow(float(row[j+2]) - float(negatif[j]), 2) for j in range(5))
            )
        }
        for i, row in enumerate(matriks_terbobot)
    ]