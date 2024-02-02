function [share1, share2, share12] = VisCrypt4(inImg)

s = size(inImg);
share1 = zeros(s(1), (2 * s(2)));
share2 = zeros(s(1), (2 * s(2)));

%% White Pixel Processing
% White Pixel share combinations
disp('White Pixel Processing...');
s1a = [1 0];
s1b = [1 0];
[x, y] = find(inImg == 1);
len = length(x);

for i = 1:len
    a = x(i);
    b = y(i);

    if (a <= s(1)) && (b <= s(2))
        pixShare = generateShare4(s1a, s1b);
        share1(a, (2 * b - 1):(2 * b)) = pixShare(1, 1:2);
        share2(a, (2 * b - 1):(2 * b)) = pixShare(2, 1:2);
    else
        disp(['Warning: Index (', num2str(a), ', ', num2str(b), ') is out of bounds.']);
    end
end

%% Black Pixel Processing
% Black Pixel share combinations
disp('Black Pixel Processing...');
s0a = [1 0];
s0b = [0 1];
[x, y] = find(inImg == 0);
len = length(x);

for i = 1:len
    a = x(i);
    b = y(i);

    if (a <= s(1)) && (b <= s(2))
        disp('1.....');
        pixShare = generateShare4(s0a, s0b);
        disp('2.....');
        share1(a, (2 * b - 1):(2 * b)) = pixShare(1, 1:2);
        disp('3.....');
        share2(a, (2 * b - 1):(2 * b)) = pixShare(2, 1:2);
        disp('4.....');
    else
        disp(['Warning: Index (', num2str(a), ', ', num2str(b), ') is out of bounds.']);
    end
end

share12 = bitor(share1, share2);
share12 = ~share12;
disp('Share Generation Completed.');
