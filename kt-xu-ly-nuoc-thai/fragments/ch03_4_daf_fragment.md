## Chương 03.4: Tuyển nổi Khí hòa tan (Dissolved Air Flotation - DAF)

### 1. Tổng quan và Nguyên lý Vận hành Hệ thống DAF (Overview & Operating Principles)

#### 1.1. Bản chất Vật lý và Cơ chế Tuyển nổi (Physical Nature & Flotation Fundamentals)

##### 1.1.1. So sánh Quá trình Tuyển nổi (Flotation) với Lắng Trọng lực (Gravity Sedimentation)
- **Bản chất động lực học phân tách pha:**
  - *Lắng trọng lực (Sedimentation):* Dựa vào chênh lệch khối lượng riêng tự nhiên dương ($\rho_p > \rho_w$) giữa hạt rắn lơ lửng và môi trường chất lỏng, hạt chuyển động đi xuống đáy bể dưới tác dụng của trọng lực với gia tốc trọng trường $g = 9.81\ \text{m/s}^2$.
  - *Tuyển nổi (Flotation):* Cưỡng bức tạo ra chênh lệch khối lượng riêng âm ($\rho_{\text{eff}} < \rho_w$) bằng cách cho các bọt khí siêu mịn (microbubbles) bám dính vào hạt cặn, tạo thành hệ liên hợp hạt - bọt khí (bubble-particle agglomerate) có khối lượng riêng biểu kiến nhỏ hơn khối lượng riêng của nước, tạo lực đẩy Archimedes làm hệ hạt nổi lên bề mặt chất lỏng.
- **Vận tốc phân tách pha và định luật Stokes mở rộng:**
  - Vận tốc lắng của hạt đơn lẻ theo Stokes:
    $$v_s = \frac{g (\rho_p - \rho_w) d_p^2}{18 \mu_w}$$
  - Vận tốc nổi của tổ hợp hạt - vi bọt khí theo Stokes mở rộng:
    $$v_f = \frac{g (\rho_w - \rho_{\text{eff}}) d_{\text{agg}}^2}{18 \mu_w}$$
    - Trong đó:
      - $v_f$: Vận tốc nổi của tổ hợp hạt cặn - vi bọt ($\text{m/s}$ hoặc $\text{cm/min}$).
      - $\rho_w$: Khối lượng riêng của nước thải ($\approx 1000\ \text{kg/m}^3$).
      - $\rho_{\text{eff}}$: Khối lượng riêng hiệu dụng của tổ hợp hạt cặn và vi bọt ($\text{kg/m}^3$, với $\rho_{\text{eff}} \ll \rho_w$).
      - $d_{\text{agg}}$: Đường kính tương đương của tổ hợp hạt cặn - vi bọt ($\text{m}$).
      - $\mu_w$: Độ nhớt động lực học của nước thải ($\approx 1.002 \times 10^{-3}\ \text{N}\cdot\text{s/m}^2$ ở $20^\circ\text{C}$).
- **So sánh các chỉ tiêu kỹ thuật chính giữa Tuyển nổi DAF và Lắng trọng lực:**
  - *Thời gian lưu thủy lực (Hydraulic Retention Time - HRT):* DAF đạt hiệu quả cao chỉ trong $\theta_{\text{tank}} = 20 - 30\ \text{phút}$ (đối với bể nông cao tải Krofta chỉ $3 - 5\ \text{phút}$), trong khi bể lắng trọng lực cần $2.0 - 4.0\ \text{giờ}$.
  - *Vận tốc phân tách:* Vận tốc nổi của bông cặn bám khí $v_f = 2.56 - 12.7\ \text{cm/min}$ ($1.54 - 7.62\ \text{m/h}$), cao gấp $2 - 5$ lần vận tốc lắng thông thường của bông keo tụ hữu cơ.
  - *Diện tích xây dựng (Footprint):* Bể DAF giảm diện tích mặt bằng từ $60 - 80\%$ so với bể lắng cơ học có cùng công suất xử lý.
  - *Độ ẩm bùn thải thu hồi:* Bùn nổi DAF có hàm lượng chất rắn tổng cộng $TS = 2.0 - 5.0\%$ (khi dùng gạt cơ học), đặc hơn đáng kể so với bùn lắng sơ cấp ($TS \approx 1.0 - 2.0\%$) và bùn hoạt tính thứ cấp ($TS \approx 0.5 - 1.0\%$).
  - *Khả năng xử lý chất khó lắng:* Tuyệt đối vượt trội đối với hạt keo nhẹ, dầu mỡ, nhũ tương FOGs (Fats, Oils, and Grease), tảo lục, vi sinh vật dạng sợi (filamentous bacteria) gây phồng bùn (sludge bulking) mà bể lắng không thể tách được.

##### 1.1.2. Định luật Henry về Hòa tan Khí và Động học Bão hòa (Henry's Law & Gas Dissolution)
- **Cơ sở nhiệt động học của sự hòa tan khí trong chất lỏng:**
  - Khả năng hòa tan của không khí vào nước tỷ lệ thuận với áp suất riêng phần của khối khí tiếp xúc trực tiếp với bề mặt chất lỏng ở điều kiện cân bằng nhiệt động.

###### 1.1.2.1. Phương trình Định luật Henry và Hệ số Hòa tan Không khí
- **Công thức định luật Henry tổng quát:**
  $$C_s = K_H \cdot P$$
  - Trong đó:
    - $C_s$: Nồng độ bão hòa của khí hòa tan trong pha lỏng tại trạng thái cân bằng ($\text{mg/L}$ hoặc $\text{mL/L}$).
    - $K_H$: Hằng số Henry phụ thuộc vào bản chất chất khí, nhiệt độ và nồng độ muối hòa tan trong nước ($\text{mg}/(\text{L}\cdot\text{atm})$).
    - $P$: Áp suất tuyệt đối của chất khí trên bề mặt chất lỏng ($\text{atm}$).
- **Độ hòa tan của không khí trong nước ($s_a$) ở áp suất khí quyển $1.0\ \text{atm}$:**
  - Độ hòa tan không khí giảm khi nhiệt độ nước tăng lên:
    - Tại $T = 0^\circ\text{C}$: $s_a = 29.2\ \text{mL/L}$.
    - Tại $T = 10^\circ\text{C}$: $s_a = 22.8\ \text{mL/L}$.
    - Tại $T = 20^\circ\text{C}$: $s_a = 18.7\ \text{mL/L}$.
    - Tại $T = 25^\circ\text{C}$: $s_a = 17.1\ \text{mL/L}$.
    - Tại $T = 30^\circ\text{C}$: $s_a = 15.7\ \text{mL/L}$.
- **Hệ số chuyển đổi khối lượng riêng không khí:**
  - Khối lượng riêng không khí khô ở điều kiện tiêu chuẩn ($0^\circ\text{C}, 1\ \text{atm}$): $\rho_{\text{air}} \approx 1.293\ \text{g/L} \approx 1.3\ \text{mg/mL}$.
  - Do đó, $1.3 \times s_a$ biểu thị khối lượng không khí bão hòa tối đa tính bằng $\text{mg air / L water}$ tại áp suất khí quyển.

###### 1.1.2.2. Hiệu suất Hòa tan Bão hòa Thực tế (Saturation Efficiency - f)
- **Định nghĩa hệ số $f$:**
  $$f = \frac{C_{\text{thực tế}}}{C_{\text{lý thuyết}}}$$
  - $f$ là tỷ lệ bão hòa thực tế đạt được bên trong bình áp lực so với mức bão hòa nhiệt động lý thuyết của định luật Henry.
- **Các yếu tố ảnh hưởng trực tiếp đến hệ số $f$:**
  - *Loại bình bão hòa (Saturator Type):*
    - Bình áp lực có lớp vật liệu đệm tiếp xúc (packed vessel): $f = 0.85 - 0.95$ (trong tính toán lý thuyết bài giảng thường lấy giá trị bảo thủ $f = 0.5$ đến $0.8$).
    - Bình phun sương không đệm (unpacked spray saturator): $f = 0.50 - 0.70$.
    - Ống nạp khí ejector trên đường ống hút của bơm nén: $f = 0.40 - 0.60$.
  - *Thời gian lưu tiếp xúc pha trong bình áp lực ($\theta_{pv}$):* Thiết kế tiêu chuẩn $\theta_{pv} = 1.0 - 3.0\ \text{phút}$ để đạt độ hòa tan mong muốn.
  - *Chiều cao lớp vật liệu đệm ($h_{\text{pack}}$):* Chiều cao tối ưu $h_{\text{pack}} = 1.0 - 1.5\ \text{m}$ sử dụng đệm vòng Raschig, đệm Pall ring hoặc đệm vi sinh ngẫu nhiên bằng nhựa polypropylene nhằm tạo diện tích tiếp xúc riêng $a = 100 - 250\ \text{m}^2/\text{m}^3$.

#### 1.2. Động thái Hạt vi bọt và Cơ chế Tiếp xúc (Microbubble Dynamics & Attachment Mechanics)

