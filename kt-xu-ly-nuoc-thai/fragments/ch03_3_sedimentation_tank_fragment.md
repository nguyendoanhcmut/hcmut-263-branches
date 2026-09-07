## Chương 03.3: Bể Lắng sơ bộ & Đợt 1 (Sedimentation Tank)

### 1. Tổng quan & Bản chất Động học Quá trình Lắng (Sedimentation Overview & Physics)
#### 1.1. Mục đích, Vai trò và Vị trí Dây chuyền Công nghệ
##### 1.1.1. Định nghĩa và Cơ chế Phân tách Trọng lực
###### 1.1.1.1. Khái niệm và Mục tiêu Công nghệ
- **Bể lắng (Sedimentation Tank / Settling Basin / Clarifier):** Là công trình xử lý cơ học đóng vai trò then chốt trong hệ thống xử lý nước thải, áp dụng hiện tượng phân tách trọng lực để loại bỏ các phần tử chất rắn có khối lượng riêng lớn hơn khối lượng riêng của nước thải ($\rho_s > \rho_w$).
- **Mục tiêu công nghệ chính:**
  - Tách cặn lơ lửng có khả năng lắng (settleable suspended solids) nhằm giảm thiểu hàm lượng chất rắn lơ lửng ($\text{TSS}$) trong dòng nước.
  - Tách các chất nổi, dầu mỡ, váng bọt (scum, oil and grease) có khối lượng riêng bé hơn nước ($\rho_{scum} < \rho_w$) thông qua hệ thống gạt váng mặt nước.
  - Làm trong pha lỏng (clarification) đồng thời cô đặc pha rắn ở đáy bể (sludge thickening).

###### 1.1.1.2. Cân bằng Lực tác động lên Hạt Lắng trong Chất lỏng
- **Trọng lực hướng xuống ($F_g$):**
  $$F_g = m \cdot g = \rho_s \cdot V_p \cdot g$$
  - $\rho_s$: Khối lượng riêng của hạt cặn ($\text{kg/m}^3$).
  - $V_p$: Thể tích của hạt cặn ($\text{m}^3$), đối với hạt hình cầu bán kính $r$, đường kính $d$: $V_p = \frac{\pi \cdot d^3}{6}$.
  - $g$: Gia tốc trọng trường ($g \approx 9.81\text{ m/s}^2$).
- **Lực đẩy Archimedes hướng lên ($F_b$):**
  $$F_b = \rho_w \cdot V_p \cdot g$$
  - $\rho_w$: Khối lượng riêng của nước thải ($\rho_w \approx 1000\text{ kg/m}^3$ ở $20^\circ\text{C}$).
- **Lực cản ma sát thủy động học ngược chiều chuyển động ($F_d$):**
  $$F_d = C_D \cdot A_p \cdot \frac{\rho_w \cdot v_s^2}{2}$$
  - $C_D$: Hệ số lực cản thủy động (Newton drag coefficient, không thứ nguyên).
  - $A_p$: Diện tích hình chiếu của hạt cặn vuông góc với hướng chuyển động ($\text{m}^2$); với hạt cầu: $A_p = \frac{\pi \cdot d^2}{4}$.
  - $v_s$: Vận tốc lắng tương đối của hạt đối với chất lỏng ($\text{m/s}$).
- **Cân bằng động học tại trạng thái lắng ổn định (Terminal Settling Velocity):**
  - Khi hạt đạt vận tốc lắng cực đại không đổi, gia tốc $\frac{dv}{dt} = 0$, lực tổng hợp triệt tiêu:
    $$F_g - F_b - F_d = 0 \implies (\rho_s - \rho_w) \cdot V_p \cdot g = C_D \cdot A_p \cdot \frac{\rho_w \cdot v_s^2}{2}$$
  - Thay $V_p = \frac{\pi d^3}{6}$ và $A_p = \frac{\pi d^2}{4}$:
    $$v_s = \sqrt{\frac{4 \cdot g \cdot (\rho_s - \rho_w) \cdot d}{3 \cdot C_D \cdot \rho_w}} = \sqrt{\frac{4 \cdot g \cdot (s - 1) \cdot d}{3 \cdot C_D}}$$
    với $s = \frac{\rho_s}{\rho_w}$ là tỷ trọng tương đối của hạt so với nước.

##### 1.1.2. Vị trí Công nghệ của Bể Lắng trong Trạm XLNT
###### 1.1.2.1. Lắng Sơ bộ / Đợt 1 (Primary Clarifier - Trước Công trình Xử lý Sinh học)
- **Vị trí bố trí:** Nằm ngay sau các công trình tiền xử lý cơ học (Song chắn rác / Lưới lọc rác thô và Bể thu cát Grit Chamber), và trước các bể phản ứng sinh học kỵ khí/thiếu khí/hiếu khí (như Bể Selector, Aerotank, SBR, BNR, Bể Lọc Sinh học nhỏ giọt Trickling Filter).
- **Mục đích:** Tách phần lớn cặn lơ lửng hữu cơ kích thước lớn và vừa có khả năng phân rã, bảo vệ thiết bị sục khí cơ học, chống sa lắng bùn vô cơ nặng trong bể sinh học, và giảm tải trọng chất hữu cơ đầu vào.

###### 1.1.2.2. Lắng Sau Quá trình Keo tụ - Tạo bông (Chemically Enhanced Settling / Post-Flocculation)
- **Vị trí bố trí:** Sau bể trộn nhanh (Rapid Mix) và bể phản ứng tạo bông (Flocculation Basin) trong các công nghệ xử lý hóa lý (như xử lý nước thải dệt nhuộm, xi mạ, thuộc da, giấy, hoặc khử Phosphor hóa học bằng phèn nhôm/sắt).
- **Mục đích:** Tách các bông cặn hydroxit kim loại và chất ô nhiễm dạng keo đã được bất hoạt và kết cụm.

###### 1.1.2.3. Lắng Đợt 2 (Secondary Clarifier / Final Settling Tank - Sau Xử lý Sinh học)
- **Vị trí bố trí:** Nằm trực tiếp sau bể phản ứng sinh học hiếu khí bùn hoạt tính (Aerotank), bể sục khí phân đoạn (Step-feed), mương oxy hóa (Oxidation Ditch) hoặc bể lọc sinh học tiếp xúc bám dính.
- **Mục đích:**
  - Tách sinh khối vi sinh vật (bùn hoạt tính - Mixed Liquor Suspended Solids - $\text{MLSS}$) ra khỏi nước sau xử lý để đạt độ trong đạt quy chuẩn xả thải.
  - Cô đặc bùn hoạt tính ở đáy bể để tuần hoàn ngược lại bể sinh học (Return Activated Sludge - $\text{RAS}$) với tỷ lệ tuần hoàn $R = Q_r / Q = 0.25 - 1.0$ nhằm duy trì nồng độ vi sinh vật cần thiết.
  - Xả bỏ lượng sinh khối dư sinh trưởng hàng ngày (Waste Activated Sludge - $\text{WAS}$) đến công trình xử lý bùn cặn.

##### 1.1.3. Hiệu suất Xử lý Đặc trưng của Bể Lắng Sơ bộ
###### 1.1.3.1. Hiệu quả Tách Cặn Lơ lửng ($\text{TSS}$)
- **Phạm vi hiệu suất chuẩn:** Tách được từ $50\% - 70\%$ tổng lượng $\text{TSS}$ trong nước thải sinh hoạt đô thị.
- **Hàm lượng $\text{TSS}$ sau lắng đợt 1:** Thường giảm từ $200 - 350\text{ mg/L}$ xuống còn khoảng $70 - 120\text{ mg/L}$.
- **Tác động của việc bổ sung hóa chất keo tụ (Chemically Enhanced Primary Treatment - CEPT):** Bổ sung phèn sắt/nhôm ($15 - 50\text{ mg/L}$) hoặc polymer anion/cation ($0.2 - 1.0\text{ mg/L}$) có thể nâng hiệu suất khử $\text{TSS}$ lên tới $80\% - 90\%$.

###### 1.1.3.2. Hiệu quả Khử Chất Hữu cơ ($\text{BOD}_5$ và $\text{COD}$)
- **Phạm vi khử $\text{BOD}_5$:** Tách từ $25\% - 40\%$ tổng $\text{BOD}_5$ của nước thải thô (chủ yếu là thành phần $\text{BOD}$ dạng hạt lơ lửng không tan - Particulate $\text{BOD}$).
- **Phạm vi khử $\text{COD}$:** Đạt $30\% - 40\%$ tổng $\text{COD}$ đầu vào.
- **Thành phần hữu cơ còn lại:** Các hợp chất hòa tan (Soluble $\text{BOD}$, Soluble $\text{COD}$) và chất keo mịn không lắng được bằng trọng lực đơn thuần sẽ đi tiếp vào bể xử lý sinh học.

###### 1.1.3.3. Tách Dầu mỡ, Váng bọt và Lợi ích Kinh tế Kỹ thuật
- **Thu gom dầu mỡ bề mặt:** Tách $50\% - 60\%$ váng nổi, dầu khoáng tự do, chất béo động thực vật thông qua tấm gạt bọt váng và ống xẻ rãnh quay.
- **Lợi ích vận hành trạm:**
  - Tiết kiệm $20\% - 30\%$ điện năng cung cấp oxy của máy thổi khí ở bể Aerotank do đã cắt giảm đáng kể tải trọng $\text{BOD}_5$ nạp vào.
  - Giảm thể tích công trình sinh học yêu cầu và nâng cao độ ổn định bùn hoạt tính.
  - Sinh ra bùn sơ bộ (Primary Sludge) có khả năng phân hủy kỵ khí sinh khí Biogas ($\text{CH}_4$) cao hơn nhiều so với bùn sinh học dư.

---

#### 1.2. Phân loại 4 Cơ chế Lắng Điển hình (Four Types of Settling)
##### 1.2.1. Lắng Loại 1: Lắng Hạt Đơn lẻ (Type 1 - Discrete Particle Settling)
###### 1.2.1.1. Định nghĩa và Đặc trưng Vật lý
- **Đặc điểm hạt:** Hạt rắn chuyển động lắng độc lập trong môi trường chất lỏng loãng; không thay đổi kích thước, hình dạng, thể tích và khối lượng riêng trong suốt thời gian rơi lắng.
- **Tương tác giữa các hạt:** Bằng không ($0$); nồng độ chất rắn rất thấp, các đường dòng thủy động xung quanh mỗi hạt không gây nhiễu loạn lẫn nhau.
- **Ứng dụng thực tế điển hình:**
  - Quá trình lắng cát, hạt khoáng, sạn, sỏi trong Bể thu cát (Grit Chamber).
  - Phân tách cát lắng trong bể lắng sơ bộ công nghiệp khoáng sản.

###### 1.2.1.2. Định luật Stokes và Phương trình Vận tốc Lắng
- **Vùng chảy tầng (Laminar flow, $Re_p < 1$):**
  - Hệ số lực cản thủy động theo nghiệm giải tích của Stokes:
    $$C_D = \frac{24}{Re_p}$$
    với số Reynolds của hạt lắng xác định bởi:
    $$Re_p = \frac{v_s \cdot d}{\nu} = \frac{\rho_w \cdot v_s \cdot d}{\mu}$$
    Trong đó: $\nu$ là độ nhớt động học của nước ($\text{m}^2/\text{s}$, $\nu \approx 1.003 \times 10^{-6}\text{ m}^2/\text{s}$ ở $20^\circ\text{C}$); $\mu$ là độ nhớt động lực học ($\text{Pa}\cdot\text{s}$ hoặc $\text{N}\cdot\text{s/m}^2$, $\mu \approx 1.003 \times 10^{-3}\text{ N}\cdot\text{s/m}^2$ ở $20^\circ\text{C}$).
  - Thay $C_D = \frac{24 \mu}{\rho_w v_s d}$ vào phương trình cân bằng lực tổng quát:
    $$v_s = \frac{g \cdot (\rho_s - \rho_w) \cdot d^2}{18 \cdot \mu} = \frac{g \cdot (s - 1) \cdot d^2}{18 \cdot \nu}$$
- **Vùng chuyển tiếp (Transition zone, $1 < Re_p < 1000$):**
  - Hệ số cản xấp xỉ theo công thức thực nghiệm:
    $$C_D \approx \frac{24}{Re_p} + \frac{3}{\sqrt{Re_p}} + 0.34 \quad \text{hoặc} \quad C_D \approx \frac{18.5}{Re_p^{0.6}}$$
  - Vận tốc lắng được tính lặp (iteration) hoặc qua công thức thực nghiệm:
    $$v_s = \left[ \frac{4}{45} \cdot \frac{(\rho_s - \rho_w)^2 \cdot g^2}{\rho_w \cdot \mu} \right]^{1/3} \cdot d$$
- **Vùng chảy rối (Turbulent flow, $Re_p > 1000$):**
  - Hệ số cản đạt giá trị không đổi phụ thuộc hình học hạt ($C_D \approx 0.44$ đối với hạt hình cầu hoàn hảo):
    $$v_s = \sqrt{\frac{4 \cdot g \cdot (\rho_s - \rho_w) \cdot d}{3 \cdot (0.44) \cdot \rho_w}} \approx 1.74 \cdot \sqrt{g \cdot (s - 1) \cdot d}$$

###### 1.2.1.3. Lý thuyết Bể Lắng Lý tưởng Hazen (Ideal Settling Basin Theory)
- **Các giả thiết cơ bản của Hazen:**
  - Dòng chảy qua bể là dòng chảy nút lý tưởng (Ideal Plug Flow), vận tốc ngang $v_H$ đồng đều tại mọi điểm trên tiết diện ướt.
  - Nồng độ cặn phân bố đều trên toàn bộ chiều cao mặt cắt ướt tại cửa vào ($t = 0, x = 0$).
  - Bất kỳ hạt cặn nào chạm đáy bể lắng được coi như đã lắng hoàn toàn và không bị cuốn ngược trở lại dòng chảy.
- **Tải trọng bề mặt tới hạn (Critical Surface Overflow Rate - $v_0$):**
  - Xét bể lắng hình chữ nhật có chiều dài $L$, chiều rộng $W$, chiều sâu hữu dụng $D$:
    - Diện tích bề mặt lắng: $A_s = L \times W$ ($\text{m}^2$).
    - Tiết diện ngang ướt: $A_c = W \times D$ ($\text{m}^2$).
    - Thể tích công tác: $V = L \times W \times D$ ($\text{m}^3$).
    - Thời gian lưu nước danh định: $t_d = \frac{V}{Q} = \frac{L}{v_H}$.
  - Hạt cặn có vận tốc lắng $v_0$ rơi từ mép mặt nước cao nhất ($y = D$) và chạm đáy bể vừa đúng tại cửa ra ($x = L$):
    $$t_d = \frac{D}{v_0} = \frac{L}{v_H} \implies v_0 = \frac{D}{t_d} = \frac{D \cdot Q}{V} = \frac{D \cdot Q}{L \cdot W \cdot D} = \frac{Q}{A_s} = \text{SOR}$$
- **Quy tắc phân tách hạt theo vận tốc lắng Hazen:**
  - **Trường hợp 1:** Những hạt cặn có vận tốc lắng $v_s \ge v_0$ sẽ được lắng giữ lại $100\%$ trong bể, bất kể hạt đi vào ở độ cao nào.
  - **Trường hợp 2:** Những hạt cặn có vận tốc lắng $v_s < v_0$ chỉ được lắng một phần theo tỷ lệ chiều cao ban đầu so với $D$:
    $$\text{Tỷ lệ lắng riêng phần } X_i = \frac{v_{s,i}}{v_0}$$
- **Tổng hiệu suất loại bỏ chất rắn của bể lắng lý tưởng:**
  $$X_T = (1 - F_0) + \int_{0}^{F_0} \frac{v_s}{v_0} \, dF$$
  Trong đó: $F_0$ là phần trăm cặn có vận tốc lắng bé hơn $v_0$ trên đường cong phân bố tích lũy vận tốc lắng $F(v_s)$.

