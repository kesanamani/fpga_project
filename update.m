function [outputImage, errorImage, filter] = update(input,desired,S)
filtersize = S.filterOrderNo+1;
[rows,cols] = size(input);
nIterations = rows*cols;

% Pre-allocations
errorImage = zeros(rows, cols);
outputImage = zeros(rows, cols);
error = zeros(rows, cols);
output = zeros(rows, cols);
filter = zeros(filtersize,filtersize);
itCount = 1;

% Initial state of the weight vector

filter(:,:) = S.initialCoefficients;

% Prefixed input
prefixedimage = input;
%padding
prefixedimage(:,(cols+1):(cols+S.filterOrderNo)) = 0;
prefixedimage((rows+1):(rows+S.filterOrderNo),:) = 0;


% Body

for i1 = 1:rows
    for i2 = 1:cols
        
        u = prefixedimage(i1+(filtersize-1):-1:i1, i2+(filtersize-1):-1:i2);
        
        ex1 = filter(:,:).*u;
        
        outputImage(i1,i2) = sum(ex1(:));
        
        errorImage(i1,i2) = desired(i1,i2) - outputImage(i1,i2);
        
        filter(:,:) = filter(:,:) + (2*S.step*errorImage(i1,i2)*u);
        
        itCount = itCount+1;
    end
end
% for i1 = 1:rows
%     for i2 = 1:cols
%         
%         u = prefixedimage(i1+(filtersize-1):-1:i1, i2+(filtersize-1):-1:i2);
%         
%         ex1 = filter(:,:,itCount-20).*u;
%         
%         output(i1,i2) = sum(ex1(:));
%         
%         error(i1,i2) = desired(i1,i2) - outputImage(i1,i2);
%         
%         
%     end
% end