##### 1.2.1. Động thái Tạo bọt và Phân bố Kích thước Vi bọt (Bubble Nucleation & Size Spectrum)
- **Hiện tượng siêu bão hòa và tạo mầm bọt khí:**
  - Nước bão hòa khí ở áp suất cao ($3.4 - 5.0\ \text{atm}$) khi đi qua van giảm áp (pressure letdown valve / needle valve) chịu sự giảm áp suất đột ngột xuống áp suất khí quyển ($1.0\ \text{atm}$) trong thời gian cực ngắn tính bằng mili giây ($< 50\ \text{ms}$).
  - Gradient áp suất cục bộ cực lớn ($dP/dt > 10^5\ \text{atm/s}$) dẫn đến trạng thái siêu bão hòa mãnh liệt, năng lượng tự do Gibbs của hệ tăng vọt, kích thích quá trình tạo mầm đồng thể (homogeneous nucleation) và dị thể (heterogeneous nucleation).
- **Phân bố kích thước vi bọt khí (Bubble Diameter - $d_b$):**
  - Dải đường kính bọt khí hình thành trong DAF: $d_b = 10 - 100\ \mu m$.
  - Đường kính trung bình tối ưu đạt hiệu suất bám dính cao nhất: $d_{b,\text{mean}} = 30 - 60\ \mu m$.
  - *Lý do không dùng bọt khí thô ($> 1\ \text{mm}$ như trong sục khí xử lý sinh học):*
    - Bọt thô nổi quá nhanh ($v_b > 20\ \text{cm/s}$) gây xáo trộn mạnh, phá vỡ cấu trúc bông cặn keo tụ nhạy cảm.
    - Diện tích bề mặt tiếp xúc riêng trên một đơn vị thể tích khí của bọt thô rất nhỏ:
      $$S_v = \frac{6}{d_b}$$
      (Khi đường kính $d_b$ giảm $100$ lần từ $5\ \text{mm}$ xuống $50\ \mu m$, tổng diện tích liên kết pha khí - lỏng tăng lên $100$ lần với cùng một thể tích khí cấp vào).

##### 1.2.2. Các Cơ chế Tiếp xúc và Bám dính Hạt - Vi bọt (Bubble-Particle Attachment Mechanisms)
- Quá trình phân tách pha trong bể DAF xảy ra thông qua 3 cơ chế hóa lý và động học va chạm:

###### 1.2.2.1. Cơ chế Bám dính Bề mặt qua Va chạm Thủy động lực học (Surface Adhesion / Collision)
- **Quy luật va chạm và tiếp xúc:**
  - Bông cặn đã hình thành sẵn (pre-formed flocs) có xu hướng chuyển động chìm xuống hoặc trôi lơ lửng, gặp các vi bọt khí đường kính $10 - 100\ \mu m$ đang chuyển động dâng lên.
  - Quá trình va chạm thủy động lực học đưa bọt khí tiếp cận lớp màng chất lỏng bao quanh hạt cặn.
- **Năng lượng tự do bám dính bề mặt và góc tiếp xúc:**
  - Quá trình bám dính chỉ diễn ra tự phát khi năng lượng tự do bề mặt Gibbs thay đổi âm ($\Delta G_{\text{att}} < 0$):
    $$\Delta G_{\text{att}} = \gamma_{LV} (\cos\theta - 1)$$
    - Trong đó:
      - $\gamma_{LV}$: Sức căng bề mặt tại mặt phân chia pha Lỏng - Khí ($\text{N/m}$).
      - $\theta$: Góc tiếp xúc (contact angle) đo qua pha lỏng tại tiếp tuyến bề mặt hạt rắn.
  - Khi bề mặt hạt có tính kỵ nước cao (hydrophobic, ví dụ dầu mỡ FOGs hoặc hạt cặn đã hấp phụ polymer cation hữu cơ), $\theta > 0$, dẫn đến $\cos\theta < 1 \implies \Delta G_{\text{att}} < 0$, bọt khí bám chặt bền vững vào bề mặt hạt cặn.
  - Các lực liên kết đóng vai trò chủ đạo: Lực Van der Waals, tương tác kỵ nước, lực hút tĩnh điện và sức căng mặt ngoài chất lỏng.

###### 1.2.2.2. Cơ chế Bẫy kẹt và Giữ bọt trong Quá trình Tạo bông (Entrapment / Incorporation)
- **Quá trình hình thành liên hợp đồng thời:**
  - Xảy ra khi vi bọt khí được cấp đồng thời vào quá trình keo tụ - tạo bông (coagulation - flocculation).
  - Khi các hạt keo mất ổn định kết tụ lại với nhau thành bông cặn lớn dưới tác dụng của chất keo tụ (PAC, phèn nhôm, phèn sắt) và polymer trợ keo, hàng triệu vi bọt khí bị bao bọc và bẫy kẹt trực tiếp bên trong ma trận mắt lưới bông cặn xốp (Floc with Bubbles).
- **Đặc điểm liên kết:**
  - Cấu trúc liên hợp có độ bền cơ học cao, bọt khí không thể tách rời khỏi bông cặn ngay cả khi có xáo trộn thủy lực nhẹ, làm giảm mạnh khối lượng riêng tổng thể của toàn bộ bông cặn.

###### 1.2.2.3. Cơ chế Tạo mầm Trực tiếp trên Bề mặt Hạt cặn (Direct Nucleation on Particle Surfaces)
- **Hiện tượng tạo mầm dị thể (Heterogeneous Nucleation):**
  - Bề mặt hạt cặn lơ lửng thô ráp, chứa các lỗ xốp, vết nứt tế vi đóng vai trò là các tâm tạo mầm (nucleation sites).
  - Khi dung dịch nước quá bão hòa khí giảm áp đột ngột, các bọt khí siêu vi sẽ ưu tiên kết tụ và phát triển ngay tại các vị trí lỗ rãnh này, bám trực tiếp vào khung hạt mà không cần giai đoạn va chạm thủy động học.

##### 1.2.3. Vận tốc Nổi của Hạt cặn bám Vi bọt (Flotation Rise Velocity)
- **Dải vận tốc thực nghiệm:**
  - Vận tốc nổi của bông cặn bám bọt khí trong vùng lắng trong (clarification zone) đạt từ $v_f = 2.56\ \text{cm/min}$ đến $12.7\ \text{cm/min}$ (tương đương $1.54 - 7.62\ \text{m/h}$).
- **Mối quan hệ với tỷ số Khí/Chất rắn ($A/S$):**
  - Vận tốc nổi $v_f$ tỷ lệ thuận trực tiếp với tỷ số $A/S$ theo quan hệ thực nghiệm:
    $$v_f = k \cdot \left(\frac{A}{S}\right)^n$$
    - Trong đó $k$ và $n$ là hằng số thực nghiệm phụ thuộc đặc tính cơ học của bông cặn và nhiệt độ nước ($n \approx 0.7 - 1.0$).
  - Khi $A/S$ đạt ngưỡng tới hạn tối ưu (thường khoảng $0.008 - 0.02\ \text{mg/mg}$), vận tốc nổi đạt giá trị bình nguyên, tăng thêm lượng khí chỉ gây nhiễu loạn thủy lực mà không làm tăng thêm vận tốc nổi.

---

### 2. Phân loại Sơ đồ Công nghệ Hệ thống DAF (DAF Systems Classification)

#### 2.1. Phân loại theo Cấu hình Dòng Thủy lực (Hydraulic Flow Configurations)

##### 2.1.1. Hệ thống Nạp khí Áp lực Toàn phần (Full-Flow Direct Pressurization without Recycle)
- **Sơ đồ cấu tạo và hành trình dòng chảy:**
  - $100\%$ lưu lượng nước thải thô đầu vào ($Q$) được bơm cao áp hút qua bộ hòa trộn hóa chất keo tụ dạng ống, đẩy trực tiếp qua bình bão hòa khí (pressure saturation vessel) có cấp khí nén từ máy nén ở áp suất $3.4 - 5.0\ \text{atm}$.
  - Toàn bộ dòng nước thải sau khi bão hòa không khí đi qua van tiết lưu giảm áp đặt ngay tại đầu vào bể tuyển nổi, bung ra hàng tỷ vi bọt đưa cặn nổi lên bề mặt.

###### 2.1.1.1. Ưu điểm Kỹ thuật
- Kích thước bể tuyển nổi là nhỏ nhất vì không cần tiếp nhận thêm lưu lượng tuần hoàn:
  $$Q_{\text{bể}} = Q$$
  Diện tích mặt bằng bể nhỏ, tiết kiệm chi phí xây dựng vỏ bể.
- Cung cấp lượng không khí hòa tan trên một đơn vị thể tích nước thô lớn nhất vì toàn bộ dòng thải đều được nén ở áp suất cao.

###### 2.1.1.2. Nhược điểm và Giới hạn Ứng dụng
- *Hiện tượng vỡ nát bông cặn (Severe Floc Shearing):* Nước thải thô chứa cặn keo tụ phải đi qua cánh bơm cao áp và van giảm áp tiết diện hẹp với vận tốc cục bộ cực cao, lực cắt xé thủy lực (shear stress) phá hủy hoàn toàn cấu trúc bông cặn, biến chúng thành các hạt siêu mịn rất khó tuyển nổi.
- *Tắc nghẽn và mài mòn thiết bị (Clogging & Erosion):* Cặn thô, hạt cát và sợi dệt trong nước thải thô dễ làm tắc các lỗ vòi phun, mài mòn cánh bơm nén và làm bẩn lớp đệm của bình áp lực.
- *Phạm vi ứng dụng hẹp:* Chỉ ứng dụng cho nước thải không cần châm hóa chất keo tụ trước, nước thải có cặn dạng hạt cứng, nước thải nhiễm dầu mỡ tự do dạng nhũ hóa phân tán cao.