##### 1.2.2. Lắng Loại 2: Lắng Tạo bông (Type 2 - Flocculent Settling)
###### 1.2.2.1. Cơ chế Động học Biến đổi Kích thước và Vận tốc
- **Đặc điểm hạt lắng:** Hạt cặn có tính chất keo dính hoặc sinh học; trong quá trình rơi chìm tự do, các hạt chuyển động với vận tốc khác nhau xảy ra va chạm cơ học, liên kết dính kết lại thành những bông cặn lớn hơn (coalescence / aggregation).
- **Sự thay đổi thông số hạt:** Khi kích thước $d$ tăng lên, tỷ trọng tương đối $s$ có thể giảm nhẹ do giữ nước mao quản, nhưng đường kính tăng bậc 2 bậc 3 khiến tốc độ rơi $v_s$ gia tăng liên tục theo thời gian và chiều sâu:
  $$\frac{dv_s}{dt} > 0 \quad \text{và} \quad \frac{dv_s}{dz} > 0$$
- **Quỹ đạo lắng:** Đường cong phi tuyến uốn cong xuống dưới (parabolic trajectory) thay vì đường thẳng như lắng loại 1.
- **Ứng dụng thực tế:**
  - Bể lắng đợt 1 (Primary Clarifier) xử lý nước thải sinh hoạt.
  - Bể lắng sau quá trình keo tụ tạo bông hóa lý (Coagulation - Flocculation).
  - Tầng trên cùng của Bể lắng đợt 2 (vùng nước trong bên trên lớp bùn).

###### 1.2.2.2. Thí nghiệm Cột Lắng Định hình (Settling Column Test)
- **Thiết bị thí nghiệm:** Cột hình trụ trong suốt có đường kính tối thiểu $150 - 200\text{ mm}$ (để loại bỏ ảnh hưởng biên của thành ống), chiều cao tương đương chiều sâu thiết kế bể lắng thực tế ($2.5 - 4.0\text{ m}$).
- **Cửa lấy mẫu (Sampling Ports):** Bố trí các vòi lấy mẫu dọc theo chiều sâu cột với khoảng cách đều nhau (ví dụ: ở các độ sâu $h_1 = 0.5\text{ m}, h_2 = 1.0\text{ m}, h_3 = 1.5\text{ m}, h_4 = 2.0\text{ m}, \dots$).
- **Quy trình thí nghiệm:**
  - Nạp đầy nước thải đã khuấy đều vào cột ($t = 0$), xác định nồng độ cặn lơ lửng ban đầu $C_0$ ($\text{mg/L}$).
  - Cho nước lắng tĩnh trong điều kiện nhiệt độ không đổi.
  - Lấy mẫu tại tất cả các độ sâu $h_j$ tại các thời điểm kế tiếp $t_1, t_2, t_3, \dots$ (ví dụ: $10, 20, 40, 60, 90, 120\text{ min}$).
  - Phân tích nồng độ cặn $C(h_j, t_i)$, xác định tỷ lệ phần trăm cặn đã lắng tại mỗi điểm:
    $$R(h_j, t_i) = \left( 1 - \frac{C(h_j, t_i)}{C_0} \right) \times 100\%$$

###### 1.2.2.3. Đường Đẳng Nồng độ & Phương pháp Tính Tổng Hiệu suất Khử Cặn
- **Biểu đồ Isoconcentration Curves:** Vẽ trục tung là chiều sâu cột lắng $Z$ (hướng xuống), trục hoành là thời gian lắng $t$. Nối các điểm có cùng giá trị hiệu quả loại bỏ $R\%$ để tạo thành các đường đẳng hiệu suất cong (ví dụ: $30\%, 40\%, 50\%, 60\%, 70\%, 80\%$).
- **Công thức tích phân tổng hiệu suất loại bỏ ($R_T$):**
  - Với một thời gian lưu nước $t_0$ đã chọn, kẻ đường thẳng đứng $t = t_0$ cắt các đường đẳng hiệu suất tại các độ sâu $h_1, h_2, h_3, \dots, h_n$ (với $h_n$ tương ứng đáy bể $Z_{tot}$):
    $$R_T = \sum_{j=1}^{n} \left[ \frac{\Delta h_j}{Z_{tot}} \cdot \frac{R_j + R_{j-1}}{2} \right] = \frac{\Delta h_1}{Z_{tot}} \cdot \frac{R_0 + R_1}{2} + \frac{\Delta h_2}{Z_{tot}} \cdot \frac{R_1 + R_2}{2} + \dots + \frac{\Delta h_n}{Z_{tot}} \cdot \frac{R_{n-1} + R_n}{2}$$
  - **Hệ số an toàn thực tế từ quy mô cột lắng sang bể thực tế (Scale-up factors):**
    - Hiệu ứng dòng đoản mạch, phân tầng nhiệt và gió làm giảm hiệu suất bể thực tế. Do đó:
      - Thời gian lưu thiết kế: $t_{\text{thiết kế}} = t_0 \times (1.25 - 1.75)$ (thường lấy $1.5 \times t_0$).
      - Tải trọng bề mặt thiết kế: $\text{SOR}_{\text{thiết kế}} = \left( \frac{Z_{tot}}{t_0} \right) \times (0.65 - 0.85)$ (thường lấy $0.70 \times \text{SOR}_{\text{cột}}$).

##### 1.2.3. Lắng Loại 3: Lắng Cản trở / Lắng Vùng (Type 3 - Hindered / Zone Settling)
###### 1.2.3.1. Cơ chế Tương tác Giữa các Bông cặn ở Nồng độ Cao
- **Điều kiện phát sinh:** Xảy ra khi nồng độ chất rắn lơ lửng trong hỗn hợp nước thải vượt qua ngưỡng trung bình ($C > 500 - 2000\text{ mg/L}$ đối với bùn hoạt tính sinh học).
- **Bản chất động lực học:** Khoảng cách giữa các hạt liền kề rất nhỏ; trường thủy động của mỗi hạt bao bọc và gây cản trở lẫn nhau. Nước bị chiếm chỗ phải di chuyển ngược lên qua các khe hở hẹp giữa các hạt với vận tốc dòng đi lên cao ($v_{\text{up}} > 0$).
- **Sự chuyển động đồng khối:** Toàn bộ các hạt cặn bị khóa vào một mạng lưới cấu trúc liên kết và rơi xuống cùng nhau với cùng một vận tốc đồng nhất, duy trì vị trí tương đối cố định với các hạt xung quanh.

###### 1.2.3.2. Sự Hình thành Mặt phân giới Nước - Bùn (Sludge Blanket Interface)
- **Ranh giới phân lớp:** Phía trên lớp bùn hình thành một mặt phân giới chất lỏng - bùn cực kỳ rõ rệt (liquid-sludge interface).
- **Phân tách pha:**
  - Phía trên mặt phân giới: Nước trong vắt gần như không có cặn lơ lửng.
  - Phía dưới mặt phân giới: Khối huyền phù bùn đậm đặc đang di chuyển xuống dưới với vận tốc lắng vùng $v_i$.
- **Vận tốc lắng vùng theo nồng độ bùn (Hàm thực nghiệm Vesilind):**
  $$v_i = v_0 \cdot e^{-n \cdot C_i}$$
  Trong đó: $v_0$ là vận tốc lắng giới hạn tối đa ở nồng độ cực loãng ($\text{m/h}$); $n$ là thông số đặc trưng độ nén của bùn ($\text{m}^3/\text{kg}$); $C_i$ là nồng độ bùn tại tầng khảo sát ($\text{kg/m}^3$).

###### 1.2.3.3. Lý thuyết Thông lượng Chất rắn (Solids Flux Theory - SFT)
- **Khái niệm Thông lượng Chất rắn ($G$):** Là khối lượng chất rắn di chuyển qua một đơn vị diện tích bề mặt bể trong một đơn vị thời gian ($\text{kg/m}^2\cdot\text{h}$ hoặc $\text{kg/m}^2\cdot\text{d}$).
- **Tổng thông lượng chất rắn qua một tiết diện ngang bể ($G_T$):** Bao gồm 2 thành phần:
  $$G_T = G_L + G_U = C_i \cdot v_i + C_i \cdot u_b$$
  - **Thông lượng lắng trọng lực ($G_L$):**
    $$G_L = C_i \cdot v_i = C_i \cdot (v_0 \cdot e^{-n \cdot C_i})$$
    Đặc điểm: Có giá trị bằng $0$ khi $C_i = 0$ và tiến về $0$ khi $C_i \to \infty$ (do $v_i \to 0$), đạt cực đại tại một nồng độ trung gian.
  - **Thông lượng rút bùn do bơm tuần hoàn/thải bỏ ($G_U$):**
    $$G_U = C_i \cdot u_b = C_i \cdot \frac{Q_r + Q_w}{A_s}$$
    Với: $Q_r$ là lưu lượng bùn tuần hoàn ($\text{m}^3/\text{h}$); $Q_w$ là lưu lượng bùn xả bỏ; $u_b$ là vận tốc dòng chuyển dịch bùn xuống đáy do hoạt động hút bùn ($\text{m/h}$). Đặc điểm: Tuyến tính bậc nhất theo nồng độ $C_i$.

###### 1.2.3.4. Thông lượng Giới hạn (Limiting Solids Flux - $G_L$) và Thiết kế Bể Lắng Đợt 2
- **Điểm thắt cổ chai (Limiting Flux Point):** Đồ thị tổng thông lượng $G_T$ theo nồng độ bùn $C$ có một điểm cực tiểu cục bộ gọi là **Thông lượng giới hạn ($G_L$)** tại nồng độ giới hạn $C_L$.
- **Hệ quả thiết kế:**
  - Nếu tải trọng chất rắn nạp vào bể vượt quá $G_L$, bùn sẽ không kịp truyền tải xuống đáy, dẫn đến hiện tượng tích lũy bùn trong bể và lớp mền bùn dâng cao tràn ra ngoài theo máng thu nước (Sludge Blanket Washout).
  - Diện tích bể lắng đợt 2 tối thiểu được kiểm soát bởi điều kiện:
    $$A_s \ge \frac{(Q + Q_r) \cdot X_{MLSS}}{G_L}$$

##### 1.2.4. Lắng Loại 4: Lắng Nén Ép (Type 4 - Compression Settling)
###### 1.2.4.1. Bản chất Cơ học và Vùng Nén Đáy Bể
- **Điều kiện xuất hiện:** Diễn ra tại đáy của bể lắng đợt 2, bể nén bùn trọng lực (Gravity Sludge Thickener), nơi nồng độ cặn bùn tích tụ đạt giá trị rất cao ($C > 5,000 - 15,000\text{ mg/L}$).
- **Cơ chế nén:** Các bông bùn tiếp xúc cơ học trực tiếp lên nhau tạo thành cấu trúc khung giàn không gian (structural matrix). Sự chìm lắng chỉ có thể tiếp tục diễn ra khi các bông cặn ở lớp dưới bị biến dạng cơ học dưới tác động của trọng lượng các lớp bông bùn đè nặng phía trên.
- **Thoát nước qua mao quản:** Nước bị giữ trong các lỗ rỗng mao quản bị vắt ép và tìm đường thoát ngược lên trên qua các rãnh dẫn nước siêu vi.

###### 1.2.4.2. Phương trình Động học Nén Ép Talmadge & Fitch
- **Phương pháp đường cong lắng thể tích trong ống đo (Cylinder Settling Test):**
  - Quan sát chiều cao bề mặt phân giới nước - bùn $H$ theo thời gian $t$.
  - Đồ thị $H(t)$ gồm 4 đoạn rõ rệt: Vùng lắng tự do ban đầu, Vùng lắng cản trở chuyển tiếp, Vùng thắt uốn (Compression Point $C$), và Vùng nén chặt tiệm cận.
- **Xác định thời gian nén bùn yêu cầu ($t_u$):**
  - Vẽ tiếp tuyến tại điểm chuyển tiếp nén $C$ và đường tiệm cận ngang ở đáy. Kẻ đường phân giác góc giao nhau để tìm điểm tới hạn.
  - Từ nồng độ bùn đáy mong muốn $C_u$ (nồng độ bùn đặc dưới đáy sau nén), tính chiều cao bùn tương đương:
    $$H_u = \frac{C_0 \cdot H_0}{C_u}$$
  - Kẻ đường nằm ngang $H = H_u$ cắt tiếp tuyến của đường lắng tại điểm có hoành độ chính là **Thời gian lưu nén bùn tối thiểu $t_u$**.
- **Diện tích nén bùn tối thiểu (Thickening Area Requirement):**
  $$A_{\text{thickening}} = \frac{Q_0 \cdot t_u}{H_0}$$
  Diện tích thiết kế của bể lắng phải là giá trị lớn nhất giữa diện tích lắng trong ($A_{\text{clarification}}$) và diện tích nén bùn ($A_{\text{thickening}}$).

---

### 2. Thông số Thiết kế & Thủy động lực học Bể Lắng (Design Parameters & Hydrodynamics)
#### 2.1. Các Thông số Vận hành & Tải trọng Kỹ thuật Cốt lõi
##### 2.1.1. Tải trọng Bề mặt (Surface Overflow Rate - $\text{SOR}$)
###### 2.1.1.1. Định nghĩa và Công thức
- **Ý nghĩa kỹ thuật:** Là lưu lượng thể tích nước thải nạp vào trên một đơn vị diện tích bề mặt ướt của bể trong một đơn vị thời gian. Đại diện cho vận tốc dâng ngược dòng của chất lỏng trong bể.
  $$\text{SOR} = \frac{Q}{A_s} = \frac{Q}{L \times W} \quad [\text{m}^3/(\text{m}^2\cdot\text{d}) \text{ hoặc m/h}]$$
  - Đổi đơn vị: $1\text{ m}^3/(\text{m}^2\cdot\text{d}) = \frac{1}{24}\text{ m/h} \approx 0.04167\text{ m/h} = 1.157 \times 10^{-5}\text{ m/s}$.

###### 2.1.1.2. Khoảng Giá trị Tiêu chuẩn Thiết kế
- **Bể lắng sơ bộ / Đợt 1 (Primary Clarifier):**
  - Nước thải sinh hoạt tại lưu lượng trung bình ($Q_{\text{avg}}$): $30 - 50\text{ m}^3/(\text{m}^2\cdot\text{d})$ (hay $1.25 - 2.08\text{ m/h}$).
  - Tại lưu lượng đỉnh giờ ($Q_{\text{peak}}$): $80 - 120\text{ m}^3/(\text{m}^2\cdot\text{d})$ (hay $3.33 - 5.0\text{ m/h}$).
  - Khi có hồi lưu bùn hoạt tính dư ($\text{WAS}$) vào đầu bể lắng 1: $24 - 32\text{ m}^3/(\text{m}^2\cdot\text{d})$.
- **Bể lắng đợt 2 (Secondary Clarifier - Sau Bùn hoạt tính):**
  - Sau quá trình bùn hoạt tính thổi khí truyền thống (Conventional Air Activated Sludge):
    - Trung bình: $16 - 28\text{ m}^3/(\text{m}^2\cdot\text{d})$ ($0.67 - 1.17\text{ m/h}$).
    - Đỉnh giờ: $32 - 48\text{ m}^3/(\text{m}^2\cdot\text{d})$ ($1.33 - 2.0\text{ m/h}$).
  - Sau công nghệ khử dinh dưỡng sinh học (BNR / Selectors):
    - Trung bình: $24 - 32\text{ m}^3/(\text{m}^2\cdot\text{d})$ ($1.0 - 1.33\text{ m/h}$).
    - Đỉnh giờ: $40 - 64\text{ m}^3/(\text{m}^2\cdot\text{d})$.

