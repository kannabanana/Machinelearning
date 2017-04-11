%PART ONE

%weights or no weights
w2 = 'Do you want to use weights? 1= yes 2= no. ';
w2 = input(w2);
disp(w2);


%get the matrix for the housing data
tt = 'Are you training (1) or testing (2)? ';
tt = input(tt);
disp(tt);


filename = 'housing_train.txt';
[X,delimiterOut] = importdata(filename);

%last column has the averages
Y = X(:,14);

%delete the last column and add the weights
X(:,14) = [];


if (w2 == 1)	%weights
	weight = ones(433,1);
	Z = [weight,X];
	W = ((transpose(Z)*Z)^-1)*transpose(Z)*Y;
%	disp(W);
	
	if (tt == 1)
		%training
		SSE = transpose(Y-(Z*W))*(Y-Z*W);
		disp(SSE);
	else	%test
		filename = 'housing_test.txt';
		[X,delimiterOut] = importdata(filename);

		Y = X(:,14);
		X(:,14) = [];
		disp(W);
		disp(weight);
		Z = [weight,X];
		disp(Z);
		SSE = transpose(Y-(Z*W))*(Y-Z*W);
		disp(SSE);
	end

else	%no weights
	W = ((transpose(X)*X)^-1)*transpose(X)*Y;
	disp(W);
	if (tt == 1) %train
		SSE = transpose(Y-(X*W))*(Y-X*W);
		disp(SSE);
	else
		filename = 'housing_test.txt';
		[X,delimiterOut] = importdata(filename);

		Y = X(:,14);
		X(:,14) = [];

		SSE = transpose(Y-(X*W))*(Y-X*W);
		disp(SSE);
	
	end
end