##### 2.1.2. Hệ thống Nạp khí Áp lực Một phần (Partial-Flow Pressurization)
- **Cấu hình dòng chảy:**
  - Một phần lưu lượng nước thải thô ($30 - 50\% Q$) được trích qua bơm cao áp và bình bão hòa khí.
  - Phần nước thải thô còn lại ($50 - 70\% Q$) được đưa thẳng vào vùng tiếp xúc của bể tuyển nổi mà không qua nén áp.
- **Đánh giá kỹ thuật:**
  - Giảm được kích thước bình bão hòa và công suất bơm cao áp so với nạp toàn dòng.
  - Vẫn tồn tại nhược điểm phá vỡ bông cặn đối với phần dòng chảy đi qua bơm nén, hiệu quả tách cặn trung bình.

##### 2.1.3. Hệ thống Nạp khí Tuần hoàn Nước trong (Pressurized Clarified Effluent Recycle)
- **Sơ đồ cấu tạo chuẩn công nghiệp:**
  - Nước thải thô ($Q$) sau khi châm hóa chất keo tụ - tạo bông nhẹ nhàng trong bể phản ứng khuấy chậm được dẫn thẳng vào vùng tiếp xúc (contact chamber) của bể tuyển nổi dưới điều kiện thủy lực êm ái, không chịu áp suất cao.
  - Một phần nước trong đã lắng tách cặn từ đáy hoặc máng thu sau bể tuyển nổi (lưu lượng tuần hoàn $R$, thường chiếm $15 - 120\%$ lưu lượng $Q$, điển hình $20 - 50\%$) được bơm cao áp hút và đẩy vào bình bão hòa áp lực.
  - Dòng nước tuần hoàn sau khi bão hòa không khí ở áp suất $3.4 - 5.0\ \text{atm}$ được dẫn qua van giảm áp bố trí tại dàn ống phân phối (manifold) ngay dưới đáy vùng tiếp xúc, phun hòa trộn với dòng nước thải thô vào bể.

###### 2.1.3.1. Ưu điểm Vượt trội
- *Bảo vệ tối đa cấu trúc bông cặn:* Bông cặn keo tụ hoàn toàn không đi qua bơm cao áp hay van giảm áp nên không bị phá vỡ, giữ nguyên kích thước lớn dễ bám dính vi bọt.
- *Chống tắc nghẽn hệ thống nạp khí:* Nước đi qua bơm nén, bình bão hòa và các vòi phun giảm áp là nước trong sạch (clarified water), loại trừ nguy cơ tắc nghẽn vòi phun và bám bẩn lớp vật liệu đệm.
- *Linh hoạt điều khiển tỷ số $A/S$:* Dễ dàng điều chỉnh tỷ lệ khí cấp vào thông qua biến tần điều khiển lưu lượng bơm tuần hoàn $R$ mà không làm xáo trộn lưu lượng nạp nước thô $Q$.
- *Tiêu chuẩn áp dụng:* Là cấu hình bắt buộc đối với xử lý nước thải công nghiệp chứa nhiều chất rắn lơ lửng, chất hữu cơ, xử lý tách bông bùn sinh học và cô đặc bùn hoạt tính dư.

###### 2.1.3.2. Nhược điểm Kỹ thuật
- Tăng tổng lưu lượng thủy lực đi vào bể tuyển nổi:
  $$Q_{\text{total}} = Q + R$$
- Yêu cầu diện tích mặt bằng bể tuyển nổi lớn hơn so với hệ thống không tuần hoàn cùng công suất.

#### 2.2. Phân loại theo Hình học và Kết cấu Bể (Tank Geometry & Mechanical Configurations)

##### 2.2.1. Bể Tuyển nổi Hình chữ nhật (Rectangular DAF Tanks)
- **Cấu tạo chi tiết và các phân vùng chức năng:**

###### 2.2.1.1. Vùng Tiếp xúc và Hòa trộn (Contact Zone / Reaction Chamber)
- Chiếm khoảng $10 - 20\%$ chiều dài bể, ngăn cách với vùng tuyển nổi chính bằng vách ngăn hướng dòng (baffle wall).
- Dàn vòi phun giảm áp (depressurization nozzles) bố trí cách nhau $s_{\text{nozzle}} = 0.2 - 0.3\ \text{m}$ phun dòng nước tuần hoàn bão hòa vi bọt góc nghiêng $45^\circ - 60^\circ$ ngược chiều hoặc cùng chiều dòng nước thải nạp vào để tăng cường xác suất va chạm hạt - bọt khí.
- Vận tốc dòng chảy trong vùng tiếp xúc duy trì $v_c = 0.05 - 0.1\ \text{m/s}$ để tránh làm vỡ bông cặn.

###### 2.2.1.2. Vùng Tuyển nổi và Tách pha (Flotation / Separation Zone)
- Dòng chảy trong vùng tuyển nổi chuyển sang chế độ chảy tầng nằm ngang (horizontal plug flow) với số Reynolds $\text{Re} < 500$.
- Chiều sâu công tác của nước trong bể: $H \le 3.0\ \text{m}$ (thông thường chọn $H = 1.5 - 2.5\ \text{m}$).
- Chiều dài bể tuyển nổi hình chữ nhật: $L \le 11.0\ \text{m}$ (tỷ lệ $L/W = 3/1$ đến $5/1$) nhằm ngăn ngừa hiện tượng dòng chảy ngắn (short-circuiting).
- Một số thiết kế cao cấp gắn thêm các tấm nghiêng (lamella plates) nghiêng $45^\circ - 60^\circ$ để tăng diện tích bề mặt lắng/nổi tương đương, cho phép vận hành ở tải trọng thủy lực cao gấp đôi.

###### 2.2.1.3. Cơ cấu Thu gom Bùn nổi và Nước trong (Skimmer & Effluent Launder)
- *Hệ gạt bọt mặt bằng xích gạt (Chain-and-flight skimmer):*
  - Các thanh gạt bằng composite sợi thủy tinh (FRP) hoặc thép không gỉ gắn trên 2 sợi xích vô tận, chuyển động chậm với vận tốc $v_{\text{skim}} = 0.3 - 1.5\ \text{m/min}$.
  - Gạt lớp váng bọt nổi (float blanket) trượt lên tấm nghiêng thoát nước (beach) đổ vào máng thu váng bọt (scum trough). Vận tốc gạt chậm nhằm hạn chế kéo nước tự do vào bùn.
- *Hệ cào bùn đáy (Bottom scraper / screw auger):*
  - Bố trí các thanh gạt đáy chạy cùng xích hoặc trục vít xoắn tải bùn (auger) gom lượng cặn nặng lắng xuống đáy bể về phễu thu cặn xả định kỳ.
- *Máng thu nước trong (Effluent discharge):*
  - Bố trí vách ngăn chắn bọt dưới nước (underflow baffle) và vách tràn răng cưa (V-notch weir) hoặc ống đục lỗ đáy thu nước trong (subnatant) thoát ra ngoài.

##### 2.2.2. Bể Tuyển nổi Hình tròn (Circular DAF Clarifiers)
- **Đặc trưng cấu tạo và vận hành:**

###### 2.2.2.1. Bể tròn Nạp tâm Truyền thống (Center-Feed Circular DAF)
- Dòng nước thô hòa trộn cùng dòng tuần hoàn bão hòa vi bọt được cấp vào qua ống trung tâm đồng tâm (concentric side-feed pipe).
- Trang bị van giảm áp chuyên dụng Haymore (Haymore back pressure control valve) giải phóng vi bọt ngay cửa nạp giếng phân phối trung tâm (dispersion well).
- Nước di chuyển theo phương xuyên tâm từ tâm ra chu vi (radial flow). Váng bọt nổi được cánh tay gạt bọt hướng tâm quay chậm gom vào hộp thu bọt (float box). Nước trong tràn qua máng răng cưa chu vi (circumferential effluent launder).

###### 2.2.2.2. Bể Tuyển nổi Nông Cao tải theo Nguyên lý "Vận tốc Bằng Không" (Zero-Velocity Circular DAF - Krofta Supracell)
- **Đột phá công nghệ KWI / Krofta:**
  - Bể hình trụ tròn nông đặc biệt với chiều sâu nước cực thấp: $H = 0.6 - 1.0\ \text{m}$.
  - Cầu quay chu vi mang toàn bộ cụm phân phối nước vào, ống cấp vi bọt, van giảm áp và cơ cấu gạt bọt xoắn ốc (spiral scoop skimmer) quay đồng bộ quanh tâm bể.
- **Nguyên lý động học "Zero Velocity":**
  - Nước thải nạp vào được phun ra từ cánh tay phân phối quay với vận tốc dòng ra $v_{\text{out}}$ chính xác bằng vận tốc quay của cánh tay $v_{\text{arm}}$ nhưng theo hướng ngược lại:
    $$v_{\text{nước tuyệt đối}} = v_{\text{arm}} - v_{\text{out}} = 0$$
  - Khi vận tốc chuyển động ngang của khối chất lỏng trong bể triệt tiêu về $0$, nước thải hoàn toàn tĩnh lặng tĩnh học đối với hệ tọa độ mặt đất ngay khi vừa nạp vào bể.
  - Các vi bọt khí chỉ chịu tác dụng của lực đẩy nổi theo phương thẳng đứng tuyệt đối, không bị phân tán bởi lực quán tính dòng ngang.
