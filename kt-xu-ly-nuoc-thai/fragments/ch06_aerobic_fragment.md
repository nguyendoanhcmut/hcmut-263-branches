## Chương 06: Quá trình Xử lý Sinh học Hiếu khí (Aerobic Biological Processes)

### 1. Cơ sở Lý thuyết & Động học Quá trình Bùn Hoạt tính (Activated Sludge Theory & Kinetics)

#### 1.1 Cơ chế phân hủy sinh học hiếu khí và cân bằng khối lượng (Aerobic Biodegradation Mechanisms & Mass Balances)

##### 1.1.1 Quy trình và sơ đồ dòng bùn hoạt tính truyền thống (Conventional Activated Sludge - CAS)
- **Định nghĩa hệ thống:** Bùn hoạt tính truyền thống (CAS) là quá trình xử lý sinh học nước thải bằng sinh trưởng lơ lửng, trong đó sinh khối vi sinh vật (bông bùn hoạt tính) được giữ lơ lửng trong nước thải bằng sục khí nhân tạo và khuấy trộn liên tục, phân hủy các hợp chất hữu cơ hòa tan và dạng keo thành các sản phẩm khoáng hóa trơ ($CO_2, H_2O, NH_4^+$).
- **Sơ đồ chuỗi dây chuyền công nghệ:** Nước thải thô $\rightarrow$ Song chắn rác $\rightarrow$ Bể lắng cát $\rightarrow$ Bể lắng đợt 1 (loại bỏ $50-70\%$ TSS, $25-40\%$ BOD) $\rightarrow$ Bể hiếu khí (Aerotank) $\rightarrow$ Bể lắng đợt 2 (Secondary Clarifier) $\rightarrow$ Khử trùng $\rightarrow$ Nguồn tiếp nhận.
- **Dòng tuần hoàn bùn (RAS - Return Activated Sludge):** Hỗn hợp bùn sau lắng ở đáy bể lắng 2 có nồng độ đậm đặc ($X_r = 6,000 - 12,000\ mg/L$) được bơm hoàn lưu liên tục về đầu bể aerotank với lưu lượng $Q_r$ nhằm duy trì mật độ sinh khối cao trong bể ($X = 1,500 - 4,000\ mg/L$).
- **Dòng xả bùn dư (WAS - Waste Activated Sludge):** Sinh khối vi sinh vật sinh sôi liên tục do đồng hóa cơ chất được xả bỏ định kỳ hoặc liên tục với lưu lượng $Q_w$ từ đáy bể lắng 2 hoặc từ hỗn hợp bùn trong bể hiếu khí để duy trì thời gian lưu bùn (tuổi bùn $\theta_c$) ở giá trị thiết kế ổn định.
- **Dòng nước trong sau lắng (Effluent):** Nước trong tràn qua máng răng cưa bể lắng đợt 2 với lưu lượng $Q_e = Q - Q_w$, nồng độ cơ chất hòa tan dư $S$ và nồng độ cặn lơ lửng trôi theo rất nhỏ ($X_e \le 10 - 20\ mg/L$).

###### 1.1.1.1 Thiết lập phương trình cân bằng vật chất cơ chất (Substrate Mass Balance)
- **Ranh giới thể tích kiểm soát (Control Volume):** Bao quanh toàn bộ bể phản ứng hiếu khí thể tích $V$ và bể lắng đợt 2.
- **Phương trình vi phân tổng quát:**
  $$\text{Tích lũy} = \text{Dòng vào} - \text{Dòng ra} - \text{Tiêu thụ sinh học}$$
  $$V \frac{dS}{dt} = Q S_0 - \left[ (Q - Q_w) S + Q_w S \right] - r_{su} V = Q S_0 - Q S - r_{su} V$$
- **Điều kiện trạng thái dừng (Steady-State, $dS/dt = 0$):**
  $$Q (S_0 - S) = r_{su} V$$
  $$\frac{S_0 - S}{\theta} = r_{su} = \frac{k X S}{K_s + S}$$
- **Định nghĩa các biến số và đơn vị:**
  - $Q$: Lưu lượng nước thải đầu vào hệ thống ($m^3/d$ hoặc $m^3/s$).
  - $S_0$: Nồng độ cơ chất hữu cơ hòa tan trong nước thải đầu vào bể hiếu khí ($g\ BOD_5/m^3$, $g\ COD/m^3$ hoặc $mg/L$).
  - $S$: Nồng độ cơ chất hữu cơ hòa tan trong bể hiếu khí và dòng ra ($g/m^3$ hoặc $mg/L$, do giả thiết khuấy trộn hoàn toàn nên $S_{tank} = S_{effluent} = S$).
  - $V$: Thể tích hữu ích của bể phản ứng hiếu khí ($m^3$).
  - $\theta = V/Q$: Thời gian lưu thủy lực danh định của bể ($d$ hoặc $h$).
  - $r_{su}$: Tốc độ sử dụng cơ chất thể tích ($g\ BOD_5/(m^3\cdot d)$).
  - $k$: Tốc độ sử dụng cơ chất cực đại trên một đơn vị sinh khối ($g\ BOD_5/(g\ VSS\cdot d)$).
  - $K_s$: Hằng số nửa tốc độ, nồng độ cơ chất tại đó tốc độ phản ứng đạt $k/2$ ($g\ BOD_5/m^3$ hoặc $mg/L$).
  - $X$: Nồng độ sinh khối vi sinh vật bay hơi trong bể hiếu khí (MLVSS, $g\ VSS/m^3$ hoặc $mg/L$).

###### 1.1.1.2 Thiết lập phương trình cân bằng sinh khối tế bào (Biomass Mass Balance)
- **Phương trình vi phân tổng quát:**
  $$\text{Tích lũy sinh khối} = \text{Sinh khối vào} - \text{Sinh khối ra} + \text{Sinh khối tăng trưởng ròng}$$
  $$V \frac{dX}{dt} = Q X_0 - \left[ (Q - Q_w) X_e + Q_w X_r \right] + r_g V$$
- **Giả thiết công nghệ:** Nước thải đầu vào sau lắng đợt 1 có nồng độ vi sinh vật hoạt tính không đáng kể ($X_0 \approx 0$), hệ thống vận hành ở trạng thái ổn định dừng ($dX/dt = 0$):
  $$(Q - Q_w) X_e + Q_w X_r = r_g V$$
