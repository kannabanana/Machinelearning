%PART ONE

%get the matrix for the housing data
filename = 'housing_train.txt';
[X,delimiterOut] = importdata(filename);

%last column has the averages
Y = X(:,14);

%delete the last column and add the weights
X(:,14) = [];

weight = ones(433,1);
Z = [weight,X];


%solve for w
W = ((transpose(Z)*Z)^-1)*transpose(Z)*Y;


%solve for SSE
SSE = transpose((Y-XW))*(Y-XW);
disp(SSE);