- **Chỉ tiêu vận hành vượt bậc:**
  - Thời gian lưu nước trong bể cực ngắn: $\theta = 3.0 - 5.0\ \text{phút}$.
  - Tải trọng thủy lực bề mặt rất cao: $SLR = 15 - 30\ \text{m}^3/(\text{m}^2\cdot\text{h})$ ($360 - 720\ \text{m}^3/(\text{m}^2\cdot\text{day})$).
  - Váng bọt thu gom liên tục bằng gạt xoắn ốc spiral scoop với độ ẩm thấp ($TS = 3.0 - 6.0\%$).

---

### 3. Cơ sở Tính toán và Lý thuyết Tỷ số Khí/Chất rắn (A/S Ratio Formulations)

#### 3.1. Ý nghĩa Vật lý và Vai trò của Tỷ số A/S (Physical Significance of A/S Ratio)

##### 3.1.1. Định nghĩa và Bản chất Thông số A/S
- **Định nghĩa toán học:**
  - Tỷ số Khí/Chất rắn ($A/S$ - Air-to-Solids ratio) là thông số điều khiển then chốt nhất trong thiết kế và vận hành DAF, biểu thị tỷ số giữa khối lượng không khí giải phóng từ trạng thái hòa tan trên khối lượng chất rắn lơ lửng có trong nước thải nạp vào bể:
    $$\frac{A}{S} = \frac{\text{Mass of Air Released (mg)}}{\text{Mass of Suspended Solids (mg)}} = \frac{\text{kg Air}}{\text{kg TSS}}$$
- **Tác động của $A/S$ lên hiệu quả phân tách:**
  - *Nếu $A/S$ quá thấp ($< 0.005\ \text{mg/mg}$):* Số lượng vi bọt không đủ bám dính lên các hạt cặn, mật độ hiệu dụng $\rho_{\text{eff}}$ không giảm đủ nhỏ hơn nước, một phần lớn hạt cặn sẽ bị trôi theo dòng nước trong ra ngoài, làm đục nước sau xử lý ($\eta_{\text{SS}} < 70\%$).
  - *Nếu $A/S$ đạt tối ưu ($0.008 - 0.02\ \text{mg/mg}$):* Bông cặn bão hòa vi bọt, nổi nhanh, lớp váng bọt nén chặt và ổn định, nước trong đạt độ đục tối thiểu, hiệu suất tách cặn $\eta_{\text{SS}} = 95 - 99\%$.
  - *Nếu $A/S$ quá cao ($> 0.06\ \text{mg/mg}$):* Tiêu tốn điện năng máy nén khí và bơm áp lực lãng phí; mật độ vi bọt quá dày đặc gây hiện tượng bọt va chạm hợp nhất (bubble coalescence) tạo bọt khí thô, làm xáo trộn lớp váng nổi và tái hòa tan cặn vào nước trong.

#### 3.2. Mô hình Toán học Tỷ số A/S cho Hệ thống Không tuần hoàn (Without Recycle Formulation)

##### 3.2.1. Phương trình Thiết kế Toàn dòng (`eq_ch03_01`)
- Phương trình tính tỷ số $A/S$ đối với hệ thống tuyển nổi nạp khí áp lực toàn dòng (không tuần hoàn):
  $$\frac{A}{S} = \frac{1.3 \cdot s_a (f \cdot P - 1)}{S_a}$$

##### 3.2.2. Định nghĩa Biến số, Ý nghĩa và Thứ nguyên Đơn vị
- **$\frac{A}{S}$:** Tỷ số không khí trên chất rắn lơ lửng ($\text{mg air / mg suspended solids}$ hoặc $\text{kg air / kg TSS}$).
- **$1.3$:** Khối lượng riêng của không khí ở điều kiện chuẩn ($1.3\ \text{mg air / mL air} = 1.3\ \text{g air / L air} = 1.3\ \text{kg air / m}^3\ \text{air}$).
- **$s_a$:** Độ hòa tan bão hòa của không khí trong nước ở nhiệt độ vận hành thực tế dưới áp suất khí quyển tiêu chuẩn $1.0\ \text{atm}$ ($\text{mL air / L water}$).
- **$f$:** Hệ số hòa tan bão hòa thực tế đạt được bên trong bình áp lực tại áp suất $P$ (không thứ nguyên, dao động $0.5 - 0.9$, thường lấy $f = 0.5$ cho bình đệm trong tính toán lý thuyết).
- **$P$:** Áp suất tuyệt đối vận hành bên trong bình áp lực ($\text{atm}$, với $P_{\text{tuyệt đối}} = P_{\text{đồng hồ}} + 1.0$).
- **$1$:** Áp suất khí quyển tiêu chuẩn ($1.0\ \text{atm}$ tuyệt đối). Lượng khí thực tế thoát ra thành vi bọt là lượng khí chênh lệch khi hạ áp từ $P$ về $1\ \text{atm}$.
- **$S_a$:** Nồng độ chất rắn lơ lửng trong nước thải thô đầu vào ($\text{mg/L}$ hoặc $\text{g/m}^3$).

##### 3.2.3. Dạng Biến đổi Tính Áp suất Vận hành Cần thiết
- Khi biết trước giá trị $A/S$ tối ưu xác định từ thí nghiệm Jar-test hoặc pilot, phương trình được biến đổi để tính áp suất tuyệt đối $P$ cần duy trì trong bình áp lực:
  $$P = \frac{\frac{(A/S) \cdot S_a}{1.3 \cdot s_a} + 1}{f}$$

#### 3.3. Mô hình Toán học Tỷ số A/S cho Hệ thống Tuần hoàn (With Recycle Formulation)

##### 3.3.1. Phương trình Thiết kế Dòng Tuần hoàn (`eq_ch03_02`)
- Phương trình tính tỷ số $A/S$ đối với hệ thống tuyển nổi nạp khí áp lực dòng tuần hoàn nước trong:
  $$\frac{A}{S} = \frac{1.3 \cdot s_a (f \cdot P - 1) \cdot R}{S_a \cdot Q}$$

##### 3.3.2. Định nghĩa Biến số Bổ sung và Ý nghĩa Dòng Tuần hoàn
- **$R$:** Lưu lượng nước trong được bơm tuần hoàn qua bình áp lực ($\text{m}^3/\text{day}$ hoặc $\text{m}^3/\text{h}$).
- **$Q$:** Lưu lượng nước thải thô nạp vào hệ thống ($\text{m}^3/\text{day}$ hoặc $\text{m}^3/\text{h}$).
- **$r$:** Tỷ lệ tuần hoàn (recycle ratio), biểu thị bằng phần trăm lưu lượng nạp thô:
  $$r = \frac{R}{Q} \times 100\%$$
- **Cơ chế cân bằng khối lượng:** Lượng không khí mang vào bể chỉ do dòng tuần hoàn $R$ cung cấp ($1.3 \cdot s_a (f \cdot P - 1) \cdot R$), nhưng toàn bộ lượng không khí này phải phục vụ để tuyển nổi toàn bộ lượng cặn có trong dòng nước thải thô $Q$ ($S_a \cdot Q$). Giả thiết nồng độ cặn trong nước tuần hoàn $S_R \approx 0\ \text{mg/L}$.

##### 3.3.3. Dạng Biến đổi Tính Lưu lượng Tuần hoàn $R$ và Tỷ lệ $r$
- Khi cố định áp suất làm việc của bình áp lực $P$ (thường chọn $P = 4.0 - 5.0\ \text{atm}$ theo tiêu chuẩn catalog nhà sản xuất):
  $$R = \frac{(A/S) \cdot S_a \cdot Q}{1.3 \cdot s_a (f \cdot P - 1)}$$
- Tỷ lệ tuần hoàn tối thiểu cần thiết:
  $$r = \frac{R}{Q} = \frac{(A/S) \cdot S_a}{1.3 \cdot s_a (f \cdot P - 1)}$$

---

### 4. Tiêu chuẩn và Thông số Thiết kế Kỹ thuật Thực nghiệm (Empirical Design Criteria & Parameters)

#### 4.1. Bảng Tiêu chuẩn Metcalf & Eddy và Thông số Vận hành (`tbl_ch03_01`)
- Bảng tổng hợp các thông số kỹ thuật tiêu chuẩn thiết kế hệ thống DAF trích dẫn từ Metcalf & Eddy và tài liệu giảng dạy:

| TT | Thông số Kỹ thuật | Ký hiệu | Khoảng Giá trị Tiêu chuẩn | Đơn vị Đo | Vùng Công nghệ Áp dụng | Ghi chú Thiết kế Kỹ thuật |
|---|---|---|---|---|---|---|
| 1 | Tỷ số Khí/Chất rắn | $A/S$ | $0.005 - 0.06$ | $\text{mg air / mg TSS}$ | Toàn hệ thống DAF | Giá trị tối ưu điển hình: $0.008\ \text{mg/mg}$; cô đặc bùn cần $0.015 - 0.03\ \text{mg/mg}$. |
| 2 | Tải trọng thủy lực bề mặt | $SLR$ | $80 - 240$ | $\text{m}^3/(\text{m}^2\cdot\text{day})$ | Vùng tuyển nổi chính | Tương đương $3.3 - 10.0\ \text{m}^3/(\text{m}^2\cdot\text{h})$. Tính trên tổng lưu lượng $(Q+R)$. |
| 3 | Tải trọng chất rắn bề mặt | $MLR$ | $2.0 - 10.0$ | $\text{kg TSS}/(\text{m}^2\cdot\text{h})$ | Vùng tuyển nổi | Áp dụng khi dùng DAF để cô đặc bùn hoạt tính dư (WAS thickening). |
| 4 | Thời gian lưu nước trong bể | $\theta_{\text{tank}}$ | $20 - 30$ | $\text{phút}$ | Bể tuyển nổi | $\theta = V_{\text{tank}} / (Q+R)$; đối với bể nông Krofta $\theta = 3 - 5\ \text{phút}$. |
| 5 | Chiều sâu công tác của bể | $H$ | $\le 3.0$ | $\text{m}$ | Bể tuyển nổi | Điển hình $1.5 - 2.5\ \text{m}$. Bể Krofta nông $0.6 - 1.0\ \text{m}$. |
| 6 | Chiều dài bể chữ nhật | $L$ | $\le 11.0$ | $\text{m}$ | Bể chữ nhật | Tỷ lệ $L/W = 3/1 - 5/1$ để phân bố thủy lực chảy tầng ổn định. |
| 7 | Tỷ lệ tuần hoàn | $r$ | $15 - 120$ | $\%$ của dòng $Q$ | Dòng nén tuần hoàn | Nước thải sinh hoạt/công nghiệp nhẹ: $20 - 50\%$; cô đặc bùn: $50 - 120\%$. |
| 8 | Áp suất vận hành bình hòa khí | $P$ | $3.4 - 4.8$ | $\text{atm}$ (tuyệt đối) | Bình bão hòa áp lực | Tương đương $2.4 - 3.8\ \text{bar}$ gauge (trong bài toán thiết kế chọn đến $5.0\ \text{atm}$). |
| 9 | Thời gian lưu trong bình áp lực | $\theta_{pv}$ | $1.0 - 3.0$ | $\text{phút}$ | Bình bão hòa áp lực | Đủ thời gian cho không khí khuếch tán hòa tan vào nước. |
| 10 | Tải trọng thủy lực bình áp lực | $HLR_{pv}$ | $1440 - 1920$ | $\text{m}^3/(\text{m}^2\cdot\text{day})$ | Bình bão hòa áp lực | Tương đương $60 - 80\ \text{m}^3/(\text{m}^2\cdot\text{h})$ tính theo tiết diện ngang bình. |
| 11 | Chiều cao lớp vật liệu đệm | $h_{\text{pack}}$ | $1.0 - 1.5$ | $\text{m}$ | Bình bão hòa áp lực | Đệm nhựa Pall ring hoặc Raschig ring tăng diện tích tiếp xúc khí - lỏng. |
| 12 | Suất nạp khí nén | $q_{\text{air}}$ | $6.0 - 10.0$ | $\text{g air / m}^3\ \text{raw water}$ | Máy nén khí | Khối lượng khí nén thực tế cấp vào hệ thống trên $1\ \text{m}^3$ nước thô. |
| 13 | Đường kính hạt vi bọt | $d_b$ | $10 - 100$ | $\mu m$ | Vùng tiếp xúc | Kích thước tối ưu trung bình $30 - 60\ \mu m$. |
| 14 | Khoảng cách vòi phun giảm áp | $s_{\text{nozzle}}$ | $0.2 - 0.3$ | $\text{m}$ | Dàn ống phân phối | Bố trí dọc theo chiều rộng đáy ngăn tiếp xúc. |
| 15 | Vận tốc nổi của bông cặn | $v_f$ | $2.56 - 12.7$ | $\text{cm/min}$ | Vùng tách pha | Tương đương $1.54 - 7.62\ \text{m/h}$. |
| 16 | Hệ số hòa tan bão hòa | $f$ | $0.5 - 0.8$ | Không thứ nguyên | Bình bão hòa | Bình có đệm thực tế đạt $0.8 - 0.9$; tính toán lý thuyết chọn $0.5$. |
| 17 | Nồng độ bùn gạt cơ học | $TS_{\text{mech}}$ | $2.0 - 3.0$ | $\% \text{ TS (w/w)}$ | Bùn nổi mặt bể | Có thể đạt tới $4.0 - 5.0\%$ nếu có vùng để ráo nước trên tấm nghiêng. |
| 18 | Nồng độ bùn tràn thủy lực | $TS_{\text{hyd}}$ | $\approx 0.5$ | $\% \text{ TS (w/w)}$ | Bùn nổi máng tràn | Bùn rất loãng, thể tích phát sinh lớn gấp $4 - 6$ lần gạt cơ học. |
| 19 | Hiệu suất loại bỏ TSS và FOG | $\eta$ | $90 - 99$ | $\%$ | Toàn hệ thống DAF | Đạt khi kết hợp keo tụ - tạo bông hóa lý thích hợp. |

#### 4.2. Hệ thống Thu gom Bùn nổi và Đặc tính Bùn váng (Skimming Mechanisms & Float Characteristics)

##### 4.2.1. So sánh Cơ cấu Gạt Cơ học (Mechanical Skimming) và Tràn Thủy lực (Hydraulic Overflow)
- **Cơ chế gạt cơ học (Mechanical Surface Scrapers):**
  - Sử dụng hệ cào xích gạt (flight-and-chain) hoặc thanh gạt xoay (rotary skimmer) quét chậm lớp váng bọt nổi trên bề mặt chất lỏng đưa lên tấm dốc ráo nước (beach plate) nghiêng $30^\circ - 45^\circ$ trước khi xả vào phễu chứa bùn.
  - Trong quá trình trượt trên tấm dốc, lượng nước tự do giữ trong váng bọt tự chảy ngược lại bể, nén ép trọng lực làm tăng nồng độ chất rắn khô lên $TS = 2.0 - 5.0\%$.
- **Cơ chế tràn thủy lực (Hydraulic Overflow):**
  - Điều chỉnh nâng mực nước trong bể để lớp bọt tự động tràn qua vách ngăn chảy vào máng thu.
  - Phương pháp này cuốn theo một lượng cực lớn nước trong bề mặt, dẫn đến nồng độ bùn chỉ đạt $TS \approx 0.5\%$.
  - *Hậu quả kỹ thuật:* Thể tích bùn lỏng phát sinh tăng từ $400 - 500\%$, gây quá tải nghiêm trọng cho các công trình xử lý bùn phía sau (bể phân hủy bùn, máy ép bùn) và tiêu tốn nhiều hóa chất polymer trợ ép bùn.

##### 4.2.2. Hệ thống Thu gom Bùn Lắng đáy (Bottom Sludge Collection)
- **Sự hình thành bùn đáy:**
  - Trong nước thải công nghiệp luôn tồn tại một tỷ lệ hạt cặn nặng ($5 - 15\%$ tổng lượng TSS) như hạt cát mịn, gỉ sét kim loại, kết tủa phèn nặng không thể bám dính vi bọt hoặc có khối lượng riêng quá lớn vượt quá lực đẩy nổi của vi bọt.
- **Biện pháp kỹ thuật thu gom:**
  - Đáy bể DAF được thiết kế dạng hình phễu nghiêng dốc tối thiểu $45^\circ - 60^\circ$ hoặc bố trí thanh gạt đáy chuyển động tịnh tiến/trục vít xoắn (screw auger) thu cặn gom vào hố thu cặn nặng ở đầu hoặc giữa bể.
  - Định kỳ tự động mở van xả đáy điều khiển bằng khí nén (pneumatic drain valve) để xả bỏ phần cặn này, chống đóng bánh đông cứng làm nghẹt đáy bể.

#### 4.3. Thiết kế Thiết bị Bão hòa Áp lực và Máy nén Khí (Saturator & Compressor Specifications)

##### 4.3.1. Tính toán Kích thước Bình Áp lực (Saturation Pressure Vessel Sizing)
- **Diện tích mặt cắt ngang của bình áp lực ($A_{pv}$):**
  $$A_{pv} = \frac{R}{HLR_{pv}}$$
  - Trong đó:
    - $R$: Lưu lượng nước tuần hoàn ($\text{m}^3/\text{day}$).
    - $HLR_{pv}$: Tải trọng thủy lực bình bão hòa ($1440 - 1920\ \text{m}^3/(\text{m}^2\cdot\text{day})$).
- **Đường kính trong của bình ($D_{pv}$):**
  $$D_{pv} = \sqrt{\frac{4 \cdot A_{pv}}{\pi}}$$
- **Chiều cao bình bão hòa áp lực ($H_{pv}$):**
  - Chiều cao lớp vật liệu đệm: $h_{\text{pack}} = 1.0 - 1.5\ \text{m}$.
  - Chiều cao khoảng không phân phối nước đỉnh và thu gom đáy: $h_{\text{dist}} = 0.5 - 0.8\ \text{m}$.
  - Tổng chiều cao bình: $H_{pv} = h_{\text{pack}} + h_{\text{dist}} \approx 1.8 - 2.5\ \text{m}$.
  - Kiểm tra thời gian lưu thủy lực trong bình: $\theta_{pv} = \frac{V_{pv}}{R} = 1.0 - 3.0\ \text{phút}$.

##### 4.3.2. Tính toán Công suất và Lưu lượng Máy nén khí (Air Compressor Sizing)
- **Lưu lượng khối lượng khí nén yêu cầu ($M_{\text{air}}$):**
  $$M_{\text{air}} = \left(\frac{A}{S}\right) \times Q \times S_a \times 10^{-3}\quad (\text{kg air/day})$$