##### 2.1.2. Thời gian Lưu Thủy lực (Hydraulic Retention Time - $\text{HRT}$ / $t_d$)
###### 2.1.2.1. Mối quan hệ giữa Thể tích, Chiều sâu và Tải trọng
$$t_d = \frac{V}{Q} = \frac{A_s \cdot D}{Q} = \frac{D}{\text{SOR}}$$
- $V$: Thể tích hữu ích công tác của bể lắng ($\text{m}^3$).
- $D$: Chiều sâu nước công tác (Sidewater Depth - $SWD$, tính bằng $\text{m}$).
- $Q$: Lưu lượng nước thải qua bể ($\text{m}^3/\text{h}$ hoặc $\text{m}^3/\text{d}$).

###### 2.1.2.2. Dải Thời gian Lưu Khuyến nghị
- **Bể lắng sơ bộ (Primary Clarifier):**
  - Chuẩn thiết kế: $1.5 - 2.5\text{ h}$ (thông dụng nhất là $2.0\text{ h}$ tại lưu lượng thiết kế trung bình ngày).
  - Tối thiểu tại lưu lượng cực đại: Không được thấp hơn $0.75 - 1.0\text{ h}$ để tránh cuốn trôi cặn thô.
  - Cảnh báo thời gian lưu quá lớn: Nếu $t_d > 3.0\text{ h}$ trong điều kiện nhiệt độ môi trường cao ($T > 28^\circ\text{C}$ như tại Việt Nam), bùn sơ bộ ở đáy sẽ phân hủy kỵ khí sinh bọt khí ($\text{CH}_4, \text{CO}_2, \text{H}_2\text{S}$), làm bùn tự bốc nổi tạo màng nổi hôi thối và phá vỡ nước trong.
- **Bể lắng đợt 2 (Secondary Clarifier):**
  - Thời gian lưu tiêu chuẩn: $2.0 - 4.0\text{ h}$ (thường chọn $2.5 - 3.5\text{ h}$).

##### 2.1.3. Tải trọng Thủy lực Máng Tràn (Weir Overflow Rate - $\text{WOR}$ / $\text{WLR}$)
###### 2.1.3.1. Định nghĩa và Biểu thức
$$\text{WOR} = \frac{Q}{L_{\text{weir}}} \quad [\text{m}^3/(\text{m}\cdot\text{d}) \text{ hoặc m}^3/(\text{m}\cdot\text{h})]$$
- $L_{\text{weir}}$: Tổng chiều dài của ngưỡng đập tràn thu nước trong ($\text{m}$).

###### 2.1.3.2. Giới hạn Kiểm tra Thiết kế
- **Theo Tiêu chuẩn TCVN 7957:2008:**
  - Tải trọng mép tràn tối đa: $\text{WOR} \le 10\text{ m}^3/(\text{m}\cdot\text{h})$ tương đương $240\text{ m}^3/(\text{m}\cdot\text{d})$.
- **Theo tiêu chuẩn quốc tế WEF MOP 8 & Ten States Standards:**
  - Trạm xử lý quy mô nhỏ ($Q < 4,000\text{ m}^3/\text{d}$): $\text{WOR} \le 125\text{ m}^3/(\text{m}\cdot\text{d})$.
  - Trạm xử lý quy mô trung bình và lớn ($Q \ge 4,000\text{ m}^3/\text{d}$):
    - Tại lưu lượng trung bình ngày: $\text{WOR} \le 125 - 250\text{ m}^3/(\text{m}\cdot\text{d})$.
    - Tại lưu lượng đỉnh ngày ($Q_{\text{peak}}$): $\text{WOR} \le 375\text{ m}^3/(\text{m}\cdot\text{d})$ (hay $15.6\text{ m}^3/\text{m}\cdot\text{h}$).
- **Hệ quả khi $\text{WOR}$ vượt chuẩn:** Vận tốc tiếp cận tại ngưỡng tràn quá lớn tạo lực hút hướng lên (upward approach current), kéo các bông cặn lơ lửng sát đáy bay qua đập tràn, gây ô nhiễm nghiêm trọng dòng ra.

##### 2.1.4. Tải trọng Chất rắn (Solids Loading Rate - $\text{SLR}$)
###### 2.1.4.1. Công thức và Ứng dụng
- Áp dụng chủ yếu cho Bể lắng đợt 2 (nơi dòng vào có nồng độ sinh khối $\text{MLSS}$ lớn):
  $$\text{SLR} = \frac{(Q + Q_r) \cdot X}{A_s} \quad [\text{kg}/(\text{m}^2\cdot\text{h}) \text{ hoặc kg}/(\text{m}^2\cdot\text{d})]$$
  - $Q$: Lưu lượng nước thải nạp vào bể ($\text{m}^3/\text{h}$).
  - $Q_r$: Lưu lượng bùn tuần hoàn ($\text{m}^3/\text{h}$).
  - $X$: Nồng độ bùn hoạt tính trong bể sinh học ($\text{MLSS}$, $\text{kg/m}^3$).
  - $A_s$: Diện tích bề mặt bể lắng ($\text{m}^2$).

###### 2.1.4.2. Dải Tiêu chuẩn Thiết kế (Slide 23, Bảng tbl_ch03_01)
- Lắng sau quá trình bùn hoạt tính cấp khí nén (Air Activated Sludge):
  - Giá trị trung bình: $4.0 - 6.0\text{ kg}/(\text{m}^2\cdot\text{h})$.
  - Cực đại giờ cao điểm: Tối đa không quá $8.0 - 10.0\text{ kg}/(\text{m}^2\cdot\text{h})$.
- Lắng sau các bể Selector, công nghệ khử dinh dưỡng Nitơ & Photpho (BNR):
  - Giá trị trung bình: $5.0 - 8.0\text{ kg}/(\text{m}^2\cdot\text{h})$.
  - Cực đại giờ cao điểm: Lên đến $9.0 - 12.0\text{ kg}/(\text{m}^2\cdot\text{h})$.

##### 2.1.5. Chiều sâu Nước và Phân vùng Thủy lực Chức năng
###### 2.1.5.1. Chiều sâu Thành bể (Sidewater Depth - $SWD$)
- Bể lắng đợt 1: $D = 3.0 - 4.5\text{ m}$ (tiêu chuẩn khuyến nghị: $3.5 - 4.0\text{ m}$).
- Bể lắng đợt 2: $D = 4.0 - 5.5\text{ m}$ (bắt buộc tối thiểu $\ge 4.0\text{ m}$ để chứa và cô đặc mền bùn sinh học, chống trôi bùn khi có biến động tải).
- Chiều sâu vùng chứa bùn đáy ($h_{\text{sludge}}$): $0.6 - 1.0\text{ m}$.
- Chiều cao an toàn bảo vệ (Freeboard - $h_{\text{FB}}$): $0.3 - 0.6\text{ m}$ (thường chọn $0.5\text{ m}$).
- Tổng chiều sâu xây dựng thành bể:
  $$H_{\text{total}} = D + h_{\text{sludge}} + h_{\text{FB}}$$

###### 2.1.5.2. Bốn Vùng Chức năng Thủy lực Trong Bể Lắng
- **Vùng vào (Inlet Zone):** Có chức năng tiêu giảm động năng dòng chảy vào, phân bố lưu lượng đều khắp chiều rộng và chiều sâu tiết diện, triệt tiêu dòng phản lực cục bộ (Jet currents).
- **Vùng lắng (Settling Zone):** Chiếm phần lớn thể tích bể; dòng chảy dịch chuyển êm ái, đạt trạng thái chảy tầng hoặc chuyển tiếp ổn định, cung cấp đủ thời gian tĩnh cho các hạt cặn lắng rơi xuống đáy.
- **Vùng chứa và cô đặc bùn (Sludge Zone):** Nằm ở phần đáy bể; có độ dốc để gom bùn, bố trí máy cào bùn gạt gom bùn vào hố gom để định kỳ hoặc liên tục hút bùn ra xử lý.
- **Vùng thu nước trong và váng nổi (Outlet Zone):** Nằm ở phía trên mặt và cuối bể; gồm các tấm chắn váng bề mặt, máng tràn và đập tràn thu nước trong đồng đều không gây xoáy hút cục bộ.

---

#### 2.2. Tiêu chí Ổn định Thủy động Lực học & Vận tốc Cuốn cặn
##### 2.2.1. Vận tốc Dòng chảy Ngang (Horizontal Velocity - $v_H$)
###### 2.2.1.1. Công thức Xác định
$$v_H = \frac{Q}{A_c} = \frac{Q}{W \times D}$$
- $A_c$: Tiết diện ướt ngang dòng chảy ($\text{m}^2$).
- $W$: Chiều rộng khoang bể lắng ($\text{m}$).
- $D$: Chiều sâu nước hữu dụng ($\text{m}$).

###### 2.2.1.2. Giới hạn Tiêu chuẩn Vận hành
- Khoảng vận tốc cho phép:
  $$0.005\text{ m/s} \le v_H \le 0.018\text{ m/s} \quad (5 - 18\text{ mm/s} \text{ hay } 0.3 - 1.08\text{ m/min})$$
- **Ý nghĩa biên giới hạn:**
  - Nếu $v_H < 0.005\text{ m/s}$: Bể quá rộng, có nguy cơ hình thành các vùng chết thủy lực (dead space) và dòng xoáy nội bộ do năng lượng dòng chảy quá yếu.
  - Nếu $v_H > 0.018\text{ m/s}$: Năng lượng dòng chảy quá mạnh tạo nhiễu động xáo trộn và gây nguy cơ cuốn trôi các lớp bùn đã lắng.

##### 2.2.2. Số Reynolds Thủy lực Bể Lắng (Reynolds Number - $Re$)
###### 2.2.2.1. Biểu thức Định lượng
$$Re = \frac{v_H \cdot R}{\nu} = \frac{v_H \cdot R \cdot \rho_w}{\mu}$$
- $R$: Bán kính thủy lực của tiết diện ướt dẫn dòng ($\text{m}$):
  $$R = \frac{A_c}{P} = \frac{W \cdot D}{W + 2D}$$
  với $P = W + 2D$ là chu vi ướt của kênh chữ nhật hở ($\text{m}$).
- $\nu$: Độ nhớt động học của nước thải ($\nu = 1.003 \times 10^{-6}\text{ m}^2/\text{s}$ ở $20^\circ\text{C}$).

###### 2.2.2.2. Tiêu chí Đánh giá Trạng thái Dòng chảy
- Trong các bể lắng hở hình chữ nhật: Để hạn chế xáo trộn do lực quán tính, thiết kế tiêu chuẩn yêu cầu:
  $$Re < 20,000 \quad \text{(khuyến nghị tối ưu } Re < 10,000\text{)}$$
  *(Lưu ý: Đối với khối tấm lắng/ống lắng cao trình, tiêu chí khắt khe hơn rất nhiều: $Re < 50$)*.

##### 2.2.3. Số Froude Thủy lực Bể Lắng (Froude Number - $Fr$)
###### 2.2.3.1. Biểu thức Định lượng Ổn định
$$Fr = \frac{v_H^2}{g \cdot R}$$
- $g$: Gia tốc trọng trường ($9.81\text{ m/s}^2$).
- $R$: Bán kính thủy lực ($\text{m}$).

###### 2.2.3.2. Tiêu chuẩn Kháng Nhiễu Động Phân tầng
- Tiêu chí thiết kế thủy lực bắt buộc:
  $$Fr > 10^{-5}$$
- **Ý nghĩa vật lý:** Số Froude đại diện cho tỷ số giữa lực quán tính và lực trọng trường. Giá trị $Fr > 10^{-5}$ đảm bảo dòng chảy có đủ tính "ổn định động học" để kháng cự lại sự hình thành các dòng đối lưu nhiệt, phân tầng mật độ và các tế bào tuần hoàn do gió tác động lên mặt nước.

##### 2.2.4. Vận tốc Cuốn cặn Tới hạn của Camp (Camp's Critical Scour Velocity - $v_c$)
###### 2.2.4.1. Phương trình Cân bằng Lực Cắt Đáy Camp
- Khi vận tốc dòng chảy ngang gần đáy bể quá lớn, ứng suất cắt đáy do chất lỏng gây ra sẽ cuốn các hạt cặn đã lắng trở lại dòng chảy (Scouring / Resuspension).
- Vận tốc tới hạn bắt đầu gây cuốn cặn được xác định theo công thức kinh điển của Camp (1946):
  $$v_c = \sqrt{\frac{8 \cdot k \cdot (s - 1) \cdot g \cdot d}{f}}$$
  - $v_c$: Vận tốc cuốn cặn tới hạn ($\text{m/s}$).
  - $k$: Hệ số dính kết của hạt cặn (Cohesion constant, không thứ nguyên):
    - Đối với cát vô cơ không dính: $k \approx 0.04$.
    - Đối với hạt cặn hữu cơ, bông bùn sinh học dính kết: $k = 0.04 - 0.06$ (thường chọn $k = 0.05$).
  - $s$: Tỷ trọng tương đối của hạt bùn cặn ($s = \rho_s / \rho_w$, thường $s \approx 1.20 - 1.25$ đối với bùn hữu cơ sơ bộ; $s \approx 1.02 - 1.05$ đối với bùn hoạt tính sinh học).
  - $g$: Gia tốc trọng trường ($9.81\text{ m/s}^2$).
  - $d$: Đường kính đặc trưng của hạt cặn lắng ($\text{m}$, đối với bông cặn hữu cơ thường chọn $d = 100\,\mu\text{m} = 10^{-4}\text{ m}$).
  - $f$: Hệ số ma sát Darcy-Weisbach của lòng bể ($f \approx 0.02 - 0.03$; bê tông nhẵn chọn $f = 0.025$).

###### 2.2.4.2. Điều kiện Đảm bảo An toàn Chống Cuốn Cặn
- Trong mọi điều kiện thủy lực (ngay cả ở lưu lượng đỉnh $Q_{\text{peak}}$):
  $$v_H \ll v_c \quad \implies \quad \text{Hệ số an toàn } FS = \frac{v_c}{v_H} \ge 3.0 - 5.0$$
  Thông thường trong thiết kế bể lắng hợp chuẩn: $v_c \approx 0.04 - 0.08\text{ m/s}$ trong khi $v_H \approx 0.005 - 0.015\text{ m/s}$, thỏa mãn tuyệt đối điều kiện chống cuốn cặn.

---

#### 2.3. Các Hiện tượng Bất thường Thủy lực & Biện pháp Khắc phục
##### 2.3.1. Hiện tượng Đoản mạch Thủy lực (Short Circuiting) và Vùng Chết (Dead Zones)
###### 2.3.1.1. Nguyên nhân & Tác hại
- Do kết cấu cửa vào phân phối lưu lượng không đều trên mặt cắt ướt, nước bị xói tập trung thành các tia dòng vận tốc lớn; hoặc do hệ thống máng tràn đầu ra phân bố không cân đối khiến các hạt nước di chuyển qua bể với thời gian thực tế $t_{\text{thực}} \ll t_d$ danh định.
- Gây giảm sút nghiêm trọng hiệu suất lắng và cuốn trôi cặn bùn ra dòng thải.
###### 2.3.1.2. Biện pháp Khắc phục Kỹ thuật
- Thiết kế mương phân phối đầu bể kèm tường vách đục lỗ tiêu năng (Perforated Diffuser Baffle Wall) với tổng diện tích lỗ mở chiếm $10\% - 20\%$ diện tích mặt cắt ướt để tạo tổn thất áp lực đồng đều ($h_L \approx 10 - 25\text{ mm}$).
- Tăng tỷ lệ chiều dài trên chiều rộng bể ($L/W \ge 6:1$) để hướng dòng chảy tiến gần trạng thái dòng chảy nút (Plug Flow).
- Bố trí hệ thống máng tràn dạng răng cưa kéo dài bao phủ từ $1/3$ đến $1/2$ chiều dài cuối bể.

