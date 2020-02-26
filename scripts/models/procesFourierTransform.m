%script que recibe una matriz en formato csv con la data de la secuencia de
%proteina codificada y con zero padding con respecto a la potencia de 2 mas
%cercana, a cada secuencia la digitaliza empleando la transformada rapida
%de fourier y se genera una matriz con la informacion de los espectros
%asociada a la matriz de interes

function procesFourierTransform(inputFile)

    %lectura de la matriz de interes
    matrixData = csvread(inputFile);
    [m,n] = size(matrixData);
    
    domainFrequence = [];
    espectralUnilateral = [];
    
    for row = 1:m
        valueConvert = matrixData(row,:);%obtener valores a transformar
        valueFFT = fft(valueConvert, n);
        
        %obtenemos los valores de los espectros bilateral y unilateral,
        %seguido del dominio y los puntos para hacer la grafica
        %correspondiente
        P2 = abs(valueFFT/n);
        P1 = P2(1:n/2+1);
        P1(2:end-1) = 2*P1(2:end-1);
        f1 = 0.5*(0:n-1)/n;
        f = 0.5*(0:(n/2))/n;
        P = abs(valueFFT/n);
                
        domainFrequence=[f;domainFrequence];
        espectralUnilateral = [P1;espectralUnilateral];                        
        
    end
    
    %exportamos los archivos en formato csv
    csvwrite("domainFrequence.csv", domainFrequence);
    csvwrite("espectralUnilateral.csv", espectralUnilateral);
    
end