- **Lưu lượng thể tích khí nén tự do (Free Air Delivery - FAD) tại điều kiện hút ($1\ \text{atm}, 20^\circ\text{C}$):**
  $$Q_{\text{air, vol}} = \frac{M_{\text{air}}}{\rho_{\text{air}} \times 1440}\quad (\text{m}^3/\text{min})$$
  - Hệ số dự phòng an toàn cho máy nén: $FS = 1.3 - 1.5$.
- **Áp suất làm việc của máy nén khí ($P_{\text{comp}}$):**
  $$P_{\text{comp}} = P_{pv} + \Delta P_{\text{line}} + \Delta P_{\text{inj}}$$
  - Thường chọn áp suất máy nén khí $P_{\text{comp}} = 6.0 - 8.0\ \text{bar}$ gauge để đảm bảo thắng áp suất làm việc của bình ($3.4 - 5.0\ \text{atm}$) và tổn thất qua van một chiều, bộ lọc khí.

---

### 5. Khắc phục Sự cố Vận hành và Thiết kế Đường ống (Operational Troubleshooting & Manifold Guidelines)

#### 5.1. Hiện tượng Hóa bọt Sớm và Hợp nhất Bọt khí trong Đường ống (Premature Nucleation & Coalescence)

##### 5.1.1. Bản chất Vật lý và Tác hại
- Nước bão hòa khí dưới áp suất cao nếu bị giảm áp trên đường ống trước khi đến vòi phun sẽ lập tức giải phóng bọt khí ngay trong đường ống dẫn.
- Trong không gian lòng ống chật hẹp, các vi bọt va chạm và kết hợp lại với nhau (coalescence) tạo thành các bọt khí kích thước lớn ($d_b > 1000\ \mu m$).
- *Tác hại:* Bọt khí lớn nổi với tốc độ hỗn loạn, không có khả năng bám dính hạt cặn và làm phá vỡ lớp bùn váng đã nổi trên mặt bể.

##### 5.1.2. Hướng dẫn Kỹ thuật và Biện pháp Giảm thiểu Tổn thất Thủy lực
- **Quy tắc 1: Bố trí chênh lệch cao trình thủy lực:**
  - Luôn duy trì mực nước bên trong bình bão hòa áp lực cao hơn mực nước tự do trong bể tuyển nổi DAF để tạo cột áp thủy tĩnh thuận lợi.
- **Quy tắc 2: Tối thiểu hóa chiều dài đường ống:**
  - Lắp đặt bình bão hòa áp lực càng gần bể DAF càng tốt; chiều dài đường ống dẫn nước bão hòa từ bình đến dàn vòi phun không nên vượt quá $2.0 - 3.0\ \text{m}$.
- **Quy tắc 3: Triệt tiêu các phụ kiện gây tổn thất áp suất cục bộ:**
  - Hạn chế tối đa việc lắp co cút góc nhọn $90^\circ$, tê thu hẹp, hoặc van chặn trên đường ống nằm giữa bình áp lực và dàn vòi phun. Chỉ sử dụng cút uốn cong bán kính lớn ($R \ge 3D$).
- **Quy tắc 4: Vận tốc dòng chảy trong ống phân phối:**
  - Vận tốc dòng nước bão hòa trong ống góp chính duy trì $v = 1.0 - 1.5\ \text{m/s}$ nhằm tránh hiện tượng tách túi khí dọc đỉnh ống.
- **Quy tắc 5: Thiết kế van giảm áp chuyên dụng:**
  - Việc giảm áp phải diễn ra tức thời $100\%$ ngay tại đầu ra của vòi phun nhúng chìm trong nước ở đáy bể DAF, không được để sụt áp dần dọc đường ống.

#### 5.2. Sự cố Hàm lượng Chất rắn Bùn nổi Quá Thấp (Low Float Solids Concentration)
- **Triệu chứng:** Bùn nổi có dạng bọt xốp lỏng, nồng độ chất rắn $TS < 1.0\%$, thể tích bùn thải xả ra quá lớn làm đầy bể chứa bùn.
- **Nguyên nhân cốt lõi:**
  - Tốc độ gạt của máy cào váng bọt quá nhanh, liên tục kéo nước bề mặt vào máng thu.
  - Tấm dốc ráo nước (beach plate) bị đặt ngập dưới mực nước hoặc chiều dốc không đủ để bùn tự ráo nước.
  - Tỷ số $A/S$ quá cao tạo lớp bọt khí thừa rỗng xốp.
- **Biện pháp xử lý:**
  - Giảm tốc độ motor truyền động cánh gạt xuống $0.3 - 0.5\ \text{m/min}$ hoặc chuyển sang chế độ gạt gián đoạn theo chu kỳ (timer-controlled intermittent skimming).
  - Điều chỉnh hạ vách tràn răng cưa để hạ mực nước làm việc của bể, đảm bảo mép dưới tấm dốc ráo nước nằm cao hơn mực nước từ $20 - 50\ \text{mm}$.
  - Giảm lưu lượng tuần hoàn $R$ hoặc giảm áp suất $P$ để đưa tỷ số $A/S$ về điểm tối ưu ($0.008\ \text{mg/mg}$).

#### 5.3. Xử lý Hạt cặn Tỷ trọng Cao và Kích thước Lớn (Heavy & Coarse Solids Ineffective Flotation)
- **Triệu chứng:** Nước trong sau bể DAF có độ đục cao do cặn nặng không nổi được mà lơ lửng rồi thoát ra máng thu nước trong, đáy bể tích tụ lượng bùn cát dày đặc gây kẹt cánh cào đáy.
- **Nguyên nhân:** Kích thước hạt cặn thô ($d_p > 200\ \mu m$) hoặc mật độ cặn quá nặng ($\rho_p > 1.5\ \text{g/cm}^3$) khiến sức nổi của chùm vi bọt không thắng nổi trọng lực hạt.
- **Biện pháp khắc phục:**
  - Lắp đặt công trình tiền xử lý phía trước bể DAF: Song chắn rác tinh ($\le 1\ \text{mm}$) và bể lắng cát (grit chamber) hoặc bể lắng sơ cấp ngắn hạn để loại bỏ cặn thô nặng trước khi vào DAF.
  - Tối ưu hóa quá trình keo tụ: Giảm liều lượng phèn vô cơ nặng, tăng cường châm polymer anionic/cationic trọng lượng phân tử cao để tạo bông cặn dạng sợi xốp có khối lượng riêng nhỏ hơn, dễ nổi hơn.

---

### 6. Bài tập Tính toán Thiết kế Mẫu Chi tiết (Comprehensive Step-by-Step Worked Design Example)

#### 6.1. Đề bài và Dữ liệu Đầu vào (Problem Statement & Given Parameters)
- **Nguồn bài tập:** Bài toán thiết kế điển hình chương 3 (`EX-CH03-01`, Slide 9 - Bài giảng Kỹ thuật Xử lý Nước thải HCMUT-263, TS. Nguyễn Hoàng Dũng).
- **Đề bài:** Thiết kế hệ thống Tuyển nổi Khí hòa tan (DAF) hoàn chỉnh trong 2 trường hợp: Không tuần hoàn (Chế độ A - Without Recycle) và Có tuần hoàn dòng nước trong nén áp (Chế độ B - With Pressurized Recycle).
- **Bảng thông số đầu vào thiết kế (Design Input Parameters):**

| Thông số Thiết kế | Ký hiệu | Giá trị | Đơn vị Đo | Ý nghĩa Kỹ thuật |
|---|---|---|---|---|
| Tỷ số Khí/Chất rắn tối ưu | $A/S$ | $0.008$ | $\text{mg air / mg TSS}$ | Xác định từ thực nghiệm Jar-test để đạt hiệu suất cao nhất |
| Nhiệt độ nước thải thiết kế | $T$ | $20.0$ | $^\circ\text{C}$ | Nhiệt độ tính toán cân bằng hòa tan khí |
| Độ hòa tan không khí ở $20^\circ\text{C}, 1\ \text{atm}$ | $s_a$ | $18.7$ | $\text{mL air / L water}$ | Tra theo định luật Henry ở $20^\circ\text{C}$ |
| Áp suất nén hệ thống tuần hoàn | $P$ | $5.0$ | $\text{atm}$ (tuyệt đối) | Áp suất vận hành bình áp lực chế độ tuần hoàn |
| Hệ số hòa tan bão hòa thực tế | $f$ | $0.5$ | Không thứ nguyên | Hiệu suất hòa tan không khí của bình áp lực |
| Tải trọng thủy lực bề mặt bể | $SLR$ | $100.0$ | $\text{m}^3/(\text{m}^2\cdot\text{day})$ | Tải trọng bề mặt lựa chọn theo khuyến cáo Metcalf & Eddy |
| Lưu lượng nước thải thiết kế trung bình | $Q$ | $400.0$ | $\text{m}^3/\text{day}$ | Lưu lượng xử lý danh định của trạm |
| Nồng độ cặn lơ lửng đầu vào | $S_a$ | $3000.0$ | $\text{mg/L}$ | Hàm lượng TSS dòng thải công nghiệp chế biến thực phẩm |

---

#### 6.2. Tính toán Tải lượng Chất rắn và Nhu cầu Không khí (Solids & Air Loading Calculations)

##### Bước 1: Tính toán Tải lượng Khối lượng Chất rắn Lơ lửng Đầu vào (Solids Mass Loading Rate)
- **Công thức áp dụng:**
  $$\text{Solids Loading} = Q \times S_a \times \frac{1000\ \text{L}}{\text{m}^3} \times \frac{1\ \text{kg}}{10^6\ \text{mg}}$$