##### 2.3.2. Phân tầng Nhiệt & Mật độ Dòng chảy (Thermal & Density Stratification)
###### 2.3.2.1. Dòng Chìm Đáy (Plunging Underflow Current)
- **Cơ chế:** Xảy ra khi nhiệt độ nước thải nạp vào lạnh hơn nước có sẵn trong bể ($\rho_{\text{in}} > \rho_{\text{tank}}$) hoặc khi nước thải có nồng độ chất rắn hòa tan/lơ lửng rất cao.
- **Tác hại:** Dòng nước nạp vào có mật độ nặng hơn lập tức chìm thẳng xuống đáy bể (Water fall effect), tạo thành dòng xiết di chuyển sát đáy với vận tốc cực lớn làm xới tung và cuốn trôi lớp bùn đã lắng về phía máng ra.
###### 2.3.2.2. Dòng Nổi Mặt (Surface Density Current)
- **Cơ chế:** Xảy ra khi nước thải nạp vào ấm hơn nước trong bể ($\rho_{\text{in}} < \rho_{\text{tank}}$).
- **Tác hại:** Dòng nước nóng nhẹ hơn trượt thẳng trên bề mặt bể và tràn trực tiếp qua đập tràn đầu ra trong vòng vài phút mà không hề trải qua quá trình lắng rơi.
###### 2.3.2.3. Giải pháp Công trình
- Lắp đặt các vách ngăn hướng dòng thẳng đứng ngập sâu (Deep-skirted baffles) tại cửa vào.
- Thiết kế giếng nạp trung tâm (Feedwell) có chiều sâu thích hợp chiếm $1/2 - 2/3$ chiều sâu nước đối với bể tròn để chuyển hướng dòng chảy vào vùng trung gian.

##### 2.3.3. Dòng Hoàn lưu do Tác động của Gió (Wind-Driven Circulation Cells)
###### 2.3.3.1. Cơ chế Phát sinh
- Gió mạnh thổi liên tục dọc theo bề mặt bể lắng hở sẽ kéo lớp nước mặt chảy xiết về phía cuối bể.
- Để cân bằng thể tích, một dòng chảy ngược chiều (Return Underflow Current) có vận tốc đáng kể sẽ hình thành ở tầng đáy chạy ngược từ cuối bể về đầu bể, gây xáo trộn mạnh mẽ lớp đệm bùn.
###### 2.3.3.2. Giải pháp Phòng chống
- Xây dựng tường chắn gió (Windbreaks / Wind baffles) trên thành bể hoặc trồng dải cây xanh cản gió xung quanh trạm xử lý.
- Lắp đặt các vách ngăn chống gió ngập nông trên mặt nước cắt ngang bể theo từng khoảng cách đều đặn.

---

### 3. Cấu tạo Hình học & Thiết bị Cơ khí Bể Lắng (Tank Geometries & Mechanical Equipment)
#### 3.1. Bể Lắng Chữ Nhật Dòng Chảy Ngang (Rectangular Sedimentation Tanks)
##### 3.1.1. Quy chuẩn Kích thước Hình học Tiêu chuẩn
###### 3.1.1.1. Tỷ lệ Kích thước Bể
- **Tỷ lệ Chiều dài trên Chiều rộng ($L/W$):**
  - Tối thiểu: $L/W \ge 4:1$.
  - Tiêu chuẩn khuyến nghị tối ưu: $L/W \ge 6:1$ (để đảm bảo tính chất dòng chảy nút và triệt tiêu xoáy ngang).
- **Tỷ lệ Chiều dài trên Chiều sâu ($L/D$):**
  - Khuyến nghị: $L/D \ge 15:1$ (thường nằm trong khoảng $15:1 - 25:1$).
- **Giới hạn chiều rộng khoang đơn ($W$):**
  - Chiều rộng một đơn nguyên bể: $W \le 6.0\text{ m}$ (do giới hạn cơ khí của nhịp thanh cào gạt bùn bằng gỗ hoặc vật liệu composite FRP để chống võng và lệch xích kéo).
  - Đối với các trạm công suất lớn, bố trí nhiều khoang bể chữ nhật song song nhau, chung vách ngăn giữa để tiết kiệm diện tích xây dựng và chi phí cốt pha bê tông.
- **Chiều dài bể ($L$):** Thường từ $25\text{ m} - 75\text{ m}$ (tối đa không nên vượt quá $90\text{ m}$ để tránh co giãn nhiệt cơ khí xích cào).

###### 3.1.1.2. Độ dốc Đáy Bể & Hố Thu Bùn
- Đáy bể có độ dốc dọc nhẹ: $S = 1:600$ đến $1:100$ (khoảng $0.17\% - 1.0\%$) nghiêng dần từ phía cuối bể về phía đầu bể (nơi đặt hố thu bùn).
- Hố thu bùn (Sludge Hopper): Đặt ngay dưới đáy ở đầu dòng vào của bể; thành hố thu có độ dốc rất dốc: tối thiểu $60^\circ$ so với phương ngang để bùn tự trượt tụ xuống đáy hố mà không bị bám dính.

##### 3.1.2. Cấu tạo Vùng Cửa Vào & Phân phối Dòng
###### 3.1.2.1. Mương Dẫn & Vách Đục Lỗ Tiêu Năng
- Nước thải từ công trình trước chảy vào mương nạp trải suốt toàn bộ chiều rộng $W$ của các đơn nguyên bể.
- Bố trí vách ngăn đục lỗ (Diffuser Wall / Perforated Baffle) cách thành đầu bể từ $0.5 - 1.0\text{ m}$:
  - Các lỗ đục hình tròn đường kính $100 - 200\text{ mm}$ được phân bố sole đều khắp diện tích.
  - Vận tốc nước qua lỗ kiểm soát ở mức: $v_{\text{lỗ}} = 0.2 - 0.3\text{ m/s}$ nhằm tạo tổn thất cột áp nhỏ vừa đủ để phân đều lưu lượng cho mọi điểm trên mặt cắt ngang.

##### 3.1.3. Cơ cấu Thu gom và Vận chuyển Bùn Đáy
###### 3.1.3.1. Máy Cào Bùn Kiểu Thanh Cào - Dây Xích (Chain-and-Flight Scrapers)
- **Cấu tạo cơ khí:**
  - Gồm hai dải xích truyền động vô tận bằng thép không gỉ hoặc nhựa công nghiệp đặc biệt chịu mài mòn, chạy vòng quanh 4 cặp bánh sao (sprockets) bố trí ở 4 góc đáy và đỉnh bể.
  - Động cơ điện và hộp giảm tốc đặt trên sàn khô trên mặt bể.
  - Các thanh cào (Flights) làm bằng gỗ redwood hoặc composite FRP cốt sợi thủy tinh, tiết diện chữ L hoặc C dài $W \le 6\text{ m}$, lắp vuông góc với dải xích cách nhau khoảng $3.0\text{ m}$.
- **Chu trình vận hành kép:**
  - Nhánh xích chạy sát đáy bể: Di chuyển chậm về phía đầu bể với vận tốc $v_{\text{scraper}} = 0.6 - 1.2\text{ m/min}$ ($10 - 20\text{ mm/s}$), gạt bùn đáy dồn vào hố thu bùn. Vận tốc này đủ chậm để không làm xáo trộn lớp bùn.
  - Nhánh xích chạy trên mặt nước (chiều ngược lại): Lộ các thanh cào lên sát mặt nước, vừa làm nhiệm vụ thanh gạt váng (Scum flight) dồn các chất nổi và bọt mỡ về phía máng thu váng ở cuối bể.

###### 3.1.3.2. Cầu Cào Bùn Tịnh tiến (Traveling-Bridge Scrapers)
- Sử dụng cho các bể có chiều rộng lớn hơn ($W = 6 - 20\text{ m}$).
- Dầm cầu thép bắc ngang qua toàn bộ chiều rộng bể, chạy trên hệ thống bánh xe cao su hoặc bánh thép lăn trên ray đặt trên thành bê tông bể.
- Cầu di chuyển tịnh tiến qua lại dọc theo chiều dài bể:
  - Khi chạy về phía đầu bể: Cánh cào bùn hạ xuống sát đáy để đẩy bùn vào hố gom, đồng thời lưỡi gạt váng nâng lên.
  - Khi chạy ngược về cuối bể: Cánh cào bùn đáy nâng lên khỏi lớp bùn, lưỡi gạt váng nổi hạ xuống để thu gom dầu mỡ bề mặt.
  - Có thể lắp trực tiếp bơm hút bùn chìm đặt trên cầu để hút bùn bằng áp lực ống hút thay vì dùng lưỡi cào cơ học.

##### 3.1.4. Thiết bị Thu gom Bọt váng Nổi (Scum Removal System)
###### 3.1.4.1. Ống Thu Bọt Váng Xẻ Rãnh Xoay (Rotating Slotted Pipe Skimmer)
- Là ống thép đường kính $DN200 - DN300$ đặt nằm ngang sát mặt nước ở cuối bể, có xẻ một khe rãnh dọc theo chiều dài ống.
- Ống có thể xoay quanh trục thông qua cơ cấu đòn bẩy tay gạt hoặc vít xoay trục vít:
  - Trạng thái bình thường không xả váng: Mép rãnh khoét nằm nhô cao hơn mặt nước $50 - 75\text{ mm}$ để ngăn nước trong tràn vào.
  - Trạng thái xả váng nổi: Xoay đòn bẩy để dìm mép rãnh chìm xuống dưới mặt nước khoảng $20 - 30\text{ mm}$. Lớp váng dầu mỡ bề mặt cùng một lượng nước mỏng lập tức tràn vào lòng ống và tự chảy theo độ dốc ống về hố thu váng tập trung.

##### 3.1.5. Cấu tạo Cửa Ra & Hệ thống Máng tràn Răng cưa
###### 3.1.5.1. Bố trí Máng Thu Dạng Ngón Tay (Finger Launders)
- Để đảm bảo tải trọng mép tràn $\text{WOR} \le 240\text{ m}^3/(\text{m}\cdot\text{d})$, chiều dài mép tràn yêu cầu thường lớn hơn nhiều so với chiều rộng $W$ của bể.
- Do đó, giải pháp công nghệ là kéo dài máng thu nước dạng các ngón tay vươn dài ngược dòng chảy, chiếm khoảng $1/3$ đến $1/2$ chiều dài cuối bể ($L_{\text{launder}} = 0.33 - 0.50 L$).
###### 3.1.5.2. Đập Tràn Răng Cưa $90^\circ$ V-Notch
- Gắn các tấm đập răng cưa bằng inox hoặc composite có vết cắt chữ V góc $90^\circ$, chiều sâu vết cắt $75\text{ mm}$, khoảng cách giữa các đỉnh rãnh là $150 - 300\text{ mm}$.
- Tấm đập có lỗ rãnh bầu dục cho phép hiệu chỉnh độ cao bằng bu lông để đảm bảo cao trình tràn đồng mức tuyệt đối trên toàn bộ chiều dài máng.
###### 3.1.5.3. Tấm Chắn Bọt Váng (Scum Baffle)
- Đặt phía trước máng tràn ở khoảng cách $200 - 300\text{ mm}$.
- Tấm chắn bằng sợi thủy tinh hoặc thép nhúng ngập sâu $150 - 250\text{ mm}$ dưới mặt nước và nhô cao $100 - 150\text{ mm}$ trên mặt nước, ngăn tuyệt đối không cho váng nổi trôi qua đập tràn.

---

#### 3.2. Bể Lắng Tròn Dòng Chảy Hướng Tâm (Circular Sedimentation Tanks)
##### 3.2.1. Cấu hình Thủy lực Phân phối Dòng vào
###### 3.2.1.1. Cấp Nước Tâm Bể (Center-Feed Clarifier)
- **Đường dẫn dòng:** Nước thải đi theo đường ống ngầm dưới đáy bể đi lên qua trụ rỗng tâm bể, thoát ra qua các cửa sổ phân phối vào **Giếng nạp trung tâm (Center Feedwell)**.
- **Giếng tiêu năng (Feedwell):** Là ống hình trụ bằng thép hoặc composite có đường kính bằng $15\% - 25\%$ đường kính bể ($D_{\text{well}} = 0.15 - 0.25 D_{\text{tank}}$) và ngập sâu $30\% - 50\%$ chiều sâu nước. Giếng có tác dụng tiêu giảm vận tốc dòng vào, hướng dòng di chuyển đi xuống dưới trước khi tỏa tròn hướng tâm (radially outward) về phía thành bể.
- **Trường vận tốc:** Vận tốc dòng chảy giảm dần theo quy luật tỷ lệ nghịch với bán kính ($v_r \propto 1/r$), tạo điều kiện lý tưởng cho các bông cặn lắng xuống đáy khi dòng chảy tiến dần ra chu vi.

###### 3.2.1.2. Cấp Nước Chu Vi (Peripheral-Feed Clarifier)
- Nước thải được nạp vào một máng phân phối chạy dọc theo toàn bộ chu vi ngoài của bể, đi vào qua các lỗ khoét hoặc vách hướng dòng dưới đáy máng.
- Dòng chảy di chuyển hướng tâm từ chu vi vào tâm hoặc chuyển động xoắn ốc (spiral flow), thu nước trong qua máng tràn đặt ở khu vực trung tâm hoặc máng chu vi thứ cấp. Có ưu thế về thủy lực ổn định nhưng cấu tạo cơ khí phức tạp hơn.

##### 3.2.2. Cấu tạo Đáy bể và Hỗ trợ Kết cấu Cơ khí
###### 3.2.2.1. Độ dốc Nón Đáy Bể
- Đáy bể tròn được đổ bê tông hình nón ngược dốc về tâm với độ dốc chuẩn:
  $$S_{\text{circ}} = 1:12 \quad (\approx 8.33\% \text{ hay khoảng } 1\text{ inch/foot})$$
- Tại tâm bể bố trí hố thu bùn trung tâm (Central Sludge Hopper) hình nón cụt hoặc hình trụ để gom toàn bộ bùn đặc trước khi xả ra ngoài bằng ống hút bùn.

###### 3.2.2.2. Kết cấu Cầu Giàn Hỗ trợ Cơ khí
- **Bể đường kính nhỏ ($D = 3.6 - 9.0\text{ m}$):** Thiết bị cào bùn được treo và đỡ hoàn toàn trên hệ dầm giàn thép (Spanning Bridge) bắc ngang qua toàn bộ đường kính bể từ thành bên này sang thành bên kia.
- **Bể đường kính lớn ($D \ge 10.5\text{ m}$ đến $40 - 60\text{ m}$):** Tại tâm bể xây dựng một trụ bê tông cốt thép trung tâm kiên cố (Central Concrete Pier). Trụ này vừa làm nhiệm vụ dẫn ống nước nạp, vừa làm bệ đỡ chịu tải trọng xoay của toàn bộ cơ cấu cào bùn và đầu tựa của cầu công tác (Walkway Bridge) dẫn từ thành bể vào tâm.

##### 3.2.3. Cơ cấu Thu gom Bùn và Gạt bọt Nổi Bể Tròn
###### 3.2.3.1. Máy Cào Bùn Trục Tâm Truyền Động Đỉnh (Center-Drive Scraper)
- Động cơ và hộp giảm tốc hành tinh lắp trên đỉnh trụ tâm, truyền mô men xoắn làm quay lồng truyền động (Drive cage) và hai hoặc bốn cánh cào thép tỏa tròn đối xứng.
- Trên mỗi cánh cào lắp các lưỡi cào dăm xoắn (Plough blades / Spiral scrapers) đặt chéo góc nghiêng theo hình học xoắn ốc Logarithm.
- Khi cánh cào quay chậm với vận tốc vòng đầu mút cánh $v_{\text{tip}} = 1.5 - 3.0\text{ m/min}$ ($0.025 - 0.05\text{ m/s}$), các lưỡi cào sẽ liên tục cào và dồn các lớp bùn đáy trượt xoắn ốc dần dần vào hố thu bùn tâm bể.

###### 3.2.3.2. Cơ cấu Cào Bùn Hút Ống Chùm (Suction Pipe Scrapers / Tow-Bro Type)
- Thường dùng riêng cho Bể lắng đợt 2 của hệ thống bùn hoạt tính sinh học nhạy cảm với thời gian lưu.
- Thay vì đẩy dồn bùn cơ học, trên cánh cào gắn một ống gom nằm ngang sát đáy với hàng loạt đầu hút áp lực hoặc hệ thống ống hút riêng biệt (Organ-pipe type).
- Bùn sinh học được hút trực tiếp tại vị trí vừa lắng xuống bằng chênh áp thủy tĩnh hoặc bơm hút, tránh hiện tượng lưu bùn quá lâu gây thiếu khí sinh học và nổi bùn.

