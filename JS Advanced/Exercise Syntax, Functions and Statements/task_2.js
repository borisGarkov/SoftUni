function egcd(a, b) {
    if (a == 0)
        return b;

    while (b != 0) {
        if (a > b)
            a = a - b;
        else
            b = b - a;
    }

    console.log(a);
}

egcd(15, 5)
egcd(2154, 458)