- **Thế số tính toán:**
  $$\text{Solids Loading} = 400\ \text{m}^3/\text{day} \times 3000\ \text{mg/L} \times 10^{-3}\ \frac{\text{kg}\cdot\text{L}}{\text{m}^3\cdot\text{mg}} = 1200.0\ \text{kg TSS/day}$$
- **Kết quả:**
  - Tải lượng cặn theo ngày: $1200.0\ \text{kg TSS/day}$.
  - Tải lượng cặn theo giờ:
    $$\text{Solids Loading}_{\text{hourly}} = \frac{1200.0}{24} = 50.0\ \text{kg TSS/h}$$

##### Bước 2: Tính toán Tổng Khối lượng Không khí Cần thiết Mỗi ngày (Required Daily Air Mass)
- **Công thức áp dụng:**
  $$\text{Air Mass} = \left(\frac{A}{S}\right) \times \text{Solids Loading}$$
- **Thế số tính toán:**
  $$\text{Air Mass} = 0.008\ \frac{\text{mg air}}{\text{mg TSS}} \times 1200.0\ \frac{\text{kg TSS}}{\text{day}} = 9.60\ \text{kg air/day}$$
- **Kết quả:**
  - Khối lượng không khí cần cung cấp: $9.60\ \text{kg air/day}$ ($0.40\ \text{kg air/h}$).
  - Suất nạp khí trên một đơn vị thể tích nước thô:
    $$q_{\text{air}} = \frac{9.60\ \text{kg air/day} \times 1000\ \text{g/kg}}{400\ \text{m}^3/\text{day}} = 24.0\ \text{g air / m}^3\ \text{raw wastewater}$$

---

#### 6.3. Chế độ A: Thiết kế Hệ thống Toàn dòng Không Tuần hoàn (Mode A: Without Recycle)

##### Bước 3: Xác định Áp suất Tuyệt đối Vận hành Bình Áp lực ($P$)
- **Phương trình xuất phát (`eq_ch03_01`):**
  $$\frac{A}{S} = \frac{1.3 \cdot s_a (f \cdot P - 1)}{S_a}$$
- **Biến đổi tìm $P$:**
  $$P = \frac{\frac{(A/S) \cdot S_a}{1.3 \cdot s_a} + 1}{f}$$
- **Thế số chi tiết:**
  $$0.008 = \frac{1.3 \times 18.7 \times (0.5 \cdot P - 1)}{3000}$$
  $$0.008 \times 3000 = 24.31 \times (0.5 \cdot P - 1)$$
  $$24.0 = 24.31 \times (0.5 \cdot P - 1)$$
  $$0.5 \cdot P - 1 = \frac{24.0}{24.31} = 0.987248$$
  $$0.5 \cdot P = 1.987248$$
  $$P = \frac{1.987248}{0.5} = 3.9745\ \text{atm}$$
- **Kết quả và Nhận xét:**
  - Áp suất tuyệt đối cần duy trì: $P = 3.97\ \text{atm}$ (làm tròn $3.97\ \text{atm}$).
  - Áp suất đồng hồ (Gauge pressure):
    $$P_{\text{gauge}} = P - 1.0 = 2.97\ \text{atm} \approx 3.0\ \text{bar} \approx 43.7\ \text{psig}$$
  - *Đánh giá kỹ thuật:* Áp suất tính toán $3.97\ \text{atm}$ nằm hoàn toàn trong phạm vi áp suất vận hành kinh tế tiêu chuẩn ($3.4 - 4.8\ \text{atm}$).

##### Bước 4: Định cỡ Kích thước Hình học Bể Tuyển nổi và Thời gian Lưu nước Chế độ A
- **Diện tích mặt thoáng bể tuyển nổi ($A_{\text{tank}}$):**
  $$A_{\text{tank}} = \frac{Q}{SLR} = \frac{400\ \text{m}^3/\text{day}}{100\ \text{m}^3/(\text{m}^2\cdot\text{day})} = 4.0\ \text{m}^2$$
- **Lựa chọn kích thước hình học:**
  - Chọn chiều sâu công tác của bể: $H = 2.0\ \text{m}$ (thỏa mãn điều kiện $H \le 3.0\ \text{m}$).
  - Chọn tỷ lệ chiều dài trên chiều rộng $L/W = 3.0$:
    $$A_{\text{tank}} = L \times W = 3.0 \cdot W^2 = 4.0\ \text{m}^2$$
    $$W = \sqrt{\frac{4.0}{3.0}} = 1.155\ \text{m} \approx 1.15\ \text{m}$$
    $$L = 3.0 \times 1.155 = 3.465\ \text{m} \approx 3.46\ \text{m}\ (\le 11.0\ \text{m})$$
- **Thể tích hữu ích của bể ($V_{\text{tank}}$):**
  $$V_{\text{tank}} = A_{\text{tank}} \times H = 4.0\ \text{m}^2 \times 2.0\ \text{m} = 8.0\ \text{m}^3$$
- **Thời gian lưu thủy lực trong bể ($\theta$):**
  $$\theta = \frac{V_{\text{tank}}}{Q} \times 1440\ \frac{\text{phút}}{\text{day}} = \frac{8.0\ \text{m}^3}{400\ \text{m}^3/\text{day}} \times 1440 = 28.8\ \text{phút}$$
- **Kiểm tra điều kiện kỹ thuật:**
  - $\theta = 28.8\ \text{phút}$ nằm hoàn hảo trong giới hạn cho phép $\theta = 20 - 30\ \text{phút}$.

---

#### 6.4. Chế độ B: Thiết kế Hệ thống Có Tuần hoàn Nước trong Nén áp (Mode B: With Pressurized Recycle)

##### Bước 5: Tính toán Lưu lượng Tuần hoàn ($R$) và Tỷ lệ Tuần hoàn ($r$)
- **Áp suất nén bình áp lực đã chọn:** $P = 5.0\ \text{atm}$ (tuyệt đối).
- **Phương trình xuất phát (`eq_ch03_02`):**
  $$\frac{A}{S} = \frac{1.3 \cdot s_a (f \cdot P - 1) \cdot R}{S_a \cdot Q}$$
- **Biến đổi tìm lưu lượng tuần hoàn $R$:**
  $$R = \frac{(A/S) \cdot S_a \cdot Q}{1.3 \cdot s_a (f \cdot P - 1)}$$
- **Thế số chi tiết:**
  $$0.008 = \frac{1.3 \times 18.7 \times (0.5 \times 5.0 - 1) \times R}{3000 \times 400}$$
  $$0.008 = \frac{24.31 \times (2.5 - 1) \times R}{1,200,000}$$
  $$0.008 = \frac{24.31 \times 1.5 \times R}{1,200,000} = \frac{36.465 \times R}{1,200,000}$$
  $$R = \frac{0.008 \times 1,200,000}{36.465} = \frac{9600}{36.465} = 263.266\ \text{m}^3/\text{day} \approx 263.27\ \text{m}^3/\text{day}$$
- **Tỷ lệ tuần hoàn tương ứng ($r$):**
  $$r = \frac{R}{Q} \times 100\% = \frac{263.27}{400.0} \times 100\% = 65.82\%$$
- **Nhận xét kỹ thuật:**
  - Tỷ lệ tuần hoàn $r = 65.82\%$ nằm hoàn toàn trong phạm vi thiết kế tiêu chuẩn khuyến nghị ($15 - 120\%$).
  - Lưu lượng bơm tuần hoàn theo giờ:
    $$R_{\text{hourly}} = \frac{263.27}{24} = 10.97\ \text{m}^3/\text{h} \approx 11.0\ \text{m}^3/\text{h}$$

##### Bước 6: Định cỡ Kích thước Hình học Bể Tuyển nổi và Thời gian Lưu nước Chế độ B
- **Tổng lưu lượng thủy lực đi vào bể DAF ($Q_{\text{total}}$):**
  $$Q_{\text{total}} = Q + R = 400.0 + 263.27 = 663.27\ \text{m}^3/\text{day}$$
- **Diện tích mặt thoáng yêu cầu ($A_{\text{tank}}$):**
  $$A_{\text{tank}} = \frac{Q_{\text{total}}}{SLR} = \frac{663.27\ \text{m}^3/\text{day}}{100\ \text{m}^3/(\text{m}^2\cdot\text{day})} = 6.633\ \text{m}^2$$
- **Lựa chọn kích thước hình học chuẩn chế tạo:**
  - Chọn chiều sâu công tác: $H = 2.0\ \text{m}$ ($\le 3.0\ \text{m}$).
  - Chọn chiều rộng bể $W = 1.50\ \text{m}$.
  - Chọn chiều dài bể $L = 4.50\ \text{m}$ (đáp ứng tỷ lệ $L/W = 3.0$ và $L \le 11.0\ \text{m}$).
  - Diện tích thực tế sau khi làm tròn:
    $$A_{\text{actual}} = 1.50\ \text{m} \times 4.50\ \text{m} = 6.75\ \text{m}^2\ (> 6.633\ \text{m}^2)$$
- **Thể tích hữu ích thực tế của bể ($V_{\text{tank}}$):**
  $$V_{\text{tank}} = A_{\text{actual}} \times H = 6.75\ \text{m}^2 \times 2.0\ \text{m} = 13.50\ \text{m}^3$$