###### 3.2.3.3. Cánh Gạt Váng Quay và Máng Trượt Váng Nổi (Scum Skimmer & Beach)
- Phía trên mặt nước, cánh gạt bọt váng quay đồng bộ cùng trục cào bùn.
- Lưỡi gạt cao su mềm quét dọc theo bề mặt sát thành ngoài bể, lùa bọt váng trượt lên một tấm dốc nghiêng thép (Scum Beach) gắn sát thành bể và đẩy rơi vào phễu gom váng (Scum Box) có đường ống xả tự chảy định kỳ.

##### 3.2.4. Hệ thống Máng thu Nước trong Đầu ra
###### 3.2.4.1. Máng Thu Chu Vi (Peripheral Launders)
- Bố trí chạy vòng quanh mép ngoài thành bể tròn:
  - Có thể là máng gắn trực tiếp sát vách bê tông thành bể (nước chỉ tràn qua bờ trong).
  - Hoặc máng dạng đúc hẫng vươn ra trong lòng bể (máng 2 bờ tràn, cho phép nước tràn đồng thời qua cả mép trong và mép ngoài, tăng gấp đôi chiều dài mép tràn $L_{\text{weir}} \approx 2 \times \pi D$).
- Phía trước mép tràn luôn có tấm chắn váng bọt nổi (Circular Scum Baffle) bằng composite FRP bao quanh.

---

#### 3.3. Bể Lắng Hình Vuông và Các Giới hạn Thiết kế
##### 3.3.1. Phạm vi Ứng dụng & Hạn chế Cốt lõi
- **Ưu điểm:** Tiết kiệm diện tích mặt bằng xây dựng hơn bể tròn do các bể có thể ghép chung vách thành khối chữ nhật nhiều ô.
- **Nhược điểm nghiêm trọng:**
  - Vùng chết 4 góc (Dead Corners): Cánh cào bùn quay tròn chỉ quét được phạm vi hình tròn nội tiếp đường kính $D = W$. Bốn vùng tam giác ở bốn góc bể nằm ngoài tầm quét của thiết bị gạt bùn cơ học.
  - Bùn tích tụ dày đặc tại 4 góc không được cào dọn sẽ bị phân hủy kỵ khí thối rữa (Septic Sludge), sinh khí metan và nitơ tự do.
  - Khí gas đẩy bùn phân hủy nổi thành các tảng lớn bốc lên mặt nước, bị cuốn tràn qua đập tràn xả ra dòng ra, phá hỏng độ trong của nước sau xử lý.

##### 3.3.2. Các Giải pháp Xử lý Cơ khí & Xây dựng
- **Góc lượn bê tông (Corner Fillets):** Đổ bê tông vát nghiêng $45^\circ$ hoặc uốn cong lượn tròn tại 4 góc đáy bể để triệt tiêu góc chết và ép bùn trượt vào bán kính hoạt động của cánh cào.
- **Cánh cào bùn quét góc (Corner Sweeps / Articulated Scraper Arms):** Lắp thêm đoạn cánh cào phụ có khớp xoay lò xo hoặc dẫn hướng bằng con lăn cơ khí tại đầu mút cánh cào chính; khi quay đến góc vuông bể, cánh phụ tự động bung dài ra nhờ cơ cấu cam để quét bùn ở góc và tự co ngắn lại khi chạm thành bên. Tuy nhiên cơ cấu này rất hay kẹt hỏng cơ khí và chi phí bảo trì cao.

---

#### 4. Bể Lắng Tốc độ Cao: Tấm Nghiêng Lamella & Khối Ống Nghiêng (High-Rate Clarification)
#### 4.1. Bản chất Vật lý và Lý thuyết Lắng Lớp Nông của Hazen
##### 4.1.1. Nguyên lý Lớp Nông (Shallow Settling Principle)
###### 4.1.1.1. Rút ngắn Hành trình Rơi của Hạt
- Theo lý thuyết bể lắng lý tưởng Hazen: Hiệu quả lắng không phụ thuộc vào chiều sâu bể $D$ mà chỉ phụ thuộc vào diện tích bề mặt $A_s$ và tải trọng thủy lực $\text{SOR} = Q/A_s$.
- Nếu một bể lắng có chiều sâu $D = 3.0\text{ m}$ được chia thành $N$ tầng nằm ngang bằng các tấm phẳng song song cách nhau khoảng cách rất nhỏ $h_0 = 50 - 100\text{ mm}$:
  - Khoảng cách rơi chìm của hạt cặn để chạm mặt lắng giảm từ $3.0\text{ m}$ xuống còn chỉ $0.05 - 0.1\text{ m}$ (giảm $30 - 60$ lần).
  - Thời gian rơi lắng yêu cầu của hạt cặn giảm tương ứng:
    $$t_{\text{lắng}} = \frac{h_0}{v_s} \ll \frac{D}{v_s}$$
  - Ngay khi hạt chạm vào bề mặt tấm lắng, nó được xem như đã tách khỏi pha lỏng.

###### 4.1.1.2. Gia tăng Diện tích Bề mặt Lắng Hiệu dụng
- Tổng diện tích lắng hiệu dụng của hệ thống tấm nghiêng được nhân lên nhiều lần:
  $$A_{\text{eff}} = A_{\text{plan}} \cdot \cos\theta + A_{\text{total}} \cdot \cos\theta \approx A_{\text{plan}} \cdot \left( \sin\theta + \frac{L_{\text{plate}}}{w} \cdot \cos\theta \right)$$
  - $A_{\text{plan}}$: Diện tích hình chiếu bằng của khối tấm lắng trên mặt bằng bể ($\text{m}^2$).
  - $L_{\text{plate}}$: Chiều dài theo phương nghiêng của tấm lắng ($\text{m}$).
  - $w$: Khoảng cách vuông góc giữa hai tấm lắng kế tiếp ($\text{m}$).
  - $\theta$: Góc nghiêng của tấm lắng so với phương nằm ngang ($^\circ$).
- Nhờ hệ số khuếch đại diện tích này, diện tích mặt bằng trạm xử lý có thể thu nhỏ từ $50\% - 75\%$ so với bể lắng trọng lực thông thường.

##### 4.1.2. Góc Nghiêng Tự Làm Sạch Tối ưu ($\theta = 60^\circ$)
###### 4.1.2.1. Cân bằng Động học Trượt Bùn
- Khi hạt cặn bám lên bề mặt tấm nghiêng, nó chịu 2 thành phần lực trọng trường:
  - Thành phần pháp tuyến ép hạt vào mặt tấm: $F_N = m \cdot g \cdot \cos\theta$.
  - Thành phần tiếp tuyến đẩy hạt trượt dốc xuống đáy: $F_T = m \cdot g \cdot \sin\theta$.
- Lực ma sát kháng trượt giữa bùn và bề mặt vật liệu tấm nhựa:
  $$F_{\text{friction}} = \mu_{\text{friction}} \cdot F_N = \tan\phi \cdot (m \cdot g \cdot \cos\theta)$$
  với $\phi$ là góc nội ma sát của bùn cặn.
- Điều kiện để khối bùn tự động trượt rơi xuống đáy mà không bị đọng bám gây nghẽn:
  $$F_T > F_{\text{friction}} \implies \tan\theta > \tan\phi \implies \theta > \phi$$

###### 4.1.2.2. Lựa chọn Góc Nghiêng Công nghệ
- **Góc nghiêng thực tế tiêu chuẩn:** Chọn $\theta = 60^\circ$ (hoặc trong khoảng $55^\circ - 60^\circ$).
- **Hạn chế kỹ thuật khi lệch góc:**
  - Nếu $\theta < 50^\circ$: Bùn cặn không thể tự trượt, sẽ bám dính tích tụ dần làm tắc nghẽn toàn bộ các khe ống và sinh khối kỵ khí bốc mùi hôi thối.
  - Nếu $\theta > 65^\circ$: Khả năng trượt bùn rất tốt nhưng diện tích hình chiếu hiệu dụng bị suy giảm mạnh, làm giảm đáng kể hiệu quả kinh tế của công trình.

##### 4.1.3. Ba Cấu hình Dòng Chảy Thủy lực Qua Khối Tấm/Ống Lắng
###### 4.1.3.1. Dòng Ngược Chiều (Counter-Current Flow)
- Nước thải mang cặn đi từ khoang dưới đáy bể chuyển động đi lên qua các khe tấm nghiêng; cặn lắng xuống bám lên vách tấm và trượt trôi dốc ngược chiều xuống đáy.
- Là cấu hình phổ biến nhất ($> 90\%$) trong các nhà máy xử lý nước thải do cấu tạo thu nước mặt và xả bùn đáy rất thuận tiện và tách biệt.
###### 4.1.3.2. Dòng Cùng Chiều (Co-Current Flow)
- Nước thải nạp từ phía trên đi xuống cùng chiều với hướng bùn trượt.
- Hạn chế nguy cơ cuốn ngược cặn nhưng việc tách pha nước trong ở đáy rất phức tạp.
###### 4.1.3.3. Dòng Cắt Ngang (Cross-Flow)
- Nước chảy theo phương ngang qua các tấm nghiêng đặt dọc, bùn trượt thẳng góc xuống đáy.
- Thường áp dụng trong xử lý nước cấp hoặc các bể công nghiệp đặc thù.

---

#### 4.2. Cấu trúc Mô-đun & Thiết bị Kỹ thuật
##### 4.2.1. Khối Ống Lắng Lục Giác (Hexagonal Honeycomb Tube Settlers)
###### 4.2.1.1. Cấu hình Kỹ thuật
- Các tấm nhựa PVC hoặc Polypropylene (PP) nhiệt dẻo được định hình gợn sóng và hàn nhiệt/dán ghép lại với nhau tạo thành mạng lưới các ống tiết diện hình lục giác đều (tổ ong).
- Kích thước đường kính trong danh định của ống: $d = 50\text{ mm}$ (dải phổ biến: $40 - 80\text{ mm}$).
- Bán kính thủy lực của ống lục giác ($R$):
  $$R = \frac{A_{\text{hex}}}{P_{\text{hex}}} = \frac{d}{4} = \frac{0.050\text{ m}}{4} = 0.0125\text{ m} \quad (12.5\text{ mm})$$

##### 4.2.2. Khối Tấm Lắng Song Song Lamella (Lamella Plate Settlers)
###### 4.2.2.1. Cấu hình Kỹ thuật
- Gồm các tấm phẳng hoặc tấm gân tăng cứng đặt nghiêng song song với nhau với khoảng cách khe hở $w = 50 - 100\text{ mm}$.
- Tấm lắng được gia công bằng vật liệu bền hóa chất cao: PVC chống tia cực tím (UV-stabilized PVC), sợi thủy tinh FRP hoặc thép không gỉ SUS304.

##### 4.2.3. Bố trí Không gian Hình học & Cơ cấu Vận hành
###### 4.2.3.1. Phân bố Chiều sâu và Mặt bằng
- Chiều cao thẳng đứng của mô-đun khối tấm/ống: $H_{\text{module}} = 0.5 - 2.0\text{ m}$ (tiêu chuẩn thông dụng nhất: $H_{\text{module}} = 0.75 - 1.0\text{ m}$).
- Chiều dài theo phương nghiêng của ống lắng ($L_{\text{tube}}$):
  $$L_{\text{tube}} = \frac{H_{\text{module}}}{\sin(60^\circ)} = \frac{0.75\text{ m}}{0.8660} \approx 0.866\text{ m}$$
- Tỷ lệ che phủ diện tích đáy bể của mô-đun:
  $$\eta_{\text{cov}} < 75\% \quad (\text{thường chọn } 65\% - 70\%)$$
  để dành khoảng trống phân phối nước êm ở đầu bể và máng xả ở cuối bể.
- Cấu trúc các tầng chiều sâu bể cao trình:
  - Tầng hố chứa bùn và cào xích đáy: $1.0 - 1.5\text{ m}$.
  - Tầng phân phối nước đều dưới khối tấm: $1.2 - 1.5\text{ m}$.
  - Tầng khối mô-đun tấm/ống nghiêng: $0.75 - 1.0\text{ m}$.
  - Tầng nước trong bên trên tấm lắng: $0.5 - 0.8\text{ m}$.
  - Chiều cao an toàn (Freeboard): $0.5\text{ m}$.
  - Tổng chiều sâu bể: $H_{\text{basin}} \approx 4.0 - 5.3\text{ m}$.

###### 4.2.3.2. Hệ thống Cơ khí Rửa Bùn Định kỳ
- **Giàn sục khí làm sạch cặn (Air Scour Grid):** Dưới đáy khối mô-đun lắp đặt một giàn ống đục lỗ cấp khí nén. Định kỳ (ví dụ mỗi tuần một lần), tiến hành sục khí thô ngắt quãng với cường độ mạnh để rung giũ và xé tan các tảng bùn dính bám lâu ngày trên vách ống.
- **Giàn phun nước rửa bề mặt:** Hệ thống vòi phun áp lực thấp quét sạch rêu tảo quang hợp bám ở mép trên khối ống.

---

#### 4.3. Tiêu chuẩn Thiết kế Thủy lực Cho Khối Lắng Cao trình (Slide 38, Bảng tbl_ch03_03)
##### 4.3.1. Các Thông số Định mức Cơ bản
- **Tải trọng bề mặt nạp vào diện tích khối tấm (Surface Loading Rate - $\text{SLR}$):**
  $$\text{SLR} = 60 - 180\text{ m}^3/(\text{m}^2\cdot\text{d}) \quad (\text{gấp 3 - 5 lần bể lắng thông thường})$$
- **Vận tốc dòng chảy tối đa dọc trục ống nghiêng ($v_{\text{tube}}$):**
  $$v_{\text{tube}} \le 0.15\text{ m/min} \quad (\approx 2.5\text{ mm/s} \text{ hay } 0.0025\text{ m/s})$$
- **Thời gian lưu thủy lực trong lòng ống/tấm lắng ($t_{d,\text{tube}}$):**
  - Khối ống tổ ong (Tube settlers): $t_d = 6 - 10\text{ phút}$.
  - Khối tấm song song Lamella (Plate settlers): $t_d = 15 - 25\text{ phút}$.

##### 4.3.2. Tiêu chí Dòng Chảy Tầng & Ổn định Thủy động
- **Số Reynolds cực thấp đảm bảo dòng tầng sâu (Deep Laminar Flow):**
  $$Re_{\text{tube}} = \frac{v_{\text{tube}} \cdot R}{\nu} < 50 \quad (\text{thực tế thường đạt } Re \approx 10 - 25)$$
  Nhờ bán kính thủy lực $R$ cực nhỏ của các ống lục giác ($R \approx 12.5\text{ mm}$), dòng chảy đạt trạng thái chảy tầng tuyệt đối, hoàn toàn triệt tiêu các xoáy rối vi mô, giúp hạt lắng rơi cực nhanh.
- **Số Froude đảm bảo tính ổn định:**
  $$Fr_{\text{tube}} = \frac{v_{\text{tube}}^2}{g \cdot R} > 10^{-5}$$

---