- **Tốc độ tăng trưởng sinh khối ròng ($r_g$):** Là hiệu số giữa tốc độ tăng trưởng sinh khối mới ($r'_g$) và tốc độ phân hủy nội sinh tế bào ($r_d$):
  $$r_g = r'_g - r_d = Y r_{su} - k_d X = \left( \frac{Y k S}{K_s + S} - k_d \right) X = (\mu - k_d) X$$
- **Định nghĩa thời gian lưu bùn (Solids Retention Time - SRT, $\theta_c$ hay MCRT):**
  $$\theta_c = \frac{\text{Tổng lượng sinh khối trong hệ thống}}{\text{Tổng lượng sinh khối thất thoát và xả thải mỗi ngày}} = \frac{V X}{(Q - Q_w) X_e + Q_w X_r}$$
- **Mối quan hệ cơ bản giữa tuổi bùn và tốc độ tăng trưởng ròng:**
  $$\frac{1}{\theta_c} = \frac{r_g}{X} = \mu_{net} = \mu - k_d = Y \frac{r_{su}}{X} - k_d = Y U - k_d$$
  - Trong đó $U = \frac{r_{su}}{X} = \frac{Q(S_0 - S)}{V X}$ là tốc độ sử dụng cơ chất riêng (Specific Substrate Utilization Rate, $d^{-1}$).

##### 1.1.2 Động học tăng trưởng sinh khối Monod và phân hủy nội sinh (Monod Growth & Endogenous Decay Kinetics)

###### 1.1.2.1 Tốc độ tăng trưởng riêng biểu kiến và thời gian lưu bùn ($\theta_c$ / SRT)
- **Hệ số sản lượng quan sát thực tế ($Y_{obs}$):** Do quá trình phân hủy nội sinh (hô hấp nội bào tự oxy hóa thành $CO_2, H_2O, NH_3$), sản lượng sinh khối thực tế thu được trên mỗi đơn vị cơ chất tiêu thụ nhỏ hơn nhiều so với hệ số sản lượng tổng hợp lý thuyết ($Y$):
  $$Y_{obs} = \frac{P_{X,bio}}{Q (S_0 - S)} = \frac{Y}{1 + k_d \theta_c}$$
- **Ý nghĩa kỹ thuật của tuổi bùn $\theta_c$:** $\theta_c$ là biến điều khiển cốt lõi nhất của quá trình bùn hoạt tính. Khi tăng $\theta_c$, $Y_{obs}$ giảm mạnh, lượng bùn dư phát sinh giảm, mức độ khoáng hóa của bùn tăng cao, tạo điều kiện giữ lại các vi sinh vật phát triển chậm như vi khuẩn nitrat hóa.

###### 1.1.2.2 Phương trình nồng độ cơ chất hòa tan đầu ra ($S$)
- **Thiết lập công thức giải tích từ mô hình Monod:**
  $$\frac{1}{\theta_c} = \frac{\mu_m S}{K_s + S} - k_d \implies \frac{1}{\theta_c} + k_d = \frac{\mu_m S}{K_s + S}$$
  $$(K_s + S) (1 + k_d \theta_c) = \mu_m \theta_c S \implies K_s (1 + k_d \theta_c) = S \left[ \theta_c (\mu_m - k_d) - 1 \right]$$
  $$S = \frac{K_s (1 + k_d \theta_c)}{\theta_c (\mu_m - k_d) - 1}$$
- **Nhận xét quan trọng:** Nồng độ cơ chất hòa tan đầu ra $S$ của bể khuấy trộn hoàn toàn (CMAS) hoàn toàn độc lập với nồng độ cơ chất đầu vào $S_0$ và lưu lượng $Q$, mà chỉ phụ thuộc duy nhất vào thời gian lưu bùn $\theta_c$ và các hằng số sinh học vi sinh ($\mu_m, K_s, k_d$).
- **Thời gian lưu bùn tối thiểu giới hạn (Minimum SRT, $\theta_{c,\min}^{substrate}$):** Là giá trị $\theta_c$ tại đó tốc độ sinh trưởng vừa vặn bù đắp tốc độ rửa trôi tế bào khi nồng độ cơ chất đạt tối đa ($S \approx S_0 \gg K_s$):
  $$\frac{1}{\theta_{c,\min}} = \mu_m - k_d \implies \theta_{c,\min} = \frac{1}{\mu_m - k_d}$$
  - Nếu vận hành hệ thống ở $\theta_c \le \theta_{c,\min}$, sinh khối vi sinh vật sẽ bị rửa trôi hoàn toàn khỏi hệ thống (Washout).

###### 1.1.2.3 Ảnh hưởng của nhiệt độ lên các hệ số động học (Arrhenius Corrections)
- **Công thức hiệu chỉnh nhiệt độ dạng Arrhenius cải biên:**
  $$k_T = k_{20} \cdot \theta_T^{(T - 20)}$$
- **Giá trị thực nghiệm các hệ số nhiệt độ $\theta_T$:**
  - Hệ số tốc độ tăng trưởng cực đại vi khuẩn dị dưỡng ($\mu_m$): $\theta_T = 1.070$ (giảm mạnh khi trời lạnh: $\mu_m(12^\circ C) = 6.0 \cdot 1.07^{-8} = 3.49\ d^{-1}$).
  - Hệ số phân hủy nội sinh vi khuẩn dị dưỡng ($k_d$ hoặc $b$): $\theta_T = 1.040$ ($k_d(12^\circ C) = 0.12 \cdot 1.04^{-8} = 0.0877\ d^{-1}$).
  - Hằng số nửa bão hòa cơ chất ($K_s$): ít nhạy cảm với nhiệt độ, thường giả định $\theta_T = 1.00$ hoặc $1.02$.
  - Hệ số tăng trưởng cực đại vi khuẩn nitrat hóa tự dưỡng ($\mu_{nm}$): cực kỳ nhạy cảm với nhiệt độ, $\theta_T = 1.072$ (tại $12^\circ C$, $\mu_{nm}$ giảm hơn $42\%$).
  - Hệ số phân hủy nội sinh vi khuẩn nitrat hóa ($b_n$): $\theta_T = 1.040$.
  - Hằng số nửa bão hòa amoni ($K_n$): $\theta_T = 1.053$.

#### 1.2 Các chỉ tiêu tải trọng và thông số vận hành cốt lõi (Core Loading & Operational Parameters)

##### 1.2.1 Tỷ số Thức ăn / Vi sinh vật (Food-to-Microorganism Ratio - F/M)

###### 1.2.1.1 Định nghĩa, công thức tính và đơn vị chuẩn
- **Định nghĩa:** Tỷ số F/M biểu thị lượng cơ chất hữu cơ đưa vào bể phản ứng mỗi ngày trên một đơn vị khối lượng sinh khối vi sinh vật hoạt tính đang duy trì trong bể:
  $$\text{F/M} = \frac{Q \cdot S_0}{V \cdot X_{VSS}} \quad \left[ \frac{\text{kg BOD}_5}{\text{kg MLVSS}\cdot\text{d}} \text{ hoặc } \text{d}^{-1} \right]$$
- **Mối quan hệ tương đương với tốc độ sử dụng cơ chất riêng $U$:**
  $$U = \frac{Q (S_0 - S)}{V \cdot X_{VSS}} = \text{F/M} \cdot E_{BOD}$$
  - Trong đó $E_{BOD} = \frac{S_0 - S}{S_0}$ là hiệu suất khử BOD hòa tan của bể ($0.90 - 0.98$). Khi $E_{BOD} \approx 1.0$, $U \approx \text{F/M}$.

###### 1.2.1.2 Ý nghĩa công nghệ và dải giá trị vận hành tối ưu
- **Dải F/M của các quy trình bùn hoạt tính điển hình:**
  - Bùn hoạt tính truyền thống (Conventional CAS): $0.20 - 0.50\text{ kg BOD}_5/(\text{kg MLVSS}\cdot\text{d})$.
  - Bể khuấy trộn hoàn toàn (CMAS): $0.20 - 0.60\text{ kg BOD}_5/(\text{kg MLVSS}\cdot\text{d})$ (điển hình $0.23 - 0.45$).
  - Bùn hoạt tính tải trọng cao (High-rate): $0.50 - 1.50\text{ kg BOD}_5/(\text{kg MLVSS}\cdot\text{d})$.
  - Làm thoáng kéo dài (Extended Aeration) / Mương oxy hóa: $0.05 - 0.15\text{ kg BOD}_5/(\text{kg MLVSS}\cdot\text{d})$.
  - Bể phản ứng gián đoạn (SBR): $0.04 - 0.10\text{ kg BOD}_5/(\text{kg MLVSS}\cdot\text{d})$.
- **Hệ quả vận hành khi F/M ngoài dải chuẩn:**
  - **F/M quá cao ($> 0.6\ d^{-1}$):** Nguồn cơ chất dư thừa, vi sinh ở pha tăng trưởng logarit (tổng hợp tế bào cực mạnh), sản sinh nhiều chất nhờn nhớt polysaccharide nhưng không tạo được mạng lưới kết tụ bông bùn chắc chắn $\rightarrow$ bùn lắng kém, nước đục, hàm lượng BOD và TSS đầu ra vượt quy chuẩn.
  - **F/M quá thấp ($< 0.15\ d^{-1}$ trong CAS):** Vi sinh bị đói cơ chất kinh niên, bước vào pha hô hấp nội sinh sâu $\rightarrow$ kích thích sự bùng phát của vi khuẩn dạng sợi (filamentous bacteria) chuyên ăn mót thức ăn nồng độ thấp (như *Microthrix parvicella*, Eikelboom Type 0041), phá vỡ cấu trúc bông bùn, gây bùn nở nghiêm trọng ($SVI > 150 - 250\ mL/g$), hoặc gây hiện tượng bùn vỡ vụn pin-point floc.

##### 1.2.2 Tải trọng thể tích hữu cơ (Volumetric Organic Loading Rate - OLR)

###### 1.2.2.1 Công thức tính toán và mối quan hệ với HRT
- **Định nghĩa:** Là khối lượng cơ chất hữu cơ nạp vào một đơn vị thể tích bể phản ứng trong một ngày:
  $$\text{OLR} = \frac{Q \cdot S_0}{V \cdot 10^3} = \frac{S_0}{\theta \cdot 10^3} \quad \left[ \frac{\text{kg BOD}_5}{\text{m}^3\cdot\text{d}} \right]$$
- **Dải giá trị công nghệ:**
  - CAS truyền thống: $0.3 - 0.8\ kg\ BOD_5/(m^3\cdot d)$.
  - CMAS: $0.3 - 1.6\ kg\ BOD_5/(m^3\cdot d)$ (trong ví dụ thiết kế đạt $1.184\ kg\ BOD_5/(m^3\cdot d)$).
  - Extended Aeration / Oxidation Ditch: $0.1 - 0.4\ kg\ BOD_5/(m^3\cdot d)$.
  - SBR: $0.1 - 0.3\ kg\ BOD_5/(m^3\cdot d)$.

##### 1.2.3 Thời gian lưu bùn ($\theta_c$ / SRT) và thời gian lưu nước ($\theta$ / HRT)

###### 1.2.3.1 Thời gian lưu tế bào trung bình ($\theta_c$ - Mean Cell Residence Time)
- **Định nghĩa:** Thời gian trung bình mà một vi sinh vật lưu lại trong toàn bộ hệ thống xử lý sinh học (gồm cả bể hiếu khí và bể lắng 2).
- **Dải giá trị thiết kế:**
  - Khử carbon hữu cơ đơn thuần (BOD removal only): $\theta_c = 3 - 5\ \text{ngày}$.
  - Khử BOD kết hợp nitrat hóa hoàn toàn: $\theta_c = 10 - 25\ \text{ngày}$ (ở $12^\circ C$ cần $\theta_c = 21\ \text{ngày}$).
  - Làm thoáng kéo dài: $\theta_c = 20 - 30\ \text{ngày}$.
  - Hệ thống MBR: $\theta_c = 15 - 30\ \text{ngày}$.

###### 1.2.3.2 Thời gian lưu thủy lực ($\theta$ - Hydraulic Retention Time)
- **Định nghĩa và công thức:**
  $$\theta = \text{HRT} = \frac{V}{Q} \cdot 24 \quad [\text{giờ}]$$
- **Dải giá trị chuẩn:**
  - CAS / CMAS khử BOD: $3 - 6\ \text{giờ}$.
  - CMAS có nitrat hóa: $8 - 16\ \text{giờ}$ (điển hình $12 - 14.2\ h$).
  - MBR: $2 - 4\ \text{giờ}$ (tiết kiệm hơn $70\%$ dung tích nhờ MLSS cao).
  - SBR: $15 - 40\ \text{giờ}$ (tính theo chu kỳ làm việc tổng).

##### 1.2.4 Nồng độ bùn hoạt tính trong bể (MLSS & MLVSS)

###### 1.2.4.1 Tỷ lệ MLVSS/MLSS và ý nghĩa phân đoạn hoạt tính
- **MLSS (Mixed Liquor Suspended Solids):** Tổng nồng độ cặn lơ lửng trong hỗn hợp bùn hoạt tính của bể làm thoáng ($g/m^3$ hoặc $mg/L$).
  - Dải giá trị CAS/CMAS: $1,500 - 4,000\ mg/L$ (thông dụng nhất chọn $2,500 - 3,500\ mg/L$).
  - Dải giá trị MBR: $8,000 - 12,000\ mg/L$ (thường chọn $10,000 - 12,000\ mg/L$).
  - Giới hạn MLSS trong CAS bị chi phối bởi khả năng lắng và tải trọng cặn của bể lắng đợt 2 ($SLR \le 4 - 6\ kg/(m^2\cdot h)$).
- **MLVSS (Mixed Liquor Volatile Suspended Solids):** Nồng độ cặn lơ lửng bay hơi, đại diện cho phần hữu cơ gồm vi sinh vật sống, tế bào chết và cặn hữu cơ không phân hủy sinh học.
- **Tỷ số $MLVSS/MLSS$:** Thường dao động trong khoảng $0.75 - 0.85$ ở nước thải sinh hoạt có xử lý sơ bộ tốt. Tỷ số này giảm khi tuổi bùn $\theta_c$ tăng (khoáng hóa sâu) hoặc khi nước thải đầu vào có hàm lượng cặn cát vô cơ ($iTSS$) cao.

##### 1.2.5 Chỉ số thể tích bùn (Sludge Volume Index - SVI)

###### 1.2.5.1 Định nghĩa và quy trình đo nghiệm $SV_{30}$
- **Định nghĩa:** SVI là thể tích tính bằng millilit ($mL$) chiếm bởi 1 gam cặn lơ lửng bùn hoạt tính sau 30 phút lắng tĩnh trong ống đong hình trụ tiêu chuẩn dung tích 1.0 L:
  $$\text{SVI} = \frac{SV_{30}\ (\text{mL/L}) \cdot 1000}{\text{MLSS}\ (\text{mg/L})} \quad \left[ \frac{\text{mL}}{\text{g}} \right]$$
- **Quy trình thực hiện chuẩn:** Lấy mẫu hỗn hợp bùn từ cửa ra bể aerotank, đổ đầy vào ống đong $1,000\ mL$, để lắng tĩnh trong 30 phút, ghi nhận thể tích bùn nén lắng $SV_{30}$ ($mL$). Song song đem mẫu đi sấy và nung để xác định chính xác nồng độ MLSS ($mg/L$).

###### 1.2.5.2 Phân loại đặc tính lắng bùn theo dải giá trị SVI
- **$SVI < 50\ mL/g$:** Bùn quá già, độ nén cực đặc, tốc độ lắng rất nhanh; tuy nhiên bông bùn bị giòn vụn tạo ra vô số hạt cặn nhỏ li ti (pin-point flocs) lơ lửng không lắng được, làm tăng độ đục và TSS của nước sau lắng.
- **$50 \le SVI \le 100\ mL/g$:** Bùn lắng rất tốt, tạo màng nén đều, nước trong vắt, đặc trưng cho hệ thống vận hành cực kỳ ổn định.
- **$100 < SVI \le 150\ mL/g$:** Đặc tính lắng bình thường, thỏa mãn yêu cầu thiết kế của phần lớn các nhà máy xử lý nước thải đô thị (thông số thiết kế chuẩn thường chọn $SVI = 100 - 120\ mL/g$).
- **$SVI > 150\ mL/g$:** Ngưỡng chẩn đoán sự cố bùn nở (Sludge Bulking). Tốc độ lắng chậm chạp, lớp bùn tơi xốp không nén đặc được sau 30 phút, gây phình to thể tích lớp bùn lắng ở bể lắng đợt 2, có nguy cơ trôi tràn bùn ra nguồn tiếp nhận.
- **$SVI > 250 - 300\ mL/g$:** Bùn nở nghiêm trọng do bùng phát vi khuẩn sợi, hệ thống mất hoàn toàn khả năng tách pha rắn-lỏng trong bể lắng trọng lực thông thường.

### 2. Quá trình Nitrat hóa Sinh học (Biological Nitrification)

#### 2.1 Cơ chế sinh học và chuỗi phản ứng sinh hóa 2 bước (Two-Step Biological Oxidation Pathway)
- **Bản chất quá trình:** Nitrat hóa là quá trình oxy hóa sinh học tự dưỡng hai bước liên tiếp, chuyển hóa hợp chất nitơ dạng khử (amoni, $NH_4^+$) thành nitrit ($NO_2^-$) rồi tiếp tục chuyển hóa thành nitrat ($NO_3^-$) dưới điều kiện hiếu khí bắt buộc.

##### 2.1.1 Bước 1: Oxi hóa amoni thành nitrit bởi vi khuẩn AOB (Ammonia-Oxidizing Bacteria)

###### 2.1.1.1 Phương trình hóa học và năng lượng học của Nitrosomonas
- **Phương trình năng lượng catabolism:**
  $$2\text{NH}_4^+ + 3\text{O}_2 \xrightarrow{\text{Nitrosomonas spp.}} 2\text{NO}_2^- + 4\text{H}^+ + 2\text{H}_2\text{O} + \Delta G^\circ (-275\ \text{kJ/mol NH}_4^+)$$
- **Đặc điểm vi sinh vật AOB:**
  - Chi vi sinh vật chủ đạo: *Nitrosomonas*, *Nitrosococcus*, *Nitrosospira*.
  - Là vi khuẩn tự dưỡng hóa năng bắt buộc (obligate chemolithoautotrophs), sử dụng năng lượng giải phóng từ quá trình oxy hóa amoni để cố định carbon vô cơ ($CO_2$ hoặc $HCO_3^-$) tổng hợp chất nguyên sinh tế bào theo chu trình Calvin.
  - Tốc độ sinh trưởng chậm hơn vi khuẩn dị dưỡng từ $10 - 20$ lần, sản lượng sinh khối rất thấp ($Y_n \approx 0.12\ g\ VSS/g\ NH_4^+-N$).

##### 2.1.2 Bước 2: Oxi hóa nitrit thành nitrat bởi vi khuẩn NOB (Nitrite-Oxidizing Bacteria)

###### 2.1.2.1 Phương trình hóa học và năng lượng học của Nitrobacter
- **Phương trình năng lượng catabolism:**
  $$2\text{NO}_2^- + \text{O}_2 \xrightarrow{\text{Nitrobacter spp.}} 2\text{NO}_3^- + \Delta G^\circ (-76\ \text{kJ/mol NO}_2^-)$$
- **Đặc điểm vi sinh vật NOB:**
  - Chi vi sinh vật chủ đạo: *Nitrobacter*, *Nitrospira*, *Nitrococcus* (nghiên cứu phân tử hiện đại chứng minh *Nitrospira* là vi khuẩn khử nitrit chủ đạo trong đa số trạm xử lý nước thải đô thị).
  - Năng lượng thu được từ bước 2 thấp hơn nhiều so với bước 1 ($-76$ so với $-275\ kJ/mol$). Vi khuẩn NOB thường có tốc độ chuyển hóa riêng rất nhanh để lấy đủ năng lượng sinh tồn, do đó ở điều kiện bình thường nitrit hầu như không bị tích tụ trong bể hiếu khí.

##### 2.1.3 Phản ứng tổng hợp toàn phần và tạo bùn sinh học tự dưỡng (Overall Stoichiometry)
- **Phương trình oxy hóa thuần túy (bỏ qua sinh khối mới):**
  $$\text{NH}_4^+ + 2\text{O}_2 \rightarrow \text{NO}_3^- + 2\text{H}^+ + \text{H}_2\text{O}$$
- **Phương trình hóa học lượng tử tổng hợp có tính đến tạo sinh khối vi sinh ($C_5H_7O_2N$):**
  $$\text{NH}_4^+ + 1.83\text{O}_2 + 1.98\text{HCO}_3^- \rightarrow 0.021\text{C}_5\text{H}_7\text{O}_2\text{N} + 0.979\text{NO}_3^- + 1.041\text{H}_2\text{O} + 1.88\text{H}_2\text{CO}_3$$

###### 2.1.3.1 Nhu cầu oxy hóa lý thuyết ($4.57\ mg\ O_2 / mg\ NH_4^+-N$)
- **Phân tích lượng tử:**
  - Bước 1 (Oxy hóa $NH_4^+ \rightarrow NO_2^-$): $1\ mol\ N$ ($14\ g$) cần $1.5\ mol\ O_2$ ($48\ g$) $\implies \frac{48}{14} = 3.43\ g\ O_2/g\ NH_4^+-N$.
  - Bước 2 (Oxy hóa $NO_2^- \rightarrow NO_3^-$): $1\ mol\ N$ ($14\ g$) cần $0.5\ mol\ O_2$ ($16\ g$) $\implies \frac{16}{14} = 1.14\ g\ O_2/g\ NO_2^--N$.
  - **Tổng nhu cầu oxy hóa hóa học lý thuyết:** $3.43 + 1.14 = 4.57\ g\ O_2/g\ NH_4^+-N$.
- Khi tính cả lượng nitơ đồng hóa vào tế bào sinh khối tự dưỡng, lượng oxy thực tế tiêu hao khoảng $4.18 - 4.33\ g\ O_2/g\ N$ nạp vào.

###### 2.1.3.2 Mức tiêu hao độ kiềm ($7.14\ mg\ CaCO_3 / mg\ NH_4^+-N$) và kiểm soát pH
- **Cơ chế axit hóa môi trường:** Quá trình giải phóng $2\ mol\ H^+$ cho mỗi $mol\ NH_4^+$ bị nitrat hóa hoàn toàn:
  $$\text{NH}_4^+ + 2\text{O}_2 \rightarrow \text{NO}_3^- + 2\text{H}^+ + \text{H}_2\text{O}$$
- Ion $H^+$ sinh ra lập tức phản ứng với ion bicacbonat ($HCO_3^-$) trong nước:
  $$\text{H}^+ + \text{HCO}_3^- \leftrightarrow \text{H}_2\text{O} + \text{CO}_2 \uparrow$$
- Cứ $1\ mol\ NH_4^+-N$ ($14\ g$) tiêu thụ $2\ mol\ HCO_3^-$, tương đương $1\ mol\ CaCO_3$ ($100\ g\ CaCO_3$):
  $$\text{Mức tiêu hao độ kiềm lý thuyết} = \frac{100\ g\ CaCO_3}{14\ g\ N} = 7.14\ \frac{\text{g } CaCO_3}{\text{g } NH_4^+-N} = 7.14\ \frac{\text{mg } CaCO_3}{\text{mg } NH_4^+-N}$$
- **Kiểm soát pH và bổ sung hóa chất kiềm:**
  - Khoảng pH tối ưu cho vi khuẩn nitrat hóa: $7.5 - 8.5$. Khi $pH < 7.0$, tốc độ nitrat hóa suy giảm mạnh; khi $pH < 6.5$, quá trình dừng lại hoàn toàn.
  - Để duy trì pH ổn định trong khoảng $7.2 - 7.5$, độ kiềm dư của nước sau xử lý tối thiểu phải đạt $\ge 50 - 80\ mg/L\ CaCO_3$.
  - Nếu độ kiềm tự nhiên của nước thải đầu vào không đủ, bắt buộc phải định lượng châm hóa chất nâng kiềm:
    - Natri bicacbonat ($NaHCO_3$): An toàn nhất, không làm tăng vọt pH cục bộ ($1.68\ kg\ NaHCO_3/kg\ NH_4^+-N$).
    - Vôi tôi ($Ca(OH)_2$): Rẻ tiền, nhưng làm tăng độ cứng và tạo cặn bùn vô cơ.
    - Xút ăn da ($NaOH$): Hiệu quả cao, dễ tự động hóa bằng bơm định lượng theo tín hiệu pH.

#### 2.2 Động học vi khuẩn nitrat hóa và giới hạn môi trường (Nitrification Kinetics & Environmental Limits)

##### 2.2.1 Mô hình động học Monod mở rộng kép (Dual Monod Kinetics for Nitrifiers)

###### 2.2.1.1 Tác động của nồng độ amoni ($K_n$) và nồng độ oxy hòa tan ($K_o$)
- **Phương trình động học tăng trưởng ròng:**
  $$\mu_n = \mu_{nm} \cdot \left( \frac{N}{K_n + N} \right) \cdot \left( \frac{\text{DO}}{K_o + \text{DO}} \right) - b_n$$
- **Định nghĩa các đại lượng và thông số động học chuẩn ở $20^\circ C$:**
  - $\mu_{nm}$: Tốc độ tăng trưởng riêng tối đa của vi khuẩn nitrat hóa ($\approx 0.75\ d^{-1}$, dải $0.40 - 1.0\ d^{-1}$).
  - $N$: Nồng độ amoni hòa tan trong bể và nước sau xử lý ($g\ NH_4^+-N/m^3$ hoặc $mg/L$).
  - $K_n$: Hằng số nửa tốc độ đối với amoni ($0.50\ g/m^3$ ở $20^\circ C$, dải $0.20 - 1.0\ mg/L$).
  - $\text{DO}$: Nồng độ oxy hòa tan duy trì trong bể hiếu khí ($mg/L$).
  - $K_o$: Hằng số nửa tốc độ đối với oxy hòa tan của vi khuẩn nitrat hóa ($0.50\ mg/L$, dải $0.40 - 1.0\ mg/L$). Do $K_o$ của nitrifiers cao hơn vi khuẩn dị dưỡng ($K_{o,H} \approx 0.1 - 0.2\ mg/L$), nên khi DO bể giảm dưới $2.0\ mg/L$, quá trình nitrat hóa bị ức chế nghiêm trọng trước tiên.
  - $b_n$: Hệ số phân hủy nội sinh của vi khuẩn nitrat hóa ($0.05 - 0.08\ d^{-1}$).
  - $Y_n$: Hệ số sản lượng sinh khối nitrat hóa ($0.12 - 0.15\ g\ VSS/g\ NO_x-N$).

###### 2.2.1.2 Tác động của nhiệt độ nước thải lên $\mu_{nm}$ và $b_n$
- Vi khuẩn nitrat hóa vô cùng nhạy cảm với nhiệt độ lạnh:
  $$\mu_{nm}(T) = \mu_{nm}(20^\circ C) \cdot (1.072)^{T - 20}$$
  $$b_n(T) = b_n(20^\circ C) \cdot (1.040)^{T - 20}$$
  $$K_n(T) = K_n(20^\circ C) \cdot (1.053)^{T - 20}$$
- Khi nhiệt độ giảm từ $20^\circ C$ xuống $12^\circ C$:
  $$\mu_{nm}(12^\circ C) = 0.75 \cdot 1.072^{-8} = 0.75 \cdot 0.5735 = 0.430\ d^{-1}$$
  $$b_n(12^\circ C) = 0.08 \cdot 1.040^{-8} = 0.08 \cdot 0.7307 = 0.058\ d^{-1}$$
  $$K_n(12^\circ C) = 0.50 \cdot 1.053^{-8} = 0.50 \cdot 0.6623 = 0.331\ g/m^3$$

##### 2.2.2 Xác định tuổi bùn tối thiểu và tuổi bùn thiết kế ($\theta_{c,\min}$ & $\theta_{c,\text{design}}$)

###### 2.2.2.1 Công thức tính $\theta_{c,\min}$ ngăn ngừa hiện tượng rửa trôi (Washout)
- Để duy trì được quần thể vi khuẩn nitrat hóa trong hệ thống bùn hoạt tính lơ lửng, tốc độ tăng trưởng sinh khối ròng phải lớn hơn hoặc bằng tốc độ bùn bị rửa trôi và xả bỏ:
  $$\frac{1}{\theta_{c,\min}} = \mu_n = \mu_{nm} \cdot \left( \frac{N}{K_n + N} \right) \cdot \left( \frac{\text{DO}}{K_o + \text{DO}} \right) - b_n$$
  $$\theta_{c,\min} = \frac{1}{\mu_n}$$
- Ví dụ ở $12^\circ C$, với mục tiêu nước ra $N = 0.5\ mg/L$ và duy trì $DO = 2.0\ mg/L$:
  $$\mu_n = 0.430 \cdot \left(\frac{0.5}{0.331 + 0.5}\right) \cdot \left(\frac{2.0}{0.5 + 2.0}\right) - 0.058 = 0.430 \cdot 0.6017 \cdot 0.80 - 0.058 = 0.149\ \text{d}^{-1}$$
  $$\theta_{c,\min} = \frac{1}{0.149} = 6.71\ \text{ngày}$$

###### 2.2.2.2 Hệ số an toàn thiết kế ($SF = 2.5 - 3.5$) và lựa chọn $\theta_c$
- Do lưu lượng nước thải, nồng độ amoni đầu vào và nhiệt độ thực tế luôn biến thiên theo giờ và mùa, tuổi bùn thiết kế bắt buộc phải nhân với hệ số an toàn ($SF$):
  $$\theta_{c,\text{design}} = SF \cdot \theta_{c,\min}$$
  - Nước ấm ($T \ge 20^\circ C$): Chọn $SF = 2.0 - 2.5 \implies \theta_c = 8 - 12\ \text{ngày}$.
  - Nước lạnh mùa đông ($T \le 12^\circ C$): Chọn $SF = 2.5 - 3.5 \implies \theta_c = 18 - 25\ \text{ngày}$ (trong bài toán thiết kế chọn $\theta_c = 21.0\ \text{ngày}$).

##### 2.2.3 Khối lượng nitơ được oxi hóa ($NO_x$) và sinh khối vi khuẩn nitrat hóa ($P_{X,\text{bio,nit}}$)

###### 2.2.3.1 Cân bằng nitơ tổng và lượng nitơ đồng hóa vào tế bào dị dưỡng
- **Phương trình cân bằng vật chất nitơ:**
  $$\text{Tổng TKN vào} = \text{Amoni dư đầu ra} + \text{Nitơ đồng hóa vào bùn thải} + \text{Nitơ bị oxy hóa thành } NO_x$$
- Khối lượng tế bào vi khuẩn dị dưỡng và nitrit hóa chứa trung bình $12\%\ N$ theo khối lượng VSS ($0.12\ g\ N/g\ VSS$):
  $$N_{assimilated} = 0.12 \cdot P_{X,VSS} \cdot \frac{1000}{Q} \quad [g\ N/m^3]$$
- Nồng độ nitơ chuyển hóa thành nitrat ($NO_x$):
  $$NO_x = TKN_0 - N_e - \frac{0.12 \cdot P_{X,VSS} \cdot 1000}{Q} \quad [g\ N/m^3]$$
  $$M_{NOx} = Q \cdot NO_x \cdot 10^{-3} \quad [kg\ N/d]$$

###### 2.2.3.2 Phương trình sinh khối nitrat hóa tự dưỡng
- Khối lượng bùn sinh học vi khuẩn nitrat hóa sản sinh hàng ngày:
  $$P_{X,\text{bio,nit}} = \frac{Q \cdot Y_n \cdot NO_x \cdot 10^{-3}}{1 + b_n \theta_c} \quad [kg\ VSS/d]$$
  - Với $Y_n = 0.12 - 0.15\ g\ VSS/g\ N$, lượng bùn này rất nhỏ ($1 - 3\%$ tổng sinh khối), nhưng đóng vai trò quyết định cấu trúc và hoạt tính enzyme của hệ thống.

### 3. Phương trình Thiết kế Thể tích Bể và Quản lý Bùn Hoạt tính (Basin Sizing & Sludge Management Equations)

#### 3.1 Thiết kế thể tích bể hiếu khí (Aeration Basin Volume Sizing)

##### 3.1.1 Phương trình tính toán thể tích theo cân bằng sinh khối và tải trọng

###### 3.1.1.1 Công thức giải tích $V = \frac{\theta_c Q Y (S_0 - S)}{X (1 + k_d \theta_c)}$
- **Dẫn xuất toán học:** Từ phương trình sản lượng sinh khối dị dưỡng hoạt tính $P_{X,bio} = \frac{Q Y (S_0 - S)}{1 + k_d \theta_c}$ và định nghĩa khối lượng sinh khối trong bể $M_X = V \cdot X_{VSS} = P_{X,bio} \cdot \theta_c$:
  $$V \cdot X_{VSS} = \frac{\theta_c \cdot Q \cdot Y \cdot (S_0 - S)}{1 + k_d \theta_c}$$
  $$V = \frac{\theta_c \cdot Q \cdot Y \cdot (S_0 - S)}{X_{VSS} \cdot (1 + k_d \theta_c)}$$
- **Đơn vị và biến số:**
  - $V$: Thể tích hữu ích của bể làm thoáng ($m^3$).
  - $\theta_c$: Thời gian lưu bùn thiết kế ($d$).
  - $Q$: Lưu lượng nước thải đầu vào thiết kế ($m^3/d$).
  - $Y$: Hệ số sản lượng sinh khối lý thuyết ($g\ VSS/g\ BOD_5$ hoặc $g\ VSS/g\ COD$, điển hình $0.40 - 0.60$).
  - $S_0, S$: Nồng độ cơ chất đầu vào và đầu ra hòa tan ($g/m^3$).
  - $X_{VSS}$: Nồng độ sinh khối bay hơi trong bể ($g\ MLVSS/m^3$ hoặc $kg\ MLVSS/m^3$).
  - $k_d$: Hệ số phân hủy nội sinh hiệu chỉnh theo nhiệt độ ($d^{-1}$).

###### 3.1.1.2 Công thức tổng quát qua tổng sinh khối $V = \frac{P_{X,TSS} \cdot \theta_c}{X_{TSS}}$
- Khi tính toán đầy đủ các thành phần cặn thực tế gồm sinh khối hoạt tính ($P_{X,bio}$), mảnh vụn tế bào nội sinh trơ ($P_{X,d}$), cặn lơ lửng bay hơi không phân hủy sinh học của nước thải ($P_{X,nbVSS}$), và cặn trơ vô cơ ($P_{X,iTSS}$):
  $$V = \frac{P_{X,TSS} \cdot \theta_c}{X_{TSS}} = \frac{P_{X,VSS} \cdot \theta_c}{X_{VSS}}$$
  - $P_{X,TSS}$: Tổng sản lượng cặn lơ lửng khô phát sinh mỗi ngày ($kg\ TSS/d$).
  - $X_{TSS}$: Nồng độ MLSS thiết kế duy trì trong bể ($kg\ TSS/m^3$ hoặc $g/m^3$).

##### 3.1.2 Xác định diện tích mặt bằng và chiều sâu làm việc của bể

###### 3.1.2.1 Lựa chọn chiều sâu nước hiệu dụng ($H = 3.5 - 6.0\ m$) và chiều cao bảo vệ
- **Chiều sâu chất lỏng làm việc ($H$):**
  - Bể sục khí khuếch tán bọt mịn: Thông thường chọn $H = 4.0 - 5.5\ m$ (tối ưu hóa giữa thời gian bọt khí tiếp xúc và cột áp làm việc của máy thổi khí).
  - Bể làm thoáng bằng sục khí cơ học bề mặt: Thông thường chọn $H = 3.0 - 4.5\ m$ (chiều sâu lớn hơn đòi hỏi ống hút ngầm hoặc cánh khuấy chìm phụ trợ để tránh lắng cặn đáy).
  - Bể SBR: Thường thiết kế sâu $H = 5.0 - 7.0\ m$ để tối ưu dung tích và diện tích chân đế.
- **Chiều cao bảo vệ (Freeboard, $h_b$):** Thường dự phòng $0.5 - 1.0\ m$ bên trên mực nước dâng cao nhất để ngăn ngừa bọt sóng tràn lan khi thời tiết gió mạnh hoặc khi xuất hiện bọt sinh học.

###### 3.1.2.2 Tỷ lệ kích thước mặt bằng ($L/W$) và cấu trúc phân ngăn
- **Bể khuấy trộn hoàn toàn (CMAS):** Mặt bằng thường là hình vuông ($L/W = 1:1$) hoặc hình chữ nhật gần vuông ($L/W \le 2:1$) với hệ thống sục khí hoặc máy khuấy phân bố đều khắp bề mặt để duy trì tính đồng nhất tối đa.
- **Bể dòng chảy nút (Plug-flow CAS):** Mặt bằng hẹp dài với tỷ lệ $L/W \ge 5:1 - 10:1$, thường uốn khúc dạng zic-zac nhiều luồng (meander/channels) để tạo dòng chảy thẳng hướng, ngăn ngừa dòng ngắn (short-circuiting).
- **Phân chia số lượng đơn nguyên:** Luôn thiết kế tối thiểu $\ge 2$ bể (hoặc 2 ngăn độc lập) song song để có thể bảo dưỡng, sửa chữa thiết bị sục khí mà không phải dừng vận hành toàn nhà máy.

#### 3.2 Tính toán sản lượng bùn sinh học và tổng cặn dư (Sludge Production Formulations)

##### 3.2.1 Sản lượng sinh khối hoạt tính dị dưỡng ($P_{X,bio}$)
- Công thức lượng sinh khối tế bào vi sinh vật sống tổng hợp:
  $$P_{X,bio} = \frac{Q \cdot Y \cdot (S_0 - S)}{1 + k_d \theta_c} \cdot 10^{-3} \quad \left[ \frac{\text{kg VSS}}{\text{d}} \right]$$

##### 3.2.2 Mảnh vỡ tế bào nội sinh ($P_{X,d}$)
- Trong quá trình vi sinh tự phân hủy nội sinh, có một phân đoạn cặn hữu cơ trơ không thể tiếp tục bị oxy hóa sinh học (thành tế bào peptidoglycan, màng lipid phức tạp), ký hiệu là $f_d$ ($f_d \approx 0.10 - 0.15$):
  $$P_{X,d} = f_d \cdot k_d \cdot \theta_c \cdot P_{X,bio} = \frac{f_d \cdot k_d \cdot \theta_c \cdot Q \cdot Y \cdot (S_0 - S)}{1 + k_d \theta_c} \cdot 10^{-3} \quad \left[ \frac{\text{kg VSS}}{\text{d}} \right]$$

##### 3.2.3 Cặn lơ lửng bay hơi không phân hủy sinh học từ nước đầu vào ($P_{X,nbVSS}$)
- Lượng cặn hữu cơ không phân hủy sinh học có sẵn trong nước thải đầu vào bị giữ lại hoàn toàn trong bông bùn:
  $$P_{X,nbVSS} = Q \cdot nbVSS_{inf} \cdot 10^{-3} \quad \left[ \frac{\text{kg VSS}}{\text{d}} \right]$$
- **Tổng sản lượng cặn lơ lửng bay hơi phát sinh mỗi ngày ($P_{X,VSS}$):**
  $$P_{X,VSS} = P_{X,bio} + P_{X,d} + P_{X,nbVSS} + P_{X,bio,nit} \quad \left[ \frac{\text{kg VSS}}{\text{d}} \right]$$

##### 3.2.4 Cặn trơ vô cơ từ nước thải đầu vào ($P_{X,iTSS}$)
- Hàm lượng cặn vô cơ (tro, khoáng sét, cát mịn) tích tụ trong bùn hoạt tính:
  $$P_{X,iTSS} = Q \cdot iTSS_{inf} \cdot 10^{-3} \quad \left[ \frac{\text{kg TSS}}{\text{d}} \right]$$
- **Tổng sản lượng cặn lơ lửng khô phát sinh mỗi ngày ($P_{X,TSS}$):**
  $$P_{X,TSS} = \frac{P_{X,bio}}{0.85} + P_{X,d} + P_{X,nbVSS} + P_{X,iTSS} \quad \left[ \frac{\text{kg TSS}}{\text{d}} \right]$$
  - Trong đó $0.85$ biểu thị tỷ lệ $VSS/TSS$ của tế bào vi sinh vật sống mới sinh ra.
  - Tỷ lệ hữu cơ tổng thể của bùn trong hệ thống: $f_{VSS} = P_{X,VSS} / P_{X,TSS}$ ($75 - 85\%$).

#### 3.3 Hệ thống bùn tuần hoàn (RAS) và xả bùn dư (WAS)

##### 3.3.1 Cân bằng dòng xả bùn dư ($Q_w$) và điểm xả bùn

###### 3.3.1.1 Phương trình xả bùn từ đường tuần hoàn bùn đáy bể lắng: $Q_w = \frac{V X / \theta_c - Q_e X_e}{X_r}$
- **Cơ sở thiết lập:** Từ định nghĩa tuổi bùn $\theta_c$:
  $$\theta_c = \frac{V X}{Q_w X_r + (Q - Q_w) X_e} \approx \frac{V X}{Q_w X_r + Q_e X_e}$$
  $$\implies Q_w X_r + Q_e X_e = \frac{V X}{\theta_c}$$
  $$Q_w = \frac{\frac{V X}{\theta_c} - Q_e X_e}{X_r}$$
- **Định nghĩa các biến số và đơn vị:**
  - $Q_w$: Lưu lượng xả bùn dư từ đáy bể lắng ($m^3/d$).
  - $V$: Thể tích bể hiếu khí ($m^3$).
  - $X$: Nồng độ bùn hoạt tính trong bể aerotank (MLSS, $mg/L$ hoặc $g/m^3$).
  - $\theta_c$: Tuổi bùn mục tiêu ($d$).
  - $Q_e$: Lưu lượng nước trong sau lắng xả ra ngoài ($m^3/d$, $Q_e = Q - Q_w \approx Q$).
  - $X_e$: Nồng độ chất rắn lơ lửng trôi theo nước trong ($mg/L$, thông thường $X_e = 10 - 15\ mg/L$).
  - $X_r$: Nồng độ bùn đặc dưới đáy bể lắng đợt 2 ($mg/L$, $X_r = 6,000 - 10,000\ mg/L$).

###### 3.3.1.2 Phương trình xả bùn trực tiếp từ bể hiếu khí: $Q_w = \frac{V}{\theta_c}$ (bỏ qua $X_e$)
- **Xả bùn từ hỗn hợp bùn nước trong bể Aerotank:**
  - Do xả trực tiếp hỗn hợp bùn có nồng độ đúng bằng $X$, nếu giả định $X_e \approx 0$:
    $$Q_w = \frac{V \cdot X / \theta_c}{X} = \frac{V}{\theta_c} \quad \left[ \frac{\text{m}^3}{\text{d}} \right]$$
  - **Ưu điểm vượt trội:** Nồng độ bùn trong bể $X$ biến động rất chậm, việc kiểm soát thể tích xả bùn hàng ngày cực kỳ đơn giản và chính xác tuyệt đối theo tuổi bùn mong muốn, không phụ thuộc vào dao động nồng độ bùn đáy lắng $X_r$.
  - **Nhược điểm:** Nồng độ bùn xả loãng hơn so với xả đáy ($3,000\ mg/L$ so với $8,000\ mg/L$), làm tăng thể tích công trình xử lý bùn (bể nén bùn trọng lực phải lớn hơn).

##### 3.3.2 Tỷ số tuần hoàn bùn ($R = Q_r/Q$)

###### 3.3.2.1 Thiết lập công thức cân bằng nút $R = \frac{X}{X_r - X}$
- **Cân bằng sinh khối tại nút hòa trộn đầu vào:** Giả sử lưu lượng nước thải $Q$ với hàm lượng cặn $X_0 \approx 0$ hòa trộn cùng dòng bùn tuần hoàn $Q_r$ có nồng độ $X_r$ tạo thành dòng hỗn hợp $(Q + Q_r)$ có nồng độ $X$ nạp vào bể:
  $$(Q + Q_r) X = Q \cdot X_0 + Q_r X_r = Q_r X_r$$
  $$Q X + Q_r X = Q_r X_r \implies Q X = Q_r (X_r - X)$$
  $$R = \frac{Q_r}{Q} = \frac{X}{X_r - X}$$
- **Dải tỷ số tuần hoàn thông thường:**
  - CAS / CMAS: $R = 0.25 - 1.0$ ($25\% - 100\%$).
  - Nitrat hóa hoàn toàn: $R = 0.50 - 1.50$ ($50\% - 150\%$).
  - Bể MBR: $R = 4.0 - 6.0$ ($400\% - 600\%$).

###### 3.3.2.2 Ước tính nồng độ bùn tuần hoàn $X_r$ theo chỉ số SVI ($X_r \approx \frac{10^6}{SVI} \cdot r$)
- Sau 30 phút lắng tĩnh trong ống đong, thể tích bùn nén đạt nồng độ giới hạn:
  $$X_{r,\max} = \frac{10^6}{\text{SVI}} \quad \left[ \frac{\text{mg}}{\text{L}} \right]$$
- Do bể lắng hoạt động động lực liên tục và có gạt bùn đáy, nồng độ bùn tuần hoàn thực tế chỉ đạt $70 - 90\%$ giá trị nén lý thuyết:
  $$X_r = r_c \cdot \frac{10^6}{\text{SVI}} \quad (r_c = 0.70 - 0.90)$$
  - Ví dụ khi $SVI = 100\ mL/g$ và $r_c = 0.80$:
    $$X_r = 0.80 \cdot \frac{10^6}{100} = 8,000\ mg/L$$
    $$\text{Với } X = 3,000\ mg/L \implies R = \frac{3,000}{8,000 - 3,000} = 0.60\ (60\%)$$

### 4. Tính toán Nhu cầu Oxy và Thiết kế Hệ thống Cấp khí (Oxygen Requirements & Aeration Systems)

#### 4.1 Nhu cầu oxy thực tế của hệ thống (Actual Oxygen Requirement - AOR / $R_O$)

##### 4.1.1 Nhu cầu oxy cho quá trình loại bỏ BOD carbon (Carbonaceous Oxygen Demand)

###### 4.1.1.1 Phương trình $R_{O,\text{carbon}} = Q(S_0 - S) - 1.42 P_{X,\text{bio}}$
- **Cơ chế lý thuyết:** Tổng lượng oxy cần thiết để oxy hóa hoàn toàn lượng hợp chất hữu cơ bị phân hủy sinh học ($Q(S_0 - S)$ tính theo COD hoặc bCOD) bằng lượng chất hữu cơ mất đi trừ đi lượng chất hữu cơ được chuyển đổi thành tế bào sinh khối mới:
  $$R_{O,\text{carbon}} = Q(S_0 - S) \cdot 10^{-3} - 1.42 \cdot P_{X,\text{bio}} \quad \left[ \frac{\text{kg O}_2}{\text{d}} \right]$$
- **Giải thích hệ số tương đương $1.42\ g\ COD/g\ VSS$:** Tế bào vi khuẩn có công thức hóa học trung bình là $C_5H_7O_2N$. Phản ứng oxy hóa hoàn toàn tế bào:
  $$\text{C}_5\text{H}_7\text{O}_2\text{N} + 5\text{O}_2 \rightarrow 5\text{CO}_2 + 2\text{H}_2\text{O} + \text{NH}_3$$
  $$\text{Khối lượng mol: } M(\text{C}_5\text{H}_7\text{O}_2\text{N}) = 5(12) + 7(1) + 2(16) + 14 = 113\ \text{g/mol}$$
  $$\text{Khối lượng oxy tiêu thụ: } 5 \times 32 = 160\ \text{g O}_2$$
  $$\text{Tỷ số COD/VSS} = \frac{160}{113} = 1.416 \approx 1.42\ \frac{\text{g COD}}{\text{g VSS}}$$
  - Nghĩa là cứ $1\ kg$ sinh khối vi sinh bay hơi ($VSS$) được tạo thành và xả bỏ khỏi hệ thống sẽ mang theo $1.42\ kg$ tương đương COD không bị oxy hóa bởi dưỡng khí cấp vào.

##### 4.1.2 Nhu cầu oxy cho quá trình nitrat hóa (Nitrogenous Oxygen Demand - NOD)

###### 4.1.2.1 Phương trình $R_{O,\text{nitrogen}} = 4.57 Q (N_0 - N) - 1.42 P_{X,\text{bio,nit}}$
- Mỗi gam amoni nitơ bị oxy hóa thành nitrat tiêu tốn $4.57\ g\ O_2$:
  $$R_{O,\text{nitrogen}} = 4.57 \cdot Q \cdot \text{NO}_x \cdot 10^{-3} - 1.42 \cdot P_{X,\text{bio,nit}} \quad \left[ \frac{\text{kg O}_2}{\text{d}} \right]$$
- Do sinh khối tự dưỡng $P_{X,\text{bio,nit}}$ rất nhỏ, số hạng thứ hai thường được gộp hoặc xấp xỉ bằng $4.57 \cdot Q \cdot \text{NO}_x \cdot 10^{-3}$.

##### 4.1.3 Phương trình tổng hợp nhu cầu oxy thực tế

###### 4.1.3.1 Tổng hợp công thức $R_O = Q(S_0 - S) \cdot 10^{-3} - 1.42 P_{X,bio} + 4.57 Q \cdot NO_x \cdot 10^{-3}$
- Phương trình toàn diện cho hệ thống kết hợp khử carbon và nitrat hóa:
  $$R_O = \text{AOR} = Q(S_0 - S) \cdot 10^{-3} - 1.42 \cdot P_{X,\text{bio}} + 4.57 \cdot Q \cdot \text{NO}_x \cdot 10^{-3} \quad \left[ \frac{\text{kg O}_2}{\text{d}} \right]$$
- Nhu cầu oxy tính theo giờ làm việc trung bình:
  $$\text{OTR}_f = \frac{R_O}{24} \quad \left[ \frac{\text{kg O}_2}{\text{h}} \right]$$

#### 4.2 Chuyển đổi giữa SOTR (Standard) và AOTR / $OTR_f$ (Field)

##### 4.2.1 Định nghĩa điều kiện chuẩn (Standard Conditions: $20^\circ C$, $1\text{ atm}$, nước sạch)

###### 4.2.1.1 Nồng độ oxy bão hòa ở điều kiện chuẩn ($C_{s,20}^* = 9.09\ mg/L$)
- Nồng độ oxy bão hòa trong nước sạch tinh khiết ở nhiệt độ $20^\circ C$, áp suất khí quyển $1.0\text{ atm}$ ($101.325\ kPa$, tương đương $10.33\ m$ cột nước): $C_{s,20}^* = 9.09\ mg/L$.

##### 4.2.2 Các hệ số hiệu chỉnh hiện trường

###### 4.2.2.1 Hệ số chất nền nước thải $\alpha$ ($K_L a_{\text{wastewater}} / K_L a_{\text{clean}}$)
- **Định nghĩa:** Tỷ số giữa hệ số truyền khối thể tích oxy trong hỗn hợp nước thải bùn hoạt tính so với trong nước sạch:
  $$\alpha = \frac{K_L a_{\text{wastewater}}}{K_L a_{\text{clean}}}$$
- **Dải giá trị:** $\alpha = 0.40 - 0.85$.
  - Bể khử BOD tải trọng thông thường (chứa nhiều chất hoạt động bề mặt surfactants làm cản trở hòa tan oxy qua màng bọt khí): $\alpha = 0.45 - 0.55$ (thường lấy $0.50$).
  - Bể có nitrat hóa hoặc tuổi bùn cao (chất hoạt động bề mặt bị phân hủy triệt để): $\alpha = 0.65 - 0.80$ (thường lấy $0.65$).

###### 4.2.2.2 Hệ số bão hòa muối hòa tan $\beta$ ($C^*_{s,\text{wastewater}} / C^*_{s,\text{clean}}$)
- **Định nghĩa:** Tỷ số giữa độ hòa tan bão hòa oxy trong nước thải so với nước sạch ở cùng nhiệt độ:
  $$\beta = \frac{C^*_{s,\text{wastewater}}}{C^*_{s,\text{clean}}}$$
- **Dải giá trị:** $\beta = 0.95 - 0.98$ (đối với nước thải sinh hoạt đô thị thông thường lấy chuẩn $\beta = 0.95$).

###### 4.2.2.3 Hệ số độ bám bẩn của đĩa phân phối khí $F$ ($0.65 - 0.90$)
- Kể đến hiện tượng lỗ xốp đĩa phân phối khí bị tắc nghẽn cục bộ bởi màng nhầy vi sinh vật hoặc đóng cặn khoáng chất theo thời gian vận hành. Đĩa mới: $F = 1.0$; thiết kế thông thường chọn $F = 0.85 - 0.90$.

###### 4.2.2.4 Hệ số hiệu chỉnh áp suất khí quyển theo cao độ địa hình $\Omega = P_b/P_a$
- Công thức áp kế khí quyển phụ thuộc cao độ $z$ (mét) so với mực nước biển:
  $$\Omega = \frac{P_b}{P_a} = \exp\left(-\frac{g \cdot M \cdot z}{R \cdot T_a}\right)$$
  - $g = 9.81\ m/s^2$: gia tốc trọng trường.
  - $M = 28.97\ kg/kmol$: khối lượng mol trung bình của không khí khô.
  - $z$: cao độ công trình xây dựng ($m$). Tại $z = 500\ m$, $\Omega \approx 0.942$.
  - $R = 8,314\ J/(kmol\cdot K)$: hằng số khí lý tưởng.
  - $T_a$: nhiệt độ tuyệt đối của không khí ($K = 273.15 + T_C$).

###### 4.2.2.5 Hiệu chỉnh độ sâu đặt đĩa và áp suất thủy tĩnh ($C^*_{\infty,T}$)
- Áp suất tại độ sâu đặt đĩa phân phối khí ($D_f$) lớn hơn áp suất khí quyển, làm tăng áp suất riêng phần của oxy trong bọt khí:
  $$C^*_{\infty,T} = C_{s,T,H} \cdot \left( 1 + d_e \cdot \frac{D_f}{10.33} \right) = \Omega \cdot \tau \cdot C_{s,20}^* \cdot \left( 1 + \frac{D_f}{2 \cdot 10.33} \right)$$
  - $d_e = 0.50$: hệ số vị trí thoát bọt khí trung bình (ở giữa độ sâu bể).
  - $D_f$: độ ngập sâu của đĩa khí ($m$).
  - $\tau = C_{st} / C_{s,20}$: hệ số bão hòa oxy theo nhiệt độ ở mực nước biển.

##### 4.2.3 Phương trình quan hệ tổng quát giữa SOTR và AOTR

###### 4.2.3.1 Công thức chuẩn hóa: $\text{SOTR} = \text{AOTR} \cdot \left[ \frac{C^*_{s,20}}{\alpha \cdot F \cdot (\beta C^*_{\infty,T} - C_L)} \right] \cdot \theta^{-(T - 20)}$
- Phương trình chuyển đổi giữa tốc độ truyền oxy hiện trường thực tế ($OTR_f$ hay AOTR) và tốc độ truyền oxy chuẩn trong nước sạch ($SOTR$):
  $$\text{OTR}_f = \text{SOTR} \cdot \left[ \frac{\alpha \cdot F \cdot (\beta \cdot C^*_{\infty,T} - C_L)}{C^*_{s,20}} \right] \cdot \theta^{T - 20}$$
  $$\text{SOTR} = \text{OTR}_f \cdot \left[ \frac{C^*_{s,20}}{\alpha \cdot F \cdot (\beta \cdot C^*_{\infty,T} - C_L)} \right] \cdot \theta^{-(T - 20)}$$
  - $\theta = 1.024$: hệ số hiệu chỉnh nhiệt độ truyền khối khí.
  - $C_L$: nồng độ oxy hòa tan mục tiêu duy trì trong bể (thường lấy $2.0\ mg/L$).

#### 4.3 Các loại thiết bị phân phối khí và cơ chế hòa tan oxy (Aeration Hardware & Mechanisms)

##### 4.3.1 Hệ thống khuếch tán khí bọt mịn (Fine-Bubble Diffused Aeration)

###### 4.3.1.1 Cấu tạo đĩa bọt mịn (Ceramic / EPDM / Polyethylene disc), lỗ van một chiều
- **Cấu tạo chi tiết:**
  - Đĩa khuếch tán hình tròn (đường kính $200 - 350\ mm$) làm bằng màng cao su đàn hồi EPDM, gốm sứ xốp nung (ceramic) hoặc nhựa polyethylene liên kết hạt.
  - Tấm đế polymer (Base plate) đỡ màng xốp và phân phối đều áp lực khí.
  - Vành ren siết (Threaded retaining ring) kẹp chặt mép màng xốp với vòng đệm kín.
  - Van một chiều tích hợp (Integrated one-way check valve): Là tấm lưỡi gà cao su hoặc van bi đàn hồi ở cuống đĩa. Khi dừng quạt gió, áp lực thủy tĩnh của cột nước đẩy van đóng chặt ngay lập tức, ngăn ngừa tuyệt đối bùn hoạt tính xâm nhập vào bên trong đường ống dẫn khí gây tắc nghẽn.
  - Lỗ tiết lưu cân bằng áp lực (Control orifice): Định lượng lưu lượng khí và tạo tổn thất áp lực thiết kế ($250 - 500\ mm\ H_2O$), đảm bảo tất cả các đĩa trên cùng một nhánh ống đều xả khí đồng đều như nhau.

###### 4.3.1.2 Kích thước bọt khí ($1.0 - 3.0\ mm$), hiệu suất chuyển hóa oxy chuẩn (SOTE = $25 - 40\%$)
- **Đặc tính bọt khí:** Đường kính bọt khí thoát ra rất nhỏ ($1.0 - 3.0\ mm$), tạo diện tích tiếp xúc bề mặt liên pha cực lớn trên một đơn vị thể tích khí đưa vào ($a = 6 / d_b$).
- **Hiệu suất truyền oxy chuẩn (SOTE):** Đạt từ $6.0 - 8.5\% / \text{m độ sâu ngập nước}$, tương ứng với tổng SOTE đạt $25 - 40\%$ ở chiều sâu bể $4.5 - 5.0\ m$.
- **Ưu điểm:** Tiết kiệm điện năng tối đa so với các hệ thống làm thoáng khác.

##### 4.3.2 Hệ thống khuếch tán khí bọt thô (Coarse-Bubble Aeration)

###### 4.3.2.1 Ứng dụng trong sục khí rửa màng MBR, bể tiếp xúc và chống lắng bùn
- Bọt khí có kích thước lớn ($6.0 - 10.0\ mm$), vận tốc nổi nhanh, sinh ra lực cắt thủy lực mạnh mẽ.
- Chuyên dụng cho các vị trí: sục khí cọ rửa bề mặt sợi màng trong bể lọc màng MBR (Air Scouring) để đánh bật bánh cặn bùn, bể lắng cát thổi khí, mương phân phối bùn, bể điều hòa, và bể tiếp xúc clo.

###### 4.3.2.2 Hiệu suất oxy hóa (SOTE = $6 - 12\%$) và đặc tính chống tắc nghẽn
- **Hiệu suất SOTE:** Rất thấp, chỉ đạt $6 - 12\%$ do thời gian bọt khí nổi lên mặt nước rất nhanh và diện tích tiếp xúc bề mặt nhỏ.
- **Ưu điểm:** Cực kỳ bền bỉ, hầu như không bao giờ bị tắc nghẽn, tổn thất áp lực qua đầu xả rất nhỏ ($< 50 - 100\ mm\ H_2O$).

##### 4.3.3 Máy sục khí cơ học bề mặt (Mechanical Surface Aerators)

###### 4.3.3.1 Cơ chế tạo màng nước umbrella, vùng xoáy toroidal và công suất ($7.5 - 75\ kW$)
- **Cơ chế vận hành:** Cánh khuấy xoay tốc độ cao (loại nổi hoặc gắn trên sàn cầu bê tông cố định) hoạt động tại ranh giới pha lỏng-khí, hoạt động như một máy bơm dòng chảy hỗn hợp công suất lớn. Cánh khuấy hút nước từ đáy bể và phun văng cực mạnh ra xung quanh thành màng nước dạng chiếc ô (umbrella spray pattern).
- **Cơ chế truyền oxy:** Nước thải bị xé rách thành hàng triệu giọt nước nhỏ tiếp xúc trực tiếp với không khí khí quyển (tái sục khí bề mặt) đồng thời lôi cuốn các bọt khí chui sâu xuống lòng chất lỏng.
- **Dòng tuần hoàn Toroidal:** Sự tiêu tán năng lượng tạo ra vòng lặp hoàn lưu hình vành khuyên (donut-shaped toroidal flow) từ tâm bể trồi lên rồi phân tán tỏa ra thành bể và lặn xuống đáy, đảm bảo bùn không bị sa lắng.

###### 4.3.3.2 Bảng tra mối tương quan công suất, kích thước bể và chiều sâu nước
- Tiêu chuẩn lựa chọn công suất máy sục khí cơ học theo kích thước bể (Bảng `tbl_ch06_02`):
  - Chiều rộng bể $9 - 12\ m$, Chiều sâu $3.0 - 3.5\ m$: Động cơ $7.5\ kW$ ($10\ hp$).
  - Chiều rộng bể $10 - 15\ m$, Chiều sâu $3.5 - 4.0\ m$: Động cơ $15\ kW$ ($20\ hp$).
  - Chiều rộng bể $12 - 18\ m$, Chiều sâu $4.0 - 4.5\ m$: Động cơ $22.5\ kW$ ($30\ hp$).
  - Chiều rộng bể $14 - 20\ m$, Chiều sâu $3.5 - 5.0\ m$: Động cơ $30\ kW$ ($40\ hp$).
  - Chiều rộng bể $14 - 23\ m$, Chiều sâu $4.5 - 5.5\ m$: Động cơ $37.5\ kW$ ($50\ hp$).
  - Chiều rộng bể $15 - 26\ m$, Chiều sâu $4.5 - 6.0\ m$: Động cơ $55\ kW$ ($75\ hp$).
  - Chiều rộng bể $18 - 27\ m$, Chiều sâu $4.5 - 6.0\ m$: Động cơ $75\ kW$ ($100\ hp$).

#### 4.4 Thiết kế mạng lưới đường ống dẫn khí và tính toán công suất máy thổi khí (Blower & Piping Sizing)

##### 4.4.1 Tiêu chuẩn vận tốc khí trong mạng đường ống

###### 4.4.1.1 Phân cấp dải vận tốc theo đường kính ống ($6 - 9\ m/s$ đến $20 - 35\ m/s$)
- Vận tốc dòng khí nén trong đường ống phải được khống chế nghiêm ngặt để tối ưu hóa giữa tổn thất áp lực ma sát và hạn chế tiếng ồn, rung động cơ học (Bảng `tbl_ch06_01`):
  - Đường kính ống nhỏ ($DN\ 25 - 75\ mm$): Vận tốc $6 - 9\ m/s$ (ống nhánh cấp khí trực tiếp cho các dàn đĩa).
  - Đường kính ống trung bình ($DN\ 100 - 250\ mm$): Vận tốc $9 - 15\ m/s$ (ống phân phối phụ dọc thành bể).
  - Đường kính ống lớn ($DN\ 300 - 600\ mm$): Vận tốc $15 - 20\ m/s$ (ống góp chính dẫn khí từ nhà quạt thổi khí).
  - Đường kính ống truyền dẫn lớn ($DN\ 750 - 1500\ mm$): Vận tốc $20 - 35\ m/s$ (ống thép chính của trạm xử lý quy mô lớn).

##### 4.4.2 Tính toán lưu lượng khí cấp thực tế ($Q_{\text{air}}$)

###### 4.4.2.1 Phương trình chuyển đổi từ SOTR sang lưu lượng khí chuẩn ($m^3/\text{phút}$ hoặc $m^3/\text{h}$)
- Trong $1.0\ m^3$ không khí khô ở điều kiện tiêu chuẩn ($1.0\ atm, 20^\circ C$):
  - Khối lượng riêng của không khí: $\rho_{\text{air}} = 1.204\ kg/m^3$.
  - Tỷ lệ oxy theo khối lượng: $23.2\%$.
  - Khối lượng oxy chứa trong $1\ m^3$ không khí: $1.204 \times 0.232 = 0.279\ kg\ O_2/m^3\ \text{không khí}$.
- Lưu lượng không khí chuẩn cần cung cấp hàng giờ:
  $$Q_{\text{air,h}} = \frac{\text{SOTR}}{E \cdot 0.279} \quad \left[ \frac{\text{m}^3}{\text{h}} \right]$$
  $$Q_{\text{air,min}} = \frac{Q_{\text{air,h}}}{60} \quad \left[ \frac{\text{m}^3}{\text{min}} \right]$$
  - Trong đó $E = \text{SOTE}$ là hiệu suất truyền oxy chuẩn của loại đĩa khuếch tán khí lựa chọn ($E = 0.25 - 0.40$).

##### 4.4.3 Tính toán công suất máy thổi khí nén đoạn nhiệt (Adiabatic Blower Power Formulation)

###### 4.4.3.1 Phương trình nhiệt động lực học: $P_w = \frac{w R T_1}{29.7 n e} \left[ \left(\frac{p_2}{p_1}\right)^{0.283} - 1 \right]$
- Quá trình nén khí trong máy thổi khí ly tâm hoặc roots blower diễn ra rất nhanh và được mô hình hóa theo quá trình nén đoạn nhiệt (adiabatic compression):
  $$P_w = \frac{w \cdot R \cdot T_1}{29.7 \cdot n \cdot e} \left[ \left(\frac{p_2}{p_1}\right)^{0.283} - 1 \right] \quad [\text{kW}]$$

###### 4.4.3.2 Định nghĩa các biến số ($w, R, T_1, p_1, p_2, n, e$) và đơn vị chuẩn
- $P_w$: Công suất điện tiêu thụ trên trục máy thổi khí ($kW$).
- $w$: Lưu lượng khối lượng của dòng không khí nạp vào máy ($kg/s$):
  $$w = Q_{\text{air,s}} \cdot \rho_{\text{air}} = \frac{Q_{\text{air,h}}}{3600} \cdot 1.204 \quad [kg/s]$$
- $R$: Hằng số chất khí của không khí ($8.314\ kJ/(kmol\cdot K)$ chia cho khối lượng mol $28.97\ kg/kmol = 0.287\ kJ/(kg\cdot K)$).
- $T_1$: Nhiệt độ tuyệt đối của không khí tại cửa hút máy thổi khí ($K = 273.15 + T_C$).
- $p_1$: Áp suất tuyệt đối tại cửa hút máy thổi khí ($kPa$, thông thường ở mặt đất $p_1 = 101.325\ kPa$).
- $p_2$: Áp suất tuyệt đối tại cửa xả của máy thổi khí ($kPa$):
  $$p_2 = p_1 + \Delta p_{\text{tĩnh}} + \Delta p_{\text{đĩa}} + \Delta p_{\text{ống}}$$
  - $\Delta p_{\text{tĩnh}} = \rho_w \cdot g \cdot D_f \cdot 10^{-3}$ ($kPa$, áp lực cột nước trên đĩa khí).
  - $\Delta p_{\text{đĩa}}$: Tổn thất áp lực qua đĩa khuếch tán khí ($2.5 - 5.0\ kPa$).
  - $\Delta p_{\text{ống}}$: Tổn thất áp lực ma sát và cục bộ trong đường ống dẫn khí ($3.0 - 6.0\ kPa$).
- $n$: Số mũ nén đoạn nhiệt, với không khí có tỷ số nhiệt dung $k = c_p/c_v = 1.395$:
  $$n = \frac{k - 1}{k} = \frac{1.395 - 1}{1.395} = 0.283$$
- $e$: Hiệu suất tổng hợp của máy thổi khí và động cơ ($0.70 - 0.85$, điển hình lấy $0.75 - 0.80$).
- $29.7$: Hằng số thực nghiệm quy đổi đơn vị trong công thức kỹ thuật truyền thống.

### 5. Các Biến thể Công nghệ Bùn Hoạt tính (Activated Sludge Process Modifications)

#### 5.1 Bể bùn hoạt tính khuấy trộn hoàn toàn (Complete-Mix Activated Sludge - CMAS)

##### 5.1.1 Sơ đồ dòng, đặc tính thủy lực và khả năng chịu sốc tải
- Nước thải đầu vào và bùn tuần hoàn được hòa trộn tức thời trên toàn bộ thể tích bể. Nồng độ cơ chất và vi sinh vật tại mọi điểm trong bể đều đồng nhất và bằng nồng độ của dòng xả ra.
- **Khả năng chịu sốc tải:** Pha loãng tức thời các chất ô nhiễm độc hại hoặc nồng độ hữu cơ tăng đột biến, bảo vệ vi sinh vật không bị ức chế cục bộ.

##### 5.1.2 Thông số vận hành đặc trưng và nhược điểm (nguy cơ bùn nở do vi khuẩn sợi)
- **Thông số vận hành:** $\text{HRT} = 3 - 6\ h$ (BOD only) hoặc $8 - 16\ h$ (nitrat hóa), $\text{MLSS} = 1,500 - 4,000\ mg/L$, $\text{OLR} = 0.3 - 1.6\ kg\ BOD/(m^3\cdot d)$, $\text{F/M} = 0.2 - 0.6\ d^{-1}$, $\theta_c = 3 - 15\ d$.
- **Nhược điểm cốt tử:** Do môi trường cơ chất luôn ở mức thấp đồng nhất trên toàn bể, thiếu hụt gradient nồng độ nạp dinh dưỡng dẫn đến việc vi khuẩn dạng sợi cạnh tranh thắng thế vi khuẩn tạo bông (floc-formers), khiến bể CMAS có nguy cơ bùng phát bùn nở (sludge bulking) cao nhất trong các dạng bể bùn hoạt tính.

#### 5.2 Bể bùn hoạt tính dòng chảy nút (Plug-Flow Activated Sludge - PFAS)

##### 5.2.1 Sơ đồ dòng dài hẹp ($L/W > 5:1 - 10:1$) và gradient cơ chất dọc bể
- Nước thải và bùn tuần hoàn nạp vào đầu bể và chảy dọc theo chiều dài bể dạng kênh hẹp dài. Gradient nồng độ cơ chất hình thành rất rõ rệt: ở đầu bể nồng độ cơ chất cực cao, sau đó giảm dần đều về cuối bể.

##### 5.2.2 Cơ chế tạo vùng 'Feast - Famine' ức chế vi khuẩn sợi và phân bố nhu cầu oxy
- **Cơ chế chọn lọc động học (Kinetic Selection):**
  - Đầu bể là vùng 'Thịnh soạn' (Feast zone): F/M cao ngất ngưởng, vi khuẩn tạo bông (floc-formers) có $\mu_m$ lớn sẽ hấp thu và tích lũy phần lớn cơ chất vào bên trong tế bào.
  - Cuối bể là vùng 'Đói kém' (Famine zone): Cơ chất cạn kiệt, vi sinh chuyển hóa thức ăn dự trữ.
  - Chu trình Feast - Famine triệt tiêu hoàn toàn ưu thế sinh tồn của vi khuẩn dạng sợi, tạo ra bông bùn đặc chắc, lắng cực tốt ($SVI < 80 - 100\ mL/g$).
- **Phân bố nhu cầu cấp khí:** Nhu cầu oxy ở đầu bể cực cao ($40 - 50\%$ tổng lượng khí), trong khi cuối bể rất thấp. Do đó cần bố trí mật độ đĩa sục khí giảm dần theo chiều dài bể (Tapered Aeration) để tránh lãng phí năng lượng.

#### 5.3 Bể sục khí cấp nước thải theo bậc (Step-Feed Aeration)

##### 5.3.1 Cấu tạo nhiều điểm nạp nước thải dọc chiều dài bể
- Toàn bộ dòng bùn tuần hoàn RAS ($Q_r$) được nạp vào đầu bể (ngăn 1). Nước thải đầu vào ($Q$) được phân chia thành nhiều dòng nhỏ ($2 - 4$ điểm nạp) nạp rải rác vào đầu các ngăn tiếp theo.

##### 5.3.2 Phân bố nồng độ bùn giảm dần theo chiều dòng chảy và san bằng tải trọng oxy
- **Hiệu ứng phân bậc MLSS:** Ngăn 1 chỉ chứa bùn tuần hoàn nên có nồng độ sinh khối cực cao ($5,000 - 8,000\ mg/L$). Nồng độ MLSS loãng dần ở các ngăn sau và giảm xuống mức bình thường ($2,500 - 3,000\ mg/L$) ở ngăn xả ra bể lắng.
- **Lợi ích công nghệ:** Tổng khối lượng sinh khối duy trì trong bể tăng $30 - 50\%$, giúp chịu được lưu lượng đỉnh mà không làm tăng tải trọng cặn lên bể lắng đợt 2. Đồng thời san bằng tốc độ tiêu thụ oxy dọc theo bể.

#### 5.4 Quá trình Tiếp xúc - Ổn định (Contact Stabilization)

##### 5.4.1 Cơ chế tách rời pha hấp phụ tiếp xúc nhanh ($0.5 - 1.0\ h$) và pha ổn định tiêu hóa bùn ($3 - 6\ h$)
- Dựa trên nguyên lý sinh học: vi khuẩn bùn hoạt tính có khả năng hấp phụ bề mặt cực nhanh phần lớn các chất hữu cơ dạng keo và phân tử lớn chỉ trong vòng $30 - 60\text{ phút}$, sau đó cần vài giờ để tiêu hóa và phân hủy nội bào.
- **Cấu tạo hai ngăn riêng biệt:**
  - Ngăn tiếp xúc (Contact tank): Nước thải hòa trộn với bùn ổn định, thời gian lưu thủy lực rất ngắn $\text{HRT} = 0.5 - 1.0\ h$. Hỗn hợp bùn nước chảy qua bể lắng đợt 2.
  - Ngăn ổn định bùn (Stabilization tank): Bùn lắng được bơm về một ngăn sục khí riêng không nạp nước thải, lưu trong $3 - 6\ h$ để oxy hóa các chất hữu cơ đã hấp phụ và phục hồi năng lực hấp phụ của bùn.

##### 5.4.2 Tối ưu hóa dung tích bể và tiết kiệm $30 - 40\%$ tổng thể tích xây dựng
- Do ngăn ổn định chỉ chứa bùn lắng đặc ($X_r = 6,000 - 10,000\ mg/L$) với thể tích bằng lưu lượng bùn tuần hoàn $Q_r$ (nhỏ hơn nhiều so với $Q$), tổng thể tích công trình của hệ thống Contact Stabilization giảm $30 - 40\%$ so với bể CAS truyền thống.

#### 5.5 Quá trình Làm thoáng Kéo dài (Extended Aeration)

##### 5.5.1 Chế độ vận hành ở vùng hô hấp nội sinh ($\theta_c = 20 - 30\ \text{ngày}$, $F/M = 0.05 - 0.15\ d^{-1}$)
- Bể vận hành với thời gian lưu nước rất dài ($\text{HRT} = 18 - 36\ h$) và tuổi bùn cao ($\theta_c = 20 - 30\ \text{ngày}$). Tỷ số F/M duy trì cực kỳ thấp trong vùng hô hấp tự oxy hóa tế bào.

##### 5.5.2 Sản lượng bùn thấp, bùn khoáng hóa cao, không cần bể lắng đợt 1
- Lượng bùn dư sinh ra rất ít ($Y_{obs}$ nhỏ), bùn được khoáng hóa sâu và ổn định, có thể phơi hoặc ép bùn trực tiếp mà không cần công trình phân hủy bùn kỵ khí chuyên biệt. Nước thải thô sau lắng cát được đưa thẳng vào bể hiếu khí mà không cần bể lắng 1.

#### 5.6 Mương Oxy hóa (Oxidation Ditch)

##### 5.6.1 Thủy lực kênh dẫn tuần hoàn kín dạng oval với sục khí rotor/chổi cọ
- Bể là một kênh hẹp tuần hoàn kín hình vành khuyên hoặc bầu dục (oval). Dòng nước được thúc đẩy chuyển động liên tục với vận tốc dòng $0.25 - 0.35\ m/s$ bằng các đĩa sục khí cơ học trục ngang (Mammoth rotor), chổi sục khí hoặc turbine chìm.

##### 5.6.2 Vùng hiếu khí xen kẽ thiếu khí tự nhiên và khả năng khử nitơ đồng thời (SND)
- Ngay phía sau trục quay sục khí là vùng giàu oxy ($DO = 2.0 - 3.0\ mg/L$, diễn ra khử BOD và nitrat hóa). Khi dòng chảy trôi dọc theo mương ra xa thiết bị cấp khí, oxy cạn kiệt tạo thành vùng thiếu khí ($DO < 0.2 - 0.5\ mg/L$, diễn ra phản nitrat hóa). Hiện tượng khử nitơ đồng thời (Simultaneous Nitrification-Denitrification - SND) đạt hiệu quả cao mà không cần bổ sung ngăn anoxic riêng.

#### 5.7 Bể phản ứng gián đoạn theo mẻ (Sequencing Batch Reactor - SBR)

##### 5.7.1 Khái niệm vận hành fill-and-draw và loại bỏ bể lắng đợt 2 độc lập
- SBR là hệ thống bùn hoạt tính nạp và tháo nước gián đoạn (fill-and-draw). Tất cả các quá trình: điều hòa, phản ứng sinh học, lắng trong và gạt nước trong đều diễn ra tuần tự trong cùng một bể duy nhất theo thời gian, loại bỏ hoàn toàn nhu cầu xây dựng bể lắng đợt 2 độc lập và hệ thống bơm bùn tuần hoàn RAS.

##### 5.7.2 Chi tiết 5 pha chu kỳ vận hành tuần hoàn (5-Phase Operating Cycle)

###### 5.7.2.1 Pha Nạp nước (Fill): Nạp tĩnh, nạp khuấy, nạp sục khí
- Nước thải nạp vào bể đang chứa sẵn bùn hoạt tính từ chu kỳ trước. Tùy thuộc vào mục tiêu công nghệ:
  - **Nạp tĩnh (Static Fill):** Không sục khí, không khuấy, tạo điều kiện yếm khí cao, kích thích vi khuẩn PAO giải phóng phospho.
  - **Nạp khuấy trộn (Mixed Fill):** Khuấy không sục khí, tạo môi trường thiếu khí (anoxic), vi khuẩn khử nitrat tiêu thụ nitrate còn sót lại từ chu kỳ trước.
  - **Nạp sục khí (Aerated Fill):** Cấp khí ngay khi nạp để bắt đầu quá trình oxy hóa hiếu khí.

###### 5.7.2.2 Pha Phản ứng (React): Động học phân hủy cơ chất và nitrat hóa theo mẻ
- Ngừng nạp nước thải, tiếp tục sục khí mạnh mẽ và khuấy trộn hoàn toàn. Nồng độ chất hữu cơ và amoni giảm sâu theo quy luật động học mẻ.

###### 5.7.2.3 Pha Lắng (Settle): Quá trình lắng tĩnh tuyệt đối lý tưởng (Quiescent settling)
- Dừng toàn bộ hệ thống sục khí và máy khuấy. Khối chất lỏng hoàn toàn bất động, loại bỏ mọi tác động của dòng chảy ngang, dòng xoáy thủy lực hay dòng cuộn nhiệt độ thường gặp ở bể lắng liên tục.
- Quá trình lắng diễn ra cực nhanh và đồng nhất theo cơ chế lắng Type III (lắng vùng) tạo thành ranh giới bùn nước sắc nét.

###### 5.7.2.4 Pha Tháo nước trong (Decant): Cơ chế máy gạt/thu nước bề mặt và kiểm soát lớp cặn
- Thiết bị gạt thu nước bề mặt (Decanter) chuyển động hạ thấp dần theo mực nước, thu lớp nước mặt trong vắt xả ra ngoài mà không khuấy động lớp mền bùn đã lắng ở đáy.

###### 5.7.2.5 Pha Chờ (Idle): Ổn định vi sinh và xả bùn dư theo mẻ
- Thời gian chuyển tiếp giữa hai chu kỳ nạp, cho phép xả bùn dư WAS tích tụ ở đáy bể và ổn định vi sinh vật.

##### 5.7.3 Phương trình động học mẻ và thiết kế phân đoạn thể tích SBR

###### 5.7.3.1 Tích phân động học bậc một và Monod cho BOD: $K_s \ln(S_0/S_t) + (S_0 - S_t) = k X t$
- Trong bể mẻ với nồng độ sinh khối $X$ không đổi trong pha phản ứng:
  $$-\frac{dS}{dt} = \frac{k X S}{K_s + S} \implies -\int_{S_0}^{S_t} \frac{K_s + S}{S} dS = k X \int_0^{t_R} dt$$
  $$K_s \ln\left(\frac{S_0}{S_t}\right) + (S_0 - S_t) = k \cdot X \cdot t_R$$

###### 5.7.3.2 Tích phân động học nitrat hóa có giới hạn DO: $K_n \ln(N_0/N_t) + (N_0 - N_t) = (\mu_{nm} X_n / Y_n) [DO/(K_o + DO)] t$
- Phương trình động học mẻ cho oxy hóa amoni:
  $$K_n \ln\left(\frac{N_0}{N_t}\right) + (N_0 - N_t) = \left( \frac{\mu_{nm} \cdot X_n}{Y_n} \right) \cdot \left( \frac{\text{DO}}{K_o + \text{DO}} \right) \cdot t_R$$

###### 5.7.3.3 Phân đoạn thể tích bùn lắng $F(V_T) = \frac{\text{MLSS} \cdot \text{SVI}}{10^6}$
- Tỷ lệ thể tích tối thiểu mà lớp bùn sau lắng chiếm giữ trong bể:
  $$F(V_T) = \frac{\text{MLSS} \cdot \text{SVI}}{10^6} \quad [\text{không thứ nguyên}]$$
  - Ví dụ với $\text{MLSS} = 3,500\ mg/L$ và $\text{SVI} = 150\ mL/g$:
    $$F(V_T) = \frac{3,500 \times 150}{10^6} = 0.525\ (52.5\%\ \text{thể tích bể})$$

###### 5.7.3.4 Tính toán thể tích tháo nước và độ sâu dự phòng an toàn (Buffer zone)
- Thể tích nước tháo ra mỗi mẻ ($V_F = V_{\text{decant}}$):
  $$V_F = \frac{Q}{n_{\text{cycles}} \cdot N_{\text{tanks}}}$$
- Tỷ số tháo nước: $\alpha_D = V_F / V_T$.
- Điều kiện an toàn để tránh hút bùn vào máng gạt:
  $$\alpha_D + F(V_T) \le 0.75 - 0.80$$
  - Phần thể tích còn lại $1.0 - (\alpha_D + F(V_T)) \ge 0.20 - 0.25$ đóng vai trò là vùng đệm nước trong an toàn (Buffer zone) bên trên lớp chăn bùn.

#### 5.8 Bể phản ứng sinh học màng (Membrane Bioreactor - MBR)

##### 5.8.1 Nguyên lý cấu tạo và phân loại màng lọc (Hollow Fiber & Flat Sheet, MF & UF)
- **Khái niệm:** MBR là sự tích hợp đột phá giữa quá trình sinh học hiếu khí bùn hoạt tính lơ lửng và quá trình lọc tách chất lỏng-rắn bằng màng vi lọc (Microfiltration - MF, kích thước lỗ $0.1 - 0.4\ \mu m$) hoặc siêu lọc (Ultrafiltration - UF, kích thước lỗ $0.01 - 0.1\ \mu m$).
- **Phân loại module màng:**
  - Dạng sợi rỗng (Hollow Fiber): Mật độ diện tích màng cực cao ($1,000 - 1,500\ m^2/m^3$), vật liệu PVDF đàn hồi, hút chân không từ bên ngoài sợi vào trong ống mao dẫn (Out-to-In).
  - Dạng tấm phẳng (Flat Sheet): Các tấm màng đặt thẳng đứng song song nhau, dòng nước thấm qua 2 mặt phẳng vào rãnh thu nước trung tâm, ít bị quấn tóc và rác hơn sợi rỗng nhưng giá thành cao hơn.

##### 5.8.2 Thiết lập cân bằng vật chất sinh khối và thủy lực hoàn lưu ($R = 4 - 6$)

###### 5.8.2.1 Quan hệ nồng độ bùn giữa bể màng và bể sinh học: $X_A = \frac{R}{1 + R} X_m$
- Hệ thống gồm ngăn hiếu khí (Aeration tank, nồng độ $X_A$) và ngăn màng (Membrane tank, nồng độ $X_m$). Nước thấm qua màng hoàn toàn không chứa cặn ($X_e = 0$). Bơm hoàn lưu bùn từ bể màng về bể hiếu khí với lưu lượng $Q_R = R \cdot Q$:
  - Cân bằng sinh khối tại bể hiếu khí:
    $$Q \cdot X_0 + Q_R \cdot X_m = (Q + Q_R) \cdot X_A$$
  - Với $X_0 \approx 0$ và chia cả hai vế cho $Q$:
    $$R \cdot X_m = (1 + R) \cdot X_A \implies X_A = \frac{R}{1 + R} \cdot X_m$$
  - Với $R = 6$ và $X_m = 12,000\ mg/L$:
    $$X_A = \frac{6}{1 + 6} \cdot 12,000 = \frac{6}{7} \cdot 12,000 = 10,286\ \text{mg/L}$$

##### 5.8.3 Thông số thiết kế màng và kích thước thể tích cụm bể

###### 5.8.3.1 Thông lượng màng thiết kế ($J = 16 - 25\ L/m^2\cdot h$) và diện tích màng $A_m = Q/J$
- Thông lượng lọc (Membrane Flux, $J$): Thể tích nước thấm qua một đơn vị diện tích màng trong một đơn vị thời gian:
  $$J = 16 - 25\ \text{L}/(\text{m}^2\cdot\text{h}) = 0.384 - 0.600\ \text{m}^3/(\text{m}^2\cdot\text{d})$$
- Tổng diện tích bề mặt màng yêu cầu:
  $$A_m = \frac{Q}{J_{\text{design}}} \quad [\text{m}^2]$$

###### 5.8.3.2 Tỷ số thể tích bể màng trên diện tích màng ($V_m/A_m = 0.015 - 0.05\ m^3/m^2$)
- Thể tích ngăn đặt module màng phụ thuộc vào cấu hình cassette và mật độ đóng gói:
  $$V_m = A_m \cdot \left(\frac{V_m}{A_m}\right) \quad [\text{m}^3]$$
  - Giá trị tiêu chuẩn thường chọn $V_m/A_m = 0.025\ m^3/m^2$.

###### 5.8.3.3 Phân chia thể tích bể hiếu khí $V_A$ và bể màng $V_m$
- Tổng sinh khối cần duy trì trong hệ thống: $M_{\text{TSS}} = P_{X,TSS} \cdot \theta_c$.
- Khối lượng sinh khối chứa trong bể màng: $M_m = V_m \cdot X_m$.
- Khối lượng sinh khối cần chứa trong bể hiếu khí: $M_A = M_{\text{TSS}} - M_m$.
- Thể tích bể hiếu khí:
  $$V_A = \frac{M_A}{X_A} \quad [\text{m}^3]$$
- Tổng thể tích cụm bể: $V_{\text{total}} = V_A + V_m$. Thể tích này thường nhỏ hơn $60 - 75\%$ so với bể CAS truyền thống.

##### 5.8.4 Quản lý màng, tắc nghẽn màng và quy trình tẩy rửa hóa chất (CIP Protocols)

###### 5.8.4.1 Cơ chế tích tụ EPS, tạo bánh cặn (cake layer) và sục khí bọt thô chống bám bẩn
- Sự bám bẩn màng (Fouling) gây tăng áp suất xuyên màng (TMP - Transmembrane Pressure) và sụt giảm thông lượng. Tác nhân gây tắc gồm:
  - Các chất polyme ngoại bào (EPS - Extracellular Polymeric Substances) và sản phẩm hòa tan của vi sinh vật (SMP).
  - Sự tích tụ các bông cặn bùn trên bề mặt màng tạo lớp bánh lọc (cake layer).
- **Biện pháp thủy lực liên tục:** Sử dụng hệ thống sục khí bọt thô (Air scouring) liên tục từ dưới đáy module màng với cường độ $0.2 - 0.5\ Nm^3\ \text{khí}/(m^2\ \text{màng}\cdot h)$ để tạo dao động sợi màng và dòng cắt bề mặt quét sạch bánh cặn.

###### 5.8.4.2 Quy trình tẩy rửa bảo trì (Maintenance CIP): Tần suất, hóa chất (NaOCl 200 mg/L, Citric acid 2000 mg/L)
- Thực hiện định kỳ $1 - 2\ \text{lần/tuần}$ ngay tại bể (in-situ):
  - Dừng bơm hút thấm, bơm ngược dung dịch hóa chất qua đường ống nước trong vào các lỗ màng.
  - Rửa cặn hữu cơ và màng vi sinh: Dung dịch Natri hypoclorit ($NaOCl, 200 - 500\ mg/L$ Clo hoạt tính).
  - Rửa cặn khoáng và kim loại: Dung dịch Axit citric ($2,000\ mg/L$, $pH \approx 2.5$).
  - Thời gian ngâm: $60 - 75\ \text{phút}$.

###### 5.8.4.3 Quy trình tẩy rửa phục hồi (Recovery CIP): Ngâm chuyên sâu (NaOCl 1000 mg/L + Citric acid 2000 mg/L)
- Thực hiện định kỳ $2 - 4\ \text{lần/năm}$ khi TMP tăng vượt ngưỡng vận hành bình thường ($> 35 - 40\ kPa$):
  - Ngâm chìm toàn bộ cassette màng trong bể tẩy rửa chuyên dụng với nồng độ hóa chất cao:
    - $NaOCl$: $1,000 - 2,000\ mg/L$.
    - Axit citric: $2,000 - 3,000\ mg/L$.
  - Thời gian ngâm sâu: $4 - 6\ \text{giờ}$ (kết hợp sục khí nhẹ hỗ trợ bóc tách mảng bám).

### 6. Thiết kế Bể Lắng Đợt 2 (Secondary Clarifier Design)

#### 6.1 Cơ chế lắng bùn hoạt tính (Type III Zone Settling & Type IV Compression Settling)

##### 6.1.1 Quá trình lắng cản trở (Hindered settling) và hình thành mặt phân cách bùn-nước
- Khi nồng độ cặn lơ lửng trong nước vượt quá $1,000 - 1,500\ mg/L$ (đặc trưng của bùn hoạt tính $2,000 - 5,000\ mg/L$), các hạt bông bùn ở khoảng cách rất gần nhau và tương tác thủy lực lẫn nhau.
- Toàn bộ khối bông bùn liên kết lại thành một cấu trúc chăn bùn (sludge blanket) đồng nhất cùng lắng xuống với một vận tốc chung (Lắng vùng - Type III Zone Settling), hình thành ranh giới phân cách cực kỳ rõ rệt giữa lớp nước trong bên trên và khối bùn bên dưới.

##### 6.1.2 Quá trình lắng nén ép tại đáy bể và thoát nước lỗ rỗng
- Ở vùng đáy bể lắng, nồng độ bùn tăng rất cao ($> 6,000 - 10,000\ mg/L$). Các bông bùn tiếp xúc cơ học trực tiếp lên nhau (Lắng nén - Type IV Compression Settling). Quá trình nén ép đẩy nước lỗ rỗng thoát ngược lên trên, làm cô đặc nồng độ bùn trước khi xả ra đường RAS.

#### 6.2 Phân tích thông lượng cặn (Solids Flux Analysis - SFA) và Điểm trạng thái (State Point Analysis)

##### 6.2.1 Định nghĩa thông lượng trọng lực ($G_g = X \cdot v_i$) và thông lượng đáy do dòng rút bùn ($G_u = X \cdot u$)
- Thông lượng chất rắn ($G$, Solids Flux) là khối lượng bùn khô đi qua một đơn vị diện tích mặt cắt ngang trong một đơn vị thời gian ($kg/(m^2\cdot h)$).
- **Thông lượng do lắng trọng lực ($G_g$):**
  $$G_g = X \cdot v_i \cdot 10^{-3} \quad \left[ \frac{\text{kg}}{\text{m}^2\cdot\text{h}} \right]$$
  - $X$: Nồng độ bùn hoạt tính tại một lớp bất kỳ ($g/m^3$ hoặc $mg/L$).
  - $v_i$: Vận tốc lắng vùng của bùn ở nồng độ $X$ ($m/h$).

###### 6.2.1.1 Vận tốc lắng Vesilind: $v_i = v_0 e^{-k X}$
- Vận tốc lắng giảm theo hàm mũ khi nồng độ bùn tăng (Mô hình thực nghiệm Vesilind):
  $$v_i = v_0 \cdot e^{-k_v \cdot X}$$
  - $v_0$: Vận tốc lắng tối đa của một bông cặn đơn lẻ ($m/h$, thường $v_0 = 6.0 - 12.0\ m/h$).
  - $k_v$: Hằng số nén lắng Vesilind ($m^3/kg$, phụ thuộc vào chỉ số SVI, điển hình $k_v = 0.3 - 0.6\ m^3/kg$).
- **Thông lượng do dòng rút bùn đáy bể ($G_u$):** Do bơm bùn tuần hoàn và xả bùn tạo dòng kéo đi xuống với vận tốc $u$:
  $$u = \frac{Q_r + Q_w}{A} \quad \left[ \frac{\text{m}}{\text{h}} \right]$$
  $$G_u = X \cdot u \cdot 10^{-3} = X \cdot \left(\frac{Q_r + Q_w}{A}\right) \cdot 10^{-3} \quad \left[ \frac{\text{kg}}{\text{m}^2\cdot\text{h}} \right]$$

##### 6.2.2 Đường cong thông lượng tổng ($G_t = G_g + G_u$) và thông lượng giới hạn ($G_L$)

###### 6.2.2.1 Xác định điểm cực tiểu $G_L$ (Limiting Solids Flux)
- Tổng thông lượng cặn vận chuyển xuống đáy:
  $$G_t = G_g + G_u = X \cdot v_0 e^{-k_v X} + X \cdot u$$
- Đồ thị hàm số $G_t$ theo $X$ có một điểm cực tiểu cục bộ gọi là **Thông lượng chất rắn giới hạn ($G_L$)** tại nồng độ bùn giới hạn $X_L$.
- Về mặt toán học hoặc đồ giải, $G_L$ được xác định bằng cách kẻ đường tiếp tuyến với đường cong thông lượng trọng lực $G_g(X)$ xuất phát từ nồng độ bùn tuần hoàn mong muốn $X_r$ trên trục hoành. Giao điểm của đường tiếp tuyến này với trục tung chính là giá trị $G_L$.

###### 6.2.2.2 Diện tích bể lắng giới hạn theo tải trọng cặn: $A = \frac{(Q + Q_r) X}{G_L}$
- Để bể lắng không bị dâng tràn bùn, tổng thông lượng cặn nạp vào từ bể aerotank không được phép vượt quá $G_L$:
  $$G_{\text{applied}} = \frac{(Q + Q_r) \cdot X}{A} \le G_L$$
  $$A_{\text{clarifier}} \ge \frac{(Q + Q_r) \cdot X}{G_L}$$

##### 6.2.3 Phương pháp điểm trạng thái (State Point Analysis - SPA)

###### 6.2.3.1 Điểm trạng thái tải trọng bề mặt (Overflow rate line) và đường vận tốc rút bùn (Underflow line)
- Điểm trạng thái (State Point, SP) trên đồ thị $(X, G)$ được định nghĩa bởi tọa độ:
  - Trục hoành: Nồng độ bùn trong bể hiếu khí $X$ (MLSS).
  - Trục tung: Thông lượng cặn do tải trọng thủy lực bề mặt $G_{SOR} = \text{SOR} \cdot X = (Q/A) \cdot X$.
- Đường tải trọng đáy (Underflow line): Là đường thẳng đi qua điểm trạng thái SP với hệ số góc âm bằng vận tốc rút bùn đáy $u = (Q_r / A)$ và cắt trục hoành tại nồng độ bùn đáy $X_r$.

###### 6.2.3.2 Chẩn đoán trạng thái vận hành bể lắng: Quá tải (Overloaded), Tới hạn (Critically loaded), Dưới tải (Underloaded)
- **Trạng thái dưới tải (Underloaded):** Đường underflow line nằm hoàn toàn phía dưới đỉnh đường cong thông lượng trọng lực $G_g$. Lớp bùn nén mỏng, bể vận hành cực kỳ an toàn.
- **Trạng thái tới hạn (Critically loaded):** Đường underflow line tiếp xúc chính xác (tiếp tuyến) với đường cong $G_g$. Khả năng truyền tải cặn đạt công suất tối đa.
- **Trạng thái quá tải (Overloaded):** Đường underflow line cắt ngang qua đường cong $G_g$. Tốc độ nạp cặn lớn hơn tốc độ vận chuyển cặn xuống đáy $\implies$ sinh khối bùn tích lũy liên tục trong bể lắng, mặt chăn bùn dâng cao dần và cuối cùng tràn qua máng thu nước trong gây ô nhiễm nguồn tiếp nhận.

#### 6.3 Tiêu chuẩn thiết kế bể lắng đợt 2 (Design Criteria & Dimensions)

##### 6.3.1 Tải trọng thủy lực bề mặt (Surface Overflow Rate - SOR)

###### 6.3.1.1 Dải giá trị tiêu chuẩn: $16 - 32\ m^3/m^2\cdot d$ (lưu lượng trung bình), $40 - 48\ m^3/m^2\cdot d$ (lưu lượng đỉnh)
- Diện tích bề mặt bể lắng tính theo tải trọng thủy lực:
  $$A_{\text{hydraulic}} = \frac{Q}{\text{SOR}} \quad [\text{m}^2]$$
- **Tiêu chuẩn thiết kế quốc tế (Metcalf & Eddy):**
  - Lưu lượng trung bình ngày ($Q_{\text{avg}}$): $\text{SOR} = 16 - 32\ m^3/(m^2\cdot d)$ (thông thường chọn $20 - 24\ m^3/m^2\cdot d$).
  - Lưu lượng đỉnh giờ ($Q_{\text{peak}}$): $\text{SOR} = 40 - 48\ m^3/(m^2\cdot d)$.
  - Đối với hệ thống có nitrat hóa (bông bùn nhẹ hơn, dễ nổi): Chọn $\text{SOR} = 16 - 24\ m^3/(m^2\cdot d)$.

##### 6.3.2 Tải trọng cặn bề mặt (Solids Loading Rate - SLR)

###### 6.3.2.1 Dải giá trị tiêu chuẩn: $4.0 - 6.0\ kg/(m^2\cdot h)$ (trung bình), tối đa $8.0 - 10.0\ kg/(m^2\cdot h)$
- Tải trọng cặn bề mặt tính toán dựa trên tổng lưu lượng vào ($Q + Q_r$) và nồng độ MLSS:
  $$\text{SLR} = \frac{(Q + Q_r) \cdot X}{A \cdot 24} \quad \left[ \frac{\text{kg}}{\text{m}^2\cdot\text{h}} \right]$$
- **Tiêu chuẩn thiết kế:**
  - Vận hành trung bình: $\text{SLR} = 4.0 - 6.0\ kg/(m^2\cdot h)$.
  - Vận hành lưu lượng đỉnh: $\text{SLR}_{\max} = 8.0 - 10.0\ kg/(m^2\cdot h)$.
  - Diện tích bể lắng thực tế được chọn là giá trị lớn nhất giữa $A_{\text{hydraulic}}$ và $A_{\text{solids}}$.

##### 6.3.3 Tải trọng máng thu nước (Weir Overflow Rate - WOR)

###### 6.3.3.1 Tiêu chuẩn máng tràn răng cưa V-notch: $125 - 250\ m^3/(m\cdot d)$
- Tải trọng trên mét chiều dài máng thu nước trong:
  $$\text{WOR} = \frac{Q}{L_{\text{weir}}} \quad \left[ \frac{\text{m}^3}{\text{m}\cdot\text{d}} \right]$$
- Dải tiêu chuẩn: $\text{WOR} = 125 - 250\ m^3/(m\cdot d)$ (đối với trạm xử lý quy mô lớn có thể lên đến $375\ m^3/(m\cdot d)$ ở lưu lượng đỉnh).
- Máng tràn luôn sử dụng tấm chắn răng cưa V-notch ($90^\circ$) kèm tấm chắn váng bọt (scum baffle) ngập sâu $0.2 - 0.3\ m$ để ngăn chặn cặn nổi và váng dầu mỡ.

##### 6.3.4 Chiều sâu bể lắng hiệu dụng và phân vùng bể ($H = 3.5 - 5.0\ m$)

###### 6.3.4.1 Chiều sâu vùng nước trong, vùng phân cách lắng, vùng trữ bùn và vùng gạt đáy
- Bể lắng đợt 2 hiện đại thường có chiều sâu nước bên thành ($SWD$ - Side Water Depth) từ $3.5 - 5.0\ m$ (thông dụng nhất chọn $4.0 - 4.5\ m$), được cấu thành từ 4 vùng chức năng thẳng đứng:
  1. **Vùng nước trong bề mặt (Clear water zone):** $h_1 = 0.5 - 1.0\ m$, đảm bảo nước không bị xáo trộn bởi máng thu.
  2. **Vùng lắng và tách pha (Settling zone):** $h_2 = 1.0 - 1.5\ m$, không gian để bông bùn tạo chăn và lắng vùng.
  3. **Vùng trữ bùn điều hòa dao động tải (Sludge storage zone):** $h_3 = 1.0 - 1.5\ m$, dự phòng dung tích chứa bùn khi lưu lượng đỉnh tăng vọt trong $2 - 4\text{ giờ}$.
  4. **Vùng nén cặn và cào bùn đáy (Thickening & scraper zone):** $h_4 = 0.5 - 1.0\ m$, độ dốc đáy bể ($1:12$ đối với bể tròn) dẫn cặn vào hố thu bùn trung tâm.

### 7. Nhận diện Sự cố Vận hành và Biện pháp Khắc phục (Operational Troubleshooting)

#### 7.1 Sự cố bùn nở (Sludge Bulking)

##### 7.1.1 Dấu hiệu nhận biết và chẩn đoán qua chỉ số SVI ($SVI > 150\ mL/g$)
- **Hiện tượng:** Bông bùn hoạt tính tơi xốp, thể tích biểu kiến phồng to bất thường, tốc độ lắng cực kỳ chậm chạp. Sau 30 phút lắng trong ống đong, lớp bùn chiếm hơn $60 - 80\%$ thể tích ống ($SV_{30} > 600 - 800\ mL/L$), chỉ số $SVI$ vọt lên $> 150 - 300\ mL/g$. Mặt chăn bùn trong bể lắng đợt 2 dâng sát máng tràn, gây thất thoát sinh khối ra nguồn tiếp nhận.

##### 7.1.2 Nguyên nhân vi sinh học và sinh thái học cạnh tranh (Filamentous Overgrowth)
- Bùn hoạt tính lý tưởng là sự cân bằng hài hòa giữa vi khuẩn tạo bông (floc-forming bacteria, chiếm $80 - 90\%$) đóng vai trò tạo khối thịt và vi khuẩn dạng sợi (filamentous bacteria, chiếm $10 - 20\%$) đóng vai trò cốt thép giằng giữ bông cặn.
- Sự cố bùn nở xảy ra khi các chủng vi khuẩn dạng sợi phát triển quá mức, mọc đâm tua tủa ra ngoài bề mặt bông bùn, tạo thành mạng lưới chông gai ngăn cản các bông bùn tiến lại gần nhau và cản trở nước thoát ra khi lắng (hiện tượng tạo cầu liên kết - filamentous bridging).

###### 7.1.2.1 Bùn nở do thiếu DO ($DO < 2.0\ mg/L$): Sphaerotilus natans, Type 1701, Haliscomenobacter
- Khi nồng độ oxy hòa tan trong bể aerotank sụt giảm dưới $1.0 - 1.5\ mg/L$, các vi khuẩn dạng sợi có tỷ số diện tích bề mặt trên thể tích lớn và hằng số nửa bão hòa oxy cực thấp ($K_o < 0.1\ mg/L$) như *Sphaerotilus natans*, *Type 1701*, *Haliscomenobacter hydrossis* sẽ lấy oxy nhanh hơn và sinh sôi lấn át vi khuẩn tạo bông.

###### 7.1.2.2 Bùn nở do tỷ số F/M thấp: Type 0041, Type 0675, Microthrix parvicella
- Trong các bể làm thoáng kéo dài hoặc CMAS vận hành ở $F/M < 0.15\ d^{-1}$, cơ chất hòa tan luôn ở nồng độ vết. Các chủng vi khuẩn sợi thích nghi môi trường nghèo kiệt cơ chất như *Microthrix parvicella*, *Eikelboom Type 0041*, *Type 0675*, *Type 0092* sẽ chiếm thế thượng phong.

###### 7.1.2.3 Bùn nở do thiếu hụt dinh dưỡng N, P hoặc độ pH thấp (< 6.5)
- Tỷ lệ dinh dưỡng chuẩn cho quá trình bùn hoạt tính hiếu khí là $BOD_5 : N : P = 100 : 5 : 1$. Khi thiếu nitơ hoặc phospho, vi khuẩn dạng sợi (như *Thiothrix*, *Type 021N*) có khả năng tích lũy dinh dưỡng cao hơn sẽ áp đảo, hoặc vi khuẩn tạo chất nhầy polysaccharide ngoại bào quá mức gây bùn nở dạng nhầy (zoogloeal bulking).
- Khi pH bể giảm xuống $< 6.5$ (do nitrat hóa làm cạn kiệt độ kiềm mà không bổ sung kịp), nấm sợi mốc (*Fungi*) và nấm men phát triển mạnh gây vỡ nát bông bùn.

###### 7.1.2.4 Bùn nở do dòng vào thối rữa và sunfua cao: Thiothrix, Beggiatoa, Type 021N
- Nước thải lưu lâu ngày trong mạng lưới cống sinh ra axit hữu cơ dễ bay hơi và hydro sunfua ($H_2S$). Các vi khuẩn oxy hóa lưu huỳnh dạng sợi như *Thiothrix spp.*, *Beggiatoa*, *Type 021N* phát triển mạnh và tích lũy các hạt lưu huỳnh khúc xạ ánh sáng bên trong tế bào.

##### 7.1.3 Biện pháp khắc phục kỹ thuật và điều khiển công nghệ

###### 7.1.3.1 Tăng cường oxy hòa tan, điều chỉnh tỷ số F/M và bổ sung dinh dưỡng
- Tăng công suất máy thổi khí, duy trì nồng độ DO trong bể nghiêm ngặt ở mức $\ge 2.0\ mg/L$ tại mọi vị trí.
- Điều chỉnh tuổi bùn $\theta_c$ và tăng lượng xả bùn WAS để đưa F/M về vùng tối ưu ($0.20 - 0.40\ d^{-1}$).
- Bổ sung chất dinh dưỡng (Urê, DAP hoặc Axit photphoric) nếu tỷ lệ $N, P$ thiếu hụt.

###### 7.1.3.2 Xây dựng bể tiếp xúc chọn lọc sinh học (Biological Selector - Aerobic, Anoxic, Anaerobic)
- **Nguyên lý căn cơ nhất:** Lắp đặt một bể tiếp xúc nhỏ (thời gian lưu $\text{HRT} = 15 - 30\ \text{phút}$) ở ngay đầu bể aerotank nạp chung nước thải và bùn tuần hoàn RAS:
  - Ngăn Selector thiếu khí (Anoxic Selector) hoặc kỵ khí (Anaerobic Selector): Vi khuẩn dạng sợi bị ức chế do không thể sử dụng nitrate hoặc không có khả năng tích lũy polyphosphate.
  - Ngăn Selector hiếu khí có gradient cao (Aerobic Selector): Tạo hiệu ứng Feast - Famine mạnh mẽ, vi khuẩn tạo bông hấp thụ tức thời cơ chất, triệt tiêu hoàn toàn vi khuẩn dạng sợi.

###### 7.1.3.3 Khử trùng có chọn lọc bùn tuần hoàn bằng clo hóa ($2 - 5\ kg\ Cl_2 / 1000\ kg\ MLSS\cdot d$) hoặc $H_2O_2$
- **Biện pháp cấp cứu khẩn cấp:** Châm dung dịch Clo ($NaOCl$ hoặc khí clo) vào đường ống bùn tuần hoàn RAS với liều lượng $2 - 5\ kg\ Cl_2$ cho mỗi $1,000\ kg\ MLSS$ xả qua mỗi ngày.
- Do vi khuẩn dạng sợi mọc chìa ra ngoài bề mặt bông bùn nên sẽ tiếp xúc trực tiếp và bị clo tiêu diệt trước tiên, trong khi vi khuẩn tạo bông nằm sâu bên trong lõi floc được bảo vệ an toàn. Dừng châm ngay khi SVI giảm xuống $< 120 - 150\ mL/g$.

#### 7.2 Sự cố tạo bọt nhớt (Sludge Foaming)

##### 7.2.1 Dấu hiệu nhận biết: Lớp váng bọt màu nâu sôcôla, dày, đặc, nhớt trên mặt bể
- Mặt bể aerotank và bể lắng đợt 2 bị bao phủ bởi một lớp bọt và váng nổi đặc quánh, màu nâu sôcôla, dai nhớt, có thể dày từ $0.1\ m$ đến hơn $0.5\ m$. Lớp bọt không bị phá vỡ bởi vòi phun nước thông thường, bốc mùi hôi thối do xác vi sinh phân hủy và gây mất mỹ quan nghiêm trọng.

##### 7.2.2 Vi sinh vật gây bọt: Xạ khuẩn Nocardia (Gordonia amarae) và Microthrix parvicella

###### 7.2.2.1 Cấu trúc thành tế bào chứa axit mycolic kỵ nước và cơ chế liên kết bọt khí ba pha
- **Sinh học:** Chủng vi sinh gây bọt phổ biến nhất là xạ khuẩn *Nocardioforms* (chủ đạo là *Gordonia amarae*, *Nocardia spp.*) và *Candidatus Microthrix parvicella*.
- **Cơ chế bọt ba pha (Gas-Liquid-Solid):** Thành tế bào của các vi khuẩn này chứa hàm lượng rất cao các hợp chất sáp lipid và axit mycolic phân tử lớn, tạo ra tính kỵ nước (hydrophobicity) cực mạnh. Khi sục khí, các sợi vi khuẩn này không chịu nằm trong nước mà di chuyển bám chặt vào bề mặt liên pha của các bọt khí nổi lên.
- Khi kết hợp với dầu mỡ, chất béo ($FOG$) và các chất hoạt động bề mặt trong nước thải, chúng liên kết lại thành một mạng lưới màng nhũ tương ba pha siêu bền vững, giữ chặt bọt khí không cho vỡ, hình thành khối bọt nổi khổng lồ trên mặt nước.

##### 7.2.3 Tác hại công nghệ và giải pháp xử lý

###### 7.2.3.1 Bẫy sinh khối mặt bể và vô hiệu hóa kiểm soát tuổi bùn từ đáy lắng
- Bọt nổi bẫy giữ một lượng lớn sinh khối vi sinh hoạt tính trên mặt bể. Do các nhà máy thường xả bùn dư WAS từ đáy bể lắng đợt 2, lượng vi khuẩn *Nocardia* nằm trên mặt bọt hoàn toàn không bị thải ra ngoài, khiến tuổi bùn thực tế của quần thể gây bọt bị kéo dài vô tận, làm vô hiệu hóa công thức tính tuổi bùn lý thuyết.

###### 7.2.3.2 Xả bùn chọn lọc trên bề mặt (Surface wasting), phun clo cục bộ ($50 - 100\ mg/L$) và kiểm soát FOG đầu vào
- **Xả bùn mặt (Surface Wasting):** Lắp đặt máng thu váng bọt chuyên dụng xả trực tiếp lớp bọt trên bề mặt bể aerotank vào hệ thống xử lý bùn.
- **Phun dung dịch Clo cục bộ:** Lắp dàn phun sương áp lực thấp phun dung dịch clo loãng ($50 - 100\ mg/L\ Cl_2$) trực tiếp lên bề mặt thảm bọt để tiêu diệt màng xạ khuẩn kỵ nước mà không làm ảnh hưởng đến khối vi sinh bên dưới lòng bể.
- **Kiểm soát nguồn FOG:** Nâng cao hiệu quả của bể tách mỡ, tuyển nổi DAF hoặc lắng đợt 1 để hạ hàm lượng dầu mỡ đầu vào xuống $< 25 - 50\ mg/L$. Giảm tuổi bùn $\theta_c < 5\ \text{ngày}$ nếu không yêu cầu nitrat hóa.

#### 7.3 Sự cố bùn nổi (Sludge Rising / Clumping)

##### 7.3.1 Cơ chế phản nitrat hóa trong bể lắng đợt 2 (Denitrification in Secondary Clarifier)

###### 7.3.1.1 Phân hủy nitrat thành khí nitơ ($N_2$) trong vùng bùn thiếu khí
- Khác hoàn toàn với bùn nở vi khuẩn sợi, sự cố bùn nổi xảy ra đối với loại bùn lắng rất tốt từ các bể hiếu khí có quá trình nitrat hóa cao ($NO_3^-$ đầu ra cao, $> 15 - 30\ mg/L$).
- Khi bùn lắng xuống đáy bể lắng đợt 2 và lưu lại quá lâu ($> 1.5 - 2.0\ h$), oxy hòa tan bị cạn kiệt ($DO \rightarrow 0$), tạo ra môi trường thiếu khí (anoxic). Các vi khuẩn dị dưỡng tùy tiện sử dụng nitrat làm chất nhận điện tử để oxy hóa chất hữu cơ nội sinh (quá trình phản nitrat hóa):
  $$2\text{NO}_3^- + 10\text{H}^+ + 10e^- \rightarrow \text{N}_2 \uparrow + 6\text{H}_2\text{O}$$

###### 7.3.1.2 Các bọt khí $N_2$ đính bám vào bông bùn làm giảm tỷ trọng và đẩy bùn nổi mảng lớn
- Khí nitơ ($N_2$) sinh ra có độ hòa tan rất kém trong nước. Các vi bọt khí $N_2$ bám dính vào mạng lưới bông bùn hoạt tính, làm tỷ trọng tổng hợp của khối bông bùn nhẹ hơn tỷ trọng của nước, kéo từng mảng bùn lớn (clumps) trồi ngược lên mặt bể lắng đợt 2.

##### 7.3.2 Phân biệt giữa bùn nở vi khuẩn sợi và bùn nổi khử nitrat
- **Kiểm tra trực quan và đo nghiệm nhanh:**
  - Bùn nở (Bulking): Đo $SVI > 150 - 200\ mL/g$, toàn bộ chăn bùn xốp phồng từ từ dâng lên, nước ranh giới mờ đục.
  - Bùn nổi (Rising): Đo nghiệm ống đong thấy bùn lắng rất nhanh và đặc trong $5 - 15\text{ phút}$ đầu ($SVI < 100\ mL/g$), nước phía trên rất trong; nhưng sau $30 - 60\text{ phút}$, xuất hiện các bọt khí nhỏ li ti sủi tăm và từng tảng bùn đáy bung lên mặt nước.

##### 7.3.3 Biện pháp kỹ thuật kiểm soát và ngăn chặn

###### 7.3.3.1 Tăng lưu lượng bùn tuần hoàn RAS, giảm thời gian lưu bùn đáy bể ($< 1.0 - 1.5\ h$)
- Tăng tốc độ bơm bùn tuần hoàn RAS để rút nhanh bùn ra khỏi đáy bể lắng đợt 2, khống chế thời gian lưu của lớp bùn lắng dưới đáy $< 1.0 - 1.5\ \text{giờ}$, không cho vi khuẩn đủ thời gian thiết lập phản ứng phản nitrat hóa.
- Tăng tốc độ quay của cầu cào bùn và vệ sinh các góc chết trong hố thu bùn.

###### 7.3.3.2 Tích hợp ngăn khử nitơ anoxic chuyên dụng ngược dòng (Quy trình MLE)
- Biện pháp triệt để lâu dài: Cải tạo dây chuyền công nghệ thành quy trình thiếu khí - hiếu khí kết hợp (Modified Ludzack-Ettinger - MLE) bằng cách bố trí bể Anoxic phía trước bể Aerotank kết hợp bơm tuần hoàn nội bộ dòng hỗn hợp bùn nước ($IR = 200 - 400\%$).
- Nitrate được chuyển hóa triệt để thành khí $N_2$ thoát ra ngay trong bể anoxic, đưa nồng độ nitrate nạp vào bể lắng đợt 2 xuống $< 5 - 8\ mg/L$, loại trừ hoàn toàn nguy cơ bùn nổi.

### 8. Ví dụ Tính toán Kỹ thuật Toàn diện Từng Bước (Comprehensive Worked Engineering Design Examples)

#### 8.1 Ví dụ 1: Tính toán Thiết kế Bể Bùn Hoạt tính Khuấy trộn Hoàn toàn (CMAS) Khử BOD Carbon

##### 8.1.1 Đề bài, thông số nước thải đầu vào và tiêu chuẩn xả thải
- **Đề bài:** Thiết kế bể bùn hoạt tính khuấy trộn hoàn toàn (CMAS) để xử lý nước thải sinh hoạt đô thị sau lắng đợt 1 với mục tiêu khử BOD carbon.
- **Thông số đầu vào:**
  - Lưu lượng nước thải: $Q = 22,700\ m^3/d$.
  - Tổng BOD đầu vào: $S_0 = 140\ g/m^3$ ($mg/L$).
  - BOD hòa tan đầu vào: $sS_0 = 70\ g/m^3$.
  - Cặn lơ lửng đầu vào: $TSS = 70\ g/m^3$ ($VSS = 60\ g/m^3$, $nbVSS = 20\ g/m^3$, $iTSS = 10\ g/m^3$).
  - Nitơ Kjeldahl tổng: $TKN = 35\ g/m^3$, Amoni: $NH_4^+-N = 25\ g/m^3$.
  - Nhiệt độ thiết kế mùa đông: $T = 12^\circ C$. Cao độ công trình: $z = 500\ m$.
- **Yêu cầu nước đầu ra:** $BOD_e \le 30\ g/m^3$, $TSS_e \le 15\ g/m^3$.
- **Thông số lựa chọn thiết kế:**
  - Tuổi bùn: $\theta_c = 5.0\ \text{ngày}$. Nồng độ MLSS thiết kế: $X_{TSS} = 3,000\ g/m^3$ ($3.0\ kg/m^3$).
  - Chiều sâu nước bể: $H = 4.9\ m$; độ sâu ngập đĩa phân phối khí: $D_f = 4.4\ m$.
  - Nồng độ DO duy trì: $C_L = 2.0\ mg/L$.
  - Hệ số sục khí: $\alpha = 0.50$, $\beta = 0.95$, $F = 0.90$.
- **Hệ số động học dị dưỡng ở $20^\circ C$:** $\mu_m = 6.0\ d^{-1}$, $K_s = 20\ g/m^3$, $Y = 0.40\ g\ VSS/g\ BOD_5$, $k_d = 0.12\ d^{-1}$, $f_d = 0.15$.

##### 8.1.2 Bước 1: Hiệu chỉnh hệ số động học theo nhiệt độ ($12^\circ C$)
- Hiệu chỉnh hệ số phân hủy nội sinh $k_d$:
  $$k_d(12^\circ C) = k_d(20^\circ C) \cdot 1.04^{12 - 20} = 0.12 \cdot 1.04^{-8} = 0.12 \cdot 0.7307 = 0.0877\ \text{d}^{-1}$$
- Hiệu chỉnh tốc độ tăng trưởng cực đại $\mu_m$:
  $$\mu_m(12^\circ C) = \mu_m(20^\circ C) \cdot 1.07^{12 - 20} = 6.0 \cdot 1.07^{-8} = 6.0 \cdot 0.5820 = 3.492\ \text{d}^{-1}$$

##### 8.1.3 Bước 2: Tính toán nồng độ cơ chất hòa tan đầu ra ($S$)
- Áp dụng công thức động học Monod cho bể CMAS:
  $$S = \frac{K_s (1 + k_d \theta_c)}{\theta_c (\mu_m - k_d) - 1} = \frac{20 \cdot (1 + 0.0877 \times 5.0)}{5.0 \cdot (3.492 - 0.0877) - 1} = \frac{20 \cdot (1.4385)}{5.0 \cdot (3.4043) - 1} = \frac{28.77}{16.02} = 1.796\ \text{g/m}^3 \approx 1.80\ \text{g/m}^3$$
- Hiệu suất khử sBOD: $E = \frac{70 - 1.80}{70} \times 100\% = 97.4\%$.

##### 8.1.4 Bước 3: Tính toán các thành phần sản lượng bùn sinh học ($P_{X,bio}, P_{X,d}, P_{X,nbVSS}, P_{X,iTSS}, P_{X,TSS}$)
- **Sản lượng sinh khối hoạt tính dị dưỡng ($P_{X,bio}$):**
  $$P_{X,bio} = \frac{Q \cdot Y \cdot (S_0 - S)}{1 + k_d \theta_c} \cdot 10^{-3} = \frac{22,700 \times 0.40 \times (140 - 1.80)}{1 + (0.0877 \times 5.0)} \times 10^{-3} = \frac{1,254,856}{1.4385 \times 1000} = 872.34\ \text{kg VSS/d}$$
- **Mảnh vụn tế bào nội sinh trơ ($P_{X,d}$):**
  $$P_{X,d} = f_d \cdot k_d \cdot \theta_c \cdot P_{X,bio} = 0.15 \times 0.0877 \times 5.0 \times 872.34 = 57.38\ \text{kg VSS/d}$$
- **Cặn hữu cơ không phân hủy sinh học từ nước đầu vào ($P_{X,nbVSS}$):**
  $$P_{X,nbVSS} = Q \cdot nbVSS \cdot 10^{-3} = 22,700 \times 20 \times 10^{-3} = 454.00\ \text{kg VSS/d}$$
- **Tổng sản lượng cặn lơ lửng bay hơi ($P_{X,VSS}$):**
  $$P_{X,VSS} = P_{X,bio} + P_{X,d} + P_{X,nbVSS} = 872.34 + 57.38 + 454.00 = 1,383.72\ \text{kg VSS/d}$$
- **Cặn trơ vô cơ từ nước đầu vào ($P_{X,iTSS}$):**
  $$P_{X,iTSS} = Q \cdot iTSS \cdot 10^{-3} = 22,700 \times 10 \times 10^{-3} = 227.00\ \text{kg TSS/d}$$
- **Tổng sản lượng bùn khô phát sinh hàng ngày ($P_{X,TSS}$):**
  $$P_{X,TSS} = P_{X,VSS} + P_{X,iTSS} = 1,383.72 + 227.00 = 1,610.72\ \text{kg TSS/d}$$
- Tỷ số $MLVSS/MLSS$ của hệ thống: $\frac{1,383.72}{1,610.72} = 0.859$ ($85.9\%$).

##### 8.1.5 Bước 4: Xác định thể tích bể ($V$), thời gian lưu nước (HRT) và diện tích bể
- Tổng khối lượng cặn lơ lửng cần duy trì trong bể:
  $$M_{\text{TSS}} = P_{X,TSS} \cdot \theta_c = 1,610.72 \times 5.0 = 8,053.6\ \text{kg TSS}$$
- Thể tích bể hiếu khí yêu cầu:
  $$V = \frac{M_{\text{TSS}}}{X_{TSS} \cdot 10^{-3}} = \frac{8,053.6}{3.0} = 2,684.53\ \text{m}^3 \approx 2,685\ \text{m}^3$$
- Thời gian lưu thủy lực (HRT, $\theta$):
  $$\theta = \frac{V}{Q} \cdot 24 = \frac{2,684.53}{22,700} \times 24 = 0.1183 \times 24 = 2.84\ \text{giờ}$$
- Diện tích mặt bằng bể ở chiều sâu $H = 4.9\ m$:
  $$A_{\text{tank}} = \frac{V}{H} = \frac{2,684.53}{4.9} = 547.86\ \text{m}^2$$
  - Chọn 2 đơn nguyên bể làm việc song song, mỗi bể có diện tích $274\ m^2$ ($L \times W = 16.55\ m \times 16.55\ m$).

##### 8.1.6 Bước 5: Kiểm tra các thông số tải trọng ($F/M$, OLR)
- Nồng độ MLVSS: $X_{VSS} = 3,000 \times 0.859 = 2,577\ g/m^3 = 2.577\ kg/m^3$.
- Tổng khối lượng MLVSS trong bể: $M_{VSS} = 2,684.53 \times 2.577 = 6,918.0\ kg\ VSS$.
- Tỷ số F/M:
  $$\text{F/M} = \frac{Q \cdot S_0}{V \cdot X_{VSS}} = \frac{22,700 \times 0.140}{6,918.0} = \frac{3,178.0}{6,918.0} = 0.459\ \frac{\text{kg BOD}_5}{\text{kg MLVSS}\cdot\text{d}}$$
  - Giá trị $0.459\ d^{-1}$ hoàn toàn nằm trong dải tối ưu của CMAS ($0.20 - 0.60\ d^{-1}$).
- Tải trọng thể tích hữu cơ (OLR):
  $$\text{OLR} = \frac{Q \cdot S_0}{V \cdot 10^3} = \frac{22,700 \times 140}{2,684.53 \times 1000} = 1.184\ \frac{\text{kg BOD}_5}{\text{m}^3\cdot\text{d}}$$

##### 8.1.7 Bước 6: Tính toán nhu cầu oxy thực tế ($OTR_f$) và nhu cầu oxy chuẩn (SOTR)
- **Nhu cầu oxy thực tế hàng ngày ($OTR_f$):**
  - Lấy tỷ số bCOD/BOD $= 1.60 \implies bCOD$ phân hủy: $1.60 \times (140 - 1.80) \times 22,700 \times 10^{-3} = 5,019.4\ kg/d$.
  - Lượng oxy thực tế tiêu hao:
    $$R_O = \Delta bCOD - 1.42 \cdot (P_{X,bio} + P_{X,d}) = 5,019.4 - 1.42 \times (872.34 + 57.38) = 5,019.4 - 1,320.2 = 3,699.2\ \text{kg O}_2/\text{d}$$
  - Tốc độ truyền oxy hiện trường: $OTR_f = \frac{3,699.2}{24} = 154.13\ kg\ O_2/h$.
- **Tính toán SOTR:**
  - Hệ số áp suất tại cao độ $500\ m$: $\Omega = \exp\left(-\frac{9.81 \times 28.97 \times 500}{8314 \times 285.15}\right) = 0.942$.
  - Nồng độ DO bão hòa ở $12^\circ C$ và $20^\circ C$ ở mực biển: $C_{st} = 10.77\ mg/L$, $C_{s,20}^* = 9.09\ mg/L$.
  - Hệ số bão hòa tại tâm ngập đĩa ($D_f = 4.4\ m$): $1 + \frac{4.4}{2 \times 10.33} = 1.213$.
  - Nồng độ bão hòa hiệu dụng: $C^*_{\infty,12} = 10.77 \times 1.213 \times 0.942 = 12.31\ mg/L$.
  - Mẫu số chuyển đổi hiệu chỉnh:
    $$\text{Correction} = \left[ \frac{\beta \cdot C^*_{\infty,12} - C_L}{C^*_{s,20}} \right] \cdot \theta^{T - 20} \cdot \alpha \cdot F$$
    $$\text{Correction} = \left[ \frac{0.95 \times 12.31 - 2.0}{9.09} \right] \cdot (1.024)^{-8} \cdot 0.50 \cdot 0.90 = \left[ \frac{9.69}{9.09} \right] \cdot 0.8266 \cdot 0.45 = 1.066 \times 0.8266 \times 0.45 = 0.3965$$
  - Nhu cầu truyền oxy chuẩn (SOTR):
    $$\text{SOTR} = \frac{\text{OTR}_f}{\text{Correction}} = \frac{154.13}{0.3965} = 388.73\ \text{kg O}_2/\text{h} = 9,329.5\ \text{kg O}_2/\text{d}$$

#### 8.2 Ví dụ 2: Tính toán Thiết kế Bể CMAS Kết hợp Khử BOD và Nitrat hóa Hoàn toàn

##### 8.2.1 Đề bài, yêu cầu chất lượng amoni đầu ra và điều kiện thiết kế
- Giữ nguyên toàn bộ dữ kiện nước thải của Ví dụ 1 ($Q = 22,700\ m^3/d$, $BOD = 140\ g/m^3$, $TKN = 35\ g/m^3$, $NH_4^+-N = 25\ g/m^3$, $T = 12^\circ C$, $z = 500\ m$, $H = 4.9\ m$, $D_f = 4.4\ m$).
- **Yêu cầu bổ sung:** Thực hiện nitrat hóa hoàn toàn đạt amoni đầu ra $N_e \le 0.50\ g/m^3$ ($mg/L$).
- Do tuổi bùn tăng cao, chất hoạt động bề mặt bị phân hủy triệt để nên hệ số $\alpha$ tăng từ $0.50$ lên $\alpha = 0.65$. Nồng độ MLSS duy trì $X_{TSS} = 3,000\ g/m^3$.

##### 8.2.2 Bước 1: Động học nitrat hóa tại $12^\circ C$ và hệ số suy giảm do DO
- Các hằng số nitrat hóa ở $12^\circ C$:
  $$\mu_{nm}(12^\circ C) = 0.75 \cdot 1.072^{-8} = 0.430\ d^{-1}$$
  $$b_n(12^\circ C) = 0.08 \cdot 1.040^{-8} = 0.058\ d^{-1}$$
  $$K_n(12^\circ C) = 0.50 \cdot 1.053^{-8} = 0.331\ g/m^3$$
- Hệ số giới hạn DO (với $K_o = 0.50\ mg/L$ và $C_L = 2.0\ mg/L$):
  $$\text{DO factor} = \frac{2.0}{0.50 + 2.0} = 0.80$$
- Tốc độ tăng trưởng riêng ròng của vi khuẩn nitrat hóa ở nước ra $N = 0.50\ mg/L$:
  $$\mu_n = 0.430 \cdot \left(\frac{0.50}{0.331 + 0.50}\right) \cdot 0.80 - 0.058 = 0.430 \cdot 0.6017 \cdot 0.80 - 0.058 = 0.207 - 0.058 = 0.149\ \text{d}^{-1}$$

##### 8.2.3 Bước 2: Xác định tuổi bùn tối thiểu $\theta_{c,\min}$ và lựa chọn tuổi bùn thiết kế $\theta_c = 21\ \text{ngày}$
- Tuổi bùn tối thiểu chống rửa trôi:
  $$\theta_{c,\min} = \frac{1}{\mu_n} = \frac{1}{0.149} = 6.71\ \text{ngày}$$
- Chọn hệ số an toàn thiết kế mùa đông $SF \approx 3.13$ để đảm bảo quá trình luôn ổn định:
  $$\theta_c = 3.13 \times 6.71 = 21.0\ \text{ngày}$$

##### 8.2.4 Bước 3: Tính toán sản lượng bùn tổng hợp và khối lượng cặn trong bể
- Tại tuổi bùn $\theta_c = 21.0\ \text{ngày}$, vi khuẩn bị phân hủy nội sinh sâu sắc hơn:
  $$1 + k_d \theta_c = 1 + (0.0877 \times 21.0) = 1 + 1.8417 = 2.8417$$
  $$P_{X,bio} = \frac{22,700 \times 0.40 \times 138.20}{2.8417 \times 1000} = 441.59\ \text{kg VSS/d}$$
  $$P_{X,d} = 0.15 \times 0.0877 \times 21.0 \times 441.59 = 122.02\ \text{kg VSS/d}$$
  $$P_{X,nbVSS} = 454.00\ \text{kg VSS/d}$$
  $$P_{X,VSS} = 441.59 + 122.02 + 454.00 + P_{X,\text{bio,nit}} \approx 1,504.4\ \text{kg VSS/d}$$
  $$P_{X,TSS} = 1,916.8\ \text{kg TSS/d}$$
- Tỷ lệ $MLVSS/MLSS = 1,504.4 / 1,916.8 = 0.785$ ($78.5\%$).
- Tổng khối lượng cặn lơ lửng MLSS trong bể:
  $$M_{\text{TSS}} = P_{X,TSS} \cdot \theta_c = 1,916.8 \times 21.0 = 40,252.8\ \text{kg MLSS} \approx 40,253\ \text{kg}$$

##### 8.2.5 Bước 4: Xác định thể tích bể ($V = 13,418\ m^3$) và thời gian lưu nước ($\text{HRT} = 14.2\ h$)
- Thể tích bể hiếu khí cần thiết:
  $$V = \frac{M_{\text{TSS}}}{X_{TSS} \cdot 10^{-3}} = \frac{40,253}{3.0} = 13,417.7\ \text{m}^3 \approx 13,418\ \text{m}^3$$
- Thời gian lưu thủy lực (HRT):
  $$\theta = \frac{13,418}{22,700} \times 24 = 14.19\ \text{giờ} \approx 14.2\ \text{giờ}$$
- **Đánh giá:** Thể tích bể tăng gấp $5.0$ lần ($13,418\ m^3$ so với $2,685\ m^3$) và HRT tăng từ $2.84\ h$ lên $14.2\ h$ khi nâng cấp từ khử BOD đơn thuần lên nitrat hóa hoàn toàn.

##### 8.2.6 Bước 5: Tính toán lượng nitơ oxi hóa ($NO_x$), nhu cầu oxy thực tế ($OTR_f = 6,282.1\ kg\ O_2/d$) và SOTR
- Lượng nitơ đồng hóa vào bùn thải: $0.12 \times 1,504.4 = 180.53\ kg\ N/d$ (tương đương $7.95\ g/m^3$).
- Nồng độ amoni bị oxy hóa thành nitrat:
  $$NO_x = TKN_0 - N_e - N_{\text{assimilated}} = 35.0 - 0.50 - 7.95 = 26.55\ \text{g/m}^3$$
  $$M_{NOx} = 22,700 \times 26.55 \times 10^{-3} = 602.69\ \text{kg N/d}$$
- Nhu cầu oxy hóa nitơ (NOD):
  $$\text{NOD} = 4.57 \times M_{NOx} = 4.57 \times 602.69 = 2,754.29\ \text{kg O}_2/\text{d}$$
- Nhu cầu oxy khử carbon (CBOD):
  $$\text{CBOD} = 5,019.4 - 1.42 \times (441.59 + 122.02 + 486.8) \approx 3,527.8\ \text{kg O}_2/\text{d}$$
- Tổng nhu cầu oxy thực tế hàng ngày:
  $$R_O = \text{CBOD} + \text{NOD} = 3,527.8 + 2,754.3 = 6,282.1\ \text{kg O}_2/\text{d}$$
  $$\text{OTR}_f = \frac{6,282.1}{24} = 261.75\ \text{kg O}_2/\text{h}$$
- Tính đổi ra SOTR với $\alpha = 0.65$:
  $$\text{Correction} = 1.066 \times 0.8266 \times (0.65 \times 0.90) = 1.066 \times 0.8266 \times 0.585 = 0.5155$$
  $$\text{SOTR} = \frac{261.75}{0.5155} = 507.76\ \text{kg O}_2/\text{h} = 12,186\ \text{kg O}_2/\text{d}$$

#### 8.3 Ví dụ 3: Tính toán Thiết kế Hệ thống Bể Phản ứng Sinh học Màng (MBR)

##### 8.3.1 Đề bài và các thông số công nghệ đầu vào ($Q = 22,700\ m^3/d$, $\text{SRT} = 21\ d$, $J = 16\ L/m^2\cdot h$, $R = 6$)
- Sử dụng cùng dữ kiện chất lượng nước và tải lượng sinh khối của Ví dụ 2 (đạt nitrat hóa hoàn toàn ở $12^\circ C$ với $\theta_c = 21\ \text{ngày}$):
  - Tổng khối lượng MLSS toàn hệ thống cần duy trì: $M_{\text{TSS}} = 40,253\ kg$.
  - Tổng sản lượng bùn: $P_{X,TSS} = 1,916.8\ kg/d$.
- **Thông số lựa chọn thiết kế MBR:**
  - Tỷ số hoàn lưu bùn bể màng về bể hiếu khí: $R = Q_R / Q = 6.0$.
  - Nồng độ MLSS thiết kế duy trì trong bể màng: $X_m = 12,000\ g/m^3$ ($12.0\ kg/m^3$).
  - Thông lượng màng thiết kế: $J = 16.0\ L/(m^2\cdot h) = 0.384\ m^3/(m^2\cdot d)$.
  - Tỷ số thể tích bể màng trên diện tích màng: $V_m / A_m = 0.025\ m^3/m^2$.

##### 8.3.2 Bước 1: Nồng độ bùn bể hiếu khí ($X_A$) từ cân bằng hoàn lưu bùn bể màng ($X_m = 12,000\ mg/L$)
- Thiết lập từ phương trình cân bằng sinh khối:
  $$X_A = \left( \frac{R}{1 + R} \right) \cdot X_m = \left( \frac{6}{1 + 6} \right) \times 12,000 = \frac{6}{7} \times 12,000 = 10,285.7\ \text{g/m}^3 \approx 10,286\ \text{g/m}^3$$

##### 8.3.3 Bước 2: Tính toán tổng diện tích bề mặt màng lọc ($A_m$)
- Lưu lượng nước trong thấm qua màng theo giờ:
  $$Q_h = \frac{22,700\ \text{m}^3/\text{d} \times 1,000\ \text{L/m}^3}{24\ \text{h/d}} = 945,833.3\ \text{L/h}$$
- Tổng diện tích màng yêu cầu:
  $$A_m = \frac{Q_h}{J} = \frac{945,833.3}{16.0} = 59,114.6\ \text{m}^2 \approx 59,115\ \text{m}^2$$

##### 8.3.4 Bước 3: Xác định thể tích ngăn màng ($V_m$) theo tỷ số đóng gói thể tích
- Thể tích ngăn màng:
  $$V_m = A_m \cdot \left(\frac{V_m}{A_m}\right) = 59,114.6 \times 0.025 = 1,477.87\ \text{m}^3 \approx 1,478\ \text{m}^3$$

##### 8.3.5 Bước 4: Phân bố khối lượng bùn giữa ngăn màng và ngăn hiếu khí
- Khối lượng MLSS chứa trong ngăn màng:
  $$M_m = V_m \cdot X_m \cdot 10^{-3} = 1,477.87 \times 12.0 = 17,734.4\ \text{kg MLSS}$$
- Khối lượng MLSS còn lại phải bố trí trong bể hiếu khí:
  $$M_A = M_{\text{TSS}} - M_m = 40,253.0 - 17,734.4 = 22,518.6\ \text{kg MLSS}$$

##### 8.3.6 Bước 5: Tính toán thể tích ngăn hiếu khí ($V_A$), tổng thể tích hệ thống và mức độ giảm mặt bằng ($72.7\%$)
- Thể tích ngăn hiếu khí:
  $$V_A = \frac{M_A}{X_A \cdot 10^{-3}} = \frac{22,518.6}{10.2857} = 2,189.31\ \text{m}^3 \approx 2,189\ \text{m}^3$$
- Tổng thể tích toàn hệ sinh học MBR:
  $$V_{\text{total}} = V_A + V_m = 2,189.3 + 1,477.9 = 3,667.2\ \text{m}^3 \approx 3,667\ \text{m}^3$$
- Thời gian lưu thủy lực tổng thể:
  $$\theta = \frac{3,667.2}{22,700} \times 24 = 3.88\ \text{giờ}$$
- **So sánh mức độ tiết kiệm thể tích xây dựng:**
  $$\text{Mức giảm thể tích} = \frac{13,418 - 3,667}{13,418} \times 100\% = 72.67\% \approx 72.7\%$$
  - Ngoài ra hệ thống hoàn toàn không cần bể lắng đợt 2 (tiết kiệm thêm hàng ngàn mét vuông đất xây dựng).

##### 8.3.7 Bước 6: Tính toán lưu lượng bơm bùn hoàn lưu ($Q_R = 136,200\ m^3/d$)
- Lưu lượng bơm bùn hoàn lưu từ bể màng về bể hiếu khí:
  $$Q_R = R \cdot Q = 6.0 \times 22,700 = 136,200\ \text{m}^3/\text{d} = 5,675\ \text{m}^3/\text{h}$$

#### 8.4 Ví dụ 4: Tính toán Thiết kế Bể Phản ứng Gián đoạn theo Mẻ (SBR) Khử BOD và Nitơ

##### 8.4.1 Đề bài và điều kiện vận hành ($Q = 7,570\ m^3/d$, 2 bể, chu kỳ $6\ h$, $SVI = 150\ mL/g$)
- **Đề bài:** Thiết kế hệ thống SBR xử lý nước thải sinh hoạt đô thị đạt khử BOD và amoni.
- **Thông số thiết kế:**
  - Lưu lượng nước thải: $Q = 7,570\ m^3/d$.
  - Số lượng bể song song: $N = 2\ \text{bể}$.
  - Thời gian một chu kỳ: $T_C = 6.0\ \text{giờ/chu kỳ}$ ($n_c = 24 / 6 = 4\ \text{chu kỳ/ngày/bể}$, tổng cộng 8 mẻ/ngày).
  - Phân bổ pha trong chu kỳ: Nạp nước ($t_F = 3.0\ h$), Phản ứng sục khí ($t_R = 2.0\ h$), Lắng tĩnh ($t_S = 0.5\ h$), Tháo nước trong ($t_D = 0.5\ h$).
  - Nồng độ MLSS tại mực nước đầy bể ($V_T$): $X_{\text{full}} = 3,500\ g/m^3$.
  - Chỉ số thể tích bùn thiết kế: $SVI = 150\ mL/g$. Nhiệt độ: $T = 12^\circ C$. Chiều sâu nước đầy: $H_{\text{full}} = 6.0\ m$.
  - Tỷ số tháo nước: $\alpha_D = V_F / V_T = 0.20$ ($20\%\ H$).

##### 8.4.2 Bước 1: Phân chia chu kỳ hoạt động và tính toán thể tích nạp mẻ ($V_F$)
- Thể tích nước thải nạp vào mỗi bể trong một chu kỳ:
  $$V_F = \frac{Q}{N \cdot n_c} = \frac{7,570}{2 \times 4} = 946.25\ \text{m}^3/\text{mẻ}$$

##### 8.4.3 Bước 2: Xác định tỷ lệ thể tích bùn lắng $F(V_T)$ và kiểm tra vùng nước trong an toàn
- Tỷ lệ thể tích bể bị chiếm giữ bởi lớp bùn sau lắng:
  $$F(V_T) = \frac{\text{MLSS} \cdot \text{SVI}}{10^6} = \frac{3,500 \times 150}{10^6} = 0.525\ (52.5\%)$$
- Tổng tỷ lệ thể tích bị chiếm giữ bởi bùn lắng và nước tháo:
  $$\text{Tổng chiếm giữ} = F(V_T) + \alpha_D = 0.525 + 0.20 = 0.725\ (72.5\%)$$
- Tỷ lệ vùng đệm nước trong dự phòng an toàn:
  $$\text{Buffer} = 1.0 - 0.725 = 0.275\ (27.5\%)$$
  - Chiều sâu đệm an toàn: $0.275 \times 6.0\ m = 1.65\ m > 1.0\ m \implies$ Đạt độ an toàn tuyệt đối chống hút bùn vào máng decanter.

##### 8.4.4 Bước 3: Tính toán thể tích tổng một bể ($V_T$), tổng thể tích công trình và kích thước hình học mặt bằng
- Thể tích công tác tối đa của một bể SBR:
  $$V_T = \frac{V_F}{\alpha_D} = \frac{946.25}{0.20} = 4,731.25\ \text{m}^3/\text{bể}$$
- Tổng thể tích 2 bể SBR:
  $$V_{\text{total}} = 2 \times 4,731.25 = 9,462.5\ \text{m}^3$$
- Diện tích mặt bằng một bể (ở chiều sâu nước đầy $H_{\text{full}} = 6.0\ m$):
  $$A_{\text{tank}} = \frac{V_T}{H_{\text{full}}} = \frac{4,731.25}{6.0} = 788.54\ \text{m}^2$$
- Thiết kế bể hình vuông:
  $$L = W = \sqrt{788.54} = 28.08\ \text{m} \approx 28.1\ \text{m}$$
- Chiều cao xây dựng thành bể (với chiều cao bảo vệ $h_b = 0.5\ m$): $H_{\text{wall}} = 6.0 + 0.5 = 6.5\ m$.

##### 8.4.5 Bước 4: Kiểm tra cao trình mực nước cao nhất, mức nước thấp nhất và nồng độ bùn sau gạt ($X_{\text{low}}$)
- Chiều sâu tháo nước: $H_{\text{decant}} = 0.20 \times 6.0 = 1.20\ m$.
- Mực nước thấp nhất sau khi xả (Low Water Level - LWL): $H_{\text{low}} = 6.0 - 1.20 = 4.80\ m$.
- Thể tích nước còn lại trong bể (Heel volume): $V_{\text{low}} = 4,731.25 - 946.25 = 3,785.0\ m^3$.
- Nồng độ MLSS trong bể tại mực nước thấp nhất:
  $$X_{\text{low}} = X_{\text{full}} \cdot \left(\frac{V_T}{V_{\text{low}}}\right) = 3,500 \times \left(\frac{4,731.25}{3,785.0}\right) = 4,375\ \text{g/m}^3 = 4.375\ \text{kg/m}^3$$

##### 8.4.6 Bước 5: Xác định thời gian lưu thủy lực toàn hệ thống ($\text{HRT} = 30.0\ h$)
- Thời gian lưu thủy lực tổng thể:
  $$\theta = \frac{V_{\text{total}}}{Q} \cdot 24 = \frac{9,462.5}{7,570} \times 24 = 1.25\ \text{ngày} = 30.0\ \text{giờ}$$
- Công suất xả nước của thiết bị gạt nước trong (Decanter capacity) trong pha tháo nước $0.5\ h$:
  $$Q_{\text{decanter}} = \frac{946.25\ \text{m}^3}{0.5\ \text{h}} = 1,892.5\ \text{m}^3/\text{h} = 525.7\ \text{L/s}$$

#### 8.5 Ví dụ 5: Tính toán Thiết kế Bể Lắng Đợt 2 theo Phương pháp Tải trọng Thủy lực và Thông lượng Cặn (Solids Flux)

##### 8.5.1 Dữ liệu thiết kế: Lưu lượng nước thải, MLSS, tỷ số tuần hoàn R, thông số lắng Vesilind
- **Dữ liệu đầu vào:**
  - Lưu lượng xử lý trung bình: $Q = 22,700\ m^3/d = 945.83\ m^3/h$.
  - Nồng độ bùn hoạt tính từ bể aerotank: $X = 3,000\ mg/L = 3.0\ kg/m^3$.
  - Tỷ số tuần hoàn bùn: $R = 0.60 \implies Q_r = 0.60 \times 22,700 = 13,620\ m^3/d = 567.5\ m^3/h$.
  - Lưu lượng xả bùn dư: $Q_w = 270\ m^3/d = 11.25\ m^3/h$.
  - Nồng độ bùn tuần hoàn mong muốn: $X_r = 8,000\ mg/L = 8.0\ kg/m^3$.
  - Hằng số phương trình vận tốc lắng Vesilind ($v_i = v_0 e^{-k_v X}$): $v_0 = 9.5\ m/h$, $k_v = 0.38\ m^3/kg$.
- **Tiêu chuẩn thiết kế:** Tải trọng thủy lực $\text{SOR} = 22\ m^3/(m^2\cdot d)$; Tải trọng cặn giới hạn $\text{SLR} \le 5.0\ kg/(m^2\cdot h)$.

##### 8.5.2 Bước 1: Tính toán diện tích bể lắng theo tải trọng thủy lực bề mặt (SOR)
- Diện tích bể lắng yêu cầu theo điều kiện thủy lực:
  $$A_{\text{hydraulic}} = \frac{Q}{\text{SOR}} = \frac{22,700\ \text{m}^3/\text{d}}{22\ \text{m}^3/(\text{m}^2\cdot\text{d})} = 1,031.8\ \text{m}^2$$

##### 8.5.3 Bước 2: Xác định thông lượng cặn giới hạn $G_L$ và diện tích bể lắng theo tải trọng cặn (SLR)
- Vận tốc rút bùn đáy bể ($u$) tương ứng diện tích giả định $A \approx 1,050\ m^2$:
  $$u = \frac{Q_r + Q_w}{A} = \frac{567.5 + 11.25}{1,050} = \frac{578.75}{1,050} = 0.551\ \text{m/h}$$
- Khảo sát hàm thông lượng tổng $G_t(X) = X \cdot v_0 e^{-k_v X} + X \cdot u$:
  - Tìm điểm cực tiểu bằng cách giải phương trình đạo hàm: $\frac{dG_t}{dX} = v_0 e^{-k_v X} (1 - k_v X) + u = 0$.
  - Với $v_0 = 9.5, k_v = 0.38, u = 0.551$, nồng độ giới hạn tại điểm thắt: $X_L \approx 4.85\ kg/m^3$.
  - Thông lượng lắng trọng lực tại $X_L$: $G_g = 4.85 \times 9.5 \times e^{-0.38 \times 4.85} = 46.075 \times 0.1583 = 7.29\ kg/(m^2\cdot h)$.
  - Thông lượng rút bùn tại $X_L$: $G_u = 4.85 \times 0.551 = 2.67\ kg/(m^2\cdot h)$.
  - Thông lượng giới hạn cực tiểu: $G_L = 4.35\ kg/(m^2\cdot h)$ (hoặc chọn theo tiêu chuẩn an toàn $G_L = 4.5\ kg/(m^2\cdot h)$).
- Tổng lượng cặn đưa vào bể lắng hàng giờ:
  $$\text{Tổng tải lượng cặn} = (Q + Q_r) \cdot X = (945.83 + 567.5) \times 3.0 = 1,513.33 \times 3.0 = 4,540.0\ \text{kg TSS/h}$$
- Diện tích bể lắng yêu cầu theo tải trọng cặn:
  $$A_{\text{solids}} = \frac{4,540.0\ \text{kg/h}}{4.35\ \text{kg}/(\text{m}^2\cdot\text{h})} = 1,043.68\ \text{m}^2$$

##### 8.5.4 Bước 3: Lựa chọn diện tích thiết kế an toàn, đường kính bể lắng tròn và chiều sâu làm việc tổng thể
- Chọn diện tích thiết kế là giá trị lớn nhất: $A = \max(1,031.8; 1,043.7) = 1,044\ m^2$.
- Phân chia thành $N = 2\ \text{bể lắng hình tròn}$ làm việc song song:
  $$A_{\text{per tank}} = \frac{1,044}{2} = 522\ \text{m}^2$$
- Đường kính mỗi bể lắng:
  $$D = \sqrt{\frac{4 \cdot A_{\text{per tank}}}{\pi}} = \sqrt{\frac{4 \times 522}{3.14159}} = \sqrt{664.63} = 25.78\ \text{m} \implies \text{Chọn } D = 26.0\ \text{m}$$
- Diện tích thực tế mỗi bể: $A_{\text{actual}} = \frac{\pi \times 26^2}{4} = 530.9\ m^2$ (Tổng diện tích 2 bể $= 1,061.8\ m^2$).
- **Xác định chiều sâu thành bên của bể ($SWD$):**
  - Vùng nước trong bề mặt: $h_1 = 0.60\ m$.
  - Vùng lắng cản trở: $h_2 = 1.20\ m$.
  - Vùng trữ bùn: $h_3 = 1.20\ m$.
  - Vùng gạt cặn và nén bùn đáy: $h_4 = 1.00\ m$.
  - Tổng chiều sâu nước công tác: $SWD = 0.60 + 1.20 + 1.20 + 1.00 = 4.00\ m$. Chiều cao bảo vệ: $h_b = 0.50\ m$.

##### 8.5.5 Bước 4: Thiết kế máng thu nước trong và kiểm tra tải trọng máng tràn (WOR)
- Bố trí máng thu nước chu vi chạy dọc theo mép trong thành bể tròn đường kính $D = 26.0\ m$:
  $$L_{\text{weir}} = \pi \cdot D = 3.14159 \times 26.0 = 81.68\ \text{m/bể}$$
- Tải trọng tràn máng của mỗi bể ở lưu lượng thiết kế trung bình ($Q_{\text{tank}} = 22,700 / 2 = 11,350\ m^3/d$):
  $$\text{WOR} = \frac{Q_{\text{tank}}}{L_{\text{weir}}} = \frac{11,350}{81.68} = 138.96\ \frac{\text{m}^3}{\text{m}\cdot\text{d}}$$
  - Kiểm tra tiêu chuẩn: $138.96\ m^3/(m\cdot d)$ nằm hoàn toàn trong phạm vi an toàn ($125 - 250\ m^3/(m\cdot d)$), thỏa mãn điều kiện thiết kế máng răng cưa.

#### 8.6 Ví dụ 6: Tính toán Công suất Máy Thổi Khí Nén Đoạn Nhiệt Cấp Khí Cho Hệ Thống Bọt Mịn

##### 8.6.1 Dữ liệu thiết kế: SOTR, độ sâu đĩa, tổn thất áp lực hệ thống, nhiệt độ không khí đầu vào
- **Dữ liệu từ Ví dụ 2 (Bể CMAS có nitrat hóa):**
  - Nhu cầu truyền oxy tiêu chuẩn: $\text{SOTR} = 507.76\ kg\ O_2/h$.
  - Hiệu suất truyền oxy chuẩn của đĩa bọt mịn: $E = \text{SOTE} = 32.0\% = 0.32$.
  - Độ sâu đặt đĩa khuếch tán: $D_f = 4.4\ m$.
  - Áp suất khí quyển tại cao độ $500\ m$: $p_1 = 95.5\ kPa$.
  - Nhiệt độ không khí mùa hè tối đa tại cửa hút máy thổi: $T_1 = 35^\circ C = 308.15\ K$.
  - Tổn thất áp lực qua màng đĩa bọt mịn: $\Delta p_{\text{đĩa}} = 3.8\ kPa$.
  - Tổn thất áp lực ma sát và van trên đường ống dẫn khí: $\Delta p_{\text{ống}} = 4.5\ kPa$.
  - Hiệu suất tổng hợp của máy thổi khí và động cơ: $e = 0.75$.

##### 8.6.2 Bước 1: Tính toán lưu lượng thể tích không khí chuẩn ($Q_{\text{air}}$)
- Lưu lượng không khí chuẩn cần cung cấp theo giờ:
  $$Q_{\text{air,h}} = \frac{\text{SOTR}}{E \cdot 0.279} = \frac{507.76}{0.32 \times 0.279} = \frac{507.76}{0.08928} = 5,687.28\ \text{m}^3/\text{h}$$
- Lưu lượng thể tích không khí tính theo phút:
  $$Q_{\text{air,min}} = \frac{5,687.28}{60} = 94.79\ \text{m}^3/\text{min}$$
- Lưu lượng khối lượng của dòng khí ($w$):
  $$w = \frac{5,687.28\ \text{m}^3/\text{h} \times 1.204\ \text{kg/m}^3}{3600\ \text{s/h}} = \frac{6,847.49}{3600} = 1.902\ \text{kg/s}$$

##### 8.6.3 Bước 2: Tính toán áp suất tuyệt đối tại đầu xả máy thổi khí ($p_2$)
- Áp lực thủy tĩnh của cột nước trên mặt đĩa khí:
  $$\Delta p_{\text{tĩnh}} = \rho_w \cdot g \cdot D_f \cdot 10^{-3} = 1000 \times 9.81 \times 4.4 \times 10^{-3} = 43.16\ \text{kPa}$$
- Tổng áp suất tuyệt đối tại cửa xả máy thổi khí ($p_2$):
  $$p_2 = p_1 + \Delta p_{\text{tĩnh}} + \Delta p_{\text{đĩa}} + \Delta p_{\text{ống}} = 95.5 + 43.16 + 3.8 + 4.5 = 146.96\ \text{kPa}$$
- Tỷ số nén của máy thổi khí:
  $$\frac{p_2}{p_1} = \frac{146.96}{95.5} = 1.5388$$

##### 8.6.4 Bước 3: Tính toán công suất điện tiêu thụ đoạn nhiệt ($P_w$) và lựa chọn động cơ
- Áp dụng phương trình nhiệt động lực học nén đoạn nhiệt:
  $$P_w = \frac{w \cdot R \cdot T_1}{29.7 \cdot n \cdot e} \left[ \left(\frac{p_2}{p_1}\right)^{0.283} - 1 \right]$$
  - Với hằng số không khí $R = 8.314 / 28.97 = 0.287\ kJ/(kg\cdot K)$:
  - Tử số: $w \cdot R \cdot T_1 = 1.902 \times 0.287 \times 308.15 = 168.21\ kW\cdot s$.
  - Mẫu số quy đổi: $n \cdot e = 0.283 \times 0.75 = 0.21225$.
  - Số hạng áp suất nén đoạn nhiệt:
    $$\left(\frac{p_2}{p_1}\right)^{0.283} - 1 = (1.5388)^{0.283} - 1 = 1.1299 - 1 = 0.1299$$
- Công thức kỹ thuật nén đoạn nhiệt tiêu chuẩn ($P_w = \frac{w R T_1}{(k-1)/k \cdot e} [ (p_2/p_1)^{(k-1)/k} - 1 ]$):
  $$P_w = \frac{1.902 \times 0.287 \times 308.15}{0.283 \times 0.75} \times 0.1299 = \frac{168.21}{0.21225} \times 0.1299 = 792.51 \times 0.1299 = 102.95\ \text{kW}$$
- **Lựa chọn máy thổi khí:**
  - Thiết kế lắp đặt cụm 3 máy thổi khí (2 máy vận hành + 1 máy dự phòng $100\%$).
  - Công suất mỗi máy khi chạy 2 máy song song: $P_{\text{unit}} = \frac{102.95}{2} = 51.48\ kW$.
  - Chọn động cơ tiêu chuẩn công nghiệp: $P_{\text{motor}} = 55.0\ kW$ (hoặc $75\ hp$) cho mỗi máy thổi khí ly tâm nhiều cấp.
