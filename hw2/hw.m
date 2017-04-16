%PART ONE

%weights or no weights
w2 = 'Do you want to use weights? 1= yes 2= no. ';
w2 = input(w2);


%get the matrix for the housing data
tt = 'Are you training (1) or testing (2)? ';
tt = input(tt);


filename = 'housing_train.txt';
[X,delimiterOut] = importdata(filename);

%last column has the averages
Y = X(:,14);

%delete the last column and add the weights
X(:,14) = [];


if (w2 == 1)	%weights
	weight = ones(433,1);
	Z = [weight,X];

%for number five - adding random uniform weights
	%---add the extra features here--%
	W = ((transpose(Z)*Z)^-1)*transpose(Z)*Y;
	
	if (tt == 1)
		%training
		
		str = 'SSE USING WEIGHTS OF TRAINING DATA IS ';
		disp(str);
		SSE = transpose(Y-(Z*W))*(Y-Z*W);
		disp(SSE);



	else	%test------------------------------------------------------
		filename = 'housing_test.txt';
		[X,delimiterOut] = importdata(filename);

		Y = X(:,14);
		X(:,14) = [];

		Z = [weight,X];
		str = 'SSE USING WEIGHTS OF TEST DATA IS ';
		disp(str);
		SSE = transpose(Y-(Z*W))*(Y-Z*W);
		disp(SSE);
	end

else	%no weights

	l = .5;
	I = transpose(X)*X;
	%finding W for part six
	W = (inv((transpose(X)*X)+l*I)*transpose(X)*Y);


	%W = ((transpose(X)*X)^-1)*transpose(X)*Y;
	disp(W);
	if (tt == 1) %train
		str = 'NO WEIGHTS AND TRAIN';
		disp (str);
		SSE = transpose(Y-(X*W))*(Y-X*W);
		disp(SSE);
	else
		str = 'NO WEIGHTS AND TEST';
		disp(str);
		filename = 'housing_test.txt';
		[X,delimiterOut] = importdata(filename);

		Y = X(:,14);
		X(:,14) = [];

		SSE = transpose(Y-(X*W))*(Y-X*W);
		disp(SSE);
	
	end
end