### 5. Tiêu chuẩn Thiết kế, Quy chuẩn Xây dựng & Vận hành (Regulatory & Design Standards)
#### 5.1. Tiêu chuẩn Quốc gia Việt Nam TCVN 7957:2008
##### 5.1.1. Yêu cầu Dự phòng và Số lượng Đơn nguyên Bể
- Trạm xử lý nước thải phải có tối thiểu $N \ge 2$ đơn nguyên bể lắng hoạt động song song để đảm bảo khả năng bảo dưỡng, nạo vét và sửa chữa cơ khí một bể mà hệ thống vẫn duy trì vận hành với bể còn lại mà không gây tràn sự cố.
##### 5.1.2. Thời gian Lưu Thủy lực và Tải trọng Máng Tràn
- Bể lắng đợt 1: Thời gian lưu $t_d = 1.5 - 2.5\text{ h}$ (không quá $3.0\text{ h}$).
- Bể lắng đợt 2: Thời gian lưu $t_d = 2.0 - 4.0\text{ h}$.
- Tải trọng máng tràn qua ngưỡng đập răng cưa: $\text{WOR} \le 10\text{ m}^3/(\text{m}\cdot\text{h})$.
- Độ dốc đáy tối thiểu: $1:600$ đối với bể chữ nhật cào xích; $1:12$ đối với bể tròn gạt bùn trục tâm.

#### 5.2. Tiêu chuẩn Nước thải Xả ra Môi trường Tiếp nhận
##### 5.2.1. QCVN 14:2008/BTNMT (Nước thải Sinh hoạt)
- Cột A (nguồn nước tiếp nhận dùng cho mục đích cấp nước sinh hoạt):
  - $\text{TSS} \le 50\text{ mg/L}$; $\text{BOD}_5 \le 30\text{ mg/L}$.
- Cột B (nguồn nước tiếp nhận không dùng cho cấp nước sinh hoạt):
  - $\text{TSS} \le 100\text{ mg/L}$; $\text{BOD}_5 \le 50\text{ mg/L}$.
##### 5.2.2. QCVN 40:2011/BTNMT (Nước thải Công nghiệp)
- Cột A: $\text{TSS} \le 50\text{ mg/L}$; $\text{COD} \le 75\text{ mg/L}$.
- Cột B: $\text{TSS} \le 100\text{ mg/L}$; $\text{COD} \le 150\text{ mg/L}$.
- Bể lắng phải vận hành đồng bộ và kiểm soát tải trọng chất rắn nghiêm ngặt để đảm bảo nước sau lắng đáp ứng các giới hạn $\text{TSS}$ nêu trên.

#### 5.3. Tiêu chuẩn Thiết kế Quốc tế WEF MOP 8 & Metcalf and Eddy
- Sidewater depth bể lắng đợt 2: Tối thiểu $4.0\text{ m}$ (khuyến nghị $4.5 - 5.5\text{ m}$ cho các công nghệ BNR quy mô lớn).
- Vận tốc cào bùn đầu mút: Giới hạn $1.5 - 3.0\text{ m/min}$ để tránh khuấy động bùn đáy.
- Hệ số chuyển đổi tải trọng đỉnh: Đảm bảo bể lắng duy trì ổn định tại lưu lượng đỉnh $Q_{\text{peak}} / Q_{\text{avg}} = 2.0 - 3.0$.

---

### 6. Bảng Tra Cứu Thông số & Sự cố Vận hành (Lookup Tables & Operational Troubleshooting)
#### 6.1. Bảng Tổng hợp Tiêu chuẩn Thiết kế Toàn diện Các Loại Bể Lắng

| Thông số Thiết kế / Kỹ thuật | Ký hiệu | Bể Lắng Sơ bộ / Đợt 1 | Bể Lắng Đợt 2 (Air AS) | Bể Lắng Đợt 2 (BNR) | Bể Lắng Cao trình (Tube/Plate) | Đơn vị |
|---|---|---|---|---|---|---|
| **Tải trọng bề mặt trung bình** | $\text{SOR}$ | $30 - 50$ | $16 - 28$ | $24 - 32$ | $60 - 180$ | $\text{m}^3/(\text{m}^2\cdot\text{d})$ |
| **Tải trọng bề mặt giờ cao điểm** | $\text{SOR}_{\text{peak}}$ | $80 - 120$ | $32 - 48$ | $40 - 64$ | - | $\text{m}^3/(\text{m}^2\cdot\text{d})$ |
| **Thời gian lưu thủy lực** | $t_d$ | $1.5 - 2.5$ | $2.0 - 4.0$ | $2.0 - 4.0$ | $0.1 - 0.4$ ($6 - 25\text{ min}$) | $\text{h}$ |
| **Chiều sâu nước thành bể** | $SWD$ | $3.0 - 4.5$ | $4.0 - 5.5$ | $4.0 - 5.5$ | $3.5 - 5.0$ | $\text{m}$ |
| **Tải trọng chất rắn trung bình** | $\text{SLR}$ | - | $4.0 - 6.0$ | $5.0 - 8.0$ | - | $\text{kg}/(\text{m}^2\cdot\text{h})$ |
| **Tải trọng máng tràn tối đa** | $\text{WOR}$ | $\le 240$ | $\le 125 - 250$ | $\le 125 - 250$ | $\le 240$ | $\text{m}^3/(\text{m}\cdot\text{d})$ |
| **Tỷ lệ chiều dài : chiều rộng** | $L/W$ | $4:1 - 6:1$ ($\ge 6:1$) | $\ge 6:1$ | $\ge 6:1$ | Tùy biến mặt bằng | - |
| **Tỷ lệ chiều dài : chiều sâu** | $L/D$ | $\ge 15:1$ | $\ge 15:1$ | $\ge 15:1$ | - | - |
| **Chiều rộng tối đa khoang xích** | $W_{\text{max}}$ | $6.0$ | $6.0$ | $6.0$ | $6.0$ | $\text{m}$ |
| **Vận tốc dòng ngang** | $v_H$ | $0.005 - 0.018$ | $0.005 - 0.018$ | $0.005 - 0.018$ | - | $\text{m/s}$ |
| **Số Reynolds dòng chảy** | $Re$ | $< 20,000$ | $< 20,000$ | $< 20,000$ | $< 50$ | Không thứ nguyên |
| **Số Froude ổn định** | $Fr$ | $> 10^{-5}$ | $> 10^{-5}$ | $> 10^{-5}$ | $> 10^{-5}$ | Không thứ nguyên |
| **Độ dốc đáy bể chữ nhật** | $S_{\text{rect}}$ | $1:600 - 1:100$ | $1:600$ | $1:600$ | $1:600$ | Tỷ lệ dốc |
| **Độ dốc đáy nón bể tròn** | $S_{\text{circ}}$ | $1:12$ ($\sim 8.3\%$) | $1:12$ | $1:12$ | $1:12$ | Tỷ lệ dốc |
| **Góc nghiêng tấm/ống lắng** | $\theta$ | - | - | - | $55^\circ - 60^\circ$ | Độ |
| **Vận tốc dọc ống tối đa** | $v_{\text{tube}}$ | - | - | - | $\le 0.15$ | $\text{m/min}$ |

---

#### 6.2. Sổ tay Xử lý Khắc phục Sự cố Vận hành (Troubleshooting Matrix)

| Sự cố Vận hành | Dấu hiệu / Hiện tượng | Nguyên nhân Cốt lõi | Biện pháp Khắc phục Kỹ thuật |
|---|---|---|---|
| **Đoản mạch thủy lực & Nước trong bị đục** | Nước sau lắng có nhiều bông cặn li ti trôi qua đập; lưu lượng phân bố không đều giữa các ngăn máng tràn. | - Chênh lệch cao trình mép đập răng cưa V-notch.<br>- Vách đục lỗ đầu vào bị bám rác gây tắc nghẽn cục bộ.<br>- Vận tốc nạp nước vào quá cao tạo tia phản lực. | - Dùng thiết bị cân livo quang học vi chỉnh lại bu lông từng tấm răng cưa.<br>- Nạo vét vệ sinh vách đục lỗ.<br>- Bổ sung tấm chắn tiêu năng (baffle plate) trước vách vào. |
| **Bùn bị phân hủy thối rữa và nổi mảng** | Các tảng bùn màu xám đen, bốc mùi trứng thối ($\text{H}_2\text{S}$), có bọt khí sủi bọt đẩy bùn nổi dầy đặc trên mặt nước. | - Chu kỳ xả bùn sơ bộ quá thưa, bùn lưu lại đáy $> 3\text{ h}$ trong điều kiện trời nóng.<br>- Thiết bị cào xích bị đứt hoặc trượt xích, bùn đọng ở góc chết. | - Tăng tần suất và thời gian bơm hút bùn đáy.<br>- Kiểm tra căng xích cào, thay bánh sao bị mòn.<br>- Rửa bùn khẩn cấp bằng nước áp lực và hạ mực nước kiểm tra. |
| **Phân tầng mật độ do nhiệt độ** | Nước đầu vào lao vút sát đáy (trời lạnh) cuốn tung bùn đáy; hoặc trượt thẳng trên mặt (trời nắng ấm) tràn ra đập trong vài phút. | Chênh lệch nhiệt độ lớn giữa nước thải nạp và nước tồn lưu trong bể dẫn đến hiện tượng chìm đáy (plunging) hoặc trượt mặt. | - Lắp tấm chắn hướng dòng ngập sâu tại cửa vào.<br>- Tăng chiều sâu giếng phân phối trung tâm ($D_{\text{well}}$) ở bể tròn.<br>- Đặt vách ngăn trung gian trong vùng lắng. |
| **Tắc nghẽn & Đóng rêu tảo khối tấm lắng** | Vận tốc dâng qua khối ống không đều; xuất hiện mảng rêu tảo xanh bám trên miệng ống; bùn tích tụ làm biến dạng sập mô-đun. | - Tấm lắng đặt góc nghiêng $< 50^\circ$ hoặc bùn dính bám không trượt được.<br>- Ánh sáng mặt trời kích thích tảo quang hợp.<br>- Nước có nhiều chất xơ, rác nilon lọt qua song chắn rác. | - Định kỳ kích hoạt giàn sục khí thô nén (Air Scour) để giũ sạch bùn dính bám.<br>- Che mái vòm composite tối màu ngăn ánh nắng mặt trời chiếu rọi trực tiếp.<br>- Phun rửa bằng vòi nước áp lực thấp. |
| **Bùn sinh học dâng cao trôi qua đập (Lắng 2)** | Chiều dày mền bùn (Sludge blanket) dâng lên chiếm quá $2/3$ chiều sâu bể, bùn tràn qua đập vào giờ cao điểm. | - Tải trọng chất rắn $\text{SLR}$ vượt quá thông lượng giới hạn $G_L$.<br>- Hiện tượng bùn khó lắng, bùn phồng (Sludge bulking) do vi khuẩn dạng sợi (Filamentous) với $\text{SVI} > 200\text{ mL/g}$. | - Tăng lưu lượng bơm bùn tuần hoàn $\text{RAS}$ để hạ thấp mền bùn.<br>- Châm bổ sung polymer trợ lắng cation hoặc hóa chất keo tụ PAC.<br>- Kiểm soát DO, F/M và bổ sung chất diệt khuẩn dạng sợi (Chlorine/$\text{H}_2\text{O}_2$) liều thấp vào dòng $\text{RAS}$. |

---

### 7. Bài Tập Tính Toán Thiết Kế Toàn Diện (Comprehensive Worked Examples)
#### 7.1. Bài toán 1: Thiết kế Bể Lắng Chữ Nhật Đợt 1 (Rectangular Primary Clarifier Design)
##### 7.1.1. Đề bài & Thông số Kỹ thuật Đầu vào
- **Nguồn trích dẫn:** Handout Chương 3, Slide 29 (`EX-CH03-01`).
- **Đề bài:** Thiết kế hệ thống bể lắng hình chữ nhật xử lý nước thải sinh hoạt với lưu lượng trung bình ngày $Q = 0.5\text{ m}^3/\text{s}$. Nước có độ nhớt động học tại $20^\circ\text{C}$ là $\nu = 1.003 \times 10^{-6}\text{ m}^2/\text{s}$.
- **Thông số nước thải thô:**
  - Lưu lượng trung bình: $Q_{\text{avg}} = 0.5\text{ m}^3/\text{s} = 1,800\text{ m}^3/\text{h} = 43,200\text{ m}^3/\text{d}$.
  - Hệ số lưu lượng đỉnh không điều hòa: $K_{\text{peak}} = 2.0 \implies Q_{\text{peak}} = 1.0\text{ m}^3/\text{s} = 86,400\text{ m}^3/\text{d}$.
  - Nồng độ cặn lơ lửng đầu vào: $\text{TSS}_{\text{in}} = 280\text{ mg/L} = 0.28\text{ kg/m}^3$.
  - Hiệu suất lắng khử $\text{TSS}$ mục tiêu: $\eta_{\text{TSS}} = 65\%$.
  - Độ ẩm bùn tươi sơ bộ tích tụ ở hố thu bùn: $p = 95\%$ (tương đương nồng độ cặn bùn $C_{\text{sludge}} = 5\% = 50,000\text{ mg/L}$, khối lượng riêng bùn $\rho_{\text{sludge}} \approx 1,020\text{ kg/m}^3$).
  - Chu kỳ xả bùn định kỳ: $T_{\text{sludge}} = 24\text{ giờ}$ (xả 1 lần/ngày).

##### 7.1.2. Bước 1: Lựa chọn Số lượng Bể & Tải trọng Bề mặt ($\text{SOR}$)
- **Số lượng đơn nguyên:** Để đảm bảo tính dự phòng linh hoạt theo TCVN 7957:2008, chọn xây dựng $N = 4$ đơn nguyên bể lắng hình chữ nhật song song nhau ($N = 4$ bays).
- **Lưu lượng tính toán cho mỗi đơn nguyên bể:**
  $$Q_1 = \frac{Q_{\text{avg}}}{N} = \frac{0.5\text{ m}^3/\text{s}}{4} = 0.125\text{ m}^3/\text{s} = 450\text{ m}^3/\text{h} = 10,800\text{ m}^3/\text{d}$$
  Tại lưu lượng đỉnh:
  $$Q_{1,\text{peak}} = \frac{1.0\text{ m}^3/\text{s}}{4} = 0.25\text{ m}^3/\text{s} = 900\text{ m}^3/\text{h} = 21,600\text{ m}^3/\text{d}$$
- **Lựa chọn Tải trọng bề mặt ($\text{SOR}$):**
  - Tra cứu dải chuẩn cho lắng sơ bộ (Slide 23): Chọn $\text{SOR} = 24.0\text{ m}^3/(\text{m}^2\cdot\text{d})$ (hay $1.0\text{ m/h}$).
- **Diện tích bề mặt ướt yêu cầu cho mỗi đơn nguyên bể:**
  $$A_s = \frac{Q_1}{\text{SOR}} = \frac{10,800\text{ m}^3/\text{d}}{24.0\text{ m}^3/(\text{m}^2\cdot\text{d})} = 450.0\text{ m}^2$$
  - Tổng diện tích mặt ướt của cả 4 bể: $A_{s,\text{total}} = 4 \times 450 = 1,800\text{ m}^2$.

##### 7.1.3. Bước 2: Xác định Kích thước Hình học Cơ bản
- **Chiều rộng đơn nguyên bể ($W$):**
  - Để áp dụng thiết bị cào bùn gạt váng kiểu thanh cào - dây xích (Chain-and-flight scraper) tiêu chuẩn mà không bị võng trục, quy chuẩn kỹ thuật quy định chiều rộng tối đa $W \le 6.0\text{ m}$.
  - Chọn $W = 6.0\text{ m}$.
- **Chiều dài hữu ích của bể ($L$):**
  $$L = \frac{A_s}{W} = \frac{450.0\text{ m}^2}{6.0\text{ m}} = 75.0\text{ m}$$
- **Kiểm tra Tỷ lệ Kích thước Hình học:**
  - Tỷ lệ dài trên rộng:
    $$\frac{L}{W} = \frac{75.0}{6.0} = 12.5:1 \ge 6:1 \quad (\text{Thỏa mãn hoàn hảo khuyến nghị } L/W \ge 6:1)$$
- **Lựa chọn Chiều sâu Nước Hữu dụng ($D$):**
  - Tra cứu phạm vi chuẩn cho bể lắng ($4.0 - 5.5\text{ m}$): Chọn $D = 4.0\text{ m}$.
- **Kiểm tra Tỷ lệ Dài trên Sâu:**
  $$\frac{L}{D} = \frac{75.0}{4.0} = 18.75:1 \ge 15:1 \quad (\text{Thỏa mãn tiêu chuẩn } L/D \ge 15:1)$$
