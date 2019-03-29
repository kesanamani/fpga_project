
clear;

%Generate test image
imm = 96;
imn = 96;

v1 = 0.8*ones(imm-25,1);
v2 = 0.2*ones(imm-25,1);

D1 = diag(v1,25);
D2 = diag(v2,-25);

image = zeros(imm,imn);
image(9:88,9:88) = 0.7;
image(17:80,17:80) = 0;
image(27:70,27:70) = 1;
image(32:65,32:65) = 0.2;
image(41:56,41:56) = 1;

for i = 1:imm
    for j = 1:imn
        if D1(i,j) > 0
            image(i,j) = D1(i,j);
        end
        if D2(i,j) > 0
            image(i,j) = D2(i,j);
        end
    end
end

% Other initilizations
ensemble = 500;
mu = 35*10^(-5);
N = 3;
inicoefs = fspecial('gaussian',[N N]);
%  inicoefs = zeros(3); 

MSE = zeros(imm,imn,ensemble);
errim = zeros(imm,imn,ensemble);
 noiseim = imnoise(image,'gaussian');
 for l = 1:ensemble
    
    S = struct('step',mu,'filterOrderNo',(N-1),'initialCoefficients',inicoefs);
    [outim, errim(:,:,l), coefs(:,:)] = TWDLMS(noiseim,image,S);
    MSE(:,:,l) = MSE(:,:,l)+(errim(:,:,l)).^2;
   inicoefs=coefs(:,:);
   
   inicoefs
    
 end

MSE_av = sum(MSE,3)/ensemble;

figure;
subplot(2,2,1),imshow(image,[]);
title('Original Image');
subplot(2,2,2),imshow(noiseim,[]);
title('Noisy Image');
subplot(2,2,3),imshow(outim,[]);
title('Output Image');
subplot(2,2,4),imshow(MSE_av,[]);
title('MSE Image');

