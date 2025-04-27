# Proyek Pertama: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Maju 

## Business Understanding
Jaya Jaya Maju adalah perusahaan multinasional yang telah beroperasi sejak tahun 2000 dengan lebih dari 1.000 karyawan di seluruh Indonesia. Meskipun sudah menjadi perusahaan besar, Jaya Jaya Maju menghadapi tantangan serius dalam pengelolaan karyawan, dengan attrition rate (rasio karyawan keluar) yang melampaui 10%. Kondisi ini berdampak pada:
- Meningkatnya biaya operasional.
- Menurunnya produktivitas kerja.
- Kehilangan talenta berpotensi tinggi.
Oleh karena itu, dibutuhkan analisis berbasis data untuk membantu perusahaan membuat strategi pengelolaan SDM yang lebih efektif dan efisien.

### Permasalahan Bisnis
Jaya Jaya Maju menghadapi masalah serius berupa tingginya tingkat attrition karyawan yang telah melampaui 10%. Kondisi ini berpotensi meningkatkan biaya operasional, menurunkan produktivitas, dan menyebabkan hilangnya pegawai potensial. Permasalahan utama yang dihadapi adalah sebagai berikut.
1. Tingginya tingkat attrition karyawan (> 10%)
2. Tidak adanya monitoring SDM yang sistematis
3. Kurangnya visibilitas terhadap tren dan faktor-faktor penyebab attrition.
4. Tidak adanya sistem prediksi dini risiko pengunduran diri.
5. Potensi kerugian finansial akibat tingginya biaya rekrutmen, pelatihan, dan turunnya produktivitas.

### Cakupan Proyek

Terdapat 4 (empat) poin penting yang menjadi cakupan proyek dalam menyelesaikan masalah terkait dengan pengelolaan sumber daya manusia dalam hal ini berfokus pada tingginya attrition rate karyawan di perusahaan Jaya Jaya Maju. Poin-poin tersebut mencakup attrition rate berdasarkan demografi karyawan, umpan balik yang diberikan oleh karyawan, pengalaman bekerja karyawan, dan kompensasi serta benefit yang didapatkan oleh karyawan. Berdasarkan poin-poin tersebut diperoleh cakupan proyek sebagai berikut.
- Demografi karyawan
1. Apakah ada perbedaan attrition rate berdasarkan usia, gender, atau status pernikahan?
2. Departemen mana yang memiliki tingkat attrition tertinggi?
3. Apakah tingkat pendidikan (SMA, Diploma, Sarjana, Pascasarjana) berpengaruh terhadap kecenderungan resign?
- Umpan Balik Karyawan
1. Seberapa besar pengaruh kepuasan terhadap lingkungan kerja terhadap keputusan karyawan untuk keluar?
2. Apakah tingkat kepuasan bekerja yang rendah berkorelasi langsung dengan meningkatnya risiko attrition?
3. Sejauh mana tingkat keterlibatan dalam pekerjaan memengaruhi kemungkinan karyawan untuk resign?
4. Bagaimana perbandingan work-life balance antara karyawan yang bertahan dan yang keluar?
- Pengalaman Bekerja
1. Apakah durasi kerja, total pelatihan yang diikuti, dan jumlah perusahaan sebelumnya berpengaruh terhadap risiko resign?
2. Bagaimana pengaruh perjalanan bisnis, jarak rumah ke kantor, dan status lembur terhadap tingkat attrition?
3. Apakah tingkat jabatan dan masa kerja di perusahaan mempengaruhi kecenderungan untuk keluar?
- Kompensasi dan benefit
1. Apakah terdapat hubungan antara job role, average monthly income, dan tingkat attrition?
2. Bagaimana pengaruh job satisfaction dan median income terhadap kemungkinan resign?
3. Sejauh mana salary hike dan stock option level berdampak terhadap risiko pengunduran diri?


### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv

