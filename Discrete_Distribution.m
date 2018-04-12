clear
clc

iniDist = [1 1];
nCrossings = 1;
nKnots = 5;
prevKnots = iniDist;

for a = 1:nKnots
    if a > 2
        prevKnots = bigKnots;
    end
bigKnots = horzcat(zeros(1,length(prevKnots)),zeros(1,length(iniDist)));
    for k = 1:nKnots*length(iniDist)
        for n = 1:length(prevKnots)
            for m = 1:length(iniDist)

                if n + m == k
                        bigKnots(1,k) = bigKnots(1,k) + prevKnots(1,n)*iniDist(1,m);
                end

            end
        end
    end
end
fprintf('Distribution for %.f knots\n',nKnots);
disp(bigKnots)

%to find mean
sum = 0;
for k = 1:nKnots*nCrossings
    sum = sum + k*bigKnots(1,k);    
end
mean = sum/8^nKnots;
fprintf('Mean for nKnots \n%f\n\n\n',mean);