- **Chiều cao Tổng cộng của Thành bể ($H_{\text{total}}$):**
  - Chiều sâu vùng chứa bùn đáy: $h_{\text{sludge}} = 0.8\text{ m}$ (dải $0.6 - 1.0\text{ m}$).
  - Chiều cao an toàn mặt thoáng (Freeboard): $h_{\text{FB}} = 0.5\text{ m}$.
  - Tổng chiều cao thành bể xây dựng:
    $$H_{\text{total}} = D + h_{\text{sludge}} + h_{\text{FB}} = 4.0 + 0.8 + 0.5 = 5.3\text{ m}$$

##### 7.1.4. Bước 3: Tính Thời gian Lưu Thủy lực ($\text{HRT}$)
- **Thể tích hữu ích công tác của một bể:**
  $$V_1 = L \times W \times D = 75.0\text{ m} \times 6.0\text{ m} \times 4.0\text{ m} = 1,800.0\text{ m}^3$$
- **Thời gian lưu thủy lực tại lưu lượng trung bình ($t_d$):**
  $$t_d = \frac{V_1}{Q_1} = \frac{1,800\text{ m}^3}{450\text{ m}^3/\text{h}} = 4.00\text{ giờ} = 240\text{ phút} \quad \left( = \frac{D}{\text{SOR}} = \frac{4.0\text{ m}}{1.0\text{ m/h}} = 4.0\text{ h} \right)$$
- **Thời gian lưu tại lưu lượng đỉnh ($t_{d,\text{peak}}$):**
  $$t_{d,\text{peak}} = \frac{1,800\text{ m}^3}{900\text{ m}^3/\text{h}} = 2.00\text{ giờ} \ge 1.0\text{ h} \quad (\text{Thỏa mãn})$$

##### 7.1.5. Bước 4: Kiểm tra Vận tốc Dòng chảy Ngang ($v_H$)
- **Tiết diện ướt ngang dòng chảy ($A_c$):**
  $$A_c = W \times D = 6.0\text{ m} \times 4.0\text{ m} = 24.0\text{ m}^2$$
- **Vận tốc dòng chảy ngang tại lưu lượng trung bình:**
  $$v_H = \frac{Q_1}{A_c} = \frac{0.125\text{ m}^3/\text{s}}{24.0\text{ m}^2} = 0.005208\text{ m/s} = 5.21\text{ mm/s} = 0.312\text{ m/min}$$
- **Kiểm tra điều kiện tiêu chuẩn:**
  $$0.005\text{ m/s} \le v_H = 0.00521\text{ m/s} \le 0.018\text{ m/s} \quad \implies \text{ĐẠT CHUẨN}$$
- Tại lưu lượng đỉnh: $v_{H,\text{peak}} = \frac{0.25}{24.0} = 0.0104\text{ m/s} \le 0.018\text{ m/s}$ (ĐẠT).

##### 7.1.6. Bước 5: Kiểm tra Ổn định Thủy động Lực học ($Re$ và $Fr$)
- **Chu vi ướt của tiết diện dẫn dòng ($P$):**
  $$P = W + 2D = 6.0 + 2 \times 4.0 = 14.0\text{ m}$$
- **Bán kính thủy lực ($R$):**
  $$R = \frac{A_c}{P} = \frac{24.0\text{ m}^2}{14.0\text{ m}} \approx 1.714\text{ m}$$
- **Kiểm tra Số Reynolds ($Re$):**
  $$Re = \frac{v_H \cdot R}{\nu} = \frac{0.005208\text{ m/s} \times 1.714\text{ m}}{1.003 \times 10^{-6}\text{ m}^2/\text{s}} = \frac{0.008927}{1.003 \times 10^{-6}} \approx 8,900$$
  - So sánh tiêu chuẩn: $Re = 8,900 < 20,000 \implies \text{ĐẠT CHUẨN ỔN ĐỊNH DÒNG CHẢY}$.
- **Kiểm tra Số Froude ($Fr$):**
  - Tại lưu lượng trung bình:
    $$Fr = \frac{v_H^2}{g \cdot R} = \frac{(0.005208)^2}{9.81 \times 1.714} = \frac{2.712 \times 10^{-5}}{16.814} \approx 1.61 \times 10^{-6}$$
  - Tại lưu lượng đỉnh ($Q_{\text{peak}} = 2 \times Q_{\text{avg}}$):
    $$v_{H,\text{peak}} = 0.01042\text{ m/s} \implies Fr_{\text{peak}} = \frac{(0.01042)^2}{9.81 \times 1.714} = \frac{1.085 \times 10^{-4}}{16.814} \approx 6.45 \times 10^{-6}$$
    *(Tại đỉnh lưu lượng, dòng chảy kháng hoàn toàn các xáo trộn mặt thoáng)*.

##### 7.1.7. Bước 6: Kiểm tra Vận tốc Cuốn Cặn Tới hạn của Camp ($v_c$)
- Áp dụng phương trình Camp với các thông số bông bùn hữu cơ:
  - Hệ số dính kết: $k = 0.05$ (dải $0.04 - 0.06$).
  - Tỷ trọng tương đối của bông cặn: $s = 1.20$.
  - Đường kính bông cặn đại diện: $d = 100\,\mu\text{m} = 0.0001\text{ m}$.
  - Hệ số ma sát lòng bể bê tông: $f = 0.025$ (dải $0.02 - 0.03$).
  - Gia tốc trọng trường: $g = 9.81\text{ m/s}^2$.
- Tính vận tốc cuốn cặn tới hạn:
  $$v_c = \sqrt{\frac{8 \cdot k \cdot (s - 1) \cdot g \cdot d}{f}} = \sqrt{\frac{8 \times 0.05 \times (1.20 - 1) \times 9.81 \times 0.0001}{0.025}}$$
  $$v_c = \sqrt{\frac{0.40 \times 0.20 \times 9.81 \times 10^{-4}}{0.025}} = \sqrt{\frac{7.848 \times 10^{-5}}{0.025}} = \sqrt{3.1392 \times 10^{-3}} \approx 0.0560\text{ m/s} = 56.0\text{ mm/s}$$
- **So sánh và Kết luận An toàn:**
  $$v_H = 0.00521\text{ m/s} \ll v_c = 0.0560\text{ m/s}$$
  - Hệ số an toàn chống cuốn bùn:
    $$FS = \frac{v_c}{v_H} = \frac{0.0560}{0.00521} \approx 10.75 > 1.0 \implies \text{TUYỆT ĐỐI KHÔNG BỊ CUỐN CẶN}$$

##### 7.1.8. Bước 7: Thiết kế Hệ thống Máng Tràn Đầu Ra & Đập Răng Cưa V-Notch
- **Kiểm tra Tải trọng Máng tràn ($\text{WOR}$):**
  - Tải trọng tràn tối đa theo TCVN 7957:2008: $\text{WOR}_{\text{max}} = 240\text{ m}^3/(\text{m}\cdot\text{d})$.
  - Chiều dài mép tràn yêu cầu tối thiểu cho mỗi bể:
    $$L_{\text{weir,req}} = \frac{Q_1}{\text{WOR}_{\text{max}}} = \frac{10,800\text{ m}^3/\text{d}}{240\text{ m}^3/(\text{m}\cdot\text{d})} = 45.0\text{ m}$$
- **Bố trí kết cấu Máng thu Ngón tay (Finger Launders):**
  - Vì chiều rộng bể chỉ có $W = 6.0\text{ m}$, nếu chỉ đặt đập tràn ngang thành cuối bể thì chiều dài chỉ đạt $6.0\text{ m} < 45.0\text{ m}$ (sẽ gây quá tải máng tràn gấp $7.5$ lần).
  - Do đó, thiết kế hệ thống $3$ máng tràn ngón tay nằm dọc song song vươn ngược dòng, mỗi máng tràn có 2 mép tràn thu nước 2 bên bờ:
    - Số mép tràn thu nước: $m = 3 \times 2 = 6$ mép tràn.
    - Chiều dài yêu cầu của mỗi máng:
      $$L_{\text{launder}} = \frac{45.0\text{ m}}{6} = 7.5\text{ m}$$
    - Chiều dài này chiếm $7.5\text{ m} / 75.0\text{ m} = 10\%$ chiều dài bể. Để tăng biên độ an toàn, thiết kế máng dài $L_{\text{launder}} = 15.0\text{ m}$ (chiếm $20\%$ chiều dài bể), mang lại tổng chiều dài mép tràn thực tế:
      $$L_{\text{weir,actual}} = 6 \times 15.0\text{ m} = 90.0\text{ m}$$
    - Tải trọng máng tràn thực tế:
      $$\text{WOR}_{\text{actual}} = \frac{10,800\text{ m}^3/\text{d}}{90.0\text{ m}} = 120.0\text{ m}^3/(\text{m}\cdot\text{d}) \quad (\text{Rất an toàn, chỉ bằng } 50\% \text{ giới hạn cho phép})$$
- **Quy cách Đập Răng cưa V-Notch:**
  - Tấm đập bằng inox 304 xẻ rãnh chữ V góc $90^\circ$, chiều sâu khía $75\text{ mm}$, khoảng cách giữa 2 đỉnh rãnh là $200\text{ mm}$ ($0.2\text{ m}$).
  - Tổng số vết cắt V-notch trên mỗi bể:
    $$N_{\text{notch}} = \frac{L_{\text{weir,actual}}}{0.2\text{ m}} = \frac{90.0}{0.2} = 450\text{ rãnh V}$$
  - Phía trước các máng tràn bố trí tấm chắn bọt váng nổi ngập sâu $200\text{ mm}$.

##### 7.1.9. Bước 8: Tính toán Lượng Bùn Tươi Sơ bộ & Kích thước Hố Thu Bùn
- **Khối lượng cặn khô lắng được mỗi ngày trong 1 đơn nguyên bể ($M_{\text{dry}}$):**
  $$M_{\text{dry}} = Q_1 \times \text{TSS}_{\text{in}} \times \eta_{\text{TSS}} = 10,800\text{ m}^3/\text{d} \times 0.280\text{ kg/m}^3 \times 0.65 = 1,965.6\text{ kg cặn khô/ngày}$$
- **Thể tích bùn tươi ướt phát sinh hàng ngày ($V_{\text{sludge}}$ với độ ẩm $p = 95\%$):**
  $$V_{\text{sludge}} = \frac{M_{\text{dry}}}{\rho_{\text{sludge}} \times (1 - p)} = \frac{1,965.6\text{ kg/d}}{1,020\text{ kg/m}^3 \times (1 - 0.95)} = \frac{1,965.6}{51.0} \approx 38.54\text{ m}^3/\text{ngày}$$
- **Kích thước Hố thu Bùn (Sludge Hopper):**
  - Xả bùn $1$ lần/ngày, hố thu cần dung tích tối thiểu $38.54\text{ m}^3$.
  - Thiết kế $2$ hố thu bùn hình chóp cụt đáy vuông đặt cạnh nhau ở đầu bể:
    - Kích thước miệng trên mỗi hố: $a_1 = 3.0\text{ m}, b_1 = 3.0\text{ m} \implies S_1 = 9.0\text{ m}^2$.
    - Kích thước đáy dưới mỗi hố: $a_2 = 1.0\text{ m}, b_2 = 1.0\text{ m} \implies S_2 = 1.0\text{ m}^2$.
    - Chiều cao hố chóp cụt ($h_h$):
      $$V_{\text{hố}} = \frac{h_h}{3} \cdot (S_1 + S_2 + \sqrt{S_1 \cdot S_2}) = \frac{h_h}{3} \cdot (9.0 + 1.0 + \sqrt{9.0}) = \frac{h_h}{3} \cdot 13.0 = 4.333 \cdot h_h$$
    - Thể tích yêu cầu cho mỗi hố: $V_{\text{req}} = 38.54 / 2 = 19.27\text{ m}^3$.
    - Chiều cao hố thu bùn yêu cầu:
      $$h_h = \frac{19.27}{4.333} \approx 4.45\text{ m}$$
    - Góc nghiêng thành hố: $\tan\beta = \frac{4.45}{(3.0 - 1.0)/2} = \frac{4.45}{1.0} = 4.45 \implies \beta \approx 77^\circ > 60^\circ$ (Đảm bảo bùn tự trượt hoàn toàn).

---

#### 7.2. Bài toán 2: Thiết kế Bể Lắng Tròn Tâm Phân Phối (Center-Feed Circular Clarifier Design)
##### 7.2.1. Đề bài & Điều kiện Kỹ thuật Đầu vào
- **Đề bài:** Thiết kế hệ thống bể lắng đợt 1 hình tròn kiểu nạp tâm (Center-feed circular clarifier) cho nhà máy xử lý nước thải sinh hoạt với công suất thiết kế trung bình $Q = 20,000\text{ m}^3/\text{d}$.
- **Thông số lựa chọn thiết kế:**
  - Số lượng bể hoạt động song song: $N = 2$ bể.
  - Tải trọng bề mặt thiết kế: $\text{SOR} = 35.0\text{ m}^3/(\text{m}^2\cdot\text{d})$ (dải $30 - 50\text{ m}^3/\text{m}^2\cdot\text{d}$).
  - Chiều sâu nước công tác thành bể: $SWD = 3.8\text{ m}$.
  - Độ dốc nón đáy bể: $1:12$ dốc về hố thu tâm bể.
  - Tải trọng máng tràn chu vi tối đa: $\text{WOR}_{\text{max}} = 180\text{ m}^3/(\text{m}\cdot\text{d})$.

##### 7.2.2. Bước 1: Tính toán Diện tích Bề mặt & Đường kính Bể
- **Lưu lượng nạp cho mỗi bể:**
  $$Q_1 = \frac{Q}{2} = \frac{20,000\text{ m}^3/\text{d}}{2} = 10,000\text{ m}^3/\text{d} \approx 416.67\text{ m}^3/\text{h} = 0.1157\text{ m}^3/\text{s}$$
- **Diện tích bề mặt ướt yêu cầu mỗi bể:**
  $$A_s = \frac{Q_1}{\text{SOR}} = \frac{10,000\text{ m}^3/\text{d}}{35.0\text{ m}^3/(\text{m}^2\cdot\text{d})} \approx 285.71\text{ m}^2$$
- **Đường kính trong của bể lắng ($D_{\text{tank}}$):**
  $$D_{\text{tank}} = \sqrt{\frac{4 \cdot A_s}{\pi}} = \sqrt{\frac{4 \times 285.71}{3.14159}} = \sqrt{363.78} \approx 19.07\text{ m}$$
  - Làm tròn chuẩn hóa thi công xây dựng: Chọn $D_{\text{tank}} = 19.5\text{ m}$.
- **Diện tích mặt bằng thực tế:**
  $$A_{s,\text{actual}} = \frac{\pi \cdot D_{\text{tank}}^2}{4} = \frac{\pi \times (19.5)^2}{4} \approx 298.65\text{ m}^2$$
- **Tải trọng bề mặt thực tế:**
  $$\text{SOR}_{\text{actual}} = \frac{10,000}{298.65} = 33.48\text{ m}^3/(\text{m}^2\cdot\text{d}) \le 35.0 \quad (\text{Thỏa mãn})$$

##### 7.2.3. Bước 2: Thiết kế Giếng Nạp Trung tâm (Center Feedwell)
- Đường kính giếng phân phối trung tâm thường chọn bằng $20\%$ đường kính bể:
  $$D_{\text{well}} = 0.20 \times D_{\text{tank}} = 0.20 \times 19.5\text{ m} = 3.90\text{ m} \quad (\text{Chọn } D_{\text{well}} = 4.0\text{ m})$$
- Chiều sâu giếng nạp ngập dưới mặt nước:
  $$h_{\text{well}} = 0.40 \times SWD = 0.40 \times 3.8\text{ m} = 1.52\text{ m} \quad (\text{Chọn } 1.50\text{ m})$$
