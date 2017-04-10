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
%W = ((transpose(X)*X)^-1)*transpose(X)*Y;


%solve for w with weights
W = ((transpose(Z)*Z)^-1)*transpose(Z)*Y;


filename = 'housing_test.txt';
[X,delimiterOut] = importdata(filename);

Y = X(:,14);
X(:,14) = [];
Z = [weight,X];

%solve for SSE of Training data without weights
%SSE = transpose(Y-(X*W))*(Y-X*W);


%solve for SSE of Training data with weights
SSE = transpose(Y-(Z*W))*(Y-Z*W);

disp(SSE);
