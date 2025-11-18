Function TOEPLITZ_MV_MULTIPLY(T, v, n):

    // Complexity: O(n log n)
    // t = [t_0, t_1, ..., t_{n-1}, t_{-(n-1)}, ..., t_{-1}] (Length 2n-1, padding needed)
    
    // The coefficients of the equivalent cyclic convolution (length N = 2n)
    N = 2 * n
    
    // Construct vector c of length N (first row of the embedding Circulant matrix)
    // c[0] = t[0]
    // c[1] to c[n-1] = t[1] to t[n-1]
    // c[n] = 0 (or arbitrary, but 0 is standard for linear convolution)
    // c[n+1] to c[2n-1] = t[-(n-1)] to t[-1] (reversed order for c[1]...c[n-1])
    Initialize c[0..N-1] // The generator for the Circulant matrix
    
    // 2. Pad the vector v
    // Pad v with n zeros to match the length N
    Initialize v_pad[0..N-1]
    v_pad[0..n-1] = v[0..n-1]
    v_pad[n..N-1] = 0 // Padding with zeros

    // 3. Compute FFTs
    FFT_c = FFT(c)
    FFT_v = FFT(v_pad)

    // 4. Compute the Hadamard (element-wise) product or convolution
    Initialize FFT_r[0..N-1]
    For k from 0 to N-1:
        FFT_r[k] = FFT_c[k] * FFT_v[k]
    
    // 5. Compute the Inverse FFT
    r_full = IFFT(FFT_r)

    // 6. Extract the result
    // The result r = Tv is the first n elements of r_full
    Initialize r[0..n-1]
    r[0..n-1] = r_full[0..n-1]
    
    Return r

Complexity: O(nlogn) The complexity of FFT.