- Diện tích mặt thoáng của giếng trung tâm:
  $$A_{\text{well}} = \frac{\pi \cdot D_{\text{well}}^2}{4} = \frac{\pi \times (4.0)^2}{4} = 12.57\text{ m}^2$$
- Diện tích lắng hữu dụng thực tế bên ngoài giếng:
  $$A_{\text{net}} = A_{s,\text{actual}} - A_{\text{well}} = 298.65 - 12.57 = 286.08\text{ m}^2 \ge 285.71\text{ m}^2 \quad (\text{ĐẠT})$$

##### 7.2.4. Bước 3: Chiều sâu Đáy Nón và Thể tích Toàn Bể
- **Độ dốc đáy bể ($1:12$):**
  - Khoảng cách từ thành bể đến mép giếng thu bùn tâm (bán kính $R = D_{\text{tank}} / 2 = 9.75\text{ m}$):
    $$\Delta h_{\text{slope}} = \frac{R}{12} = \frac{9.75\text{ m}}{12} = 0.8125\text{ m}$$
- **Chiều sâu nước tại tâm bể ($H_{\text{center}}$):**
  $$H_{\text{center}} = SWD + \Delta h_{\text{slope}} = 3.8\text{ m} + 0.81\text{ m} = 4.61\text{ m}$$
- **Thể tích phần hình trụ trên đáy ($V_{\text{cylinder}}$):**
  $$V_{\text{cylinder}} = A_{s,\text{actual}} \times SWD = 298.65\text{ m}^2 \times 3.8\text{ m} \approx 1,134.87\text{ m}^3$$
- **Thể tích phần nón cụt đáy bể ($V_{\text{cone}}$):**
  $$V_{\text{cone}} = \frac{1}{3} \times A_{s,\text{actual}} \times \Delta h_{\text{slope}} = \frac{1}{3} \times 298.65 \times 0.8125 \approx 80.89\text{ m}^3$$
- **Tổng thể tích hữu ích của bể:**
  $$V_{\text{total}} = V_{\text{cylinder}} + V_{\text{cone}} = 1,134.87 + 80.89 = 1,215.76\text{ m}^3$$
- **Thời gian lưu thủy lực ($\text{HRT}$):**
  $$t_d = \frac{V_{\text{total}}}{Q_1} = \frac{1,215.76\text{ m}^3}{416.67\text{ m}^3/\text{h}} \approx 2.92\text{ giờ} \quad (\text{Thỏa mãn dải } 1.5 - 3.0\text{ h})$$

##### 7.2.5. Bước 4: Kiểm tra Chiều dài Mép tràn & Tải trọng Máng tràn Chu vi
- **Bố trí máng tràn đơn dọc theo toàn bộ chu vi vách ngoài bể:**
  - Đường kính đường mép tràn: $D_{\text{weir}} \approx D_{\text{tank}} = 19.5\text{ m}$.
  - Chiều dài mép tràn chu vi:
    $$L_{\text{weir}} = \pi \times D_{\text{weir}} = \pi \times 19.5\text{ m} \approx 61.26\text{ m}$$
- **Kiểm tra Tải trọng Máng tràn ($\text{WOR}$):**
  $$\text{WOR} = \frac{Q_1}{L_{\text{weir}}} = \frac{10,000\text{ m}^3/\text{d}}{61.26\text{ m}} \approx 163.2\text{ m}^3/(\text{m}\cdot\text{d})$$
- **So sánh tiêu chuẩn:**
  $$\text{WOR} = 163.2\text{ m}^3/(\text{m}\cdot\text{d}) \le 180\text{ m}^3/(\text{m}\cdot\text{d}) \quad (\text{ĐẠT TIÊU CHUẨN KỸ THUẬT})$$
  *(Không cần thiết kế máng hai bờ tràn, giúp đơn giản hóa kết cấu cốp pha và giảm chi phí xây dựng)*.

---

#### 7.3. Bài toán 3: Thiết kế Bể Lắng Cao Trình Ống Nghiêng (High-Rate Tube Settler Basin Design)
##### 7.3.1. Đề bài & Điều kiện Kỹ thuật Đầu vào
- **Nguồn trích dẫn:** Handout Chương 3, Slide 39 (`EX-CH03-02`).
- **Đề bài:** Thiết kế bể lắng tốc độ cao sử dụng khối ống lắng nghiêng lục giác (Tube Settlers) cho nhà máy xử lý nước thải sinh hoạt có lưu lượng trung bình $Q = 0.5\text{ m}^3/\text{s} = 43,200\text{ m}^3/\text{d}$. Độ nhớt động học nước ở $20^\circ\text{C}$ là $\nu = 1.003 \times 10^{-6}\text{ m}^2/\text{s}$. Đường kính trong của các ống lắng là $d = 50\text{ mm} = 0.05\text{ m}$.
- **Thông số quy chuẩn tra cứu (Slide 38, Bảng tbl_ch03_03):**
  - Tải trọng bề mặt thiết kế khối ống: $\text{SLR} = 120.0\text{ m}^3/(\text{m}^2\cdot\text{d})$ (dải $60 - 180\text{ m}^3/\text{m}^2\cdot\text{d}$).
  - Góc nghiêng ống lắng so với phương ngang: $\theta = 60^\circ$ (đảm bảo bùn tự trượt dốc).
  - Vận tốc dòng chảy tối đa cho phép dọc ống: $v_{\text{max}} \le 0.15\text{ m/min}$.
  - Tỷ lệ diện tích đáy bể được lắp đặt mô-đun ống: $\eta_{\text{cov}} = 70\%$ ($< 75\%$).
  - Chiều cao thẳng đứng của khối mô-đun ống: $H_{\text{module}} = 0.75\text{ m}$ (dải $0.5 - 2.0\text{ m}$).
  - Số lượng đơn nguyên bể: $N = 2$ bể song song.
  - Chiều rộng mỗi khoang bể: $W = 6.0\text{ m}$ (khớp kích thước chuẩn của thanh cào xích đáy).

##### 7.3.2. Bước 1: Tính Diện tích Mặt bằng Khối Ống & Toàn Bể Lắng
- **Lưu lượng nạp tổng thể:**
  $$Q = 0.5\text{ m}^3/\text{s} = 30.0\text{ m}^3/\text{min} = 1,800\text{ m}^3/\text{h} = 43,200\text{ m}^3/\text{d}$$
- **Tổng diện tích mặt bằng yêu cầu lắp đặt ống lắng ($A_{\text{tube,plan}}$):**
  $$A_{\text{tube,plan}} = \frac{Q}{\text{SLR}} = \frac{43,200\text{ m}^3/\text{d}}{120.0\text{ m}^3/(\text{m}^2\cdot\text{d})} = 360.0\text{ m}^2$$
- **Tổng diện tích mặt thoáng toàn bộ công trình bể lắng ($A_{\text{basin}}$):**
  $$A_{\text{basin}} = \frac{A_{\text{tube,plan}}}{\eta_{\text{cov}}} = \frac{360.0\text{ m}^2}{0.70} \approx 514.29\text{ m}^2$$
- **Phân chia cho $N = 2$ đơn nguyên bể:**
  - Diện tích khối ống mỗi bể: $A_{\text{tube},1} = \frac{360.0}{2} = 180.0\text{ m}^2$.
  - Diện tích mặt bằng mỗi bể: $A_{\text{basin},1} = \frac{514.29}{2} \approx 257.14\text{ m}^2$.

##### 7.3.3. Bước 2: Xác định Kích thước Hình học Đơn nguyên Bể
- **Chiều rộng mỗi bể:** $W = 6.0\text{ m}$.
- **Chiều dài vùng lắp đặt mô-đun ống lắng ($L_{\text{tube}}$):**
  $$L_{\text{tube}} = \frac{A_{\text{tube},1}}{W} = \frac{180.0\text{ m}^2}{6.0\text{ m}} = 30.0\text{ m}$$
- **Chiều dài tổng cộng của bể lắng ($L_{\text{basin}}$):**
  $$L_{\text{basin}} = \frac{A_{\text{basin},1}}{W} = \frac{257.14\text{ m}^2}{6.0\text{ m}} \approx 42.86\text{ m} \quad (\text{Chọn chuẩn hóa } L_{\text{basin}} = 43.0\text{ m})$$
  - Bố trí chiều dài bể:
    - Vùng phân phối nước vào và hố thu bùn đầu bể: $L_{\text{inlet}} = 6.5\text{ m}$.
    - Vùng lắp đặt khối ống lắng cao trình: $L_{\text{tube}} = 30.0\text{ m}$.
    - Vùng thu nước trong và máng xả cuối bể: $L_{\text{outlet}} = 6.5\text{ m}$.
    - Tổng cộng: $L_{\text{basin}} = 6.5 + 30.0 + 6.5 = 43.0\text{ m}$.
- **Cấu hình Chiều sâu Bể Lắng Cao trình:**
  - Chiều sâu hố thu và khoang chứa bùn đáy: $h_1 = 1.0\text{ m}$.
  - Chiều sâu vùng dẫn và phân phối nước dưới khối ống: $h_2 = 1.5\text{ m}$.
  - Chiều cao thẳng đứng khối mô-đun ống lắng: $H_{\text{module}} = 0.75\text{ m}$.
  - Chiều sâu lớp nước trong trên mặt khối ống: $h_3 = 0.5\text{ m}$.
  - Chiều cao an toàn bảo vệ (Freeboard): $h_{\text{FB}} = 0.5\text{ m}$.
  - **Tổng chiều sâu thành bể:**
    $$H_{\text{basin}} = 1.0 + 1.5 + 0.75 + 0.5 + 0.5 = 4.25\text{ m}$$

##### 7.3.4. Bước 3: Tính toán Vận tốc Dòng chảy Dọc Trục Ống Lắng
- **Chiều dài thực tế dọc theo ống lắng nghiêng ($L_{\text{tube,axial}}$):**
  $$L_{\text{tube,axial}} = \frac{H_{\text{module}}}{\sin(60^\circ)} = \frac{0.75\text{ m}}{\sin(60^\circ)} = \frac{0.75}{0.866025} \approx 0.866\text{ m}$$
- **Vận tốc dâng thẳng đứng của dòng nước tiếp cận ($v_v$):**
  $$v_v = \frac{Q}{A_{\text{tube,plan}}} = \frac{0.5\text{ m}^3/\text{s}}{360.0\text{ m}^2} = 0.001389\text{ m/s} = 0.08333\text{ m/min}$$
- **Vận tốc thực tế của dòng nước di chuyển dọc theo trục ống nghiêng $60^\circ$ ($v_{\text{tube}}$):**
  $$v_{\text{tube}} = \frac{v_v}{\sin(60^\circ)} = \frac{0.08333\text{ m/min}}{0.866025} \approx 0.09622\text{ m/min} = 0.001604\text{ m/s} = 1.604\text{ mm/s}$$
- **Kiểm tra tiêu chuẩn vận tốc:**
  $$v_{\text{tube}} = 0.0962\text{ m/min} \le v_{\text{max}} = 0.15\text{ m/min} \quad \implies \text{ĐẠT CHUẨN (Thấp hơn giới hạn 36\%)}$$

##### 7.3.5. Bước 4: Kiểm tra Thời gian Lưu Thủy lực Trong Ống Lắng
- **Thời gian lưu trong khoang ống ($t_{d,\text{tube}}$):**
  $$t_{d,\text{tube}} = \frac{L_{\text{tube,axial}}}{v_{\text{tube}}} = \frac{0.866\text{ m}}{0.09622\text{ m/min}} \approx 9.00\text{ phút}$$
- **So sánh tiêu chuẩn (Slide 38):**
  $$6.0\text{ phút} \le t_{d,\text{tube}} = 9.00\text{ phút} \le 10.0\text{ phút} \quad \implies \text{ĐẠT CHUẨN HOÀN HẢO}$$

##### 7.3.6. Bước 5: Kiểm tra Thủy động Lực học Dòng chảy Tầng ($Re$ và $Fr$)
- **Bán kính thủy lực của ống lục giác đường kính $d = 50\text{ mm}$:**
  $$R = \frac{d}{4} = \frac{0.050\text{ m}}{4} = 0.0125\text{ m}$$
- **Kiểm tra Số Reynolds Trong Ống ($Re_{\text{tube}}$):**
  $$Re_{\text{tube}} = \frac{v_{\text{tube}} \cdot R}{\nu} = \frac{0.0016037\text{ m/s} \times 0.0125\text{ m}}{1.003 \times 10^{-6}\text{ m}^2/\text{s}} = \frac{2.0046 \times 10^{-5}}{1.003 \times 10^{-6}} \approx 19.99$$
  - Tiêu chuẩn: $Re_{\text{tube}} < 50$.
  - Đánh giá: $Re = 19.99 < 50 \implies \text{ĐẠT TRẠNG THÁI DÒNG CHẢY TẦNG TUYỆT ĐỐI}$. Các bông cặn lắng rơi trong môi trường tĩnh lặng lý tưởng không bị nhiễu động xáo trộn.
- **Kiểm tra Số Froude Trong Ống ($Fr_{\text{tube}}$):**
  $$Fr_{\text{tube}} = \frac{v_{\text{tube}}^2}{g \cdot R} = \frac{(0.0016037)^2}{9.81 \times 0.0125} = \frac{2.5718 \times 10^{-6}}{0.122625} \approx 2.10 \times 10^{-5}$$
  - Tiêu chuẩn: $Fr_{\text{tube}} > 10^{-5}$.
  - Đánh giá: $Fr = 2.10 \times 10^{-5} > 10^{-5} \implies \text{ĐẠT CHUẨN ỔN ĐỊNH THỦY ĐỘNG}$. Dòng chảy hoàn toàn miễn nhiễm với các hiện tượng phân tầng mật độ.

##### 7.3.7. Bước 6: Tổng Hợp Đặc Tính Kỹ Thuật Công Trình

| Hạng mục / Thông số | Giá trị Tính toán | Đơn vị | Quy chuẩn / Đánh giá |
|---|---|---|---|
| **Số lượng đơn nguyên bể** | $2$ | Bể | Song song vận hành |
| **Chiều rộng mỗi bể ($W$)** | $6.0$ | $\text{m}$ | Tiêu chuẩn cào xích |
| **Chiều dài vùng ống lắng ($L_{\text{tube}}$)** | $30.0$ | $\text{m}$ | Lắp đặt tấm PVC $60^\circ$ |
| **Chiều dài toàn bể ($L_{\text{basin}}$)** | $43.0$ | $\text{m}$ | Gồm vùng vào và vùng ra |
| **Tổng chiều sâu bể ($H_{\text{basin}}$)** | $4.25$ | $\text{m}$ | Thành bể bê tông cốt thép |
| **Chiều cao mô-đun ống ($H_{\text{module}}$)** | $0.75$ | $\text{m}$ | Nghiêng $60^\circ$ |
| **Đường kính trong ống lắng ($d$)** | $50$ | $\text{mm}$ | Hình lục giác tổ ong |
| **Tải trọng bề mặt khối ống ($\text{SLR}$)** | $120.0$ | $\text{m}^3/(\text{m}^2\cdot\text{d})$ | Dải chuẩn $60 - 180$ |
| **Vận tốc nước dọc ống ($v_{\text{tube}}$)** | $0.0962$ | $\text{m/min}$ | $\le 0.15\text{ m/min}$ (ĐẠT) |
| **Thời gian lưu trong ống ($t_d$)** | $9.00$ | Phút | Dải chuẩn $6 - 10\text{ min}$ (ĐẠT) |
| **Số Reynolds ($Re_{\text{tube}}$)** | $19.99$ | - | $< 50$ (Dòng tầng sâu) |
| **Số Froude ($Fr_{\text{tube}}$)** | $2.10 \times 10^{-5}$ | - | $> 10^{-5}$ (Ổn định cao) |
| **Thiết bị thu gom bùn đáy** | Chain-and-flight scraper | - | Cào xích liên tục |
| **Thiết bị súc rửa phụ trợ** | Air Scour Grid | - | Sục khí định kỳ đáy ống |
