clf
clear all;
close all;
fclose('all');
global FontS;
FontS=20; % Set the font size
fprintf('\N Dont forget to change INPUT FILENAME! \n');

%% FIRST extract the sensofar.plux file with 7Zip. 
% You will get a LAYER_0.raw, LAYER_0.stack.raw, recipe.txt and ANALYSIS
% subfolder (where you have display.txt and recipe.txt) 
% N.B: There are two recipe.txt files and the RECIPE.TXT which contains measuremt settings 
% is the one inside the ANALYSIS folder.

fin=fopen('LAYER_0.raw','r');                 % Read in raw data file
meas_settings=importdata('recipe.txt');       % Read in measurement settings
data_original = fread(fin, 'single');         % Single line vector
[z_inp,dx,dy,x,y,NX,NY]=processing_general(data_original,meas_settings);     % Get step size, surface size and dimension
z_inp=fillmissing(z_inp,'linear');   % Fill missing values using linear interpolation of neighboring, non-missing values

%% 
Input_surface_filename='Part - 2';

%% FIT THE SURFACE PROFILE & CORRECT THE TILT AND SHIFT TO ZERO REFERENCE PLANE
% First reshape the matrices [x,y,z] so that they are compatible to do curve fitting analysis.

[x, y]=meshgrid(x,y);             
x_vec=reshape(x,[(NX*NY),1]);      % Vector containing X-coordinates
y_vec=reshape(y,[(NX*NY),1]);      % Vector containing Y-coordinates
z_vec=reshape(z_inp,[(NX*NY),1]);  % Vector containing Y-coordinates

[sf] = fit([x_vec, y_vec],z_vec,'poly11'); % Pol11- linear, pol22- quadratic (for ROLL SURFACE!!)
% plot(sf,[x_vec, y_vec],z_vec)
data_interp = sf([x_vec, y_vec]); % surface height values of the interpolated function
data_interp_re=reshape(data_interp,[NY, NX]); % Vector containing Y-coordinates
z=z_inp-data_interp_re; % Shifted (to zero) and Tilt corrected surface roughness

%% ROUGHNESS VALUES
Ra=mean(abs(z(:)));          % Ra roughness value
Rq = std(z(:));              % Rq roughness value  

%% Plotting corrected surface topography
close all;
h1=figure; 
set(h1, 'Name', 'Surface topography');
h2=surf (x,y,z);
view(2);
colormap jet;
c = colorbar;
c.Label.String = 'Surface height (\mum)';
set(h2, 'edgecolor','none');
axis([0 max(x_vec) 0 max(y_vec)]);  % In case of 3D axis([0 max(xx_1) 0 max(yy_1) min(z(:)) max(z(:))]);
xlabel('x (\mum)', 'fontsize', FontS); ylabel('y (\mum)', 'fontsize', FontS);zlabel('Height (\mum)', 'fontsize', FontS);
title('Strip surface');
set(gca,'FontSize',FontS);
axis equal;
axis tight;

%% SURFACE HEIGHT DISTRIBUTION AND BEARING AREA

% Surface height distribution and bearing area curve
nbins=400; % Number of bins in the histogram distribution
% edges=linspace(min(z(:)),max(z(:)),nbins+1);
edges=linspace(-13,17,nbins+1);
[Z_old_pdf,Z_old_val]=histcounts(z(:),edges, 'Normalization', 'probability');
Z_val = ((Z_old_val(1:end-1) + Z_old_val(2:end))/2)';
binwidth = (Z_old_val(end)-Z_old_val(1))/nbins;               % The width of each bin in histogram
Z_pdf_nonnormalized = Z_old_pdf';                             % This is the PDF without normaliz
Z_pdf = Z_pdf_nonnormalized/binwidth';                                % This is the normalized PDF with the bin width
Bearing_area= 1- cumsum(Z_pdf_nonnormalized); 


% HEIGHT DISTRIBUTION
h3=figure;
plot(Z_val,Z_pdf,'LineWidth',1.5);
% hold on
% plot(sep,norm_surface_pdf,'LineWidth',1.5);
grid on
set(h3, 'Name', 'Surface height PDF');
xlabel(' Height (\mum)', 'fontsize', FontS); 
ylabel('Frequency', 'fontsize', FontS);
title('Surface height PDF')
% legend('Measured surface');
set(gca,'FontSize',FontS);

% BEARING AREA
h5=figure;
plot(fliplr(Z_val),Bearing_area,'LineWidth',1.5);
% hold on
% plot(sep,norm_surface_cdf,'LineWidth',1.5);
xlabel('Height in (\mum) ', 'fontsize', FontS); ylabel('Bearing area', 'fontsize', FontS);
% legend('Measured surface');
title('Bearing Area')
set(gca,'FontSize',FontS);


 %% WRITING TO THE FILE - surface Height, PDF and CDF

% Writing height in csv file
 filename = strcat(Input_surface_filename,'.csv');
 fileID = fopen(filename,'w');
 fprintf(fileID, 'Row 1 = dx - resolution along x, Row 2 = dy - resolution along y \n');
 fprintf(fileID, 'Row 3 = NX - number of pixels along x, Row 4 = NY - number of pixels along y \n');
 fprintf(fileID, '%6.2f  \n', dx);
 fprintf(fileID, '%6.2f  \n', dy);
 fprintf(fileID, '%6.2f  \n', NX);
 fprintf(fileID, '%6.2f  \n', NY);
 fprintf(fileID, '\n \n');
 dlmwrite(filename,z,'-append');
 fclose(fileID);


 % Writing Ra, Rq, PDF & BA of the surface into csv file
 tpv=horzcat(Z_val,Z_pdf,Bearing_area); % Horizontally concatenating 
 filename1 = strcat(Input_surface_filename,'Ra Rq PDF & BA.txt');
 fileID = fopen(filename1,'w');
 fprintf(fileID, 'Row 1 = Ra (microns), Row 2 = Rq (microns) \n');
 fprintf(fileID, 'Column 1 = Height, Column 2 = PDF and Column 3 = CDF \n');
 fprintf(fileID, '%6.2f  \n', Ra);
 fprintf(fileID, '%6.2f  \n', Rq);
 fprintf(fileID, '\n \n');
 dlmwrite(filename1,tpv,'-append','delimiter','\t','precision',12);
 fclose(fileID);
 fclose('all');


function [z_inp,dx,dy,x,y, NX, NY]=processing_general(data_original,meas_settings)

% Obtain strings for dx,dy,NX,NY and remove unnecessary symbols from strings

% A = cell2mat(meas_settings)
x_step=regexprep(meas_settings(6),'[^0-9 .]','');
y_step=regexprep(meas_settings(7),'[^0-9 .]','');
NX=regexprep(meas_settings(8),'[^0-9 .]','');
NY=regexprep(meas_settings(9),'[^0-9 .]','');

% Convert strings to numeric values
% dx=str2double(x_step)*1e-3;        % Rescale to millimeter dimension
dx=str2double(x_step);          
dy=str2double(y_step);
NX=str2double(NX);                   % Number of pixels in x direction
NY=str2double(NY);                   % Number of pixels in y direction
z_inp=reshape(data_original,NX,NY)';  % Reshape original data (vector) to measurement size (matrix)
z_inp=flip(z_inp);
x=0:dx:(NX-1)*dx;                    % Generating x and y coordinates            
y=0:dy:(NY-1)*dy; 
end 