The data contains demographic details, work-related metrics and attrition flag.
* EmployeeId - Employee Identifier
* Attrition - Did the employee attrition? (0=no, 1=yes)
* Age - Age of the employee
* BusinessTravel - Travel commitments for the job
* DailyRate - Daily salary
* Department - Employee Department
* DistanceFromHome - Distance from work to home (in km)
* Education - 1-Below College, 2-College, 3-Bachelor, 4-Master,5-Doctor
* EducationField - Field of Education
* EnvironmentSatisfaction - 1-Low, 2-Medium, 3-High, 4-Very High
* Gender - Employee's gender
* HourlyRate - Hourly salary
* JobInvolvement - 1-Low, 2-Medium, 3-High, 4-Very High
* JobLevel - Level of job (1 to 5)
* JobRole - Job Roles
* JobSatisfaction - 1-Low, 2-Medium, 3-High, 4-Very High
* MaritalStatus - Marital Status
* MonthlyIncome - Monthly salary
* MonthlyRate - Mounthly rate
* NumCompaniesWorked - Number of companies worked at
* Over18 - Over 18 years of age?
* OverTime - Overtime?
* PercentSalaryHike - The percentage increase in salary last year
* PerformanceRating - 1-Low, 2-Good, 3-Excellent, 4-Outstanding
* RelationshipSatisfaction - 1-Low, 2-Medium, 3-High, 4-Very High
* StandardHours - Standard Hours
* StockOptionLevel - Stock Option Level
* TotalWorkingYears - Total years worked
* TrainingTimesLastYear - Number of training attended last year
* WorkLifeBalance - 1-Low, 2-Good, 3-Excellent, 4-Outstanding
* YearsAtCompany - Years at Company
* YearsInCurrentRole - Years in the current role
* YearsSinceLastPromotion - Years since the last promotion
* YearsWithCurrManager - Years with the current manager

Setup environment:

```
pandas - Digunakan untuk manipulasi data dan analisis data.

numpy - Digunakan untuk komputasi numerik, operasi array, dan aljabar linear.

scikit-learn - Digunakan untuk machine learning, termasuk algoritma klasifikasi, regresi, clustering, dan evaluasi model.

matplotlib - Digunakan untuk visualisasi data dalam bentuk grafik 2D.

seaborn - Library visualisasi berbasis matplotlib yang memberikan interface yang lebih mudah untuk membuat grafik statistik.

scipy - Digunakan untuk komputasi ilmiah, termasuk optimasi, integrasi, interpolasi, eigenvalue, dll.

statsmodels - Digunakan untuk analisis statistik dan model statistik.

imbalanced-learn - Digunakan untuk menangani masalah ketidakseimbangan kelas dalam dataset untuk machine learning.
```

## Business Dashboard
Berdasarkan data yang ditampilkan, tingkat attrition atau pengunduran diri karyawan terlihat berbeda berdasarkan usia, gender, dan status pernikahan. Karyawan berusia 26–35 tahun memiliki tingkat attrition yang lebih tinggi dibanding kelompok usia lainnya. Selain itu, karyawan yang belum menikah cenderung lebih sering resign dibandingkan yang sudah menikah, untuk baik pria maupun wanita. Dari sisi departemen, R&D (Research & Development) mencatat tingkat attrition tertinggi dibanding HRD dan Sales. Ini menunjukkan bahwa tingkat ketahanan karyawan di R&D perlu mendapatkan perhatian lebih. Dalam hal latar belakang pendidikan, terlihat bahwa attrition terjadi di semua tingkat pendidikan, namun karyawan dengan gelar Sarjana (Bachelor) dan Master mendominasi jumlah pengunduran diri. Artinya, tingkat pendidikan lebih tinggi tidak serta-merta membuat karyawan lebih bertahan dalam perusahaan. Sementara itu, berdasarkan feedback karyawan, proporsi tingkat kepuasan karyawan terhadap lingkungan kerja (Environment Satisfaction) dan kepuasan kerja (Job Satisfaction) menunjukkan pola yang cukup serupa. Sekitar 30% karyawan merasa sangat puas (skor 4) dan 30% lainnya puas (skor 3). Sementara itu, sisanya (sekitar 39%) merasa kurang puas atau tidak puas. Jika ditinjau dari tingkat keterlibatan karyawan (Job Involvement), sekitar 59% karyawan melaporkan memiliki keterlibatan kerja yang tinggi (skor 3). Menariknya, di kelompok ini, attrition rate relatif rendah, yaitu hanya sekitar 8%, menunjukkan bahwa keterlibatan tinggi dapat membantu menekan angka turnover. Dalam hal Work-Life Balance, data menunjukkan bahwa sebagian besar karyawan (60%) merasa memiliki work-life balance yang baik (skor 3). Hanya sekitar 5% karyawan yang merasa memiliki work-life balance yang buruk (skor 1), yang mengindikasikan bahwa manajemen waktu kerja dan kehidupan pribadi umumnya berjalan cukup seimbang di perusahaan ini. Visualisasi dalam dashboard juga memperjelas bahwa semakin rendah tingkat kepuasan terhadap lingkungan kerja, kepuasan kerja, keterlibatan kerja, dan work-life balance, semakin tinggi kecenderungan karyawan untuk keluar dari perusahaan. Faktor Total Working Years dan Duration at Company memperlihatkan bahwa risiko resign tertinggi terjadi di masa awal karir (0–9 tahun) dan menurun drastis seiring bertambahnya pengalaman dan loyalitas. Total Training Completed menggambarkan bahwa mayoritas karyawan menerima 2-3 pelatihan, tetapi tingginya pelatihan tidak secara signifikan mengurangi risiko attrition. Faktor Business Travel juga menarik untuk dicermati. Karyawan yang "Travel Rarely" justru menunjukkan angka attrition lebih tinggi dibandingkan mereka yang "Travel Frequently" atau bahkan tidak melakukan perjalanan bisnis sama sekali.Dalam hal Total Companies Worked, semakin banyak perusahaan yang pernah menjadi tempat kerja karyawan, semakin besar kecenderungan mereka untuk resign lagi di masa depan, menandakan adanya pola mobilitas karir yang tinggi. Distance from Home ternyata tidak terlalu berpengaruh signifikan terhadap keputusan resign, baik bagi yang tinggal dekat maupun jauh dari kantor. Job Level menunjukkan bahwa karyawan di level rendah (1-2) memiliki risiko attrition lebih tinggi dibandingkan level senior. Sedangkan dari sisi Overtime Status, lembur berhubungan kuat dengan tingginya tingkat resign: karyawan yang sering lembur lebih cenderung meninggalkan perusahaan. Terdapat hubungan erat antara job role, average monthly income, dan tingkat attrition. Jabatan dengan pendapatan lebih tinggi seperti Manager cenderung memiliki tingkat pengunduran diri lebih rendah, namun beberapa jabatan seperti Research Director tetap menunjukkan attrition tinggi meski berpenghasilan besar. Selain itu, karyawan dengan job satisfaction rendah dan median income lebih kecil cenderung lebih mudah resign dibandingkan mereka yang lebih puas dan berpenghasilan lebih tinggi. Kenaikan gaji (salary hike) yang besar dan pemberian stock option level tinggi terbukti efektif menurunkan risiko pengunduran diri, menunjukkan pentingnya strategi kompensasi dalam mempertahankan karyawan.