- **Thời gian lưu thủy lực thực tế ($\theta$):**
  $$\theta = \frac{V_{\text{tank}}}{Q_{\text{total}}} \times 1440\ \frac{\text{phút}}{\text{day}} = \frac{13.50\ \text{m}^3}{663.27\ \text{m}^3/\text{day}} \times 1440 = 29.31\ \text{phút} \approx 29.3\ \text{phút}$$
- **Kiểm tra điều kiện kỹ thuật:**
  - $\theta = 29.3\ \text{phút}$ hoàn toàn đáp ứng tiêu chuẩn thiết kế $\theta = 20 - 30\ \text{phút}$.

##### Bước 7: Thiết kế Kích thước Bình Bão hòa Áp lực (Saturation Pressure Vessel Sizing)
- **Lựa chọn thông số thiết kế bình bão hòa có đệm (Packed saturator):**
  - Tải trọng thủy lực bình nén: Chọn $HLR_{pv} = 1680.0\ \text{m}^3/(\text{m}^2\cdot\text{day})$ (nằm giữa dải khuyến nghị $1440 - 1920\ \text{m}^3/(\text{m}^2\cdot\text{day})$).
- **Diện tích mặt cắt ngang bình ($A_{pv}$):**
  $$A_{pv} = \frac{R}{HLR_{pv}} = \frac{263.27\ \text{m}^3/\text{day}}{1680.0\ \text{m}^3/(\text{m}^2\cdot\text{day})} = 0.1567\ \text{m}^2 \approx 0.157\ \text{m}^2$$
- **Đường kính trong của bình bão hòa ($D_{pv}$):**
  $$D_{pv} = \sqrt{\frac{4 \cdot A_{pv}}{\pi}} = \sqrt{\frac{4 \times 0.1567}{3.14159}} = 0.4467\ \text{m} \approx 0.45\ \text{m}\ (450\ \text{mm})$$
- **Chiều cao và cấu tạo bình:**
  - Chọn chiều cao lớp vật liệu đệm: $h_{\text{pack}} = 1.20\ \text{m}$ (thỏa mãn dải $1.0 - 1.5\ \text{m}$).
  - Tổng chiều cao bình bão hòa: Chọn $H_{pv} = 2.0\ \text{m}$.
- **Kiểm tra thời gian lưu trong bình áp lực ($\theta_{pv}$):**
  $$\theta_{pv} = \frac{A_{pv} \times H_{pv}}{R / 1440} = \frac{0.1567\ \text{m}^2 \times 2.0\ \text{m}}{263.27 / 1440\ \text{m}^3/\text{min}} = \frac{0.3134}{0.1828} = 1.714\ \text{phút} \approx 1.72\ \text{phút}$$
  - Thỏa mãn điều kiện tiêu chuẩn $\theta_{pv} = 1.0 - 3.0\ \text{phút}$.

---

#### 6.5. Cân bằng Khối lượng Bùn và Tính toán Thể tích Bùn Thu hồi (Sludge Mass Balance)

##### Bước 8: Tính toán Khối lượng Bùn Khô và Thể tích Bùn Thu hồi
- **Hiệu suất thu hồi cặn lơ lửng của bể DAF:** Chọn $\eta_{\text{removal}} = 99\%$ (theo chỉ tiêu thiết kế công nghệ DAF).
- **Khối lượng cặn khô thu gom được mỗi ngày ($M_{\text{dry}}$):**
  $$M_{\text{dry}} = \text{Solids Loading} \times \eta_{\text{removal}} = 1200.0\ \text{kg TSS/day} \times 0.99 = 1188.0\ \text{kg dry solids/day}$$
- **Trường hợp 1: Thu gom bằng Cơ cấu Gạt Cơ học (Mechanical Skimming):**
  - Hàm lượng chất rắn trong bùn nổi: Lấy $TS = 2.5\%$ (nằm trong khoảng $2.0 - 3.0\%$).
  - Khối lượng riêng bùn nổi gần bằng nước: $\rho_{\text{sludge}} \approx 1000\ \text{kg/m}^3$.
  - Thể tích bùn lỏng thu gom mỗi ngày:
    $$V_{\text{sludge, mech}} = \frac{M_{\text{dry}}}{\rho_{\text{sludge}} \times (TS / 100)} = \frac{1188.0}{1000 \times 0.025} = 47.52\ \text{m}^3/\text{day}$$
- **Trường hợp 2: Thu gom bằng Tràn Thủy lực (Hydraulic Skimming):**
  - Hàm lượng chất rắn loãng: $TS = 0.5\%$.
  - Thể tích bùn lỏng thu gom mỗi ngày:
    $$V_{\text{sludge, hyd}} = \frac{M_{\text{dry}}}{\rho_{\text{sludge}} \times (TS / 100)} = \frac{1188.0}{1000 \times 0.005} = 237.60\ \text{m}^3/\text{day}$$
- **So sánh thể tích và Đánh giá Lợi ích Kinh tế:**
  $$\frac{V_{\text{sludge, hyd}}}{V_{\text{sludge, mech}}} = \frac{237.60}{47.52} = 5.0\ \text{lần}$$
  - *Kết luận:* Gạt cơ học làm giảm thể tích bùn thải tới $5$ lần ($190.08\ \text{m}^3/\text{day}$), giúp tiết kiệm vượt trội chi phí đầu tư bể chứa bùn, đường ống, máy ép bùn và giảm $80\%$ hóa chất polymer xử lý bùn.

---

#### 6.6. Bảng Tổng hợp So sánh Kỹ thuật Giữa Hai Cấu hình (Comparative Technical Synthesis)

| Hạng mục So sánh Kỹ thuật | Ký hiệu | Đơn vị Đo | Chế độ A (Không Tuần hoàn) | Chế độ B (Có Tuần hoàn) | Nhận định Chuyên gia / Lý do Lựa chọn |
|---|---|---|---|---|---|
| Lưu lượng nước thải thô xử lý | $Q$ | $\text{m}^3/\text{day}$ | $400.0$ | $400.0$ | Công suất xử lý cơ sở không đổi |
| Tải lượng chất rắn lơ lửng | - | $\text{kg TSS/day}$ | $1200.0$ | $1200.0$ | $50.0\ \text{kg TSS/h}$ |
| Tỷ số Khí/Chất rắn yêu cầu | $A/S$ | $\text{mg/mg}$ | $0.008$ | $0.008$ | Điểm làm việc tối ưu |
| Khối lượng không khí hòa tan | $M_{\text{air}}$ | $\text{kg/day}$ | $9.60$ | $9.60$ | Nhu cầu bão hòa khí tương đương |
| Áp suất vận hành bình hòa khí | $P$ | $\text{atm}$ | $3.97$ | $5.0$ | Chế độ B chọn trước $P=5.0\ \text{atm}$ theo chuẩn bơm |
| Lưu lượng nén tuần hoàn | $R$ | $\text{m}^3/\text{day}$ | $0.0$ | $263.27$ | Chế độ B cần lưu lượng nén $11.0\ \text{m}^3/\text{h}$ |
| Tỷ lệ tuần hoàn | $r$ | $\%$ | $0\%$ | $65.82\%$ | Nằm trong dải tiêu chuẩn $15 - 120\%$ |
| Tổng lưu lượng vào bể DAF | $Q_{\text{total}}$ | $\text{m}^3/\text{day}$ | $400.0$ | $663.27$ | Chế độ B tăng tải thủy lực thêm $65.8\%$ |
| Tải trọng bề mặt thiết kế | $SLR$ | $\text{m}^3/(\text{m}^2\cdot\text{d})$ | $100.0$ | $100.0$ | Áp dụng theo Metcalf & Eddy |
| Diện tích mặt thoáng bể DAF | $A_{\text{tank}}$ | $\text{m}^2$ | $4.0$ | $6.75$ | Chế độ B diện tích bể lớn hơn $68.7\%$ |
| Kích thước bể chữ nhật ($L \times W \times H$) | - | $\text{m}$ | $3.46 \times 1.15 \times 2.0$ | $4.50 \times 1.50 \times 2.0$ | Cả hai đều thỏa mãn $L \le 11\ \text{m}, H \le 3\ \text{m}$ |
| Thể tích hữu ích bể DAF | $V_{\text{tank}}$ | $\text{m}^3$ | $8.0$ | $13.5$ | Chế độ B lớn hơn $5.5\ \text{m}^3$ |
| Thời gian lưu nước trong bể | $\theta$ | $\text{phút}$ | $28.8$ | $29.3$ | Cả hai đều đạt tối ưu trong dải $20 - 30\ \text{phút}$ |
| Đường kính bình áp lực | $D_{pv}$ | $\text{mm}$ | Không áp dụng | $450$ | Bình bão hòa đệm cao $2.0\ \text{m}$ |
| Khối lượng bùn khô thu hồi | $M_{\text{dry}}$ | $\text{kg/day}$ | $1188.0$ | $1188.0$ | Tại hiệu suất thu hồi $\eta = 99\%$ |
| Thể tích bùn lỏng (Gạt cơ học) | $V_{\text{sludge}}$ | $\text{m}^3/\text{day}$ | $47.52$ | $47.52$ | Tại độ khô $TS = 2.5\%$ |
| Nguy cơ vỡ bông cặn keo tụ | - | Đánh giá | Rất cao (xấu) | Không có (tuyệt vời) | **Chế độ B là tiêu chuẩn bắt buộc cho nước thải có hóa lý** |
| Nguy cơ tắc nghẽn vòi phun & bình | - | Đánh giá | Rất cao do cặn thô | Hoàn toàn triệt tiêu | Chế độ B chỉ nén nước đã lắng trong |
