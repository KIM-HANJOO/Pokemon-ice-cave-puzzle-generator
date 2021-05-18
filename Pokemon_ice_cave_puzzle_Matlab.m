clc;
clear all;

%%

width = 5;
length = 4;

startpoint_x = [2, 3];
startpoint_y = [0];

endpoint_x = [6];
endpoint_y = [2, 3];

%% randomly set startpoint & endpoint

size_s_x = max(size(startpoint_x(1, :)));
size_s_y = max(size(startpoint_y(1, :)));
size_e_x = max(size(endpoint_x(1, :)));
size_e_y = max(size(endpoint_y(1, :)));

s_rand_x = randperm(size_s_x) - 1;
s_rand_y = randperm(size_s_y) - 1;
e_rand_x = randperm(size_e_x) - 1;
e_rand_y = randperm(size_e_y) - 1;

startpoint = zeros(1, 2);
endpoint = zeros(1, 2);

startpoint(1, 1) = startpoint_x(1, 1) + s_rand_x(1, 1);
startpoint(1, 2) = startpoint_y(1, 1) + s_rand_y(1, 1);

endpoint(1, 1) = endpoint_x(1, 1) + e_rand_x(1, 1);
endpoint(1, 2) = endpoint_y(1, 1) + e_rand_y(1, 1);

clearvars startpoint_x; clearvars startpoint_y;
clearvars endpoint_x; clearvars endpoint_y;

% clearvars size_s_x; clearvars size_s_y;
% clearvars size_e_x; clearvars size_e_y;

clearvars s_rand_x; clearvars s_rand_y;
clearvars e_rand_x; clearvars e_rand_y;

%% generate path (1 means 'yes')

if size_e_x > 1
    if size_e_y < 2
        horizontal_e = 0;
        vertical_e = 1;
    else
        disp('wrong endpoint')
    end
elseif size_e_x < 2
    if size_e_y > 1
        horizontal_e = 1;
        vertical_e = 0;
    else
        disp('wrong endpoint')
    end
end

if size_s_x > 1
    if size_s_y < 2
        horizontal_s = 0;
        vertical_s = 1;
    else
        disp('wrong startpoint')
    end
elseif size_s_x < 2
    if size_s_y > 1
        horizontal_s = 1;
        vertical_s = 0;
    else
        disp('wrong startpoint')
    end
end


%%
keep = 1;

x = startpoint(1, 1);
y = startpoint(1, 2);
%%
if horizontal_e == 0 % vertical
    if x == endpoint(1, 1)
        keep = 0;
    end
elseif horizontal_e == 1 % horizontal
    if y == endpoint(1, 2)
        keep = 0;
    end
end

%% basic case
%% have to add and consider rocks

while keep == 1
     if horizontal_s == 0
         y_r = randperm(length);
         y = y_r(1, 1);
         if horizontal_e == 0 % vertical
            if x == endpoint(1, 1)
               keep = 0;
            end
         elseif horizontal_e == 1 % horizontal
            if y == endpoint(1, 2)
               keep = 0;
            end
         end
         t = horizontal_s;
         horizontal_s = vertical_s;
         vertical_s = t;
            
     elseif horizontal_s == 1
         x_r = randperm(width);
         x = x_r(1, 1);
         if horizontal_e == 0 % vertical
            if x == endpoint(1, 1)
               keep = 0;
            end
         elseif horizontal_e == 1 % horizontal
            if y == endpoint(1, 2)
               keep = 0;
            end
         end
         t = horizontal_s;
         horizontal_s = vertical_s;
         vertical_s = t;
     end
end

clearvars x_r; clearvars y_r;