## Conclusion
Berdasarkan hasil analisis, tingkat attrition di Jaya Jaya Maju dipengaruhi oleh berbagai faktor penting. Dari sisi demografi, karyawan berusia 26–35 tahun dan yang belum menikah memiliki kecenderungan resign lebih tinggi. Departemen Research & Development (R&D) mencatat tingkat pengunduran diri tertinggi, menunjukkan perlunya perhatian khusus dalam retensi di unit tersebut. Dalam hal pendidikan, karyawan bergelar Sarjana dan Master justru mendominasi angka resign, menandakan bahwa pendidikan tinggi tidak otomatis meningkatkan loyalitas. Analisis employee feedback menunjukkan bahwa tingkat kepuasan terhadap lingkungan kerja, kepuasan kerja, keterlibatan dalam pekerjaan, dan work-life balance sangat berkorelasi dengan risiko pengunduran diri. Semakin rendah tingkat kepuasan dan keterlibatan, semakin tinggi potensi turnover. Faktor pengalaman kerja seperti masa kerja pendek (0–9 tahun), mobilitas antar perusahaan yang tinggi, beban lembur berlebih, serta jabatan rendah (level 1-2) juga menjadi penyebab utama tingginya attrition. Dari sisi kompensasi, jabatan dengan pendapatan bulanan lebih tinggi dan karyawan yang menerima kenaikan gaji serta stock option memiliki risiko resign yang jauh lebih rendah, memperkuat pentingnya peran kompensasi dalam mempertahankan talenta.

### Rekomendasi Action Items (Optional)

Berikut action item yang dapat dijalankan oleh perusahaan

- Fokus retensi usia muda dengan membuat program mentoring dan career development serta membuat career path yang jelas
- Tingkatkan kepuasan dan keterlibatan karyawan dengan melakukan survei kepuasan rutin dan tindak lanjuti feedback karyawan. Dan lakukan pengembangan program employee engagement seperti penghargaan dan internal event.
- Optimalkan Work-Life balance dengan menerapkan kebijakan fleksibilitas jam kerja, WFA, remote working, serta lakukan management beban kerja untuk setiap departemen
- Perbaiki retensi di departemen R&D dengan melakukan evaluasi beban kerja, kompensasi, dan kultur kerja di departemen ini
- Perkuat strategi kompensasi dengan menyesuaikan salary structure berdasarkan benchmark industri dan buat kebijakan kenaikan gaji berkala, bonus kinerja, dan program stock option
- Manajemen mobilitas karir dengan bijak untuk membuka kesempatan rotasi antar departemen atau rotasi antar job role untuk karyawan dan lakukan  career coaching untuk karyawan yang memiliki riwayat pindah kerja tinggi
- Minimalkan risiko dari overtime dengan membatasi jumlah lembur dan berikan kompensasi waktu atau insentif bagi karyawan yang terpaksa lembur
- Menjalankan program onboarding dan early retention untuk karyawan baru (0–9 tahun masa kerja) agar cepat beradaptasi
