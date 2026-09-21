## Chương 5: Quá trình Lắng (Sedimentation)


### 5.1 Tổng quan Quá trình Lắng và Cơ sở Lý thuyết Bốn Loại Lắng Cặn (Sedimentation Overview & Theoretical Principles of Four Settling Types)

#### 5.1.1 Mục tiêu Quá trình và Cân bằng Khối lượng Bùn Cặn (Process Objectives & Sludge Mass Balance)

##### 5.1.1.1 Vai trò của Quá trình Lắng trong Dây chuyền Xử lý Nước cấp
- **Khái niệm và bản chất vật lý**:
  - Quá trình lắng (Sedimentation / Clarification) tách các hạt rắn ra khỏi pha lỏng bằng trọng lực.
  - Quá trình diễn ra trong điều kiện dòng chảy tĩnh lặng hoặc chảy tầng ổn định.
- **Vị trí công nghệ trong dây chuyền**:
  - Vị trí sau bể keo tụ - tạo bông (Coagulation - Flocculation): Lắng các bông cặn hydroxit kim loại ($Al(OH)_3, Fe(OH)_3$) liên kết với hạt keo sét, hạt màu và vi sinh vật.
  - Vị trí sau công đoạn oxy hóa Sắt và Mangan (Fe/Mn Oxidation): Lắng các kết tủa oxyhydroxit ferric ($Fe(OH)_3$) và mangan dioxide ($MnO_2$).
  - Vị trí sau công đoạn làm mềm bằng vôi - soda (Lime-Soda Ash Softening): Lắng các tinh thể kết tủa canxi cacbonat ($CaCO_3$) và magie hydroxit ($Mg(OH)_2$).
- **Ngưỡng kích thước hạt lắng trọng lực**:
  - Trọng lực phân tách hiệu quả các hạt rắn có đường kính danh định lớn hơn $1\ \mu\text{m}$ ($d_p > 1\ \mu\text{m}$).
  - Hạt mịn dưới $1\ \mu\text{m}$ chịu chi phối mạnh bởi chuyển động nhiệt Brown và lực đẩy tĩnh điện.
  - Hạt mịn dưới $1\ \mu\text{m}$ không thể lắng tự nhiên trong thời gian lưu nước kinh tế ($t_0 \le 4\ \text{h}$).
  - Nhà máy phải keo tụ các hạt mịn này thành bông cặn lớn trước khi lắng.
- **Bảo vệ công trình lọc hạ nguồn**:
  - Bể lắng loại bỏ từ $80\%$ đến $95\%$ tổng lượng chất rắn lơ lửng (TSS) và độ đục của nước thô.
  - Quá trình lắng giúp giảm tải lượng cặn nạp lên các bể lọc nhanh trọng lực (Rapid Sand Filters).
  - Nước lắng tốt kéo dài chu kỳ lọc cát từ 24 đến 72 giờ.
  - Chu kỳ lọc dài giúp giảm lượng nước rửa lọc và giảm điện năng bơm rửa ngược.
- **Mục tiêu chất lượng nước sau lắng**:
  - Quy chuẩn QCVN 01-1:2018/BYT quy định độ đục nước sạch sau lọc nhỏ hơn hoặc bằng $2.0\ \text{NTU}$.
  - Mục tiêu kỹ thuật tối ưu sau lọc là nhỏ hơn hoặc bằng $0.5\ \text{NTU}$.
  - Độ đục của nước sau bể lắng phải kiểm soát trong ngưỡng:
    $$\text{Turbidity}_{\text{settled}} \le 2.0 - 5.0\ \text{NTU}$$
  - Nước sau lắng có độ đục lớn hơn $5.0\ \text{NTU}$ sẽ gây nghẹt nhanh lớp cát lọc.

##### 5.1.1.2 Cân bằng Vật chất và Phương trình Khối lượng Bùn Cặn Hàng ngày
- **Phương trình cân bằng khối lượng bùn khô tổng cộng**:
  - Lượng bùn khô sinh ra mỗi ngày bao gồm cặn lơ lửng ban đầu và các kết tủa hóa học:
    $$M_s = Q \cdot \left[(\text{TSS}_{\text{inf}} - \text{TSS}_{\text{eff}}) + K_{\text{alum}} \cdot \text{Dose}_{\text{alum}} + K_{\text{Fe}} \cdot \text{Dose}_{\text{Fe}} + 2.5 \cdot \text{CH}_{\text{rem}} + 1.8 \cdot \text{NCH}_{\text{rem}}\right] \times 10^{-3}$$
  - $M_s$: Khối lượng chất rắn bùn khô sinh ra mỗi ngày ($\text{kg dry solids/d}$).
  - $Q$: Lưu lượng nước xử lý của nhà máy ($\text{m}^3/\text{d}$).
  - $\text{TSS}_{\text{inf}}$: Hàm lượng chất rắn lơ lửng trong nước thô vào bể lắng ($\text{mg/L}$ hoặc $\text{g/m}^3$).
  - $\text{TSS}_{\text{eff}}$: Hàm lượng chất rắn lơ lửng trong nước sau lắng ($\text{mg/L}$).
  - $\text{Dose}_{\text{alum}}$: Liều lượng châm phèn nhôm thương phẩm $\text{Al}_2(\text{SO}_4)_3 \cdot 14\text{H}_2\text{O}$ ($\text{mg/L}$).
  - $K_{\text{alum}}$: Hệ số sinh bùn hydroxit nhôm khô thực tế ($0.26 - 0.44\ \text{kg Al(OH)}_3 / \text{kg alum}$).
  - $\text{Dose}_{\text{Fe}}$: Liều lượng châm phèn sắt thương phẩm ($\text{mg/L}$).
  - $K_{\text{Fe}}$: Hệ số sinh bùn hydroxit sắt khô ($1.35 - 1.91\ \text{kg Fe(OH)}_3 / \text{kg Fe}$).
  - $\text{CH}_{\text{rem}}$: Độ cứng cacbonat loại bỏ dưới dạng kết tủa $\text{CaCO}_3$ ($\text{mg/L as CaCO}_3$).
  - $\text{NCH}_{\text{rem}}$: Độ cứng phi cacbonat loại bỏ dưới dạng $\text{Mg(OH)}_2$ ($\text{mg/L as CaCO}_3$).
  - $10^{-3}$: Hệ số chuyển đổi đơn vị từ $\text{g}$ sang $\text{kg}$.
- **Hệ số sinh bùn hydroxit nhôm ($K_{\text{alum}}$)**:
  - Phản ứng thủy phân phèn nhôm thương phẩm:
    $$\text{Al}_2(\text{SO}_4)_3 \cdot 14\text{H}_2\text{O} + 3\text{Ca(HCO}_3)_2 \to 2\text{Al(OH)}_3\downarrow + 3\text{CaSO}_4 + 14\text{H}_2\text{O} + 6\text{CO}_2\uparrow$$
  - Khối lượng mol của $\text{Al}_2(\text{SO}_4)_3 \cdot 14\text{H}_2\text{O}$ bằng $594.4\ \text{g/mol}$.
  - Khối lượng kết tủa $2\text{Al(OH)}_3$ bằng $156.0\ \text{g/mol}$.
  - Hệ số sinh bùn lý thuyết:
    $$K_{\text{alum, theoretical}} = \frac{156.0}{594.4} \approx 0.2625\ \text{kg Al(OH)}_3 / \text{kg alum}$$
  - Thực tế thiết kế lấy $K_{\text{alum}} = 0.26 - 0.44$ do có thêm tạp chất và hidrat hóa.
- **Hệ số sinh bùn hydroxit sắt ($K_{\text{Fe}}$)**:
  - Phản ứng thủy phân của phèn sắt:
    $$\text{FeCl}_3 + 3\text{H}_2\text{O} \to \text{Fe(OH)}_3\downarrow + 3\text{HCl}$$
  - Một mol $\text{Fe}^{3+}$ ($55.85\ \text{g}$) sinh ra một mol $\text{Fe(OH)}_3$ ($106.87\ \text{g}$).
  - Hệ số sinh bùn theo khối lượng sắt nguyên chất:
    $$K_{\text{Fe}} = \frac{106.87}{55.85} = 1.913\ \text{kg Fe(OH)}_3 / \text{kg Fe}$$
  - Hệ số sinh bùn tính theo muối khan $\text{FeCl}_3$ bằng $0.659\ \text{kg Fe(OH)}_3 / \text{kg FeCl}_3$.
- **Hệ số sinh kết tủa làm mềm nước**:
  - Khử độ cứng canxi cacbonat bằng vôi tôi sinh ra kết tủa $\text{CaCO}_3$:
    $$\text{Ca(HCO}_3)_2 + \text{Ca(OH)}_2 \to 2\text{CaCO}_3\downarrow + 2\text{H}_2\text{O}$$
  - Khí $CO_2$ tự do trong nước cũng phản ứng với vôi tạo kết tủa:
    $$\text{CO}_2 + \text{Ca(OH)}_2 \to \text{CaCO}_3\downarrow + \text{H}_2\text{O}$$
  - Hệ số thực nghiệm trung bình đạt $2.5\ \text{kg kết tủa} / \text{kg CH loại bỏ}$.
  - Khử độ cứng magie phi cacbonat sinh ra kết tủa $\text{Mg(OH)}_2$ và $\text{CaCO}_3$:
    $$\text{Mg}^{2+} + \text{Ca(OH)}_2 + \text{Na}_2\text{CO}_3 \to \text{Mg(OH)}_2\downarrow + \text{CaCO}_3\downarrow + 2\text{Na}^+$$
  - Hệ số thực nghiệm trung bình đạt $1.8\ \text{kg kết tủa} / \text{kg NCH loại bỏ}$.
- **Thể tích bùn ướt hàng ngày ($V_{\text{sludge}}$)**:
  - Bùn lắng nước cấp có độ ẩm rất cao ($P = 97.0\% - 99.5\%$).
  - Nồng độ chất rắn khô chỉ chiếm $\%S = 0.5\% - 3.0\%$ theo khối lượng.
  - Tỷ trọng bùn ướt ($\text{SG}_{\text{sludge}}$) dao động từ $1.002$ đến $1.020$.
  - Công thức tính thể tích bùn ướt hàng ngày:
    $$V_{\text{sludge}} = \frac{M_s}{\rho_w \cdot \text{SG}_{\text{sludge}} \cdot \left(\frac{100 - P}{100}\right)} = \frac{M_s \times 100}{\rho_w \cdot \text{SG}_{\text{sludge}} \cdot \%S}$$
    - $V_{\text{sludge}}$: Thể tích bùn ướt xả ra mỗi ngày ($\text{m}^3/\text{d}$).
    - $\rho_w$: Khối lượng riêng của nước ($1,000\ \text{kg/m}^3$).
    - $P$: Độ ẩm bùn (%).
    - $\%S$: Phần trăm chất rắn khô trong bùn (%, $\%S = 100 - P$).
- **Định cỡ hố thu bùn và chu kỳ xả bùn**:
  - Hố thu bùn đáy bể phải chứa đủ thể tích bùn tích lũy giữa hai lần xả:
    $$V_{\text{hopper}} \ge V_{\text{sludge}} \cdot \frac{t_{\text{storage}}}{24}$$
    - $V_{\text{hopper}}$: Thể tích làm việc của hố thu bùn ($\text{m}^3$).
    - $t_{\text{storage}}$: Thời gian lưu bùn giữa hai chu kỳ xả ($\text{h}$, thường từ $8\ \text{h}$ đến $24\ \text{h}$).
  - Xả bùn chậm trễ gây phân hủy kỵ khí chất hữu cơ. Bọt khí sinh ra làm nổi mảng bùn lên mặt nước.

#### 5.1.2 Phân loại Bốn Cơ chế Lắng Trọng lực (Classification of Four Settling Regimes)

##### 5.1.2.1 Ma trận Phân loại theo Nồng độ và Tương tác Hạt
- **Bảng tổng hợp đặc tính bốn loại lắng**:

| Cơ chế Lắng | Tên Gọi Kỹ Thuật | Đặc Tính Hạt và Tương Tác | Nồng Độ Chất Rắn (TSS) | Mô Hình Lý Thuyết Chi Phối | Ứng Dụng Công Nghệ Thực Tế |
|---|---|---|---|---|---|
| **Type I** | Lắng hạt rời rạc (Discrete Settling) | Hạt rơi độc lập, không thay đổi kích thước, hình dạng hoặc khối lượng | Loãng ($< 500\ \text{mg/L}$) | Cân bằng lực Newton, Định luật Stokes, Bể lý tưởng Camp | Bể lắng cát, bể sơ lắng, lắng cát hạt rửa lọc |
| **Type II** | Lắng tạo bông (Flocculant Settling) | Hạt liên tục va chạm kết tụ, kích thước và vận tốc lắng tăng theo độ sâu | Loãng đến trung bình ($50 - 1,000\ \text{mg/L}$) | Cột lắng thực nghiệm, Tích phân đường cong đẳng nồng độ | Bể lắng sau keo tụ phèn nhôm, phèn sắt, kết tủa Fe/Mn |
| **Type III** | Lắng cản trở / Lắng vùng (Hindered / Zone Settling) | Hạt cản trở dòng chảy của nhau, lắng thành khối đệm bùn có ranh giới rõ | Đặc ($> 1,000\ \text{mg/L}$) | Lý thuyết thông lượng chất rắn (Solids Flux Theory), Kynch, Vesilind | Bể lắng tiếp xúc chất rắn, bể lắng làm mềm vôi, tầng đệm bùn |
| **Type IV** | Lắng nén ép (Compression Settling) | Hạt tựa cơ học lên nhau tạo khung xốp, nước lỗ rỗng bị nén ép thoát lên | Rất đặc ($> 10,000\ \text{mg/L}$) | Lý thuyết cố kết cơ học đất Terzaghi | Đáy hố thu cặn bể lắng, bể nén bùn trọng lực |

- **Bản chất lực tương tác giữa các hạt**:
  - Lắng Type I: Khoảng cách giữa các hạt rất lớn. Lực hút Van der Waals và lực đẩy tĩnh điện không tương tác.
  - Lắng Type II: Chênh lệch vận tốc rơi gây va chạm động học. Lực hút Van der Waals và cầu nối polymer dính kết các hạt.
  - Lắng Type III: Nồng độ hạt dày đặc. Dòng nước dâng qua khe hẹp tạo lực cản thủy động triệt tiêu chuyển động riêng lẻ.
  - Lắng Type IV: Các hạt tiếp xúc điểm trực tiếp. Cấu trúc khung hạt chịu tải trọng tĩnh của lớp cặn phía trên.

##### 5.1.2.2 Sự Đồng tồn tại của Bốn Tầng Lắng trong Bể Thực tế
- **Phân bố các tầng lắng theo chiều sâu**:
  - Tầng mặt và tầng nước trong (Clarified Zone): Lắng hạt rời rạc Type I đối với các hạt sót lại.
  - Tầng giữa (Clarification Zone): Lắng tạo bông Type II đối với các bông cặn đang kết tụ lớn dần.
  - Tầng màng bùn lơ lửng (Sludge Blanket Zone): Lắng cản trở Type III với ranh giới phân pha rõ rệt.
  - Tầng đáy và hố thu bùn (Sludge Hopper Zone): Lắng nén ép Type IV nén bùn đặc và thoát nước lỗ rỗng.
- **Ngưỡng nồng độ chuyển pha động học**:
  - Sự chuyển pha diễn ra liên tục theo nồng độ cặn $C(z, t)$.
  - Khi nồng độ vượt ngưỡng $800 - 1,200\ \text{mg/L}$, quá trình lắng chuyển hẳn từ Type II sang Type III.

#### 5.1.3 Lắng Hạt Rời rạc Type I và Thủy động lực học Hạt (Type I Discrete Settling Hydrodynamics)

##### 5.1.3.1 Cân bằng Ba Lực Newton trên Hạt Rơi Tự do
- **Trọng lực tác dụng thẳng đứng xuống dưới ($F_G$)**:
  - Trọng lực tỷ lệ thuận với thể tích và khối lượng riêng của hạt:
    $$F_G = \rho_s \cdot g \cdot V_p = \rho_s \cdot g \cdot \left(\frac{\pi}{6} d^3\right)$$
    - $F_G$: Trọng lực kéo hạt chìm xuống ($\text{N}$).
    - $\rho_s$: Khối lượng riêng của hạt rắn ($\text{kg/m}^3$, cát thạch anh bằng $2,650\ \text{kg/m}^3$).
    - $g$: Gia tốc trọng trường ($9.81\ \text{m/s}^2$).
    - $V_p$: Thể tích hình học của hạt hình cầu ($\text{m}^3$, $V_p = \frac{\pi}{6} d^3$).
    - $d$: Đường kính hình cầu tương đương của hạt ($\text{m}$).
- **Lực đẩy nổi Archimedes tác dụng thẳng đứng lên trên ($F_B$)**:
  - Lực đẩy nổi bằng trọng lượng chất lỏng bị hạt chiếm chỗ:
    $$F_B = \rho \cdot g \cdot V_p = \rho \cdot g \cdot \left(\frac{\pi}{6} d^3\right)$$
    - $F_B$: Lực đẩy nổi Archimedes ($\text{N}$).
    - $\rho$: Khối lượng riêng của nước ($\text{kg/m}^3$, tại $20^\circ\text{C}$ lấy $\rho = 998.2\ \text{kg/m}^3 \approx 1,000\ \text{kg/m}^3$).
- **Lực cản thủy động học hướng lên trên ($F_D$)**:
  - Chất lỏng tác dụng lực cản nhớt và lực cản áp suất ngược chiều chuyển động của hạt:
    $$F_D = C_D \cdot A_p \cdot \rho \cdot \frac{v^2}{2} = \frac{1}{2} C_D \cdot \left(\frac{\pi}{4} d^2\right) \cdot \rho \cdot v^2$$
    - $F_D$: Lực cản thủy động học ($\text{N}$).
    - $C_D$: Hệ số cản Newton (Newton drag coefficient, không thứ nguyên).
    - $A_p$: Diện tích cản của hạt vuông góc với hướng rơi ($\text{m}^2$, $A_p = \frac{\pi}{4} d^2$).
    - $v$: Vận tốc chuyển động tương đối của hạt đối với chất lỏng ($\text{m/s}$).
- **Cân bằng lực và vận tốc lắng giới hạn ($v_s$)**:
  - Định luật II Newton mô tả chuyển động rơi của hạt:
    $$m \frac{dv}{dt} = F_G - F_B - F_D$$
  - Khi hạt mới bắt đầu rơi, vận tốc $v = 0$ và lực cản $F_D = 0$. Gia tốc rơi đạt cực đại.
  - Vận tốc tăng làm lực cản $F_D$ tăng tỷ lệ thuận với $v^2$.
  - Sau thời gian rất ngắn ($< 0.1\ \text{s}$), lực cản cân bằng với trọng lượng hiệu dụng chìm trong nước:
    $$F_G = F_B + F_D \iff F_G - F_B = F_D$$
  - Khi lực cân bằng, gia tốc triệt tiêu hoàn toàn ($\frac{dv}{dt} = 0$). Hạt đạt vận tốc lắng giới hạn không đổi ($v_s$).

##### 5.1.3.2 Số Reynolds của Hạt và Ba Chế độ Chảy Thủy động
- **Phương trình xác định số Reynolds của hạt ($Re$)**:
  - Số Reynolds biểu thị tỷ số giữa lực quán tính và lực ma sát nhớt:
    $$Re = \frac{\rho \cdot v_s \cdot d}{\mu} = \frac{v_s \cdot d}{\nu}$$
    - $Re$: Số Reynolds của hạt (không thứ nguyên, ký hiệu tương đương là $R$).
    - $v_s$: Vận tốc lắng giới hạn của hạt ($\text{m/s}$).
    - $d$: Đường kính của hạt ($\text{m}$).
    - $\mu$: Độ nhớt động lực học của nước ($\text{Pa}\cdot\text{s}$, tại $20^\circ\text{C}$ $\mu = 1.002 \times 10^{-3}\ \text{Pa}\cdot\text{s}$).
    - $\nu$: Độ nhớt động học của nước ($\text{m}^2/\text{s}$, $\nu = \mu/\rho$, tại $20^\circ\text{C}$ $\nu = 1.004 \times 10^{-6}\ \text{m}^2/\text{s}$).
- **Đặc trưng lớp biên và đuôi xoáy**:
  - Ở $Re$ thấp ($Re \le 1.0$): Dòng chảy dính sát quanh hạt. Ma sát nhớt bề mặt chiếm ưu thế.
  - Ở $Re$ trung bình ($0.5 < Re < 10^4$): Lớp biên tách khỏi bề mặt sau hạt, hình thành xoáy áp suất thấp.
  - Ở $Re$ cao ($Re > 10^4$): Vùng xoáy cuộn hỗn loạn sau hạt chi phối toàn bộ lực cản.

##### 5.1.3.3 Hệ số Lực Cản Newton ($C_D$) theo Ba Vùng Chảy
- **Vùng chảy tầng (Laminar Flow Regime - Stokes' Law)**:
  - Áp dụng khi số Reynolds hạt $Re < 0.5$ (hoặc chấp nhận đến $Re \le 1.0$).
  - Ma sát nhớt thuần túy điều khiển chuyển động:
    $$C_D = \frac{24}{Re}$$
- **Vùng chảy chuyển tiếp (Transitional Flow Regime)**:
  - Áp dụng khi số Reynolds hạt nằm trong khoảng $0.5 < Re < 10^4$.
  - Công thức bán thực nghiệm Fair, Geyer & Okun mô tả hệ số cản:
    $$C_D = \frac{24}{Re} + \frac{3}{\sqrt{Re}} + 0.34$$
  - Thành phần $\frac{24}{Re}$ biểu thị ma sát tầng.
  - Thành phần $\frac{3}{\sqrt{Re}}$ biểu thị sự chuyển tiếp lớp biên.
  - Thành phần $0.34$ biểu thị lực cản xoáy quán tính.
- **Vùng chảy xoáy hoàn toàn (Fully Turbulent Flow Regime - Newton's Law)**:
  - Áp dụng khi số Reynolds hạt $Re > 10^4$.
  - Lực cản áp suất đuôi xoáy giữ hệ số cản gần như không đổi:
    $$C_D = 0.40 \approx 0.44$$

##### 5.1.3.4 Thiết lập Vận tốc Lắng Giới hạn ($v_s$)
- **Phương trình tổng quát cho mọi chế độ chảy**:
  - Xuất phát từ cân bằng ba lực $F_G - F_B = F_D$:
    $$(\rho_s - \rho) g \left(\frac{\pi}{6} d^3\right) = \frac{1}{2} C_D \left(\frac{\pi}{4} d^2\right) \rho v_s^2$$
  - Rút gọn phương trình và giải tìm $v_s$:
    $$v_s = \sqrt{\frac{4 g (\rho_s - \rho) d}{3 C_D \rho}} = \sqrt{\frac{4 g (\text{SG} - 1) d}{3 C_D}}$$
    - $\text{SG}$: Tỷ trọng tương đối của hạt so với nước ($\text{SG} = \rho_s/\rho$).
- **Định luật Stokes cho vùng chảy tầng ($Re \le 1.0$)**:
  - Thay hệ số cản $C_D = \frac{24}{Re} = \frac{24 \mu}{\rho v_s d}$ vào phương trình tổng quát:
    $$v_s = \frac{g (\rho_s - \rho) d^2}{18 \mu} = \frac{g (\text{SG} - 1) d^2}{18 \nu}$$
  - Vận tốc lắng tầng tỷ lệ thuận với bình phương kích thước hạt ($d^2$).
  - Vận tốc lắng tầng tỷ lệ nghịch với độ nhớt động lực học của nước ($\mu$).
- **Phương trình vận tốc cho vùng chảy xoáy ($Re > 10^4$)**:
  - Thay giá trị $C_D = 0.44$ vào phương trình tổng quát:
    $$v_s = \sqrt{\frac{4 g (\rho_s - \rho) d}{3 (0.44) \rho}} \approx 1.74 \sqrt{\frac{g (\rho_s - \rho) d}{\rho}}$$
  - Vận tốc lắng chảy xoáy chỉ tỷ lệ thuận với căn bậc hai của kích thước hạt ($\sqrt{d}$).
  - Vận tốc lắng chảy xoáy không phụ thuộc vào độ nhớt chất lỏng.

##### 5.1.3.5 Ảnh hưởng của Hình dạng Hạt và Độ Cầu
- **Khái niệm độ cầu ($\psi$)**:
  - Độ cầu xác định mức độ sai lệch hình học của hạt thực tế so với hình cầu lý tưởng:
    $$\psi = \frac{A_{\text{sphere}}}{A_{\text{particle}}} \le 1.0$$
    - $A_{\text{sphere}}$: Diện tích bề mặt hình cầu có cùng thể tích với hạt ($\text{m}^2$).
    - $A_{\text{particle}}$: Diện tích bề mặt thực tế của hạt ($\text{m}^2$).
  - Hạt cát tròn cạnh có độ cầu $\psi \approx 0.85 - 0.90$.
  - Hạt cát góc cạnh có độ cầu $\psi \approx 0.65 - 0.75$.
  - Bông cặn phèn phân nhánh có độ cầu $\psi \approx 0.50 - 0.60$.
- **Hiệu chỉnh thủy động học cho hạt không tròn**:
  - Hạt góc cạnh có diện tích cản gió lớn hơn và gây tách dòng sớm hơn.
  - Hệ số cản thực tế lớn hơn hệ số cản của hình cầu tương đương.
  - Vận tốc lắng thực tế giảm từ $15\%$ đến $40\%$ so với tính toán lý thuyết Stokes.

##### 5.1.3.6 Quy trình Tính toán Lặp Vận tốc Lắng Hạt Rời rạc
1. Xác định đường kính hạt $d$ và khối lượng riêng hạt $\rho_s$ (hoặc tỷ trọng $\text{SG}$).
2. Tra cứu khối lượng riêng nước $\rho$, độ nhớt động lực $\mu$ và độ nhớt động học $\nu$ theo nhiệt độ $T$.
3. Giả thiết hạt rơi trong vùng chảy tầng ($Re \le 1.0$).
4. Tính vận tốc lắng ban đầu theo Định luật Stokes:
   $$v_s = \frac{g (\rho_s - \rho) d^2}{18 \mu}$$
5. Tính số Reynolds tương ứng của hạt:
   $$Re = \frac{\rho \cdot v_s \cdot d}{\mu}$$
6. Kiểm tra điều kiện số Reynolds:
   - Nếu $Re \le 1.0$: Kết luận giả thiết chảy tầng đúng. Vận tốc Stokes là giá trị chính xác.
   - Nếu $0.5 < Re < 10^4$: Dòng chảy thuộc vùng chuyển tiếp. Thực hiện bước tính lặp tiếp theo.
   - Nếu $Re \ge 10^4$: Dòng chảy xoáy. Áp dụng $C_D = 0.44$ và tính trực tiếp vận tốc xoáy.
7. Tính hệ số cản $C_D$ chuyển tiếp:
   $$C_D = \frac{24}{Re} + \frac{3}{\sqrt{Re}} + 0.34$$
8. Tính lại vận tốc lắng $v_{s,\text{new}}$ từ phương trình tổng quát:
   $$v_{s,\text{new}} = \sqrt{\frac{4 g (\rho_s - \rho) d}{3 C_D \rho}}$$
9. Tính lại $Re_{\text{new}}$ theo $v_{s,\text{new}}$.
10. Lặp lại bước 7 đến bước 9 cho đến khi sai số giữa hai lần lặp nhỏ hơn $1\%$.

##### 5.1.3.7 Bài tập Tính toán Thực hành Lắng Hạt Type I

<!-- exercise-start: Ví dụ 5-1: Tính vận tốc lắng giới hạn của hạt cát trong vùng chảy chuyển tiếp -->
- **Ví dụ 5-1: Tính vận tốc lắng giới hạn của hạt cát trong vùng chảy chuyển tiếp**
  - **Cho**:
    - Bán kính hạt cát: $r = 0.10\ \text{mm} = 1.0 \times 10^{-4}\ \text{m}$.
    - Đường kính hạt cát: $d = 2 \cdot r = 0.20\ \text{mm} = 2.0 \times 10^{-4}\ \text{m}$.
    - Tỷ trọng hạt cát: $\text{SG} = 2.65$ ($\rho_s = 2,650\ \text{kg/m}^3$).
    - Nhiệt độ nước: $T = 20^\circ\text{C}$.
    - Khối lượng riêng nước: $\rho = 1,000\ \text{kg/m}^3$.
    - Độ nhớt động lực học nước: $\mu = 1.002 \times 10^{-3}\ \text{Pa}\cdot\text{s}$.
    - Gia tốc trọng trường: $g = 9.81\ \text{m/s}^2$.
  - **Tìm**:
    - Vận tốc lắng giới hạn $v_s$ của hạt cát.
    - Kiểm tra chế độ chảy của dòng chất lỏng quanh hạt.
  - **Phương trình áp dụng**:
    $$v_{s,\text{Stokes}} = \frac{g (\rho_s - \rho) d^2}{18 \mu}$$
    $$Re = \frac{\rho \cdot v_s \cdot d}{\mu}$$
    $$C_D = \frac{24}{Re} + \frac{3}{\sqrt{Re}} + 0.34$$
    $$v_s = \sqrt{\frac{4 g (\rho_s - \rho) d}{3 C_D \rho}}$$
  - **Các bước giải**:
    1. Giả thiết dòng chảy tầng ($Re \le 1.0$) và tính vận tốc Stokes ban đầu:
       $$v_s = \frac{9.81 \cdot (2650 - 1000) \cdot (2.0 \times 10^{-4})^2}{18 \cdot (1.002 \times 10^{-3})} = \frac{9.81 \cdot 1650 \cdot 4.0 \times 10^{-8}}{0.018036} = 0.0359\ \text{m/s} = 3.59\ \text{cm/s}$$
    2. Kiểm tra số Reynolds với vận tốc Stokes vừa tìm:
       $$Re = \frac{1000 \cdot 0.0359 \cdot (2.0 \times 10^{-4})}{1.002 \times 10^{-3}} = 7.17$$
       Vì $Re = 7.17 > 1.0$, giả thiết chảy tầng sai. Hạt chuyển động trong vùng chảy chuyển tiếp ($0.5 < Re < 10^4$). Công thức Stokes tính thừa vận tốc khoảng $47.5\%$.
    3. Bước lặp 1:
       $$C_D = \frac{24}{7.17} + \frac{3}{\sqrt{7.17}} + 0.34 = 3.347 + 1.120 + 0.340 = 4.807$$
       $$v_s = \sqrt{\frac{4 \cdot 9.81 \cdot 1650 \cdot (2.0 \times 10^{-4})}{3 \cdot 4.807 \cdot 1000}} = \sqrt{\frac{12.9492}{14421}} = 0.0300\ \text{m/s}$$
       $$Re = \frac{1000 \cdot 0.0300 \cdot (2.0 \times 10^{-4})}{1.002 \times 10^{-3}} = 5.98$$
    4. Bước lặp 2:
       $$C_D = \frac{24}{5.98} + \frac{3}{\sqrt{5.98}} + 0.34 = 4.013 + 1.227 + 0.340 = 5.580$$
       $$v_s = \sqrt{\frac{12.9492}{3 \cdot 5.580 \cdot 1000}} = 0.0278\ \text{m/s}$$
       $$Re = \frac{1000 \cdot 0.0278 \cdot (2.0 \times 10^{-4})}{1.002 \times 10^{-3}} = 5.55$$
    5. Bước lặp 3:
       $$C_D = \frac{24}{5.55} + \frac{3}{\sqrt{5.55}} + 0.34 = 4.324 + 1.274 + 0.340 = 5.938$$
       $$v_s = \sqrt{\frac{12.9492}{3 \cdot 5.938 \cdot 1000}} = 0.0270\ \text{m/s}$$
       $$Re = \frac{1000 \cdot 0.0270 \cdot (2.0 \times 10^{-4})}{1.002 \times 10^{-3}} = 5.39$$
    6. Bước lặp 4: Kết quả hội tụ chính xác:
       $$C_D = 6.45$$
       $$v_s = 0.0245\ \text{m/s} = 2.45\ \text{cm/s}$$
       $$Re = 4.88$$
  - **Đáp số**:
    `v_s = 2.45 cm/s (0.0245 m/s); Re = 4.88; C_D = 6.45`
<!-- exercise-end -->

#### 5.1.4 Lắng Keo tụ Tạo bông Type II và Phân tích Cột Lắng (Type II Flocculant Settling & Column Analysis)

##### 5.1.4.1 Cơ chế Động học Kết tụ Bông Cặn
- **Va chạm động học trong quá trình lắng**:
  - Hạt lớn có vận tốc lắng nhanh đuổi kịp hạt nhỏ lắng chậm hơn trên cùng đường rơi.
  - Các va chạm này kích thích dính kết bề mặt tạo thành bông cặn lớn hơn.
  - Kích thước hạt tăng dần theo chiều sâu rơi ($d_p \uparrow$).
  - Vận tốc rơi của hạt gia tốc phi tuyến theo độ sâu lắng ($v_s = f(z)$).
- **Nguyên nhân Định luật Stokes không áp dụng cho Type II**:
  - Kích thước hạt biến thiên liên tục trong suốt hành trình lắng.
  - Bông cặn ngậm nước trong các vi lỗ rỗng. Khi bông lớn dần, khối lượng riêng giảm tiệm cận với nước ($\rho_s \to \rho_w$).
  - Hình dạng bông cặn bất đối xứng và dễ biến dạng dưới ứng suất cắt.
  - Thiết kế bể lắng cho cặn Type II bắt buộc phải dùng số liệu đo đạc thực nghiệm từ cột lắng.

##### 5.1.4.2 Quy trình Thí nghiệm Cột Lắng
- **Cấu tạo thiết bị cột lắng thí nghiệm**:
  - Cột lắng chế tạo bằng ống mica trong suốt hoặc thủy tinh chịu lực.
  - Đường kính trong của cột từ $10\ \text{cm}$ đến $20\ \text{cm}$ để triệt tiêu ma sát thành ống.
  - Chiều cao cột tương đương chiều sâu bể lắng thực tế ($H = 2.0 - 3.0\ \text{m}$).
  - Cổng lấy mẫu bố trí dọc thân cột cách nhau khoảng đều $\Delta h = 0.5\ \text{m}$.
- **Các bước tiến hành thí nghiệm cột lắng**:
  1. Lấy mẫu nước sau bể tạo bông và nạp đầy vào cột lắng.
  2. Khuấy nhẹ phân tán đều mẫu để nồng độ ban đầu $C_0$ đồng nhất trên toàn chiều cao cột.
  3. Đặt cột lắng trong môi trường đẳng nhiệt và tĩnh lặng hoàn toàn.
  4. Bắt đầu bấm giờ tại thời điểm $t = 0$.
  5. Rút mẫu thể tích nhỏ ($50 - 100\ \text{mL}$) tại các độ sâu định trước theo từng mốc thời gian ($10, 20, 30, 45, 60, 90, 120\ \text{phút}$).
  6. Sấy khô mẫu ở $105^\circ\text{C}$ và cân xác định nồng độ cặn lơ lửng $C_t$.
- **Xác định hiệu suất loại bỏ cặn từng điểm ($R\%$)**:
  - Hiệu suất loại bỏ chất rắn lơ lửng tại độ sâu $h$ và thời điểm $t$:
    $$R\% = \frac{C_0 - C_t}{C_0} \times 100\%$$
    - $R\%$: Phần trăm cặn lơ lửng đã lắng qua vị trí lấy mẫu (%).
    - $C_0$: Nồng độ chất rắn lơ lửng đồng nhất ban đầu trong cột ($\text{mg/L}$).
    - $C_t$: Nồng độ chất rắn lơ lửng đo được tại độ sâu $h$ ở thời điểm $t$ ($\text{mg/L}$).

##### 5.1.4.3 Đường cong Đẳng nồng độ trên Không gian Pha Thời gian - Độ sâu
- **Thiết lập lưới đường cong đẳng nồng độ**:
  - Trục hoành biểu diễn thời gian lắng $t$ ($\text{min}$).
  - Trục tung biểu diễn độ sâu cột lắng $h$ ($\text{m}$, gốc $h = 0$ ở mặt nước, chiều dương hướng xuống đáy).
  - Điền các giá trị $R\%$ đo được vào các tọa độ thực nghiệm $(t, h)$.
  - Nội suy đường cong nối các điểm có cùng giá trị phần trăm loại bỏ ($40\%, 50\%, 60\%, 70\%, 80\%$).
- **Đặc trưng độ cong nhận diện hạt lắng**:
  - Hạt Type I (rời rạc): Vận tốc rơi không đổi. Các đường đẳng nồng độ là các đường thẳng qua gốc tọa độ ($h = v_s \cdot t$).
  - Hạt Type II (tạo bông): Vận tốc rơi gia tốc theo độ sâu. Các đường đẳng nồng độ có bề lõm hướng xuống dưới.

##### 5.1.4.4 Tích phân Hình thang Tính Tổng Hiệu suất Loại bỏ Cặn
- **Phương trình tích phân hình thang theo độ sâu**:
  - Tại thời gian lưu thiết kế $t_0$, tổng hiệu suất loại bỏ cặn tính bằng công thức:
    $$R_{\text{total}} = R_0 + \sum_{i=1}^n \frac{\Delta h_i}{H} \cdot \left(\frac{R_i + R_{i-1}}{2}\right)$$
    - $R_{\text{total}}$: Tổng phần trăm chất rắn lơ lửng bể lắng loại bỏ (%).
    - $R_0$: Giá trị đường đẳng nồng độ chạm đáy cột $H$ tại thời gian $t_0$ (%). Toàn bộ phần này lắng $100\%$.
    - $H$: Chiều sâu làm việc của bể lắng ($\text{m}$).
    - $\Delta h_i$: Khoảng cách thẳng đứng giữa hai đường đẳng nồng độ kề nhau tại thời gian $t_0$ ($\text{m}$).
    - $R_i, R_{i-1}$: Phần trăm loại bỏ của hai đường đẳng nồng độ liền kề (%).
- **Trình tự giải tích đồ họa**:
  1. Dựng đường gióng thẳng đứng tại thời điểm thiết kế $t = t_0$.
  2. Xác định giao điểm của đường gióng với đáy cột $H$ để tìm $R_0$.
  3. Đo các khoảng cách thẳng đứng $\Delta h_i$ giữa các đường đẳng nồng độ cắt đường gióng $t_0$.
  4. Tính tích phân diện tích theo công thức hình thang để tìm $R_{\text{total}}$.

##### 5.1.4.5 Hệ số An toàn Phóng to Hiện trường (Field Scale-Up Factors)
- **Hệ số phóng to thời gian lưu nước ($t_{0,\text{field}}$)**:
  - Cột lắng trong phòng thí nghiệm tĩnh lặng lý tưởng. Bể lắng thực tế chịu nhiều xáo trộn thủy lực.
  - Kỹ sư nhân thời gian lưu cột lắng với hệ số an toàn:
    $$t_{0,\text{field}} = (1.25 - 1.75) \times t_{0,\text{lab}}$$
    - Giá trị thiết kế thông dụng chọn hệ số bằng $1.50$.
- **Hệ số giảm tải trọng bề mặt ($\text{SOR}_{\text{field}}$)**:
  - Tải trọng bề mặt thực tế phải giảm so với kết quả thí nghiệm:
    $$\text{SOR}_{\text{field}} = (0.65 - 0.85) \times \text{SOR}_{\text{lab}}$$
    - Giá trị thiết kế thông dụng chọn hệ số bằng $0.70$.
- **Bốn nguyên nhân thủy lực làm giảm hiệu quả lắng ngoài hiện trường**:
  1. Dòng xáo trộn cửa vào: Dòng nước vào bể phân bố không đều tạo xoáy cuộn cục bộ.
  2. Dòng đối lưu mật độ do nhiệt: Nước thô chênh lệch $0.5^\circ\text{C}$ so với nước trong bể sinh ra dòng chảy ngắn.
  3. Ma sát gió trên mặt thoáng: Gió thổi trên mặt nước gây dòng chảy bề mặt và dòng hoàn lưu đáy xới cặn.
  4. Lực hút dâng ở máng tràn: Tải trọng máng quá lớn tạo lực hút cuốn các bông cặn ra ngoài.

#### 5.1.5 Lắng Cản trở Type III và Lắng Nén ép Type IV (Type III Hindered & Type IV Compression Settling)

##### 5.1.5.1 Động học Huyền phù Đặc Nồng độ Cao (> 1,000 mg/L)
- **Cơ chế thủy động của huyền phù đặc**:
  - Khi nồng độ cặn vượt $1,000\ \text{mg/L}$, khoảng cách giữa các hạt rất nhỏ.
  - Các hạt cùng rơi xuống đẩy một thể tích nước tương đương dâng ngược lên qua các khe hở hẹp.
  - Dòng nước dâng tạo lực cản nhớt mạnh làm chậm tốc độ rơi của toàn bộ tập hợp hạt.
- **Hình thành ranh giới phân pha màng bùn**:
  - Các hạt liên kết với nhau thành một khối màng bùn xốp đồng nhất (sludge blanket).
  - Mặt trên của màng bùn hạ thấp dần, tạo ranh giới phân tách rõ giữa nước trong bên trên và bùn đặc bên dưới.
  - Hiện tượng này gọi là Lắng vùng (Zone Settling) hoặc Lắng cản trở (Hindered Settling).

##### 5.1.5.2 Phân tầng Cột Lắng Gián đoạn (Bốn Phân vùng A, B, C, D)
- **Đặc trưng bốn vùng phân tầng theo chiều cao**:
  - Vùng A (Tầng nước trong - Supernatant Clarified Zone): Nằm trên cùng, cặn đã lắng hết, nước trong hoàn toàn. Chiều dày tăng dần theo thời gian.
  - Vùng B (Tầng nồng độ ban đầu đồng nhất - Uniform Settling Zone): Nồng độ cặn giữ nguyên bằng nồng độ ban đầu $C_0$. Ranh giới hạ xuống với vận tốc không đổi $v_i$.
  - Vùng C (Tầng chuyển tiếp cô đặc - Transition Zone): Nồng độ cặn tăng dần theo độ sâu, vận tốc lắng giảm dần do cản trở cơ học.
  - Vùng D (Tầng nén ép cặn đáy - Compression Layer): Các hạt cặn tựa trực tiếp lên nhau, tạo khung xốp chịu lực ở đáy bể.

##### 5.1.5.3 Phân tích Đường cong Suy giảm Mặt Bùn theo Thời gian
- **Đoạn suy giảm tuyến tính với vận tốc không đổi**:
  - Đồ thị biểu diễn chiều cao mặt phân cách bùn $H_i$ theo thời gian $t$.
  - Ở giai đoạn đầu, mặt bùn hạ thấp với tốc độ tuyến tính ổn định.
  - Vận tốc lắng cản trở $v_i$ chính là độ dốc của đoạn thẳng này:
    $$v_i = -\frac{dH_i}{dt} = \text{const}$$
- **Giai đoạn giảm tốc độ hạ mặt bùn**:
  - Vùng đồng nhất B thu hẹp và biến mất. Mặt bùn tiếp xúc với vùng chuyển tiếp C.
  - Độ dốc đồ thị thoải dần do nồng độ hạt tăng làm tăng lực cản cơ học.
- **Xác định Điểm nén bằng Phương pháp Đồ họa Talmadge-Fitch**:
  1. Kẻ đường tiếp tuyến thứ nhất với đoạn thẳng tuyến tính ban đầu (vận tốc lắng cản trở $v_i$).
  2. Kẻ đường tiếp tuyến thứ hai với đoạn tiệm cận nằm ngang của giai đoạn nén cặn cuối cùng.
  3. Kẻ đường phân giác của góc nhọn tạo bởi hai đường tiếp tuyến trên.
  4. Xác định giao điểm của đường phân giác với đường cong lắng thực nghiệm. Giao điểm này là Điểm nén (Compression Point) với tọa độ $(t_c, H_c)$.

##### 5.1.5.4 Mô hình Vận tốc Lắng Cản trở Vesilind
- **Phương trình hàm mũ Vesilind (1968)**:
  - Vận tốc lắng cản trở giảm theo hàm mũ khi nồng độ cặn $C$ tăng:
    $$v_i = v_0 \cdot e^{-k \cdot C}$$
    - $v_i$: Vận tốc lắng cản trở của màng bùn ở nồng độ $C$ ($\text{m/h}$).
    - $v_0$: Vận tốc lắng tối đa lý thuyết khi độ pha loãng vô cùng ($C \to 0$) ($\text{m/h}$).
    - $k$: Hệ số cản trở thực nghiệm phụ thuộc vào đặc tính bông cặn ($\text{m}^3/\text{kg}$ hoặc $\text{L/g}$).
    - $C$: Nồng độ chất rắn lơ lửng trong huyền phù ($\text{kg/m}^3$ hoặc $\text{g/L}$).

##### 5.1.5.5 Lý thuyết Thông lượng Chất rắn (Solids Flux Theory - SFT)
- **Phương trình tổng thông lượng chất rắn chuyển động xuống đáy**:
  - Bể lắng kết hợp cô đặc bùn (Clarifier-Thickener) có tổng thông lượng cặn bằng tổng thông lượng lắng trọng lực và thông lượng rút bùn đáy:
    $$G_{\text{total}} = G_g + G_u = C \cdot v_i + C \cdot u_b = C \cdot v_i + C \cdot \frac{Q_u}{A}$$
    - $G_{\text{total}}$: Tổng thông lượng chất rắn đi xuống đáy ($\text{kg/m}^2\cdot\text{h}$).
    - $G_g$: Thông lượng cặn do lắng trọng lực cản trở ($\text{kg/m}^2\cdot\text{h}$, $G_g = C \cdot v_i$).
    - $G_u$: Thông lượng cặn do bơm rút bùn đáy tạo ra ($\text{kg/m}^2\cdot\text{h}$, $G_u = C \cdot u_b$).
    - $C$: Nồng độ chất rắn lơ lửng tại mặt cắt tính toán ($\text{kg/m}^3$).
    - $v_i$: Vận tốc lắng cản trở ở nồng độ $C$ ($\text{m/h}$).
    - $u_b$: Vận tốc khối chất lỏng chuyển động xuống do rút bùn ($\text{m/h}$, $u_b = Q_u / A$).
    - $Q_u$: Lưu lượng bùn xả đáy rút ra khỏi công trình ($\text{m}^3/\text{h}$).
    - $A$: Diện tích mặt bằng đáy bể lắng cô đặc ($\text{m}^2$).
- **Đặc tuyến thông lượng trọng lực ($G_g = C \cdot v_i$)**:
  - Khi $C \to 0$, nồng độ cặn nhỏ khiến thông lượng $G_g$ rất bé.
  - Khi $C$ rất lớn, vận tốc $v_i \to 0$ khiến thông lượng $G_g$ cũng triệt tiêu.
  - Đồ thị $G_g(C)$ có một đỉnh cực đại và một điểm trũng cực tiểu địa phương.
- **Đặc tuyến thông lượng rút bùn ($G_u = C \cdot u_b$)**:
  - Thông lượng rút bùn là đường thẳng bậc nhất đi qua gốc tọa độ.
  - Độ dốc của đường thẳng bằng chính vận tốc rút nước bùn $u_b$.
- **Phân tích điểm trạng thái và thông lượng giới hạn ($G_L$)**:
  - Đồ thị tổng thông lượng $G_{\text{total}}(C)$ xuất hiện một giá trị cực tiểu địa phương gọi là Thông lượng giới hạn ($G_L$).
  - Giá trị $G_L$ tương ứng với nồng độ nghẽn mạch dòng chảy bùn ($C_L$).
  - Nếu tải lượng cặn cấp vào bể vượt quá $G_L$, bùn sẽ ứ đọng tại tầng nồng độ $C_L$. Mặt bùn sẽ dâng cao và tràn ra máng thu nước trong.
- **Tính toán diện tích mặt bằng cô đặc bùn ($A_{\text{thickening}}$)**:
  - Diện tích mặt bằng tối thiểu để bể lắng hoàn thành chức năng cô đặc bùn:
    $$A_{\text{thickening}} = \frac{Q_0 \cdot C_0}{G_L}$$
    - $Q_0$: Lưu lượng nước cấp vào bể ($\text{m}^3/\text{h}$).
    - $C_0$: Nồng độ chất rắn lơ lửng đi vào bể ($\text{kg/m}^3$).
    - $G_L$: Thông lượng cặn giới hạn xác định từ đồ thị thông lượng ($\text{kg/m}^2\cdot\text{h}$).
  - Diện tích thiết kế thực tế của bể chọn theo giá trị lớn hơn giữa diện tích làm trong và diện tích nén bùn:
    $$A_{\text{basin}} = \max(A_{\text{clarification}}, A_{\text{thickening}})$$

##### 5.1.5.6 Cơ chế Lắng Nén ép Type IV và Mô hình Cố kết Terzaghi
- **Mô hình tương tự cố kết cơ học đất Karl Terzaghi**:
  - Quá trình nén ép bùn cặn tương tự như sự cố kết đất ngập nước.
  - Các hạt cặn đã tựa trực tiếp lên nhau tạo thành khung xương xốp chịu lực.
  - Ứng suất tổng cộng gồm ứng suất hiệu dụng khung hạt và áp lực nước lỗ rỗng:
    $$\sigma = \sigma' + u$$
    - $\sigma$: Ứng suất tổng cộng của các tầng cặn đè lên ($\text{N/m}^2$).
    - $\sigma'$: Ứng suất hiệu dụng do khung xương hạt gánh chịu ($\text{N/m}^2$).
    - $u$: Áp lực thủy tĩnh của nước trong lỗ rỗng ($\text{N/m}^2$).
- **Động học nén ép giải phóng nước mao quản**:
  - Quá trình lắng nén ép thực chất là sự thoát nước từ các lỗ rỗng mao dẫn lên trên.
  - Bùn càng nén chặt, độ rỗng càng giảm, hệ số thấm của khối bùn giảm theo hàm mũ.
  - Tốc độ nén ép chậm dần theo thời gian và tiệm cận độ ẩm cân bằng giới hạn.
- **Tác dụng của cánh khuấy cọc quay chậm**:
  - Bể nén bùn trang bị các cọc khuấy thẳng đứng quay rất chậm ($v = 0.02 - 0.05\ \text{m/s}$).
  - Cánh khuấy cọc tạo các rãnh thẳng đứng nhân tạo trong khối bùn đặc.
  - Nước lỗ rỗng theo các rãnh này thoát nhanh lên bề mặt, tăng tốc độ cô đặc bùn.

### 5.2 Bể Lắng Ngang Lý Tưởng Camp và Hệ Thống Máng Ngón Tay Thu Nước Trong (Camp's Ideal Horizontal Basin & Effluent Launders)

#### 5.2.1 Mô hình Lý thuyết Bể Lắng Ngang Lý tưởng Camp (Camp's Rational Ideal Basin Model)

##### 5.2.1.1 Bảy Giả thiết Cơ bản của Thomas R. Camp (Camp's Seven Assumptions)
- Thomas R. Camp thiết lập mô hình toán học giải tích cho bể lắng lý tưởng vào năm 1936 và 1946.
- Mô hình áp dụng bảy giả thiết thủy lực và cơ học:
  1. **Chế độ lắng hạt rời rạc Type I**: Hạt lắng độc lập trong suốt quá trình lắng. Hạt không thay đổi kích thước, hình dạng hoặc khối lượng riêng. Không xảy ra hiện tượng tạo bông hoặc vỡ hạt.
  2. **Bốn vùng thủy lực phân định riêng biệt**: Thể tích bể chia thành bốn vùng không chồng lấn. Bốn vùng gồm Vùng vào (Inlet Zone), Vùng lắng (Settling Zone), Vùng bùn (Sludge Zone) và Vùng ra (Outlet Zone).
  3. **Phân phối lưu lượng đồng đều ở vùng vào**: Dòng nước đi vào vùng lắng phân bố đều trên toàn bộ mặt cắt ướt ngang. Vận tốc dòng chảy ngang $v_h$ có độ lớn và hướng đồng nhất tại mọi điểm.
  4. **Thu nước đồng đều ở vùng ra**: Máng thu nước rút nước đều trên toàn bộ chiều rộng bể. Dòng chảy rời khỏi vùng lắng có vận tốc đồng nhất.
  5. **Phân bố cặn đồng đều theo chiều sâu đầu vào**: Cặn phân bố nồng độ đồng nhất trên toàn bộ chiều sâu $H$ tại mặt cắt bắt đầu vùng lắng ($x = 0$).
  6. **Bắt giữ cặn vĩnh viễn trong vùng bùn**: Bất kỳ hạt cặn nào chạm đáy vùng lắng đều bị giữ lại hoàn toàn. Dòng chảy không gây xới cặn hoặc cuốn trôi cặn ngược lại.
  7. **Hạt đi vào vùng ra bị cuốn trôi**: Hạt cặn chưa chạm đáy trước ranh giới vùng ra sẽ thoát ra ngoài theo dòng nước tràn.
- **Ý nghĩa kỹ thuật và giới hạn thực tế**:
  - Bể lắng thực tế luôn chịu ảnh hưởng của dòng chảy ngắn (short-circuiting).
  - Gió bề mặt và chênh lệch nhiệt độ tạo dòng xoáy hoàn lưu.
  - Mô hình Camp thiết lập chuẩn so sánh lý thuyết để định cỡ kích thước hình học bể.

##### 5.2.1.2 Bốn Vùng Chức năng Thủy lực (Four Functional Hydraulic Zones)
- **Vùng vào (Inlet Zone)**:
  - Vị trí: Đầu bể lắng.
  - Chức năng: Tiếp nhận nước từ bể tạo bông với vận tốc từ $0.4\text{ m/s}$ đến $0.8\text{ m/s}$.
  - Nhiệm vụ: Triệt tiêu động năng dư thừa. Phân bố đều các đường dòng trên toàn bộ mặt cắt ướt trước khi vào vùng lắng.
  - Cấu tạo: Kênh phân phối nước, tấm chắn triệt tiêu động năng (target baffles) và vách ngăn đục lỗ (perforated baffle wall).
  - Thông số thiết kế vách đục lỗ:
    - Đường kính lỗ khoét: $d_{\text{port}} = 50 - 150\text{ mm}$ (thông dụng $75 - 100\text{ mm}$).
    - Vận tốc nước qua lỗ: $v_{\text{port}} = 0.15 - 0.30\text{ m/s}$. Vận tốc này ngăn vỡ bông cặn và phân bố đều dòng chảy.
    - Tổn thất áp lực qua vách đục lỗ: $h_L = 10 - 25\text{ mm}$ cột nước.
    - Tổng diện tích lỗ mở: Chiếm $10\% - 20\%$ diện tích mặt cắt ướt ngang của bể.
- **Vùng lắng (Settling Zone)**:
  - Vị trí: Thân bể nằm giữa vùng vào và vùng ra.
  - Chức năng: Cung cấp không gian tĩnh lặng cho hạt cặn lắng bằng trọng lực.
  - Chế độ dòng chảy: Dòng chảy nút lý tưởng (plug flow).
  - Vận tốc ngang trung bình của dòng nước:
    $$v_h = \frac{Q}{A_x} = \frac{Q}{W \cdot H}$$
    - $v_h$: Vận tốc dòng chảy ngang trung bình ($\text{m/s}$ hoặc $\text{mm/s}$).
    - $Q$: Lưu lượng nước qua bể ($\text{m}^3/\text{s}$).
    - $A_x$: Diện tích mặt cắt ướt ngang vùng lắng ($\text{m}^2$, $A_x = W \cdot H$).
    - $W$: Chiều rộng vùng lắng ($\text{m}$).
    - $H$: Chiều sâu nước lắng hữu ích ($\text{m}$).
  - Chuyển động của hạt: Hạt di chuyển ngang theo vận tốc nước $v_h$ và rơi thẳng đứng với vận tốc lắng $v_s$.
- **Vùng bùn (Sludge Zone)**:
  - Vị trí: Dưới đáy vùng lắng.
  - Chức năng: Thu gom và chứa cặn đã lắng.
  - Nhiệm vụ: Cách ly lớp cặn khỏi trường vận tốc ngang của vùng lắng để ngăn cuốn xới cặn.
  - Cấu tạo: Đáy bê tông tạo dốc và các hố thu cặn hình kim tự tháp cụt (pyramidal sludge hoppers).
  - Thông số độ dốc:
    - Độ dốc sàn đáy bể khi có máy cào bùn: $1:600$ đến $1:100$ ($0.17\% - 1.0\%$).
    - Độ dốc sàn đáy bể khi xả bùn thủy lực tự do: $\ge 1:50$ ($2.0\%$).
    - Góc nghiêng vách hố thu cặn: $\theta_{\text{hopper}} \ge 45^\circ - 60^\circ$ (bông cặn phèn nhôm ưu tiên $\ge 55^\circ - 60^\circ$). Vách dốc ngăn bùn bám dính.
- **Vùng ra (Outlet Zone)**:
  - Vị trí: Cuối bể lắng.
  - Chức năng: Thu gom lớp nước trong trên bề mặt bể lắng.
  - Nhiệm vụ: Chuyển tiếp nước êm dịu sang kênh dẫn đến bể lọc nhanh. Hệ thống ngăn dòng xoáy hút dâng cuốn bùn từ đáy lên.
  - Cấu tạo: Mạng lưới máng răng cưa ngón tay (finger launders) và vách tràn răng cưa tam giác $90^\circ$ V-notch.

#### 5.2.2 Động học Lắng Hạt và Tải Trọng Tràn Bề Mặt (Particle Kinematics & Surface Overflow Rate)

##### 5.2.2.1 Phương trình Quỹ đạo Hạt Cặn trong Hệ Tọa độ Descartes
- Xét hệ tọa độ vuông góc $(x, z)$ tại ranh giới đầu vùng lắng:
  - Trục $x$: Phương dòng chảy ngang từ cửa vào ($x = 0$) đến cửa ra ($x = L$).
  - Trục $z$: Phương thẳng đứng hướng từ mặt nước ($z = 0$) xuống đáy bể ($z = H$).
- Phương trình vi phân chuyển động của hạt cặn:
  $$\frac{dx}{dt} = v_h = \frac{Q}{W \cdot H} = \text{const}$$
  $$\frac{dz}{dt} = v_s = \text{const}$$
- Tích phân theo thời gian $t$:
  $$x(t) = v_h \cdot t$$
  $$z(t) = z_0 + v_s \cdot t$$
  - $z_0$: Cao độ ban đầu của hạt tại cửa vào $x = 0$ ($0 \le z_0 \le H$).
- Khử biến thời gian $t = \frac{x}{v_h}$:
  $$z(x) = z_0 + \left(\frac{v_s}{v_h}\right) x$$
- Quỹ đạo chuyển động của hạt cặn rời rạc trong bể lắng ngang lý tưởng là một đường thẳng nghiêng dốc xuống. Độ dốc đường quỹ đạo bằng tỷ số $\frac{v_s}{v_h}$.

##### 5.2.2.2 Vận tốc Lắng Tới hạn và Tải trọng Tràn Bề mặt (Critical Velocity & SOR)
- **Định nghĩa vận tốc lắng tới hạn ($v_0$)**: Vận tốc lắng nhỏ nhất của hạt cặn xuất phát từ mặt nước tại đầu vào ($x = 0, z_0 = 0$) chạm đáy đúng cuối vùng lắng ($x = L, z = H$).
- Hạt cặn có vận tốc lắng $v_s \ge v_0$ sẽ lắng hoàn toàn xuống đáy bể. Hiệu suất loại bỏ nhóm hạt này đạt $100\%$.
- Thay tọa độ điểm cuối ($x = L, z = H, z_0 = 0$) vào phương trình quỹ đạo:
  $$H = \left(\frac{v_0}{v_h}\right) L \implies v_0 = \frac{H \cdot v_h}{L}$$
- Thay $v_h = \frac{Q}{W \cdot H}$:
  $$v_0 = \frac{H \cdot Q}{L \cdot W \cdot H} = \frac{Q}{L \cdot W} = \frac{Q}{A_s}$$
- Biểu thức xác lập công thức tính tải trọng tràn bề mặt (Surface Overflow Rate - $\text{SOR}$):
  $$v_0 = \text{SOR} = \frac{Q}{A_s} = \frac{H}{t_0}$$
  - $v_0$: Vận tốc lắng tới hạn ($\text{m/s}$, $\text{m/h}$ hoặc $\text{m/d}$).
  - $\text{SOR}$: Tải trọng tràn bề mặt ($\text{m}^3/\text{m}^2\cdot\text{d}$ hoặc $\text{m}^3/\text{m}^2\cdot\text{h}$).
  - $Q$: Lưu lượng nước cấp vào bể ($\text{m}^3/\text{d}$ hoặc $\text{m}^3/\text{s}$).
  - $A_s$: Diện tích mặt bằng vùng lắng ($\text{m}^2$, $A_s = L \cdot W$).
  - $H$: Chiều sâu nước lắng hữu ích ($\text{m}$).
  - $t_0$: Thời gian lưu nước lý thuyết ($\text{h}$ hoặc $\text{s}$).

##### 5.2.2.3 Thời gian Lưu Thủy lực Danh định (Hydraulic Retention Time)
- Thời gian lưu thủy lực lý thuyết ($t_0$) biểu thị thời gian trung bình nước lưu trong thể tích vùng lắng:
  $$t_0 = \frac{V}{Q} = \frac{L \cdot W \cdot H}{Q} = \frac{A_s \cdot H}{Q} = \frac{H}{v_0}$$
  - $t_0$: Thời gian lưu thủy lực danh định ($\text{h}$ hoặc $\text{s}$).
  - $V$: Thể tích nước hữu ích của vùng lắng ($\text{m}^3$, $V = L \cdot W \cdot H = A_s \cdot H$).
  - $Q$: Lưu lượng nước qua bể ($\text{m}^3/\text{h}$ hoặc $\text{m}^3/\text{s}$).

##### 5.2.2.4 Định lý Diện tích Bề mặt Hazen (Hazen's Surface Area Principle)
- Allen Hazen thiết lập nguyên lý lắng nông vào năm 1904:
  - Khả năng làm trong của bể lắng lý tưởng độc lập với chiều sâu bể $H$.
  - Khả năng làm trong chỉ phụ thuộc vào diện tích mặt bằng $A_s$ (hoặc tỷ số $Q/A_s$).
- **Chứng minh toán học**:
  - Giả sử giảm chiều sâu bể từ $H$ xuống $H/n$ ($n > 1$). Giữ nguyên lưu lượng $Q$ và diện tích mặt bằng $A_s$.
  - Thời gian lưu nước mới giảm $n$ lần:
    $$t_0' = \frac{t_0}{n}$$
  - Quãng đường hạt rơi chạm đáy cũng giảm $n$ lần:
    $$H' = \frac{H}{n}$$
  - Tải trọng bề mặt mới của bể:
    $$v_0' = \frac{H'}{t_0'} = \frac{\left(\frac{H}{n}\right)}{\left(\frac{t_0}{n}\right)} = \frac{H}{t_0} = v_0 = \frac{Q}{A_s}$$
  - Tải trọng bề mặt $v_0$ không đổi. Hạt có vận tốc lắng $v_s$ vẫn chạm đáy ở vị trí tương đương.
  - Nguyên lý này là nền tảng cho công nghệ lắng tấm nghiêng (Lamella) và ống lắng nghiêng tốc độ cao.

##### 5.2.2.5 Tiêu chuẩn Phân tách trong Bể Lắng Đứng (Upflow Clarifier Separation Criterion)
- Trong bể lắng đứng (Upflow Clarifier), nước dâng thẳng đứng từ dưới lên qua diện tích mặt bằng $A_s$.
- Vận tốc nước dâng biểu kiến bằng chính tải trọng bề mặt:
  $$v_{\text{upward}} = v_0 = \frac{Q}{A_s}$$
- Vận tốc tổng hợp của hạt cặn theo phương thẳng đứng:
  $$v_{\text{net}} = v_s - v_0$$
- **Điều kiện phân tách nhị phân (Binary Separation Criterion)**:
  $$v_s \ge v_0 \quad \text{với} \quad v_0 = \frac{Q}{A_s}$$
  - Nếu $v_s \ge v_0$: Hạt rơi xuống đáy hoặc lơ lửng. Hiệu suất loại bỏ đạt $100\%$.
  - Nếu $v_s < v_0$: Nước dâng cuốn hạt trôi lên máng tràn. Hiệu suất loại bỏ bằng $0\%$.
- **So sánh với bể lắng ngang**: Bể lắng ngang vẫn thu hồi được một phần hạt cặn có $v_s < v_0$ nhờ vị trí xuất phát thấp hơn.

##### 5.2.2.6 Hiệu suất Loại bỏ Hạt Phân đoạn Dưới Tới hạn (Fractional Removal for Sub-Critical Particles)
- Xét nhóm hạt cặn rời rạc có vận tốc lắng nhỏ hơn vận tốc tới hạn ($v_s < v_0$).
- Cặn phân bố đều trên toàn bộ chiều sâu $H$ tại đầu vào ($x = 0$). Hạt chạm đáy trong chiều dài $L$ nếu cao độ ban đầu $z_0$ thỏa mãn:
  $$H - z_0 \le v_s \cdot t_0 = v_s \cdot \left(\frac{L}{v_h}\right) = v_s \cdot \left(\frac{H}{v_0}\right)$$
  $$z_0 \ge H \left(1 - \frac{v_s}{v_0}\right)$$
- Chiều sâu thu nhận cặn thẳng đứng tính từ đáy lên:
  $$h_{\text{capture}} = H - z_0 = H \cdot \left(\frac{v_s}{v_0}\right)$$
- Tỷ lệ loại bỏ phân đoạn ($r$) của nhóm hạt có vận tốc $v_s$:
  $$r = \frac{h_{\text{capture}}}{H} = \frac{v_s}{v_0} = \frac{v_s \cdot A_s}{Q} = \frac{v_s \cdot t_0}{H} \quad (\text{với } v_s < v_0)$$
  - $r$: Tỷ số loại bỏ phân đoạn ($0 \le r < 1.0$).
  - $v_s$: Vận tốc lắng của nhóm hạt ($\text{m/s}$).
  - $v_0$: Tải trọng bề mặt của bể ($\text{m/s}$).

##### 5.2.2.7 Tích phân Hiệu suất Loại bỏ Tổng thể cho Huyền phù Đa phân tán (Cumulative Removal Integration)
- Huyền phù thực tế chứa nhiều cỡ hạt. Phân bố khối lượng hạt theo vận tốc lắng mô tả bằng hàm tích lũy $F(v)$.
- Gọi $F_0$ là phần khối lượng cặn có vận tốc lắng $v_s \le v_0$.
- Nhóm hạt có vận tốc $v_s \ge v_0$ chiếm phần khối lượng $(1 - F_0)$. Nhóm này được loại bỏ $100\%$.
- Nhóm hạt có vận tốc $v_s < v_0$ chỉ được loại bỏ theo tỷ số $r = \frac{v_s}{v_0}$.
- Tổng hiệu suất loại bỏ chất rắn lơ lửng của bể lắng lý tưởng:
  $$R_{\text{total}} = (1 - F_0) + \int_0^{F_0} \frac{v_s}{v_0} \, dF = (1 - F_0) + \frac{1}{v_0} \int_0^{F_0} v_s \, dF$$
  - $R_{\text{total}}$: Tổng hiệu suất loại bỏ chất rắn lơ lửng ($0 \le R_{\text{total}} \le 1.0$).
  - $F_0$: Phần khối lượng tích lũy của hạt có vận tốc lắng $v_s \le v_0$.
  - $(1 - F_0)$: Phần khối lượng cặn lắng hoàn toàn $100\%$.
  - $\int_0^{F_0} v_s \, dF$: Diện tích hình học giới hạn bởi đường cong phân bố vận tốc từ $F = 0$ đến $F = F_0$.
- Tính toán thực tế dùng công thức tích phân hình thang:
  $$\int_0^{F_0} v_s \, dF \approx \sum_{i=1}^n \left(\frac{v_{s,i} + v_{s,i-1}}{2}\right) \Delta F_i$$

#### 5.2.3 Thủy động Lực học Chống Xới Cặn và Ổn định Dòng Chảy (Anti-Scour Hydrodynamics & Hydraulic Stability)

##### 5.2.3.1 Phương trình Vận tốc Xới Cặn Camp (Camp Scour Velocity Equation)
- Dòng nước chảy ngang trên đáy bể sinh ra ứng suất cắt ma sát bề mặt $\tau_0$.
- Khi ứng suất cắt thắng lực ma sát trọng lực giữ hạt, hạt cặn bị xới tung và cuốn ngược vào dòng nước.
- Thomas R. Camp ứng dụng lý thuyết Shields thiết lập phương trình vận tốc xới cặn tới hạn ($v_{\text{scour}}$):
  $$v_{\text{scour}} = \sqrt{\frac{8 k (s - 1) g d}{f}} = \sqrt{\frac{8 k (\text{SG} - 1) g d}{f}}$$
  - $v_{\text{scour}}$: Vận tốc dòng chảy ngang trung bình bắt đầu gây xới bùn đáy ($\text{m/s}$).
  - $k$: Hằng số thực nghiệm biểu thị tính dính bám của hạt cặn:
    - $k \approx 0.04$: Hạt cát rời rạc, không dính.
    - $k \approx 0.06$: Hạt cát có keo dính nhẹ.
    - $k \approx 0.10 - 0.15$: Bông cặn keo tụ nhôm hoặc sắt có tính liên kết nhớt.
  - $s$ (hoặc $\text{SG}$): Tỷ trọng tương đối của hạt cặn so với nước ($\text{SG} = \rho_s/\rho_w$):
    - Cát và sỏi vô cơ: $\text{SG} = 2.65$.
    - Bông cặn keo tụ phèn nhôm: $\text{SG} = 1.001 - 1.005$.
    - Bông cặn kết tủa mềm vôi: $\text{SG} = 1.002 - 1.010$.
  - $g$: Gia tốc trọng trường ($9.81\text{ m/s}^2$).
  - $d$: Đường kính của hạt cặn nằm trên sàn đáy ($\text{m}$).
  - $f$: Hệ số ma sát Darcy-Weisbach của đáy bể lắng:
    - Sàn bê tông xoa phẳng: $f \approx 0.02 - 0.03$ (thường chọn $f = 0.025$).

##### 5.2.3.2 Vận tốc Dòng Chảy Ngang và Tiêu chuẩn An toàn Chống Xới Cặn
- Tiêu chuẩn an toàn thiết kế khống chế vận tốc dòng chảy ngang trung bình ($v_h$):
  $$v_h \le \frac{1}{2} v_{\text{scour}} \quad \text{đến} \quad \frac{1}{3} v_{\text{scour}}$$
- Đối với bông cặn keo tụ phèn nhôm nhẹ, vận tốc xới cặn thực tế đạt khoảng $15 - 20\text{ mm/s}$.
- Giới hạn vận tốc dòng chảy ngang thiết kế trong bể lắng ngang đô thị:
  $$v_h = 0.15 - 0.90\text{ m/min} \quad (2.5 - 15\text{ mm/s})$$
- Quy phạm thiết kế thường khống chế:
  $$v_h \le 0.50\text{ m/min} \quad (8.3\text{ mm/s})$$
  Vận tốc này đảm bảo lớp bùn đáy không bị cuốn trôi.

##### 5.2.3.3 Kiểm tra Ổn định Thủy lực: Số Reynolds và Số Froude
- **Bán kính thủy lực ($R_h$) của mặt cắt ngang bể**:
  $$R_h = \frac{A_x}{P} = \frac{W \cdot H}{W + 2H}$$
  - $A_x$: Diện tích mặt cắt ướt ngang ($W \cdot H$, $\text{m}^2$).
  - $P$: Chu vi ướt ($W + 2H$, $\text{m}$).
- **Số Reynolds của bể lắng ($Re_{\text{basin}}$)**:
  $$Re_{\text{basin}} = \frac{v_h \cdot R_h}{\nu}$$
  - $v_h$: Vận tốc dòng chảy ngang trung bình ($\text{m/s}$).
  - $\nu$: Độ nhớt động học của nước ($\text{m}^2/\text{s}$, ở $20^\circ\text{C}$ có $\nu = 1.004 \times 10^{-6}\text{ m}^2/\text{s}$).
  - Tiêu chuẩn khống chế xoáy rối cho bể lắng ngang kích thước lớn:
    $$Re_{\text{basin}} < 20,000 \quad (\text{khuyến nghị tối ưu } < 10,000)$$
- **Số Froude của bể lắng ($Fr$)**:
  $$Fr = \frac{v_h^2}{g \cdot R_h}$$
  - Tiêu chuẩn duy trì tính ổn định của các đường dòng:
    $$Fr > 10^{-5} \quad (\text{thực tế thiết kế đạt } 10^{-6} - 10^{-5})$$

#### 5.2.4 Kích Thước Hình Học và Cấu Tạo Bể Lắng Ngang (Geometric Ratios & Basin Construction)

##### 5.2.4.1 Tỷ lệ Hình học Tiêu chuẩn: L:W, H, L:H và Chiều cao An toàn
- **Tỷ số chiều dài trên chiều rộng ($L:W$)**:
  $$\frac{L}{W} \ge 4:1 \quad (\text{dải tiêu chuẩn } 4:1 - 6:1,\ \text{tối đa } 8:1)$$
  - Tỷ lệ này triệt tiêu các xoáy cuộn hai bên thành bể. Dòng chảy tiếp cận trạng thái dòng chảy nút.
- **Chiều sâu nước lắng hữu ích ($H$)**:
  $$H = 3.0 - 5.0\text{ m} \quad (\text{thông dụng } 3.5 - 4.5\text{ m})$$
  - Chiều sâu này gồm tầng nước trong ($0.5 - 1.0\text{ m}$), tầng lắng chính ($1.5 - 2.5\text{ m}$) và tầng bùn ($0.5 - 1.0\text{ m}$).
- **Tỷ số chiều dài trên chiều sâu ($L:H$)**:
  $$\frac{L}{H} = 15:1 - 25:1$$
  - Tỷ số này giữ ổn định các đường dòng nằm ngang suốt chiều dài bể.
- **Chiều cao an toàn mặt thoáng ($H_{\text{freeboard}}$)**:
  $$H_{\text{freeboard}} = 0.3 - 0.6\text{ m} \quad (\text{tiêu chuẩn chọn } 0.5 - 0.6\text{ m})$$
  - Khoảng trống này ngăn nước tràn bờ do sóng gió hoặc dao động lưu lượng.

##### 5.2.4.2 Vách Ngăn Phân Phối Đục Lỗ Vùng Vào (Perforated Distribution Baffle Wall)
- Vị trí: Đặt cách cửa vào từ $1.0\text{ m}$ đến $2.0\text{ m}$, phủ kín mặt cắt ngang bể.
- Cấu tạo: Vách bê tông cốt thép hoặc composite khoan các lỗ tròn đường kính $50 - 150\text{ mm}$.
- Cách bố trí: Lỗ đục so le hoa mai, phân bố từ $0.5\text{ m}$ dưới mặt nước đến $0.5 - 1.0\text{ m}$ cách đáy.
- Vận tốc nước qua lỗ:
  $$v_{\text{port}} = 0.15 - 0.30\text{ m/s}$$
  - Nếu $v_{\text{port}} < 0.15\text{ m/s}$: Tổn thất cột áp nhỏ, dòng chảy phân bố không đều giữa các lỗ.
  - Nếu $v_{\text{port}} > 0.30\text{ m/s}$: Gradient vận tốc lớn làm vỡ các bông cặn phèn nhôm.
- Tổn thất cột áp qua vách đục lỗ:
  $$h_L = 10 - 25\text{ mm}$$

##### 5.2.4.3 Cấu tạo Đáy Bể và Hố Thu Cặn Đầu Bể (Sludge Hopper & Floor Slope)
- Đáy bể lắng đổ dốc dọc về phía đầu bể (nơi tích lũy hơn $70\%$ tổng lượng cặn).
- Độ dốc sàn đáy bê tông:
  $$S_{\text{floor}} = 1:600 - 1:100 \quad (0.17\% - 1.0\%)$$
- Tại đầu bể bố trí từ một đến ba hố thu cặn hình kim tự tháp cụt (pyramidal hoppers).
- Góc nghiêng vách hố thu:
  $$\theta_{\text{hopper}} \ge 45^\circ - 60^\circ$$
  Vách dốc giúp cặn tự trượt xuống đáy hố, tránh hiện tượng tạo phễu rỗng (rat-holing) khi mở van xả.
- Thiết bị xả bùn: Van lồng xả bùn (telescoping valve) hoặc van xả tự động điều khiển khí nén.

#### 5.2.5 Hệ Thống Máng Răng Cưa Ngón Tay Thu Nước Trong (Effluent Finger Launder Network)

##### 5.2.5.1 Cấu hình Máng Ngón Tay và Cơ chế Chống Dòng Hút Dâng (Finger Launders vs End Wall)
- **Hạn chế của vách tràn ngang cuối bể (Single End-Wall Weir)**:
  - Chiều dài vách tràn chỉ bằng chiều rộng bể ($L_w = W$).
  - Toàn bộ lưu lượng nước thoát qua mặt cắt hẹp tạo vận tốc hút dâng cực lớn.
  - Dòng hút cuốn các bông cặn lơ lửng vượt qua vách tràn thoát ra ngoài.
- **Cấu hình máng răng cưa ngón tay (Finger Launders)**:
  - Máng thu nước đặt dọc song song nhau, vươn ngược vào trong vùng lắng.
  - Chiều dài máng phủ từ $20\%$ đến $33\%$ (khoảng $1/5$ đến $1/3$) chiều dài cuối bể.
  - Nước tràn vào máng từ cả hai phía thành máng (double-sided weirs).
  - Cấu hình này tăng chiều dài tràn hữu hiệu lên $4 - 8$ lần so với vách tràn cuối bể.
  - Dòng thu nước phân tán đều trên diện tích rộng, triệt tiêu hoàn toàn dòng hút dâng cục bộ.
- **Khoảng cách lắp đặt giữa các tim máng nhánh ($S_{\text{launder}}$)**:
  $$S_{\text{launder}} \le 3.0 - 4.0\text{ m}$$
  Khoảng cách này giữ cho đường đi ngang của phần tử nước tới mép tràn nhỏ hơn $2.0\text{ m}$.

##### 5.2.5.2 Tiêu chuẩn Tải trọng Vách Tràn Mét Dài (Weir Loading Rate - WLR)
- Công thức tính tải trọng mét dài vách tràn:
  $$\text{WLR} = \frac{Q}{L_w}$$
  - $\text{WLR}$: Tải trọng tràn trên mét dài vách tràn ($\text{m}^3/\text{m}\cdot\text{d}$ hoặc $\text{m}^3/\text{m}\cdot\text{h}$).
  - $Q$: Lưu lượng nước qua bể ($\text{m}^3/\text{d}$ hoặc $\text{m}^3/\text{h}$).
  - $L_w$: Tổng chiều dài hữu hiệu của mép tràn trong bể ($\text{m}$).
- **Giới hạn tiêu chuẩn thiết kế**:
  - Bông cặn phèn nhôm nhẹ, dễ vỡ:
    $$\text{WLR}_{\text{alum}} \le 150 - 180\text{ m}^3/\text{m}\cdot\text{d} \quad (6.25 - 7.5\text{ m}^3/\text{m}\cdot\text{h})$$
  - Bông cặn nặng hoặc kết tủa làm mềm vôi:
    $$\text{WLR}_{\text{heavy}} \le 200 - 250\text{ m}^3/\text{m}\cdot\text{d} \quad (8.33 - 10.4\text{ m}^3/\text{m}\cdot\text{h})$$
- **Cơ sở vật lý chống hút dâng**: Khống chế $\text{WLR}$ giữ cho vận tốc nước dâng cục bộ nhỏ hơn vận tốc lắng của hạt:
  $$v_{\text{upward, local}} \ll v_s$$

##### 5.2.5.3 Thủy lực Vách Tràn Răng Cưa Tam Giác 90° (90° V-Notch Weir Hydraulics)
- Thành máng thu gắn các tấm vách tràn răng cưa tam giác $90^\circ$ V-notch bằng thép không gỉ (Inox 304/316) hoặc nhựa FRP.
- Phương trình Thomson / Kindsvater-Shen tính lưu lượng qua một khe răng cưa:
  $$Q_{\text{notch}} = \frac{8}{15} C_d \sqrt{2g} \tan\left(\frac{\theta}{2}\right) H_w^{5/2}$$
  - Thay $\theta = 90^\circ$, $\tan(45^\circ) = 1.0$, $g = 9.81\text{ m/s}^2$, $C_d \approx 0.585$:
    $$Q_{\text{notch}} \approx 1.38 \cdot H_w^{5/2}$$
    - $Q_{\text{notch}}$: Lưu lượng xả qua một khe răng cưa ($\text{m}^3/\text{s}$).
    - $H_w$: Cột nước tràn đo từ đỉnh góc nhọn chữ V lên mặt nước tĩnh trong bể ($\text{m}$).
    - $C_d$: Hệ số lưu lượng vách tràn gờ sắc ($0.58 - 0.60$).
- **Cột nước tràn thiết kế ($H_w$)**:
  $$H_w = 25 - 75\text{ mm} \quad (0.025 - 0.075\text{ m})$$
  - Nếu $H_w < 25\text{ mm}$: Sức căng mặt ngoài làm nước dính vào thành, lưu lượng phân bố không đều.
  - Nếu $H_w > 75\text{ mm}$: Nước dâng ngập đỉnh răng cưa.
- **Kích thước hình học răng cưa**:
  - Bước răng (khoảng cách giữa hai đỉnh kề nhau): $P_{\text{notch}} = 150 - 300\text{ mm}$ (thông dụng $200\text{ mm}$).
  - Chiều sâu khe khoét: $h_{\text{notch}} = 50 - 100\text{ mm}$.
  - Bulông cố định có rãnh trượt ô-van thẳng đứng. Rãnh trượt cho phép dùng máy cân bằng laser điều chỉnh cao độ với sai số $\le \pm 1.0\text{ mm}$.

##### 5.2.5.4 Thủy lực Lòng Máng Thu và Vận tốc Tự Làm Sạch (Launder Channel Hydraulics)
- Dòng chảy trong máng thu là dòng biến đổi liên tục có lưu lượng tăng dần (spatially varied flow).
- Độ dốc đáy máng thu đổ về kênh tập trung nước:
  $$S_{\text{invert}} = 1:100 - 1:50 \quad (1.0\% - 2.0\%)$$
- Khoảng rơi tự do từ đáy chữ V xuống mực nước cao nhất trong máng:
  $$H_{\text{drop}} = 0.10 - 0.15\text{ m}$$
  Khoảng rơi này đảm bảo điều kiện xả tràn tự do, không bị ngập chân vách tràn.
- Vận tốc dòng chảy trong lòng máng và kênh thu:
  $$v_{\text{channel}} = 0.4 - 0.8\text{ m/s}$$
  Vận tốc này cuốn trôi cặn mịn và ngăn cặn tái lắng đọng trong máng.

#### 5.2.6 Quy Trình Thiết Kế Kỹ Thuật Bể Lắng Ngang (Engineering Design Procedure)
Quy trình định cỡ hệ thống bể lắng ngang chữ nhật gồm mười bước thực hiện:
1. Xác định lưu lượng thiết kế ngày lớn nhất $Q_{\text{total}}$ ($\text{m}^3/\text{d}$ hoặc $\text{m}^3/\text{s}$).
2. Chọn số lượng đơn nguyên bể lắng song song $N \ge 2$ để đảm bảo dự phòng bảo trì.
3. Tính lưu lượng tính toán cho mỗi bể: $Q_{\text{basin}} = Q_{\text{total}} / N$.
4. Chọn tải trọng tràn bề mặt thiết kế $\text{SOR}$ theo đặc tính cặn ($\text{SOR} = 20 - 40\text{ m}^3/\text{m}^2\cdot\text{d}$ cho phèn nhôm).
5. Tính diện tích mặt bằng yêu cầu cho mỗi bể: $A_s = Q_{\text{basin}} / \text{SOR}$.
6. Chọn tỷ số chiều dài trên chiều rộng $L:W \ge 4:1$. Tính chiều rộng $W = \sqrt{A_s / (L:W)}$ và chiều dài $L = (L:W) \cdot W$.
7. Chọn chiều sâu nước hữu ích $H = 3.5 - 4.5\text{ m}$. Tính thời gian lưu nước $t_0 = (A_s \cdot H) / Q_{\text{basin}}$ và kiểm tra tiêu chuẩn $2.0 - 4.0\text{ h}$.
8. Tính vận tốc dòng chảy ngang $v_h = Q_{\text{basin}} / (W \cdot H)$. Kiểm tra điều kiện chống xới cặn $v_h < 0.50\text{ m/min}$ và các số $Re, Fr$.
9. Thiết kế máng ngón tay thu nước trong: Xác định tổng chiều dài vách tràn $L_w = Q_{\text{basin}} / \text{WLR}$ (với $\text{WLR} \le 180\text{ m}^3/\text{m}\cdot\text{d}$).
10. Bố trí số lượng máng ngón tay, kiểm tra khoảng cách tim máng $S \le 3.0 - 4.0\text{ m}$ và tỷ lệ bao phủ $20\% - 33\%$ chiều dài bể.

#### 5.2.7 Chẩn Đoán Sự Cố Vận Hành và Biện Pháp Xử Lý (Basin Operational Troubleshooting)
- **Sự cố 1: Phân tầng nhiệt và dòng chảy tắt mật độ**:
  - Dấu hiệu nhận biết: Nước sau lắng đục đột ngột. Thời gian lưu thực tế giảm xuống dưới 30 phút.
  - Nguyên nhân gốc rễ: Chênh lệch nhiệt độ giữa nước vào và nước trong bể vượt quá $0.5^\circ\text{C}$. Nước ấm nổi lên mặt hoặc nước lạnh chìm xuống đáy tạo dòng chảy ngầm.
  - Biện pháp khắc phục:
    1. Lắp đặt vách ngăn đục lỗ toàn bộ chiều sâu tại vùng vào.
    2. Duy trì vận tốc qua lỗ vách ngăn $v_{\text{port}} = 0.15 - 0.30\text{ m/s}$ để triệt tiêu năng lượng và hòa trộn dòng nhiệt.
    3. Xây dựng mái che hoặc tấm chắn giảm bức xạ nhiệt trực tiếp lên mặt bể.
- **Sự cố 2: Xới cặn do gió thổi bề mặt**:
  - Dấu hiệu nhận biết: Lớp bùn đáy bị xới tung ở cuối bể. Độ đục nước đầu ra tăng cao khi có gió mạnh.
  - Nguyên nhân gốc rễ: Gió thổi dọc bể dài tạo dòng chảy mặt kéo theo dòng hoàn lưu đáy chảy ngược. Vận tốc đáy vượt ngưỡng $v_{\text{scour}}$.
  - Biện pháp khắc phục:
    1. Lắp đặt các vách ngăn ngang chắn gió (cross baffles) ngập sâu $0.5 - 1.0\text{ m}$ dưới mặt nước.
    2. Duy trì tỷ lệ hình học $L:H \le 25:1$.
    3. Khống chế vận tốc ngang dòng nước $v_h < 0.50\text{ m/min}$.
- **Sự cố 3: Cuốn cặn do quá tải vách tràn máng thu**:
  - Dấu hiệu nhận biết: Cặn lơ lửng bị hút dâng thẳng lên mép vách tràn máng thu nước.
  - Nguyên nhân gốc rễ: Chiều dài vách tràn không đủ khiến tải trọng vượt ngưỡng ($\text{WLR} > 250\text{ m}^3/\text{m}\cdot\text{d}$). Vận tốc nước dâng cục bộ vượt quá vận tốc lắng hạt.
  - Biện pháp khắc phục:
    1. Kéo dài hệ thống máng ngón tay vươn sâu vào vùng lắng phủ $1/3$ chiều dài bể.
    2. Lắp đặt thêm các máng nhánh để giảm $\text{WLR} \le 150 - 180\text{ m}^3/\text{m}\cdot\text{d}$.
    3. Cân chỉnh cao độ đáy chữ V của răng cưa bằng máy laser.
- **Sự cố 4: Nổi bùn do phân hủy kỵ khí trong hố thu**:
  - Dấu hiệu nhận biết: Các mảng bùn đen nổi lên mặt bể. Mặt nước sủi bọt khí có mùi hôi.
  - Nguyên nhân gốc rễ: Chu kỳ xả bùn quá dài. Bùn hữu cơ phân hủy kỵ khí sinh khí $\text{CH}_4$ và $\text{CO}_2$. Bọt khí bám vào bông cặn đẩy bùn nổi lên mặt.
  - Biện pháp khắc phục:
    1. Tăng tần suất xả bùn định kỳ từ hố thu cặn.
    2. Đảm bảo góc nghiêng vách hố thu $\theta_{\text{hopper}} \ge 55^\circ - 60^\circ$ để bùn không đọng trên thành.
    3. Sử dụng cầu cào hút bùn liên tục để hút cặn trực tiếp từ đáy bể.

#### 5.2.8 Bài Tập Tính Toán Kỹ Thuật Thiết Kế (Engineering Sizing Calculations)

<!-- exercise-start: Ví dụ 5-2: Thiết kế Bể lắng Ngang Chữ nhật Xử lý Nước cấp -->
- **Ví dụ 5-2: Thiết kế Bể lắng Ngang Chữ nhật Xử lý Nước cấp**
  - Cho:
    - Lưu lượng thiết kế ngày lớn nhất: $Q = 0.5\text{ m}^3/\text{s}$ ($43,200\text{ m}^3/\text{d}$).
    - Tải trọng bề mặt thiết kế: $\text{SOR} = 32.5\text{ m}^3/\text{m}^2\cdot\text{d}$.
    - Số lượng bể song song: $N = 2$ bể.
    - Tỷ số chiều dài trên chiều rộng: $L:W = 4:1$.
    - Chiều sâu nước lắng hữu ích: $H = 4.0\text{ m}$.
    - Chiều sâu dự phòng vùng bùn: $H_{\text{sludge}} = 0.8\text{ m}$.
    - Chiều cao an toàn mặt thoáng: $H_{\text{freeboard}} = 0.6\text{ m}$.
    - Tải trọng vách tràn thiết kế: $\text{WLR} = 180\text{ m}^3/\text{d}\cdot\text{m}$.
    - Độ nhớt động học của nước ở $20^\circ\text{C}$: $\nu = 1.004 \times 10^{-6}\text{ m}^2/\text{s}$.
    - Gia tốc trọng trường: $g = 9.81\text{ m/s}^2$.
  - Tìm:
    1. Kích thước hình học mỗi bể ($W, L, H_{\text{total}}$) và diện tích mặt bằng thực tế.
    2. Thể tích và thời gian lưu thủy lực ($t_0$).
    3. Vận tốc dòng chảy ngang ($v_h$) và kiểm tra điều kiện chống xới cặn.
    4. Số Reynolds ($Re$) và số Froude ($Fr$).
    5. Cấu tạo hệ thống máng ngón tay thu nước trong ($L_w, L_{\text{launder}}$, số máng).
  - Phương trình áp dụng:
    $$Q_{\text{basin}} = \frac{Q_{\text{total}}}{N}$$
    $$A_s = \frac{Q_{\text{basin}}}{\text{SOR}}$$
    $$L = 4W \implies A_s = 4W^2$$
    $$t_0 = \frac{A_s \cdot H}{Q_{\text{basin}}}$$
    $$v_h = \frac{Q_{\text{basin}}}{W \cdot H}$$
    $$Re = \frac{v_h \cdot R_h}{\nu} \quad \text{với} \quad R_h = \frac{W \cdot H}{W + 2H}$$
    $$Fr = \frac{v_h^2}{g \cdot R_h}$$
    $$L_{\text{weir}} = \frac{Q_{\text{basin}}}{\text{WLR}}$$
  - Các bước giải:
    1. Bước 1: Phân bổ lưu lượng cho hai bể song song:
       $$Q_{\text{total}} = 0.5\text{ m}^3/\text{s} \times 86,400\text{ s/d} = 43,200\text{ m}^3/\text{d}$$
       $$Q_{\text{basin}} = \frac{43,200\text{ m}^3/\text{d}}{2} = 21,600\text{ m}^3/\text{d} = 0.25\text{ m}^3/\text{s} = 900\text{ m}^3/\text{h}$$
    2. Bước 2: Tính diện tích mặt bằng yêu cầu mỗi bể:
       $$A_s = \frac{Q_{\text{basin}}}{\text{SOR}} = \frac{21,600\text{ m}^3/\text{d}}{32.5\text{ m}^3/\text{m}^2\cdot\text{d}} = 664.62\text{ m}^2$$
    3. Bước 3: Tính kích thước mặt bằng chiều rộng $W$ và chiều dài $L$:
       $$A_s = 4 W^2 = 664.62\text{ m}^2 \implies W^2 = 166.155\text{ m}^2 \implies W = 12.89\text{ m}$$
       Chọn kích thước chẵn thi công:
       $$W = 13.0\text{ m}$$
       Chiều dài vùng lắng tương ứng:
       $$L = 4 \times 13.0\text{ m} = 52.0\text{ m}$$
       Diện tích mặt bằng thực tế mỗi bể:
       $$A_{s,\text{actual}} = 52.0\text{ m} \times 13.0\text{ m} = 676.0\text{ m}^2$$
       Tải trọng tràn bề mặt thực tế:
       $$\text{SOR}_{\text{actual}} = \frac{21,600\text{ m}^3/\text{d}}{676.0\text{ m}^2} = 31.95\text{ m}^3/\text{m}^2\cdot\text{d} \le 32.5\text{ m}^3/\text{m}^2\cdot\text{d} \quad (\text{Đạt})$$
    4. Bước 4: Tính thể tích, chiều cao thành bể và thời gian lưu nước:
       $$V_{\text{basin}} = A_{s,\text{actual}} \times H = 676.0\text{ m}^2 \times 4.0\text{ m} = 2,704.0\text{ m}^3$$
       $$t_0 = \frac{V_{\text{basin}}}{Q_{\text{basin}}} = \frac{2,704.0\text{ m}^3}{0.25\text{ m}^3/\text{s}} = 10,816\text{ s} = 3.004\text{ h} \approx 3.0\text{ h}$$
       Tổng chiều sâu xây dựng thành bể bê tông:
       $$H_{\text{total}} = H + H_{\text{sludge}} + H_{\text{freeboard}} = 4.0 + 0.8 + 0.6 = 5.4\text{ m}$$
    5. Bước 5: Kiểm tra vận tốc dòng chảy ngang và chống xới cặn:
       $$A_x = W \times H = 13.0\text{ m} \times 4.0\text{ m} = 52.0\text{ m}^2$$
       $$v_h = \frac{Q_{\text{basin}}}{A_x} = \frac{0.25\text{ m}^3/\text{s}}{52.0\text{ m}^2} = 0.00481\text{ m/s} = 4.81\text{ mm/s} = 0.288\text{ m/min}$$
       Kiểm tra điều kiện chống xới cặn:
       $$v_h = 0.288\text{ m/min} < 0.50\text{ m/min} \quad (\text{Đạt})$$
    6. Bước 6: Kiểm tra ổn định thủy lực Reynolds và Froude:
       Chu vi ướt:
       $$P = W + 2H = 13.0 + 2 \times 4.0 = 21.0\text{ m}$$
       Bán kính thủy lực:
       $$R_h = \frac{A_x}{P} = \frac{52.0\text{ m}^2}{21.0\text{ m}} = 2.476\text{ m}$$
       Số Reynolds:
       $$Re = \frac{v_h \cdot R_h}{\nu} = \frac{0.00481\text{ m/s} \times 2.476\text{ m}}{1.004 \times 10^{-6}\text{ m}^2/\text{s}} = 11,862 < 20,000 \quad (\text{Đạt})$$
       Số Froude:
       $$Fr = \frac{v_h^2}{g \cdot R_h} = \frac{(0.00481)^2}{9.81 \times 2.476} = 9.53 \times 10^{-7} \approx 1.0 \times 10^{-6} \quad (\text{Đạt})$$
    7. Bước 7: Tính toán hệ thống vách tràn và máng răng cưa ngón tay:
       Tổng chiều dài vách tràn yêu cầu mỗi bể:
       $$L_{\text{weir}} = \frac{Q_{\text{basin}}}{\text{WLR}} = \frac{21,600\text{ m}^3/\text{d}}{180\text{ m}^3/\text{d}\cdot\text{m}} = 120.0\text{ m}$$
       Bố trí $m = 4$ máng nhánh ngón tay đặt song song dọc theo chiều dài bể.
       Khoảng cách giữa các tim máng nhánh:
       $$S = \frac{W}{m} = \frac{13.0\text{ m}}{4} = 3.25\text{ m} \le 4.0\text{ m} \quad (\text{Đạt})$$
       Mỗi máng thu nước từ hai phía thành máng (double-sided weirs). Chiều dài mép tràn trên một máng nhánh:
       $$L_{\text{weir,single}} = \frac{L_{\text{weir}}}{m} = \frac{120.0\text{ m}}{4} = 30.0\text{ m}$$
       Chiều dài xây dựng của mỗi máng nhánh vươn vào vùng lắng:
       $$L_{\text{launder}} = \frac{L_{\text{weir,single}}}{2} = \frac{30.0\text{ m}}{2} = 15.0\text{ m}$$
       Tỷ lệ chiều dài máng so với chiều dài bể:
       $$\frac{L_{\text{launder}}}{L} = \frac{15.0\text{ m}}{52.0\text{ m}} = 28.8\%$$
       Tỷ lệ này nằm trọn vẹn trong khoảng quy chuẩn $20\% - 33\%$ chiều dài cuối bể.
  - **Đáp số**:
    - Số lượng bể: `2 bể song song`
    - Kích thước mỗi bể: `L = 52.0 m`, `W = 13.0 m`, `H = 4.0 m` (Tổng chiều sâu thành bể `H_total = 5.4 m`)
    - Diện tích mặt bằng mỗi bể: `A_s = 676.0 m^2` (Tổng diện tích hai bể `1,352.0 m^2`)
    - Thời gian lưu nước: `t_0 = 3.0 h` (`10,816 s`)
    - Vận tốc dòng chảy ngang: `v_h = 4.81 mm/s` (`0.288 m/min`)
    - Số Reynolds: `Re = 11,862` (`< 20,000`), Số Froude: `Fr = 9.53 x 10^-7`
    - Hệ thống máng ngón tay: `4 máng nhánh`, mỗi máng dài `15.0 m`, thu nước hai bên, tổng chiều dài tràn `120.0 m`
<!-- exercise-end -->

### 5.3 Công nghệ Lắng Tốc độ Cao: Bể Lắng Lamella, Cụm Ống Nghiêng và Keo tụ Dằn tải Vi cát (High-Rate Clarification: Lamella Plate, Tube Settlers & Ballasted Flocculation)

#### 5.3.1 Cơ sở Thủy động học và Cơ chế Tăng tốc Lắng (Hydrodynamic Fundamentals & Settling Acceleration)

##### 5.3.1.1 Đòn bẩy Thủy động học từ Định luật Stokes (Stokes' Law Levers)
- Định luật Stokes xác định vận tốc lắng của hạt cầu trong dòng chảy tầng:
  $$v_s = \frac{g (\rho_s - \rho) d^2}{18 \mu}$$
  Trong đó:
  - $v_s$: Vận tốc lắng trọng lực của hạt cặn ($\text{m/s}$).
  - $g$: Gia tốc trọng trường ($9.81\ \text{m/s}^2$).
  - $\rho_s$: Khối lượng riêng của hạt cặn ($\text{kg/m}^3$).
  - $\rho$: Khối lượng riêng của nước ($1,000\ \text{kg/m}^3$ ở $4^\circ\text{C}$).
  - $d$: Đường kính danh định của hạt cặn ($\text{m}$).
  - $\mu$: Độ nhớt động lực của nước ($1.002 \times 10^{-3}\ \text{Pa}\cdot\text{s}$ ở $20^\circ\text{C}$).
- Kỹ sư điều khiển hai thông số then chốt để tăng tốc độ lắng:
  - Gia tăng độ chênh lệch khối lượng riêng $(\rho_s - \rho)$. Kỹ sư bổ sung vi cát thạch anh tỷ trọng cao vào bông cặn.
  - Rút ngắn khoảng cách rơi của hạt từ vài mét xuống vài xentimét. Kỹ sư đặt các vách ngăn mỏng song song trong vùng lắng.
- Bông cặn phèn nhôm thông thường có cấu trúc rỗng xốp. Tỷ trọng của bông cặn chỉ đạt $\text{SG} \approx 1.001 - 1.005$.
- Bông cặn gắn vi cát nâng tỷ trọng lên $\text{SG} \approx 1.20 - 1.40$. Vận tốc lắng tăng từ $1 - 2\ \text{m/h}$ lên $20 - 60\ \text{m/h}$.

##### 5.3.1.2 Nguyên lý Bể lắng Nông Hazen (Hazen's Shallow-Depth Settling Principle)
- Allen Hazen thiết lập nguyên lý lắng nông năm 1904.
- Hiệu suất lắng chỉ phụ thuộc vào diện tích mặt bằng hứng cặn. Chiều sâu bể không ảnh hưởng đến hiệu suất lắng.
- Vận tốc lắng tới hạn của bể lắng lý tưởng:
  $$v_0 = \frac{Q}{A_s} = \frac{H}{t_0}$$
  Trong đó:
  - $v_0$: Tải trọng bề mặt hoặc vận tốc lắng tới hạn ($\text{m/s}$ hoặc $\text{m}^3/\text{m}^2\cdot\text{d}$).
  - $Q$: Lưu lượng nước cấp vào bể ($\text{m}^3/\text{s}$ hoặc $\text{m}^3/\text{d}$).
  - $A_s$: Diện tích mặt bằng vùng lắng ($\text{m}^2$).
  - $H$: Chiều sâu tầng nước lắng ($\text{m}$).
  - $t_0$: Thời gian lưu nước danh định ($\text{s}$).
- Phân chia chiều sâu $H$ thành $n$ khoang mỏng bằng các khay song song:
  - Khoảng cách giữa các khay giảm xuống: $h = H / n$.
  - Tổng diện tích hứng cặn hữu dụng tăng $n$ lần:
    $$A_{\text{eff}} = n \cdot A_s$$
  - Vận tốc lắng tới hạn giảm đi $n$ lần:
    $$v_{0,\text{new}} = \frac{Q}{n \cdot A_s} = \frac{v_0}{n}$$
  - Hạt cặn chạm khay thu gom nhanh hơn. Bể giữ lại được các hạt cặn nhỏ hơn.
- Khay nằm ngang tích tụ bùn nhanh. Bùn gây nghẹt khoang hẹp. Kỹ sư không thể đưa máy cào cơ học vào khoảng hở nhỏ giữa các khay.

##### 5.3.1.3 Góc Nghiêng Tối ưu 60° và Cơ chế Bùn Tự Trượt Dốc (60° Inclination & Self-Cleaning Mechanism)
- Kỹ sư đặt các tấm phẳng hoặc ống lắng nghiêng góc $\theta$ so với mặt phẳng ngang.
- Thành phần trọng lực kéo khối bùn trượt xuống đáy ống:
  $$F_s = m \cdot g \cdot \sin\theta$$
- Lực ma sát chống trượt giữa bùn và bề mặt tấm nghiêng:
  $$F_f = \mu_f \cdot m \cdot g \cdot \cos\theta$$
  Trong đó:
  - $m$: Khối lượng ướt của cụm cặn ($\text{kg}$).
  - $\theta$: Góc nghiêng của vách ống so với phương ngang (độ, $^\circ$).
  - $\mu_f$: Hệ số ma sát giữa bùn lắng và vật liệu vách lamen.
- Điều kiện để bùn tự trượt liên tục xuống đáy không cần máy cào:
  $$\tan\theta > \mu_f$$
- Phân tích các ngưỡng góc nghiêng:
  - Góc nghiêng $\theta < 45^\circ$: Lực ma sát thắng lực kéo. Bùn bám dính gây tắc nghẽn toàn bộ lòng ống.
  - Góc nghiêng $\theta = 55^\circ - 60^\circ$: Bùn nén thành vệt dày. Khối bùn tự trượt ổn định xuống đáy bể.
  - Góc nghiêng $\theta > 60^\circ$: Bùn trượt rất tốt. Tuy nhiên diện tích hình chiếu mặt bằng giảm mạnh theo hàm $\cos\theta$.
  - Giá trị góc nghiêng chuẩn trong kỹ thuật cấp nước: $\theta = 60^\circ$.

#### 5.3.2 Cấu tạo Hình học và Thủy lực Module Lắng Lamella và Ống Nghiêng (Lamella Plates & Tube Settlers)

##### 5.3.2.1 Hình học và Vật liệu Chế tạo Module Lắng (Geometry & Materials)
- Kỹ sư lắp các module lamen vào phần trên của bể lắng ngang hoặc bể lắng đứng.
- Các dạng hình học tiết diện module thông dụng:
  - Ống tiết diện vuông (Square tubes): Kích thước $50 \times 50\ \text{mm}$.
  - Cụm ống chùm lục giác tổ ong (Hexagonal honeycomb): Chịu lực tốt và cung cấp tỷ diện tích cao nhất.
  - Tấm phẳng lượn sóng song song (Corrugated lamella plates): Phù hợp cho bể kích thước lớn và dễ xịt rửa.
- Vật liệu module:
  - Nhựa PVC cứng (Polyvinyl Chloride): Giá thành rẻ, kháng hóa chất tốt.
  - Nhựa ABS hoặc HDPE: Bền cơ học cao, chống nứt vỡ dưới tia tử ngoại (UV).
- Đường kính thủy lực danh định ($d_h$ hoặc khoảng cách vách $w$):
  - Giá trị chuẩn: $w = d_h = 40 - 60\ \text{mm}$ (thông dụng nhất $w = 50\ \text{mm} = 0.05\ \text{m}$).
  - Kích thước $50\ \text{mm}$ ngăn chặn tắc cặn và duy trì trạng thái chảy tầng.
- Chiều dài ống nghiêng dọc theo trục:
  - Phạm vi chiều dài: $L = 1.0 - 2.0\ \text{m}$ (tiêu chuẩn chế tạo $L = 1.0\ \text{m}$ hoặc $1.2\ \text{m}$).
- Chiều cao thẳng đứng của khối module:
  $$H_{\text{module}} = L \cdot \sin\theta = L \cdot \sin(60^\circ) = 0.866 \cdot L$$
  - Khi $L = 1.0\ \text{m}$, chiều cao thẳng đứng của tầng module đạt $H_{\text{module}} = 0.87\ \text{m}$.

##### 5.3.2.2 Cấu hình Hướng Dòng chảy qua Module Lắng (Flow Direction Configurations)
- Dòng chảy ngược chiều (Countercurrent Flow):
  - Nước thô đi từ đáy bể dâng ngược lên đỉnh module.
  - Cặn lắng xuống vách ống và trượt dốc ngược chiều dòng nước rơi xuống đáy.
  - Cấu hình này phổ biến nhất trong các nhà máy cấp nước.
- Dòng chảy cùng chiều (Cocurrent Flow):
  - Nước và bùn cùng chuyển động chúc xuống đáy ống.
  - Kỹ sư khó bố trí hệ thống thu nước trong riêng biệt dưới đáy bể.
- Dòng chảy cắt ngang (Crosscurrent Flow):
  - Nước chảy theo phương ngang qua khe hở giữa các tấm nghiêng.
  - Bùn lắng rơi theo phương thẳng đứng xuống máng đáy.
  - Dòng nước dễ phân bố không đều giữa các khoang dẫn.

##### 5.3.2.3 Mô hình Vận tốc Lắng Tới hạn K. M. Yao (Yao's Critical Settling Velocity Formulation)
- K. M. Yao phân tích quỹ đạo hạt cặn trong kênh lắng nghiêng chảy ngược chiều.
- Thành phần vận tốc dọc theo trục kênh:
  $$v_x = v_0 - v_s \sin\theta$$
- Thành phần vận tốc vuông góc với trục kênh:
  $$v_y = -v_s \cos\theta$$
- Thời gian tối đa để hạt cặn chạm vách dưới của kênh nghiêng:
  $$t_{\text{fall}} = \frac{w}{v_y} = \frac{w}{v_s \cos\theta}$$
  Trong đó:
  - $w$: Khoảng cách vuông góc giữa hai bản nghiêng ($\text{m}$).
  - $v_s$: Vận tốc lắng riêng của hạt cặn ($\text{m/s}$).
  - $\theta$: Góc nghiêng vách ống ($60^\circ$).
- Quãng đường hạt dịch chuyển dọc trục không vượt quá chiều dài kênh $L$:
  $$x_{\text{travel}} = (v_0 - v_s \sin\theta) \left(\frac{w}{v_s \cos\theta}\right) \le L$$
- Vận tốc nước dâng tới hạn bên trong ống lắng:
  $$v_0 = \frac{v_s}{\sin\theta + \frac{L}{w}\cos\theta}$$
- Vận tốc lắng nhỏ nhất của hạt được giữ lại $100\%$ ($v_{s,\min}$):
  $$v_{s,\min} = v_0 \left(\sin\theta + \frac{L}{w} \cos\theta\right)^{-1}$$
- Ví dụ với ống nghiêng $\theta = 60^\circ$ và tỷ số hình học $L/w = 1.0 / 0.05 = 20$:
  $$\sin 60^\circ + 20 \cos 60^\circ = 0.866 + 10 = 10.866$$
  $$v_{s,\min} = \frac{v_0}{10.866} \approx 0.092 \cdot v_0$$
  Module lắng bắt được các hạt có vận tốc lắng nhỏ hơn 10 lần vận tốc nước dâng.
- Ảnh hưởng của dạng hình học tiết diện ống qua hệ số hình dạng $S_c$:
  $$v_0 = \frac{v_s}{S_c \left(\sin\theta + \frac{L}{w} \cos\theta\right)}$$
  - Bản phẳng song song: $S_c = 1.0$.
  - Ống tròn: $S_c = \frac{4}{\pi} \approx 1.273$.
  - Ống tiết diện vuông: $S_c = \frac{11}{8} = 1.375$.

##### 5.3.2.4 Diện tích Hình chiếu Hữu ích Tương đương (Effective Projected Settling Area)
- Tổng diện tích lắng ngang tương đương của cụm $N$ tấm lắng nghiêng:
  $$A_{\text{eff}} = N \cdot W \cdot (L \cos\theta + w \sin\theta) \approx N \cdot W \cdot L \cos\theta$$
  Trong đó:
  - $A_{\text{eff}}$: Diện tích lắng hữu hiệu tương đương theo phương ngang ($\text{m}^2$).
  - $N$: Tổng số lượng vách nghiêng trong cụm module.
  - $W$: Chiều rộng của tấm vách nghiêng ($\text{m}$).
  - $L$: Chiều dài của tấm vách dọc theo phương dốc ($\text{m}$).
  - $w$: Khoảng cách hở vuông góc giữa hai tấm vách kế tiếp ($\text{m}$).
  - $\theta$: Góc nghiêng của vách so với phương ngang ($60^\circ$).
- Khi góc nghiêng $\theta = 60^\circ$, hệ số hình chiếu đạt $\cos 60^\circ = 0.50$. Mỗi mét vuông diện tích vách cung cấp $0.50\ \text{m}^2$ diện tích lắng ngang.

##### 5.3.2.5 Kiểm tra Chế độ Thủy lực Chảy tầng trong Ống (Laminar Flow Verification)
- Vận tốc chảy dọc trục bên trong ống nghiêng:
  $$v_{\text{tube}} = \frac{v_{0,\text{module}}}{\sin\theta} = \frac{v_{0,\text{module}}}{\sin 60^\circ} = \frac{v_{0,\text{module}}}{0.866}$$
  Trong đó:
  - $v_{\text{tube}}$: Vận tốc nước chảy dọc theo trục ống ($\text{m/s}$).
  - $v_{0,\text{module}}$: Tải trọng bề mặt tính trên diện tích mặt bằng phủ module ($\text{m/s}$).
- Số Reynolds của dòng chảy trong ống lắng:
  $$Re = \frac{v_{\text{tube}} \cdot d_h}{\nu}$$
  Trong đó:
  - $d_h$: Đường kính thủy lực của ống ($0.05\ \text{m}$).
  - $\nu$: Độ nhớt động học của nước ($1.004 \times 10^{-6}\ \text{m}^2/\text{s}$ ở $20^\circ\text{C}$).
- Giá trị vận tốc thực tế $v_{\text{tube}} \approx 2.0\ \text{mm/s}$ tạo ra số Reynolds:
  $$Re = \frac{0.0020 \times 0.05}{1.004 \times 10^{-6}} \approx 99.6 \ll 500$$
- Dòng chảy bên trong ống đạt trạng thái chảy tầng hoàn hảo. Hiện tượng xoáy cuộn bị triệt tiêu hoàn toàn.
- Chiều dài phát triển dòng chảy tầng từ miệng ống:
  $$L_e = 0.058 \cdot Re \cdot d_h = 0.058 \times 99.6 \times 0.05 \approx 0.29\ \text{m}$$
  Ống dài $1.0\ \text{m}$ có hơn $70\%$ chiều dài hoạt động ở trạng thái chảy tầng ổn định.

#### 5.3.3 Công nghệ Keo tụ Dằn tải Vi cát Actiflo (Ballasted Flocculation - Actiflo Process)

##### 5.3.3.1 Bản chất Quá trình và Đặc tính Kỹ thuật của Vi cát (Microsand Specifications)
- Công nghệ Actiflo bổ sung vi cát thạch anh mịn vào nước thô sau pha châm keo tụ.
- Vi cát đóng vai trò hạt nhân dằn tải có tỷ trọng cao.
- Thông số kỹ thuật của vi cát thạch anh:
  - Khối lượng riêng hạt cát: $\rho_{\text{sand}} = 2,500 - 2,650\ \text{kg/m}^3$.
  - Tỷ trọng chất rắn: $\text{SG} = 2.50 - 2.65$.
  - Đường kính hạt danh định: $d_{\text{sand}} = 20 - 200\ \mu\text{m}$ (kích thước tối ưu $80 - 130\ \mu\text{m}$, cỡ sàng $120 - 200\ \text{mesh}$).
- Hạt cát đủ nặng để tăng tốc độ rơi. Hạt cát đủ nhỏ để lơ lửng trong ngăn khuấy và không phá hủy cánh khuấy.
- Chuỗi polymer hữu cơ gắn kết bông cặn keo tụ xung quanh bề mặt vi cát. Bông cặn hỗn hợp đạt mật độ cao và độ bền cơ học lớn.

##### 5.3.3.2 Sơ đồ Dây chuyền Bốn Ngăn Liên hoàn (Actiflo Unit Process Flowsheet)
- Hệ thống Actiflo tích hợp bốn ngăn liên hoàn khép kín:
  1. Ngăn trộn nhanh keo tụ (Coagulation Flash Mix Tank): Châm chất keo tụ phèn nhôm hoặc phèn sắt. Cánh khuấy quay nhanh tạo gradient vận tốc $G = 300 - 500\ \text{s}^{-1}$. Thời gian lưu nước $t = 1 - 2\ \text{phút}$.
  2. Ngăn châm vi cát và polymer (Injection Tank): Châm hạt vi cát tuần hoàn và châm dung dịch polymer trợ lắng anion. Cánh khuấy hoạt động ở cường độ trung bình $G = 150 - 200\ \text{s}^{-1}$. Thời gian lưu $t = 1 - 2\ \text{phút}$.
  3. Ngăn hoàn thiện bông cặn (Maturation Tank): Cánh khuấy tua bin hoạt động êm dịu $G = 50 - 80\ \text{s}^{-1}$. Thời gian lưu $t = 4 - 6\ \text{phút}$. Bông cặn bọc cát phát triển kích thước tối đa.
  4. Ngăn lắng vách nghiêng Lamella (Lamella Clarifier): Nước dâng ngược qua dàn tấm nghiêng $60^\circ$. Bông cặn nặng lắng xuống đáy chỉ trong vài phút. Nước trong tràn qua máng răng cưa phía trên.

##### 5.3.3.3 Vòng Tuần hoàn Thu hồi Vi cát bằng Xyclon Thủy lực (Hydrocyclone Sand Separation Loop)
- Bơm bùn hút liên tục hỗn hợp vi cát và cặn bẩn từ hố thu đáy bể lắng.
- Bơm đẩy huyền phù vào thiết bị phân ly ly tâm Hydrocyclone dưới áp lực $1.5 - 2.5\ \text{bar}$.
- Trường lực ly tâm cực mạnh phân tách hai pha rắn dựa vào tỷ trọng:
  - Pha vi cát nặng ($\text{SG} = 2.65$): Lực ly tâm đẩy hạt cát văng ra sát thành nón. Cát trượt xuống miệng xả đáy dưới (underflow). Dòng cát sạch chảy thẳng về ngăn châm vi cát để tái sử dụng.
  - Pha bùn hydroxit nhẹ ($\text{SG} \approx 1.01$): Lực kéo hướng tâm đẩy cặn bùn vào lõi lốc xoáy. Bùn thoát ra ở cửa xả đỉnh trên (overflow) và chảy sang cụm xử lý bùn thải.
- Hiệu suất thu hồi vi cát qua xyclon thủy lực đạt trên $99.5\%$.
- Lượng cát hao hụt bổ sung định kỳ rất nhỏ, thường dưới $2 - 5\ \text{g/m}^3$ nước xử lý.

##### 5.3.3.4 Tải trọng Bề mặt Siêu cao và Thời gian Lưu Thủy lực (Ultra-High Overflow Rates & Retention Time)
- Tải trọng bề mặt thiết kế của bể lắng vi cát:
  $$\text{SOR}_{\text{ballasted}} = 40 - 80\ \text{m/h} \quad (1,000 - 2,000\ \text{m}^3/\text{m}^2\cdot\text{d})$$
  - Khi tính toán trên mặt bằng bể lắng hoàn thiện, tải trọng đạt $150 - 250\ \text{m}^3/\text{m}^2\cdot\text{d}$ (gấp $5 - 8$ lần bể lắng ngang).
  - Tải trọng cực đại có thể nâng lên $300\ \text{m}^3/\text{m}^2\cdot\text{d}$ khi xử lý nước lũ đột biến.
- Tổng thời gian lưu nước của toàn bộ chu trình chỉ từ $10$ đến $20\ \text{phút}$.
- Hệ thống tiết kiệm từ $85\%$ đến $90\%$ diện tích xây dựng so với bể lắng ngang truyền thống.
- Thời gian khởi động nhanh. Nước sau lắng đạt độ đục tiêu chuẩn dưới $1.0\ \text{NTU}$ chỉ sau 15 phút vận hành.

#### 5.3.4 Quy trình Tính toán Thiết kế Module Lắng Lamella Tốc độ Cao (Engineering Design Procedure for High-Rate Settlers)

1. Xác định lưu lượng thiết kế $Q$ ($\text{m}^3/\text{s}$ hoặc $\text{m}^3/\text{d}$) và chọn số đơn nguyên bể song song $N \ge 2$ để đảm bảo dự phòng.
2. Tính lưu lượng nạp cho từng bể:
   $$Q_{\text{basin}} = \frac{Q}{N}$$
3. Lựa chọn đặc tính hình học module:
   - Góc nghiêng module: $\theta = 60^\circ$.
   - Đường kính thủy lực ống: $w = 0.05\ \text{m}$ ($50\ \text{mm}$).
   - Chiều dài ống nghiêng: $L_{\text{tube}} = 1.0\ \text{m}$.
   - Chiều cao thẳng đứng của khối module: $H_{\text{module}} = L_{\text{tube}} \cdot \sin(60^\circ) = 0.87\ \text{m}$.
4. Chọn tải trọng bề mặt module trên diện tích mặt bằng: $\text{SOR}_{\text{module}} = 120 - 150\ \text{m}^3/\text{m}^2\cdot\text{d}$ ($5.0 - 6.25\ \text{m/h}$).
5. Tính diện tích mặt bằng lắp đặt module ống lắng cho mỗi bể:
   $$A_{\text{module}} = \frac{Q_{\text{basin}}}{\text{SOR}_{\text{module}}}$$
6. Xác định kích thước mặt bằng bể chứa module:
   - Chọn chiều rộng bể $W$ (ví dụ $W = 6.0 - 8.0\ \text{m}$).
   - Tính chiều dài phần đặt module: $L_{\text{module}} = A_{\text{module}} / W$.
   - Bổ sung chiều dài ngăn phân phối vào ($L_{\text{inlet}} = 2.0 - 3.0\ \text{m}$) và ngăn thu nước ra ($L_{\text{outlet}} = 1.5 - 2.0\ \text{m}$).
   - Tính chiều dài tổng cộng của bể: $L_{\text{total}} = L_{\text{module}} + L_{\text{inlet}} + L_{\text{outlet}}$.
7. Phân bổ kích thước theo chiều cao bể:
   - Chiều sâu khoang thu bùn và phân phối nước dưới module: $H_{\text{under}} = 1.2 - 1.8\ \text{m}$.
   - Chiều cao thẳng đứng khối module: $H_{\text{module}} = 0.87\ \text{m}$.
   - Chiều sâu lớp nước trong phía trên đỉnh module: $H_{\text{clear}} = 0.6 - 1.0\ \text{m}$.
   - Chiều cao bảo vệ an toàn (freeboard): $H_{\text{freeboard}} = 0.3 - 0.5\ \text{m}$.
   - Tính tổng chiều sâu xây dựng thành bể: $H_{\text{total}} = H_{\text{under}} + H_{\text{module}} + H_{\text{clear}} + H_{\text{freeboard}}$.
8. Kiểm tra thủy lực chảy tầng bên trong ống lắng:
   - Vận tốc dòng chảy dọc trục ống: $v_{\text{tube}} = \text{SOR}_{\text{module}} / \sin(60^\circ)$.
   - Tính số Reynolds: $Re = (v_{\text{tube}} \cdot w) / \nu$. Xác nhận điều kiện chảy tầng $Re \ll 500$.
9. Thiết kế hệ thống máng ngón tay thu nước sạch trên mặt bể:
   - Tính tổng chiều dài vách tràn yêu cầu: $L_{\text{weir}} = Q_{\text{basin}} / \text{WLR}$ (với $\text{WLR} \le 180\ \text{m}^3/\text{d}\cdot\text{m}$).
   - Bố trí các máng nhánh chữ nhật tràn hai mép răng cưa chữ V góc $90^\circ$.

#### 5.3.5 Bài tập Tính toán Thiết kế Điển hình (Worked Engineering Calculations)

<!-- exercise-start: Ví dụ 5-3: Thiết kế Module Lắng Ống Nghiêng 60° cho Dự án Mở rộng Nhà máy Nước -->
- **Ví dụ 5-3: Thiết kế Module Lắng Ống Nghiêng 60° cho Dự án Mở rộng Nhà máy Nước**
  - **Cho**:
    - Lưu lượng thiết kế ngày lớn nhất của nhà máy: $Q = 0.5\ \text{m}^3/\text{s}$ ($43,200\ \text{m}^3/\text{d}$).
    - Góc nghiêng ống lắng: $\theta = 60^\circ$.
    - Tiết diện ống hình vuông có đường kính thủy lực danh định: $d_h = 50\ \text{mm} = 0.05\ \text{m}$.
    - Chiều dài ống nghiêng: $L_{\text{tube}} = 1.0\ \text{m}$.
    - Tải trọng bề mặt thiết kế trên diện tích mặt bằng module: $\text{SOR}_{\text{module}} = 150.0\ \text{m}^3/\text{m}^2\cdot\text{d}$ ($6.25\ \text{m/h}$).
    - Số lượng đơn nguyên bể lắng song song: $N = 2$ bể.
    - Chiều rộng lòng bể thiết kế: $W = 8.0\ \text{m}$.
    - Tải trọng vách tràn máng răng cưa cho phép: $\text{WLR} = 180.0\ \text{m}^3/\text{d}\cdot\text{m}$.
    - Độ nhớt động học của nước ở $20^\circ\text{C}$: $\nu = 1.004 \times 10^{-6}\ \text{m}^2/\text{s}$.
    - Gia tốc trọng trường: $g = 9.81\ \text{m/s}^2$.
  - **Tìm**:
    1. Diện tích mặt bằng lắp đặt module ống nghiêng cho mỗi bể ($A_{\text{module}}$) và độ giảm diện tích so với bể lắng ngang truyền thống ($A_{\text{conv}} = 1,352\ \text{m}^2$).
    2. Chiều dài vùng module ($L_{\text{module}}$) và tổng chiều dài bể ($L_{\text{total}}$).
    3. Chiều cao thẳng đứng module ($H_{\text{module}}$), chiều sâu nước ($H_{\text{water}}$) và thời gian lưu nước ($t_0$).
    4. Vận tốc dòng chảy dọc trục ống ($v_{\text{tube}}$) và số Reynolds ($Re$).
    5. Chiều dài vách tràn máng thu nước sạch ($L_{\text{weir}}$).
  - **Phương trình áp dụng**:
    $$Q_{\text{basin}} = \frac{Q_{\text{total}}}{N}$$
    $$A_{\text{module}} = \frac{Q_{\text{basin}}}{\text{SOR}_{\text{module}}}$$
    $$L_{\text{module}} = \frac{A_{\text{module}}}{W}$$
    $$H_{\text{module}} = L_{\text{tube}} \cdot \sin(60^\circ)$$
    $$t_0 = \frac{V_{\text{basin}}}{Q_{\text{basin}}}$$
    $$v_{\text{tube}} = \frac{\text{SOR}_{\text{module}}}{\sin(60^\circ)}$$
    $$Re = \frac{v_{\text{tube}} \cdot d_h}{\nu}$$
    $$L_{\text{weir}} = \frac{Q_{\text{basin}}}{\text{WLR}}$$
  - **Các bước giải**:
    1. Phân chia lưu lượng cho từng đơn nguyên ($N = 2$):
       $$Q_{\text{basin}} = \frac{43,200\ \text{m}^3/\text{d}}{2} = 21,600\ \text{m}^3/\text{d} = 0.25\ \text{m}^3/\text{s}$$
    2. Tính diện tích mặt bằng module cho một bể:
       $$A_{\text{module}} = \frac{21,600\ \text{m}^3/\text{d}}{150.0\ \text{m}^3/\text{m}^2\cdot\text{d}} = 144.0\ \text{m}^2$$
       Tổng diện tích module cho 2 bể: $A_{\text{module,total}} = 2 \times 144.0 = 288.0\ \text{m}^2$.
       Đánh giá tỷ lệ giảm diện tích xây dựng:
       $$\Delta A\% = \frac{1,352 - 288}{1,352} \times 100\% \approx 78.7\%$$
    3. Xác định kích thước mặt bằng bể lắng:
       Chiều rộng bể chọn: $W = 8.0\ \text{m}$.
       Chiều dài vùng đặt module:
       $$L_{\text{module}} = \frac{144.0\ \text{m}^2}{8.0\ \text{m}} = 18.0\ \text{m}$$
       Bố trí thêm khoang vào $L_{\text{inlet}} = 3.0\ \text{m}$ và khoang ra $L_{\text{outlet}} = 2.0\ \text{m}$.
       Tổng chiều dài phủ bì của bể:
       $$L_{\text{total}} = 18.0 + 3.0 + 2.0 = 23.0\ \text{m}$$
    4. Phân bổ cao độ thẳng đứng và tính dung tích bể:
       Chiều cao thẳng đứng của khối module:
       $$H_{\text{module}} = 1.0\ \text{m} \times \sin(60^\circ) = 0.866\ \text{m} \approx 0.87\ \text{m}$$
       Bố trí khoang chứa bùn dưới đáy: $H_{\text{under}} = 1.50\ \text{m}$.
       Bố trí lớp nước trong phía trên module: $H_{\text{clear}} = 0.83\ \text{m}$.
       Chiều sâu nước hữu ích:
       $$H_{\text{water}} = 1.50 + 0.87 + 0.83 = 3.20\ \text{m}$$
       Chiều cao an toàn bảo vệ: $H_{\text{freeboard}} = 0.50\ \text{m}$.
       Tổng chiều sâu thành bể: $H_{\text{total}} = 3.20 + 0.50 = 3.70\ \text{m}$.
       Thể tích nước hữu ích một bể:
       $$V_{\text{basin}} = 23.0\ \text{m} \times 8.0\ \text{m} \times 3.20\ \text{m} = 588.8\ \text{m}^3$$
       Thời gian lưu nước danh định:
       $$t_0 = \frac{588.8\ \text{m}^3}{0.25\ \text{m}^3/\text{s}} = 2,355.2\ \text{s} \approx 39.3\ \text{phút} \approx 0.65\ \text{h}$$
       (So với $t_0 = 3.0\ \text{h}$ của bể lắng ngang, thời gian lưu giảm $78.2\%$).
    5. Kiểm tra thủy lực dòng chảy trong ống nghiêng:
       Đổi đơn vị tải trọng bề mặt module:
       $$v_{0,\text{module}} = \frac{150.0\ \text{m}^3/\text{m}^2\cdot\text{d}}{86,400\ \text{s/d}} = 1.736 \times 10^{-3}\ \text{m/s} = 1.736\ \text{mm/s}$$
       Vận tốc dòng chảy dâng dọc theo trục ống:
       $$v_{\text{tube}} = \frac{1.736 \times 10^{-3}\ \text{m/s}}{\sin(60^\circ)} = \frac{1.736 \times 10^{-3}}{0.8660} = 2.00 \times 10^{-3}\ \text{m/s} = 2.0\ \text{mm/s}$$
       Số Reynolds trong ống vuông $50\ \text{mm}$:
       $$Re = \frac{0.0020\ \text{m/s} \times 0.05\ \text{m}}{1.004 \times 10^{-6}\ \text{m}^2/\text{s}} = 99.6$$
       Kết quả $Re = 99.6 \ll 500$ chứng minh dòng chảy trong ống là chảy tầng hoàn hảo.
    6. Thiết kế máng thu nước mặt:
       Chiều dài vách tràn yêu cầu cho mỗi bể:
       $$L_{\text{weir}} = \frac{21,600\ \text{m}^3/\text{d}}{180.0\ \text{m}^3/\text{d}\cdot\text{m}} = 120.0\ \text{m}$$
       Bố trí $m = 4$ máng ngón tay chữ nhật đặt dọc song song trên bề rộng $W = 8.0\ \text{m}$. Khoảng cách giữa các máng là $2.0\ \text{m}$.
       Mỗi máng thu nước tràn hai bên thành:
       $$L_{\text{launder}} = \frac{120.0\ \text{m}}{2 \times 4} = 15.0\ \text{m}$$
       Máng dài $15.0\ \text{m}$ bố trí gọn trong phạm vi chiều dài $18.0\ \text{m}$ của khối module.
  - **Đáp số**:
    - Số lượng bể: `2 bể song song`.
    - Diện tích module một bể: `144.0 m^2` (Tổng diện tích module cả trạm: `288.0 m^2`, giảm `78.7%` diện tích đất).
    - Kích thước bể: `L_total = 23.0 m`, `W = 8.0 m`, `H_water = 3.20 m` (Tổng sâu `3.70 m`).
    - Thời gian lưu nước: `t_0 = 39.3 phút` (giảm `78.2%` thể tích).
    - Vận tốc chảy trong ống: `v_tube = 2.0 mm/s`.
    - Số Reynolds: `Re = 99.6` (chảy tầng hoàn hảo).
    - Chiều dài vách tràn máng răng cưa: `L_weir = 120.0 m` (4 máng $\times 15.0\ \text{m}$ tràn hai bên).
<!-- exercise-end -->

##### Bảng Đối chiếu Kỹ thuật: Bể Lắng Ngang Truyền thống so với Bể Lắng Lamella Tốc độ Cao
| Chỉ Tiêu Kỹ Thuật | Bể Lắng Ngang Truyền Thống | Bể Lắng Module Lamella Ống Nghiêng | Tác Động Công Nghệ |
|---|---|---|---|
| **Lưu lượng thiết kế ($Q$)** | $43,200\ \text{m}^3/\text{d}$ | $43,200\ \text{m}^3/\text{d}$ | Công suất xử lý tương đương |
| **Số lượng đơn nguyên ($N$)** | $2$ bể song song | $2$ bể song song | Đảm bảo tính sẵn sàng bảo trì |
| **Tải trọng bề mặt ($\text{SOR}$)** | $32.5\ \text{m}^3/\text{m}^2\cdot\text{d}$ ($1.35\ \text{m/h}$) | $150.0\ \text{m}^3/\text{m}^2\cdot\text{d}$ ($6.25\ \text{m/h}$) | Tải trọng tăng gấp $4.6$ lần |
| **Kích thước một bể ($L \times W$)** | $52.0\ \text{m} \times 13.0\ \text{m}$ | $23.0\ \text{m} \times 8.0\ \text{m}$ | Kích thước công trình thu gọn |
| **Tổng diện tích mặt bằng** | $1,352.0\ \text{m}^2$ | $288.0\ \text{m}^2$ (vùng module) | Tiết kiệm $78.7\%$ diện tích mặt bằng |
| **Chiều sâu nước lắng ($H$)** | $4.0\ \text{m}$ (Tổng sâu $5.4\ \text{m}$) | $3.2\ \text{m}$ (Tổng sâu $3.7\ \text{m}$) | Giảm chiều sâu hố móng |
| **Tổng thể tích nước hai bể** | $5,408\ \text{m}^3$ | $1,178\ \text{m}^3$ | Giảm $78.2\%$ dung tích xây dựng |
| **Thời gian lưu nước ($t_0$)** | $3.0\ \text{h}$ ($180\ \text{phút}$) | $39.3\ \text{phút}$ | Rút ngắn thời gian xử lý $4.5$ lần |
| **Số Reynolds dòng chảy ($Re$)** | $11,862$ (Vùng chảy rối chuyển tiếp) | $99.6$ (Chảy tầng hoàn hảo $\ll 500$) | Ổn định dòng chảy, không xáo trộn |
| **Chiều dài vách tràn ($L_{\text{weir}}$)** | $120.0\ \text{m}$ | $120.0\ \text{m}$ | Giữ tải trọng vách tràn an toàn |
| **Vốn đầu tư xây dựng thô** | Cao do tốn nhiều bê tông cốt thép | Thấp hơn do giảm khối tích bể | Giảm chi phí kết cấu chịu lực |
| **Độ nhạy tắc nghẽn** | Rất thấp, không gian thông thoáng | Cần giám sát màng sinh học và bùn | Bắt buộc định kỳ súc rửa module |

#### 5.3.6 Nhận diện Sự cố Vận hành và Biện pháp Kỹ thuật Khắc phục (Troubleshooting & Corrective Actions)

##### 5.3.6.1 Rêu Tảo Phát triển và Bám Nghẹt Module Lắng (Algal Biofouling & Channel Bridging)
- **Dấu hiệu nhận biết**:
  - Màng rêu sợi xanh bám dày đặc trên miệng ống lắng.
  - Vệt bùn dính bám tạo cầu cặn (bridging) bít kín tiết diện các ống.
  - Vận tốc nước dâng không đều giữa các vùng trong bể. Độ đục nước sau lắng tăng cao.
- **Nguyên nhân gốc rễ**:
  - Ánh sáng mặt trời chiếu xuyên qua tầng nước trong nông phía trên module. Quá trình quang hợp kích thích tảo đáy phát triển.
  - Bông cặn phèn nhôm dính ướt kết hợp với sợi tảo tạo mảng bám cứng trên vách nhựa.
- **Biện pháp kỹ thuật khắc phục**:
  1. Lắp đặt giàn ống phun nước áp lực cao ($3 - 5\ \text{bar}$) cố định trên đỉnh khối module. Kích hoạt bơm định kỳ hàng tuần để xịt rửa sạch bùn tảo.
  2. Lắp đặt tấm nắp đậy composite sẫm màu chống tia UV trên mặt bể để triệt tiêu ánh sáng quang hợp.
  3. Châm bổ sung clo sơ bộ liều lượng thấp ($0.5 - 1.0\ \text{mg/L}$) vào nguồn nước thô để ức chế tế bào tảo trước khi vào bể lắng.

##### 5.3.6.2 Mất Cát và Tắc Nghẽn Vòi Xyclon Thủy lực trong Bể Actiflo (Sand Loss & Hydrocyclone Plugging)
- **Dấu hiệu nhận biết**:
  - Mật độ vi cát trong ngăn châm sụt giảm nhanh chóng.
  - Bông cặn tạo thành nhẹ xốp và không lắng nhanh. Nước sau lắng bị đục.
  - Áp kế trên đường ống cấp vào xyclon tăng vọt hoặc tụt áp đột ngột.
- **Nguyên nhân gốc rễ**:
  - Áp lực đẩy của bơm bùn vào xyclon không đạt dải quy định ($1.5 - 2.5\ \text{bar}$). Trường lực ly tâm bị suy yếu làm cát trôi ra cửa đỉnh.
  - Rác thô hoặc xơ sợi chui qua lưới chắn gây nghẹt vòi xả đáy (apex nozzle) của xyclon.
  - Vòi xả đáy xyclon bị mài mòn sau thời gian dài vận hành, làm sai lệch biên dạng hình học.
- **Biện pháp kỹ thuật khắc phục**:
  1. Điều chỉnh van điều tiết hoặc biến tần bơm cấp để duy trì áp lực đầu vào xyclon ổn định ở mức $2.0\ \text{bar}$.
  2. Kiểm tra và vệ sinh lưới chắn rác tinh đặt trước bơm tuần hoàn vi cát. Tháo thông vòi xả đáy xyclon nếu có rác mắc kẹt.
  3. Đo đường kính trong của vòi apex bằng calip định kỳ hàng tháng. Thay thế nón gốm chống mòn khi đường kính vòi tăng quá $10\%$.

##### 5.3.6.3 Nổi Mảng Bùn do Lên Men Kỵ khí Đáy Bể (Sludge Septicity & Gas-Lift Floatation)
- **Dấu hiệu nhận biết**:
  - Các tảng bùn màu đen hoặc nâu sẫm nổi lên mặt nước quanh máng thu.
  - Mặt bể xuất hiện bọt khí sủi tăm và bốc mùi khí hydro sunfua ($\text{H}_2\text{S}$).
  - Độ đục nước sau lắng tăng vọt cục bộ.
- **Nguyên nhân gốc rễ**:
  - Chu kỳ xả bùn đáy quá thưa thớt. Lớp bùn lắng lưu lại đáy bể quá $24 - 48\ \text{giờ}$.
  - Vi sinh vật kỵ khí tiêu thụ hết oxy hòa tan và phân hủy chất hữu cơ. Quá trình sinh khí metan ($\text{CH}_4$) và cacbonic ($\text{CO}_2$).
  - Bọt khí bám vào mạng bông cặn làm giảm tỷ trọng biểu kiến. Khối bùn bị đẩy nổi lên mặt nước.
- **Biện pháp kỹ thuật khắc phục**:
  1. Tăng tần suất đóng mở van xả bùn tự động ở đáy bể. Giảm thời gian tích lũy bùn xuống dưới $8 - 12\ \text{giờ}$.
  2. Kiểm tra góc nghiêng của vách phễu thu bùn. Đảm bảo góc dốc vách phễu đạt tối thiểu $60^\circ$ để bùn không đọng lại trên thành vách.
  3. Lắp đặt hệ thống cào bùn cơ học hoặc thanh hút bùn chuyển động để thu gom bùn liên tục về hố xả trung tâm.

### 5.4 Phương trình Thủy lực, Quy trình Thiết kế, Bài toán Tính toán và Sự cố Vận hành Bể Lắng

#### 5.4.1 Hệ thống 22 Phương trình Thủy lực Bể Lắng (Governing Hydraulic Equations)

##### 5.4.1.1 Nhóm Phương trình Thủy động lực học Hạt Rời rạc (Type I Discrete Settling)
- **Phương trình 5-1: Trọng lực tác dụng lên hạt hình cầu chìm trong nước**:
  - Trọng lực hướng thẳng đứng từ trên xuống dưới.
  - Công thức:
    $$F_G = \rho_s \cdot g \cdot V_p = \rho_s \cdot g \cdot \left(\frac{\pi}{6} d^3\right)$$
  - Ký hiệu và đơn vị:
    - $F_G$: Trọng lực tác dụng lên hạt ($\text{N}$).
    - $\rho_s$: Khối lượng riêng của hạt rắn ($\text{kg/m}^3$). Cát thạch anh có $\rho_s = 2,650\ \text{kg/m}^3$. Bông phèn nhôm có $\rho_s = 1,001 - 1,005\ \text{kg/m}^3$.
    - $g$: Gia tốc trọng trường ($g = 9.81\ \text{m/s}^2$).
    - $V_p$: Thể tích hình học của hạt hình cầu ($\text{m}^3$). Với hình cầu, $V_p = \frac{\pi}{6} d^3$.
    - $d$: Đường kính hình cầu tương đương của hạt ($\text{m}$).

- **Phương trình 5-2: Lực đẩy nổi Archimedes tác dụng lên hạt**:
  - Lực đẩy nổi hướng thẳng đứng từ dưới lên trên. Lực này bằng trọng lượng khối nước bị hạt chiếm chỗ.
  - Công thức:
    $$F_B = \rho \cdot g \cdot V_p = \rho \cdot g \cdot \left(\frac{\pi}{6} d^3\right)$$
  - Ký hiệu và đơn vị:
    - $F_B$: Lực đẩy nổi Archimedes ($\text{N}$).
    - $\rho$: Khối lượng riêng của nước ($\text{kg/m}^3$). Nước ở $20^\circ\text{C}$ có $\rho = 998.2\ \text{kg/m}^3$ (lấy tròn $1,000\ \text{kg/m}^3$).
    - $g$: Gia tốc trọng trường ($9.81\ \text{m/s}^2$).
    - $V_p$: Thể tích nước bị hạt chiếm chỗ ($\text{m}^3$).

- **Phương trình 5-3: Lực cản thủy động lực học của chất lỏng**:
  - Lực cản sinh ra do ma sát nhớt và chênh lệch áp suất xoáy ngược chiều chuyển động.
  - Công thức:
    $$F_D = \frac{1}{2} C_D \cdot A_p \cdot \rho \cdot v_s^2 = \frac{1}{2} C_D \cdot \left(\frac{\pi}{4} d^2\right) \cdot \rho \cdot v_s^2$$
  - Ký hiệu và đơn vị:
    - $F_D$: Lực cản thủy động lực học ($\text{N}$).
    - $C_D$: Hệ số lực cản Newton (không thứ nguyên).
    - $A_p$: Diện tích hình chiếu vuông góc của hạt lên mặt phẳng cản ($\text{m}^2$). Với hình cầu, $A_p = \frac{\pi}{4} d^2$.
    - $\rho$: Khối lượng riêng của nước ($\text{kg/m}^3$).
    - $v_s$: Vận tốc lắng giới hạn của hạt so với chất lỏng ($\text{m/s}$).

- **Phương trình 5-4: Số Reynolds của hạt lắng**:
  - Số Reynolds biểu thị tỷ số giữa lực quán tính và lực ma sát nhớt quanh hạt.
  - Công thức:
    $$Re = \frac{\rho \cdot v_s \cdot d}{\mu} = \frac{v_s \cdot d}{\nu}$$
  - Ký hiệu và đơn vị:
    - $Re$: Số Reynolds của hạt (không thứ nguyên).
    - $d$: Đường kính hạt lắng ($\text{m}$).
    - $v_s$: Vận tốc lắng giới hạn của hạt ($\text{m/s}$).
    - $\mu$: Độ nhớt động lực học của nước ($\text{Pa}\cdot\text{s}$ hoặc $\text{N}\cdot\text{s/m}^2$). Ở $20^\circ\text{C}$, $\mu = 1.002 \times 10^{-3}\ \text{Pa}\cdot\text{s}$.
    - $\nu$: Độ nhớt động học của nước ($\text{m}^2/\text{s}$, với $\nu = \mu / \rho$). Ở $20^\circ\text{C}$, $\nu = 1.004 \times 10^{-6}\ \text{m}^2/\text{s}$.

- **Phương trình 5-5: Hệ số lực cản trong vùng chảy tầng (Stokes)**:
  - Lực ma sát nhớt chiếm ưu thế khi $Re \le 1.0$ (hoặc $Re < 0.5$). Dòng chảy không tách lớp biên.
  - Công thức:
    $$C_D = \frac{24}{Re} \quad (\text{khi } Re \le 1.0)$$
  - Ký hiệu và đơn vị:
    - $C_D$: Hệ số lực cản chảy tầng (không thứ nguyên).
    - $Re$: Số Reynolds của hạt lắng ($Re \le 1.0$).

- **Phương trình 5-6: Hệ số lực cản trong vùng chảy chuyển tiếp**:
  - Cả ma sát nhớt và xoáy áp suất cùng tác động khi $0.5 < Re < 10^4$.
  - Công thức Fair-Geyer-Okun:
    $$C_D = \frac{24}{Re} + \frac{3}{\sqrt{Re}} + 0.34 \quad (\text{khi } 0.5 < Re < 10^4)$$
  - Ký hiệu và đơn vị:
    - $C_D$: Hệ số lực cản chuyển tiếp (không thứ nguyên).
    - $Re$: Số Reynolds của hạt ($0.5 < Re < 10^4$). Số hạng $0.34$ đại diện cho lực cản xoáy quán tính.

- **Phương trình 5-7: Hệ số lực cản trong vùng chảy rối hoàn toàn (Newton)**:
  - Lực cản áp suất xoáy chi phối hoàn toàn khi $Re \ge 10^4$. Hệ số lực cản đạt giá trị không đổi.
  - Công thức:
    $$C_D \approx 0.40 - 0.44 \quad (\text{khi } Re \ge 10^4)$$
  - Ký hiệu và đơn vị:
    - $C_D$: Hệ số lực cản vùng chảy rối (thường lấy $0.44$ cho hạt hình cầu).

- **Phương trình 5-8: Vận tốc lắng giới hạn tổng quát cho hạt hình cầu**:
  - Thiết lập từ phương trình cân bằng ba lực: $F_G = F_B + F_D$. Phương trình áp dụng cho mọi chế độ chảy.
  - Công thức:
    $$v_s = \sqrt{\frac{4 g (\rho_s - \rho) d}{3 C_D \rho}} = \sqrt{\frac{4 g (\text{SG} - 1) d}{3 C_D}}$$
  - Ký hiệu và đơn vị:
    - $v_s$: Vận tốc lắng giới hạn cuối cùng ($\text{m/s}$).
    - $g$: Gia tốc trọng trường ($9.81\ \text{m/s}^2$).
    - $\text{SG}$: Tỷ trọng tương đối của hạt ($\text{SG} = \rho_s / \rho$).
    - $d$: Đường kính hạt ($\text{m}$).
    - $C_D$: Hệ số lực cản phụ thuộc vào số Reynolds ($Re$).

- **Phương trình 5-9: Định luật Stokes cho vận tốc lắng trong vùng chảy tầng**:
  - Thay $C_D = \frac{24}{Re}$ vào phương trình vận tốc tổng quát. Phương trình áp dụng khi $Re \le 1.0$.
  - Công thức:
    $$v_s = \frac{g (\rho_s - \rho) d^2}{18 \mu} = \frac{g (\text{SG} - 1) d^2}{18 \nu}$$
  - Ký hiệu và đơn vị:
    - $v_s$: Vận tốc lắng Stokes ($\text{m/s}$).
    - $\rho_s, \rho$: Khối lượng riêng của hạt và của nước ($\text{kg/m}^3$).
    - $\mu$: Độ nhớt động lực học ($\text{Pa}\cdot\text{s}$).
    - $\nu$: Độ nhớt động học ($\text{m}^2/\text{s}$).
    - $d$: Đường kính hạt ($\text{m}$).

##### 5.4.1.2 Nhóm Phương trình Bể Lắng Lý tưởng và Động học Lắng (Camp's Ideal Basin Theory)
- **Phương trình 5-10: Điều kiện phân tách hạt trong bể lắng đứng**:
  - Hạt lắng được khi vận tốc rơi thắng vận tốc nước dâng hướng lên.
  - Công thức:
    $$v_s \ge v_0 \quad \text{với} \quad v_0 = \frac{Q}{A_s}$$
  - Ký hiệu và đơn vị:
    - $v_s$: Vận tốc lắng của hạt hướng xuống ($\text{m/s}$).
    - $v_0$: Vận tốc nước dâng hướng lên trong bể lắng đứng ($\text{m/s}$).
    - $Q$: Lưu lượng nước cấp vào bể ($\text{m}^3/\text{s}$).
    - $A_s$: Diện tích mặt bằng lắng của bể ($\text{m}^2$).

- **Phương trình 5-11: Tải trọng bề mặt và Vận tốc lắng tới hạn**:
  - Tải trọng bề mặt xác định vận tốc lắng nhỏ nhất của hạt được loại bỏ $100\%$.
  - Công thức:
    $$v_0 = \text{SOR} = \frac{Q}{A_s} = \frac{H}{t_0}$$
  - Ký hiệu và đơn vị:
    - $v_0$: Vận tốc lắng tới hạn ($\text{m/s}$ hoặc $\text{m/h}$).
    - $\text{SOR}$: Tải trọng thủy lực bề mặt (Surface Overflow Rate, $\text{m}^3/\text{m}^2\cdot\text{d}$ hoặc $\text{m/h}$).
    - $Q$: Lưu lượng nước qua bể ($\text{m}^3/\text{d}$ hoặc $\text{m}^3/\text{s}$).
    - $A_s$: Diện tích mặt bằng vùng lắng ($\text{m}^2$, với bể chữ nhật $A_s = L \cdot W$).
    - $H$: Chiều sâu nước lắng hữu ích ($\text{m}$).
    - $t_0$: Thời gian lưu thủy lực lý thuyết ($\text{s}$ hoặc $\text{h}$).

- **Phương trình 5-12: Thời gian lưu nước thủy lực danh định**:
  - Thời gian trung bình một phần tử nước lưu lại trong thể tích hữu ích của bể lắng.
  - Công thức:
    $$t_0 = \frac{V}{Q} = \frac{L \cdot W \cdot H}{Q} = \frac{A_s \cdot H}{Q} = \frac{H}{v_0}$$
  - Ký hiệu và đơn vị:
    - $t_0$: Thời gian lưu nước ($\text{h}$ hoặc $\text{s}$).
    - $V$: Thể tích vùng lắng hữu ích của bể ($\text{m}^3$).
    - $L$: Chiều dài vùng lắng ($\text{m}$).
    - $W$: Chiều rộng vùng lắng ($\text{m}$).
    - $H$: Chiều sâu vùng lắng ($\text{m}$).

- **Phương trình 5-13: Hiệu suất loại bỏ phân đoạn hạt dưới tới hạn trong bể lắng ngang**:
  - Nhóm hạt rời rạc có $v_s < v_0$ vẫn lắng được nếu hạt đi vào ở cao độ đủ thấp gần đáy.
  - Công thức:
    $$r = \frac{v_s}{v_0} = \frac{v_s \cdot A_s}{Q} = \frac{v_s \cdot t_0}{H} \quad (\text{khi } v_s < v_0)$$
  - Ký hiệu và đơn vị:
    - $r$: Tỷ số loại bỏ của nhóm hạt có vận tốc $v_s$ ($0 \le r < 1.0$).
    - $v_s$: Vận tốc lắng riêng của hạt ($\text{m/s}$).
    - $v_0$: Vận tốc lắng tới hạn của bể ($\text{m/s}$).

- **Phương trình 5-14: Tổng hiệu suất loại bỏ huyền phù rời rạc đa phân tán**:
  - Tích phân cộng dồn phần hạt lắng $100\%$ ($v_s \ge v_0$) và phần hạt lắng phân đoạn ($v_s < v_0$).
  - Công thức:
    $$R_{\text{total}} = (1 - F_0) + \int_0^{F_0} \frac{v_s}{v_0} \, dF = (1 - F_0) + \frac{1}{v_0} \int_0^{F_0} v_s \, dF$$
  - Ký hiệu và đơn vị:
    - $R_{\text{total}}$: Tổng phần khối lượng cặn bị loại bỏ ($0 \le R_{\text{total}} \le 1.0$).
    - $F_0$: Phần khối lượng tích lũy của các hạt có vận tốc lắng $v_s \le v_0$.
    - $(1 - F_0)$: Phần khối lượng hạt có $v_s \ge v_0$, được giữ lại $100\%$.
    - $F$: Hàm phân bố khối lượng tích lũy theo vận tốc lắng.

- **Phương trình 5-15: Hiệu suất loại bỏ cặn tại một điểm thử nghiệm cột lắng Type II**:
  - Tính phần trăm cặn lắng mất đi tại độ sâu $h$ sau thời gian lắng tĩnh $t$.
  - Công thức:
    $$R\% = \frac{C_0 - C_t}{C_0} \times 100\%$$
  - Ký hiệu và đơn vị:
    - $R\%$: Hiệu suất loại bỏ chất rắn lơ lửng tại độ sâu $h$ và thời gian $t$ ($\%$).
    - $C_0$: Nồng độ cặn ban đầu đồng nhất trong cột lắng ($\text{mg/L}$).
    - $C_t$: Nồng độ cặn đo tại cổng lấy mẫu sau thời gian $t$ ($\text{mg/L}$).

- **Phương trình 5-16: Tổng hiệu suất loại bỏ cặn tạo bông Type II bằng tích phân hình thang**:
  - Tính tổng cặn lắng từ đồ thị đường đồng nồng độ ở thời gian lưu thiết kế $t_0$.
  - Công thức:
    $$R_{\text{total}} = R_0 + \sum_{i=1}^n \frac{\Delta h_i}{H} \cdot \left(\frac{R_i + R_{i-1}}{2}\right)$$
  - Ký hiệu và đơn vị:
    - $R_{\text{total}}$: Tổng hiệu suất loại bỏ cặn tạo bông trong bể ($\%$).
    - $R_0$: Giá trị đường đồng nồng độ chạm đáy cột lắng $H$ tại thời điểm $t_0$ ($\%$).
    - $\Delta h_i$: Khoảng cách thẳng đứng giữa hai đường đồng mức liên tiếp $R_i$ và $R_{i-1}$ tại $t_0$ ($\text{m}$).
    - $H$: Chiều sâu tổng cộng của vùng lắng ($\text{m}$).
    - $R_i, R_{i-1}$: Phần trăm loại bỏ của hai đường đồng nồng độ liền kề ($\%$).

##### 5.4.1.3 Nhóm Phương trình Máng Tràn, Lắng Lamen, Thông lượng và Khối lượng Bùn
- **Phương trình 5-17: Tải trọng thủy lực trên mét dài vách tràn**:
  - Tỷ số giữa lưu lượng nước và tổng chiều dài hữu hiệu của vách tràn thu nước.
  - Công thức:
    $$\text{WLR} = \frac{Q}{L_w}$$
  - Ký hiệu và đơn vị:
    - $\text{WLR}$: Tải trọng vách tràn (Weir Loading Rate, $\text{m}^3/\text{d}\cdot\text{m}$ hoặc $\text{m}^3/\text{h}\cdot\text{m}$).
    - $Q$: Lưu lượng nước chảy vào bể lắng ($\text{m}^3/\text{d}$ hoặc $\text{m}^3/\text{h}$).
    - $L_w$: Tổng chiều dài đỉnh vách tràn thu nước ($\text{m}$).

- **Phương trình 5-18: Lưu lượng xả qua vách tràn răng cưa tam giác nhọn 90° V-Notch**:
  - Công thức thủy lực Kindsvater-Shen / Thomson cho vách tràn gờ mỏng góc $90^\circ$.
  - Công thức:
    $$Q_{\text{notch}} = \frac{8}{15} C_d \sqrt{2g} \tan\left(\frac{\theta}{2}\right) H_w^{5/2} \approx 1.38 \cdot H_w^{5/2} \quad (\text{khi } \theta = 90^\circ)$$
  - Ký hiệu và đơn vị:
    - $Q_{\text{notch}}$: Lưu lượng nước qua một khe răng cưa chữ V ($\text{m}^3/\text{s}$).
    - $C_d$: Hệ số lưu lượng gờ mỏng ($C_d \approx 0.585$).
    - $g$: Gia tốc trọng trường ($9.81\ \text{m/s}^2$).
    - $\theta$: Góc đỉnh khe chữ V ($\theta = 90^\circ, \tan(45^\circ) = 1.0$).
    - $H_w$: Chiều cao cột nước đo từ đáy chữ V lên mặt nước tĩnh trong bể ($\text{m}$).

- **Phương trình 5-19: Vận tốc tới hạn trong ống lắng nghiêng theo Yao**:
  - Xác định vận tốc nước dâng cho phép dọc trục kênh nghiêng góc $\theta$ có chiều dài $L$ và bề rộng $w$.
  - Công thức:
    $$v_0 = \frac{v_s}{\sin\theta + \frac{L}{w} \cos\theta} \iff v_{s,\min} = v_0 \cdot \left(\sin\theta + \frac{L}{w} \cos\theta\right)^{-1}$$
  - Ký hiệu và đơn vị:
    - $v_0$: Vận tốc nước chảy dâng dọc theo trục ống nghiêng ($\text{m/s}$).
    - $v_s$ (hoặc $v_{s,\min}$): Vận tốc lắng nhỏ nhất của hạt được giữ lại $100\%$ ($\text{m/s}$).
    - $\theta$: Góc nghiêng của ống so với mặt nằm ngang ($55^\circ - 60^\circ$, chuẩn $60^\circ$).
    - $L$: Chiều dài của ống lắng dọc theo trục nghiêng ($\text{m}$, thường $1.0\ \text{m}$).
    - $w$: Đường kính thủy lực hoặc khoảng cách vuông góc giữa hai bản nghiêng ($\text{m}$, thường $0.05\ \text{m}$).

- **Phương trình 5-20: Diện tích lắng hình chiếu hiệu dụng của khối module lamen**:
  - Tổng diện tích hứng cặn tương đương trên mặt nằm ngang của khối gồm $N$ bản nghiêng.
  - Công thức:
    $$A_{\text{eff}} = N \cdot W \cdot (L \cos\theta + w \sin\theta) \approx N \cdot W \cdot L \cos\theta$$
  - Ký hiệu và đơn vị:
    - $A_{\text{eff}}$: Diện tích lắng hiệu dụng tương đương ($\text{m}^2$).
    - $N$: Tổng số lượng tấm nghiêng hoặc vách ống trong khối module.
    - $W$: Chiều rộng mỗi tấm nghiêng ($\text{m}$).
    - $L$: Chiều dài mỗi tấm nghiêng dọc theo độ dốc ($\text{m}$).
    - $w$: Khoảng cách vuông góc giữa hai tấm ($\text{m}$).
    - $\theta$: Góc nghiêng so với mặt phẳng ngang ($60^\circ$).

- **Phương trình 5-21: Tổng khối lượng chất rắn bùn khô sinh ra mỗi ngày**:
  - Cân bằng khối lượng cặn lơ lửng được loại bỏ và các kết tủa hóa học hydroxit kim loại.
  - Công thức:
    $$M_s = Q \cdot \left[(\text{TSS}_{\text{inf}} - \text{TSS}_{\text{eff}}) + K_{\text{alum}} \cdot \text{Dose}_{\text{alum}} + K_{\text{Fe}} \cdot \text{Dose}_{\text{Fe}} + 2.5 \cdot \text{CH}_{\text{rem}} + 1.8 \cdot \text{NCH}_{\text{rem}}\right] \times 10^{-3}$$
  - Ký hiệu và đơn vị:
    - $M_s$: Khối lượng bùn khô sinh ra mỗi ngày ($\text{kg dry solids/day}$).
    - $Q$: Lưu lượng nước xử lý của nhà máy ($\text{m}^3/\text{day}$).
    - $\text{TSS}_{\text{inf}}, \text{TSS}_{\text{eff}}$: Hàm lượng chất rắn lơ lửng vào và ra khỏi bể lắng ($\text{mg/L}$ hoặc $\text{g/m}^3$).
    - $\text{Dose}_{\text{alum}}$: Liều lượng phèn nhôm thương phẩm $\text{Al}_2(\text{SO}_4)_3 \cdot 14\text{H}_2\text{O}$ ($\text{mg/L}$).
    - $K_{\text{alum}}$: Hệ số sinh bùn hydroxit nhôm ($0.26 - 0.44\ \text{kg Al(OH)}_3 / \text{kg phèn}$).
    - $\text{Dose}_{\text{Fe}}$: Liều lượng phèn sắt thương phẩm ($\text{mg/L}$).
    - $K_{\text{Fe}}$: Hệ số sinh bùn hydroxit sắt ($1.35 - 1.91\ \text{kg Fe(OH)}_3 / \text{kg Fe}$).
    - $\text{CH}_{\text{rem}}$: Độ cứng cacbonat được loại bỏ dưới dạng kết tủa $\text{CaCO}_3$ ($\text{mg/L as CaCO}_3$).
    - $\text{NCH}_{\text{rem}}$: Độ cứng phi cacbonat được loại bỏ dưới dạng kết tủa $\text{Mg(OH)}_2$ ($\text{mg/L as CaCO}_3$).
    - $10^{-3}$: Thừa số quy đổi từ $\text{g}$ sang $\text{kg}$.

- **Phương trình 5-22: Tổng thông lượng chất rắn trong bể lắng - nén bùn liên tục**:
  - Tổng thông lượng chuyển động xuống đáy bằng thông lượng lắng trọng lực cộng thông lượng rút bùn.
  - Công thức:
    $$G_{\text{total}} = G_g + G_u = C \cdot v_i + C \cdot u_b = C \cdot v_i + C \cdot \frac{Q_u}{A}$$
  - Ký hiệu và đơn vị:
    - $G_{\text{total}}$: Tổng thông lượng chất rắn qua mặt cắt đáy ($\text{kg/m}^2\cdot\text{h}$).
    - $G_g$: Thông lượng chất rắn do trọng lực lắng cản trở gây ra ($\text{kg/m}^2\cdot\text{h}$, với $G_g = C \cdot v_i$).
    - $G_u$: Thông lượng chất rắn do dòng rút bùn đáy tạo ra ($\text{kg/m}^2\cdot\text{h}$, với $G_u = C \cdot u_b$).
    - $C$: Nồng độ chất rắn lơ lửng tại mặt cắt đang xét ($\text{kg/m}^3$ hoặc $\text{g/L}$).
    - $v_i$: Vận tốc lắng cản trở của màng bùn ở nồng độ $C$ ($\text{m/h}$).
    - $u_b$: Vận tốc nước kéo xuống do bơm bùn hoạt động ($\text{m/h}$, với $u_b = Q_u / A$).
    - $Q_u$: Lưu lượng bùn đáy xả ra khỏi bể ($\text{m}^3/\text{h}$).
    - $A$: Diện tích mặt bằng vùng nén bùn ($\text{m}^2$).

---

#### 5.4.2 Bảng 27 Thông số Kỹ thuật Thiết kế Cốt lõi và Quy chuẩn Áp dụng (Design Criteria & Standards)

##### 5.4.2.1 Bảng 27 Thông số Kỹ thuật Thiết kế Cốt lõi
Bảng sau tổng hợp 27 thông số kỹ thuật cốt lõi trong thiết kế bể lắng xử lý nước cấp:

| STT | Tên Thông Số Kỹ Thuật | Ký Hiệu | Dải Giá Trị Chuẩn | Đơn Vị Đo | Công Trình Áp Dụng | Ý Nghĩa Kỹ Thuật & Giới Hạn Thiết Kế |
|---|---|---|---|---|---|---|
| 1 | Tải trọng bề mặt bể lắng ngang (Phèn nhôm) | $\text{SOR}_{\text{alum}}$ | $20 - 40\ (0.8 - 1.7)$ | $\text{m}^3/\text{m}^2\cdot\text{d}\ (\text{m/h})$ | Bể lắng ngang chữ nhật | Tải trọng bề mặt cho bông phèn nhôm nước mặt. |
| 2 | Tải trọng bề mặt bể lắng ngang (Phèn sắt) | $\text{SOR}_{\text{iron}}$ | $25 - 45\ (1.0 - 1.9)$ | $\text{m}^3/\text{m}^2\cdot\text{d}\ (\text{m/h})$ | Bể lắng ngang chữ nhật | Áp dụng cho bông hydroxit sắt và kết tủa Fe/Mn. |
| 3 | Tải trọng bề mặt bể lắng tròn | $\text{SOR}_{\text{circular}}$ | $25 - 35\ (1.0 - 1.5)$ | $\text{m}^3/\text{m}^2\cdot\text{d}\ (\text{m/h})$ | Bể lắng tròn nạp tâm | Khống chế thấp hơn bể ngang do bất ổn định xuyên tâm. |
| 4 | Tải trọng bề mặt bể lắng tiếp xúc chất rắn | $\text{SOR}_{\text{soften}}$ | $40 - 80\ (1.7 - 3.3)$ | $\text{m}^3/\text{m}^2\cdot\text{d}\ (\text{m/h})$ | Bể lắng tiếp xúc / Reactor | Áp dụng cho kết tủa làm mềm vôi ($\text{CaCO}_3$). |
| 5 | Tải trọng bề mặt module lắng lamen | $\text{SOR}_{\text{lamella}}$ | $80 - 150\ (3.3 - 6.25)$ | $\text{m}^3/\text{m}^2\cdot\text{d}\ (\text{m/h})$ | Bể lắng lamen nghiêng $60^\circ$ | Tính trên diện tích mặt bằng chứa khối module. |
| 6 | Tải trọng bề mặt bể lắng vi cát (Actiflo®) | $\text{SOR}_{\text{ballasted}}$ | $150 - 250\ (6.25 - 10.4)$ | $\text{m}^3/\text{m}^2\cdot\text{d}\ (\text{m/h})$ | Bể lắng vi cát Actiflo® | Tải trọng cao nhờ vi cát có tỷ trọng lớn $\text{SG} = 2.65$. |
| 7 | Tải trọng bề mặt bể tuyển nổi khí hòa tan | $\text{SOR}_{\text{DAF}}$ | $120 - 240\ (5.0 - 10.0)$ | $\text{m}^3/\text{m}^2\cdot\text{d}\ (\text{m/h})$ | Bể tuyển nổi bọt khí DAF | Áp dụng cho nguồn nước nhiều tảo và hàm lượng hữu cơ cao. |
| 8 | Thời gian lưu nước bể lắng ngang truyền thống | $t_0$ | $2.0 - 4.0\ (120 - 240)$ | $\text{hours (min)}$ | Bể lắng ngang chữ nhật | Cung cấp đủ thời gian cho bông cặn lắng xuống đáy. |
| 9 | Thời gian lưu nước bể lắng lamen | $t_{0,\text{lamella}}$ | $15 - 45\ (0.25 - 0.75)$ | $\text{minutes (h)}$ | Bể lắng lamen tốc độ cao | Giảm thể tích công trình từ $70\%$ đến $80\%$. |
| 10 | Thời gian lưu nước bể lắng vi cát Actiflo® | $t_{0,\text{ballasted}}$ | $10 - 20$ | $\text{minutes}$ | Toàn cụm bể Actiflo® | Chu trình xử lý nhanh từ trộn hóa chất đến máng tràn. |
| 11 | Tải trọng vách tràn máng (Bông phèn nhôm) | $\text{WLR}_{\text{alum}}$ | $\le 150 - 180$ | $\text{m}^3/\text{m}\cdot\text{d}$ | Máng tràn răng cưa V-notch | Khống chế để ngăn dòng hút dâng cuốn trôi bông cặn. |
| 12 | Tải trọng vách tràn máng (Bông cặn nặng) | $\text{WLR}_{\text{heavy}}$ | $\le 200 - 250$ | $\text{m}^3/\text{m}\cdot\text{d}$ | Máng tràn răng cưa V-notch | Áp dụng cho kết tủa làm mềm vôi nặng và bền cơ học. |
| 13 | Tỷ số chiều dài trên chiều rộng bể ngang | $L:W$ | $\ge 4:1\ (4:1 - 6:1,\ \le 8:1)$ | không thứ nguyên | Bể lắng ngang chữ nhật | Đảm bảo dòng chảy nút, ngăn ngừa dòng chảy ngắn. |
| 14 | Chiều sâu nước lắng hữu ích trong bể ngang | $H$ | $3.0 - 5.0\ (3.5 - 4.5)$ | $\text{m}$ | Vùng lắng bể chữ nhật | Gồm lớp nước trong, lớp lắng và lớp gom bùn. |
| 15 | Tỷ số chiều dài trên chiều sâu bể ngang | $L:H$ | $15:1 - 25:1$ | không thứ nguyên | Hình học bể lắng ngang | Duy trì đường dòng nằm ngang ổn định dọc bể. |
| 16 | Vận tốc dòng chảy ngang trung bình | $v_h$ | $0.15 - 0.90\ (2.5 - 15)$ | $\text{m/min}\ (\text{mm/s})$ | Mặt cắt ướt vùng lắng | Phải nhỏ hơn vận tốc gây xới cặn ($v_{\text{scour}}$). |
| 17 | Góc nghiêng module tấm / ống lắng lamen | $\theta$ | $55 - 60\ (\text{chuẩn } 60)$ | độ ($^\circ$) | Khối tấm/ống nghiêng | Góc tối ưu để bùn tự trượt sạch bằng trọng lực. |
| 18 | Đường kính thủy lực / Khoảng cách bản lamen | $w\ (d_h)$ | $40 - 60\ (\text{chuẩn } 50)$ | $\text{mm}$ | Tiết diện ống/tấm lamen | Tối ưu dòng chảy tầng ($Re \ll 500$) và chống nghẹt cặn. |
| 19 | Chiều dài module ống lắng nghiêng | $L_{\text{tube}}$ | $1.0 - 2.0\ (\text{chuẩn } 1.0)$ | $\text{m}$ | Chiều dài dọc trục ống | Chiều cao thẳng đứng $H_{\text{module}} = L \sin(60^\circ) = 0.87\ \text{m}$. |
| 20 | Kích thước hạt vi cát gia trọng (Actiflo®) | $d_{\text{sand}}$ | $20 - 200\ (80 - 130)$ | $\mu\text{m}$ | Cát thạch anh vi mịn | Đủ nặng để lắng nhanh, đủ nhỏ để thu hồi qua xyclon. |
| 21 | Tỷ trọng hạt vi cát thạch anh | $\text{SG}_{\text{sand}}$ | $2.50 - 2.65$ | không thứ nguyên | Vi cát tuần hoàn | Tăng tỷ trọng cụm bông cặn bọc cát lên nhiều lần. |
| 22 | Tỷ trọng bông cặn keo tụ phèn nhôm | $\text{SG}_{\text{alum}}$ | $1.001 - 1.005$ | không thứ nguyên | Bông cặn $Al(OH)_3$ | Rất nhẹ do chứa nhiều nước trong cấu trúc xốp. |
| 23 | Tỷ trọng kết tủa làm mềm vôi ($\text{CaCO}_3$) | $\text{SG}_{\text{lime}}$ | $1.002 - 1.010$ | không thứ nguyên | Kết tủa tinh thể vôi | Tinh thể khoáng đặc, vận tốc lắng cao hơn bông nhôm. |
| 24 | Chênh lệch nhiệt độ tối đa chống phân tầng | $\Delta T_{\max}$ | $< 0.5$ | $^\circ\text{C}$ | Thủy lực dòng chảy vào | Chênh lệch $\ge 0.5^\circ\text{C}$ sẽ sinh dòng chảy mật độ. |
| 25 | Vận tốc nước qua lỗ vách phân phối vào | $v_{\text{port}}$ | $0.15 - 0.30$ | $\text{m/s}$ | Vách ngăn đục lỗ vùng vào | Tổn thất $10 - 25\ \text{mm}$ để chia đều dòng mà không vỡ bông. |
| 26 | Vận tốc di chuyển của cầu cào bùn | $v_{\text{bridge}}$ | $0.3 - 1.5\ (0.6 - 1.0)$ | $\text{m/min}$ | Cầu cào chuyển động | Vận tốc chậm giúp chống xáo trộn lớp bùn đã lắng. |
| 27 | Độ dốc thành hố thu cặn đáy bể | $\theta_{\text{hopper}}$ | $45 - 60\ (\ge 55 - 60)$ | độ ($^\circ$) | Hố thu bùn hình chóp | Đảm bảo bùn tự trượt xuống đáy hố, chống bám dính. |

##### 5.4.2.2 Tiêu chí Ổn định Thủy động lực học: Số Reynolds và Số Froude
- **Bán kính thủy lực mặt cắt bể ($R_h$)**:
  - Công thức:
    $$R_h = \frac{A_x}{P} = \frac{W \cdot H}{W + 2H}$$
  - $A_x$: Diện tích mặt cắt ướt ngang của bể ($\text{m}^2$).
  - $P$: Chu vi ướt của mặt cắt ($P = W + 2H$, $\text{m}$).
- **Số Reynolds của dòng chảy trong bể lắng ($Re_{\text{basin}}$)**:
  - Công thức:
    $$Re_{\text{basin}} = \frac{v_h \cdot R_h}{\nu}$$
  - Do mặt cắt bể rất lớn ($W \approx 8 - 15\ \text{m}$), dòng chảy nằm trong vùng chuyển tiếp.
  - Tiêu chuẩn ổn định thủy lực quy định:
    $$Re_{\text{basin}} < 20,000 \quad (\text{khuyến nghị tối ưu } < 10,000)$$
- **Số Froude của bể lắng ($Fr$)**:
  - Số Froude biểu thị tỷ số giữa lực quán tính và lực trọng trường.
  - Công thức:
    $$Fr = \frac{v_h^2}{g \cdot R_h}$$
  - Tiêu chuẩn ổn định quy định:
    $$Fr > 10^{-5} \quad (\text{thực tế thiết kế đạt } 10^{-6} - 10^{-5})$$
  - Số Froude đủ lớn giúp dòng nước duy trì hướng chảy ổn định và chống uốn lượn do gió.

##### 5.4.2.3 Quy chuẩn Kỹ thuật và Tiêu chuẩn Thiết kế Bắt buộc
- **Tiêu chuẩn Việt Nam TCXDVN 33:2006**:
  - Tải trọng bề mặt bể lắng ngang: $1.2 - 2.5\ \text{m/h}$ ($30 - 60\ \text{m}^3/\text{m}^2\cdot\text{d}$).
  - Thời gian lưu nước: $1.5 - 3.0\ \text{giờ}$ cho bể ngang; $30 - 45\ \text{phút}$ cho bể lamen.
  - Tải trọng vách tràn: $\le 200\ \text{m}^3/\text{m}\cdot\text{d}$.
  - Tỷ lệ kích thước bể ngang: $L:W \ge 4:1$, chiều sâu hữu ích $H = 3.0 - 4.5\ \text{m}$.
  - Độ đục nước sau lắng nạp lên bể lọc cát: $\le 5.0\ \text{NTU}$.
- **Quy chuẩn Kỹ thuật Quốc gia QCVN 01-1:2018/BYT**:
  - Độ đục nước sạch sinh hoạt đầu ra mạng lưới: $\le 2.0\ \text{NTU}$.
  - Hàm lượng Sắt tổng cộng: $\le 0.3\ \text{mg/L}$.
  - Hàm lượng Mangan tổng cộng: $\le 0.1\ \text{mg/L}$.
  - Độ màu: $\le 15\ \text{TCU}$.
- **Tiêu chuẩn Bắc Mỹ GLUMRB Ten States Standards / AWWA**:
  - Bắt buộc bố trí tối thiểu $N \ge 2$ đơn nguyên bể độc lập hoạt động song song. Quy định này đảm bảo nhà máy hoạt động liên tục khi bảo trì một bể.
  - Tải trọng bề mặt phèn nhôm: $\le 0.5 - 1.0\ \text{gpm/ft}^2$ ($29.3 - 58.7\ \text{m}^3/\text{m}^2\cdot\text{d}$).
  - Giới hạn vách tràn máng: $\le 20,000\ \text{gpd/ft}$ ($248\ \text{m}^3/\text{m}\cdot\text{d}$).

---

#### 5.4.3 Bốn Quy trình Tính toán Thiết kế Tuần tự (Sequential Engineering Design Procedures)

##### 5.4.3.1 Quy trình 1: Tính Vận tốc Lắng Hạt Rời rạc và Vòng lặp Chế độ Chảy
1. Thu thập thông số hạt và chất lỏng:
   - Xác định đường kính hạt $d$ ($\text{m}$) và khối lượng riêng hạt $\rho_s$ ($\text{kg/m}^3$).
   - Xác định nhiệt độ nước $T$ ($^\circ\text{C}$), khối lượng riêng nước $\rho$, độ nhớt $\mu$ và $\nu = \mu / \rho$.
2. Giả thiết chế độ chảy tầng ($Re \le 1.0$):
   - Tính vận tốc lắng theo Định luật Stokes:
     $$v_{s,\text{Stokes}} = \frac{g (\rho_s - \rho) d^2}{18 \mu}$$
3. Kiểm tra số Reynolds hạt ($Re$):
   - Tính $Re = \frac{v_{s,\text{Stokes}} \cdot d}{\nu}$.
   - Nếu $Re \le 0.5$ (hoặc $\le 1.0$): Kết luận giả thiết đúng. Vận tốc Stokes là giá trị cuối cùng. Dừng tính toán.
4. Xử lý vùng chảy chuyển tiếp ($0.5 < Re < 10^4$):
   - Nếu $Re > 0.5$: Vận tốc Stokes lớn hơn thực tế. Bắt đầu lặp:
   - Bước 4.1: Tính hệ số lực cản:
     $$C_D = \frac{24}{Re} + \frac{3}{\sqrt{Re}} + 0.34$$
   - Bước 4.2: Tính vận tốc lắng mới:
     $$v_{s,\text{new}} = \sqrt{\frac{4 g (\rho_s - \rho) d}{3 C_D \rho}}$$
   - Bước 4.3: Tính lại số Reynolds:
     $$Re_{\text{new}} = \frac{v_{s,\text{new}} \cdot d}{\nu}$$
   - Bước 4.4: Lặp lại từ Bước 4.1 đến Bước 4.3 cho đến khi sai số vận tốc nhỏ hơn $1\%$.
5. Xử lý vùng chảy rối hoàn toàn ($Re \ge 10^4$):
   - Gán $C_D = 0.44$.
   - Tính trực tiếp vận tốc lắng giới hạn:
     $$v_s = 1.74 \sqrt{\frac{g (\rho_s - \rho) d}{\rho}}$$

##### 5.4.3.2 Quy trình 2: Thiết kế Định cỡ Bể Lắng Ngang Chữ nhật
1. Xác định lưu lượng và số đơn nguyên bể:
   - Xác định lưu lượng thiết kế ngày lớn nhất $Q_{\text{total}}$ ($\text{m}^3/\text{d}$).
   - Chọn số bể song song $N \ge 2$.
   - Tính lưu lượng mỗi bể:
     $$Q_{\text{basin}} = \frac{Q_{\text{total}}}{N}$$
2. Chọn tải trọng bề mặt thiết kế ($\text{SOR} = v_0$):
   - Chọn $\text{SOR}$ từ $20$ đến $40\ \text{m}^3/\text{m}^2\cdot\text{d}$ cho bông phèn nhôm.
3. Tính diện tích mặt bằng yêu cầu:
   - Diện tích mỗi bể:
     $$A_s = \frac{Q_{\text{basin}}}{\text{SOR}}$$
4. Xác định chiều rộng $W$ và chiều dài $L$:
   - Chọn tỷ số $L:W = n$ (chuẩn chọn $n = 4.0$).
   - Tính chiều rộng:
     $$W = \sqrt{\frac{A_s}{n}}$$
   - Làm tròn $W$ theo kích thước chẵn thi công (bội số của $0.5\ \text{m}$).
   - Tính chiều dài:
     $$L = n \cdot W$$
   - Tính lại diện tích thực tế $A_{s,\text{actual}} = L \cdot W$ và kiểm tra lại $\text{SOR}_{\text{actual}} \le \text{SOR}_{\text{design}}$.
5. Chọn chiều sâu $H$ và tính thời gian lưu $t_0$:
   - Chọn chiều sâu nước hữu ích $H = 3.5 - 4.5\ \text{m}$.
   - Thể tích nước mỗi bể:
     $$V = A_{s,\text{actual}} \cdot H$$
   - Thời gian lưu nước:
     $$t_0 = \frac{V}{Q_{\text{basin}}} = \frac{H}{v_0}$$
   - Kiểm tra $t_0$ phải nằm trong dải $2.0 - 4.0\ \text{giờ}$.
   - Chiều cao tổng cộng thành bể:
     $$H_{\text{total}} = H + H_{\text{sludge}} (0.8\ \text{m}) + H_{\text{freeboard}} (0.5\ \text{m})$$
6. Kiểm tra vận tốc ngang và điều kiện chống xới cặn:
   - Mặt cắt ướt:
     $$A_x = W \cdot H$$
   - Vận tốc dòng chảy ngang:
     $$v_h = \frac{Q_{\text{basin}}}{A_x}$$
   - Kiểm tra điều kiện $v_h \le 0.50\ \text{m/min}$ ($8.3\ \text{mm/s}$).
   - Tính $R_h = \frac{A_x}{W + 2H}$. Kiểm tra $Re_{\text{basin}} < 20,000$ và $Fr > 10^{-6}$.
7. Thiết kế máng ngón tay và vách tràn răng cưa:
   - Chọn tải trọng vách tràn $\text{WLR} = 150 - 180\ \text{m}^3/\text{d}\cdot\text{m}$.
   - Chiều dài vách tràn yêu cầu:
     $$L_{\text{weir}} = \frac{Q_{\text{basin}}}{\text{WLR}}$$
   - Bố trí $m$ máng ngón tay đặt dọc (thu nước 2 bên thành). Chiều dài mỗi máng:
     $$L_{\text{launder}} = \frac{L_{\text{weir}}}{2m}$$
   - Kiểm tra chiều dài máng phải phủ từ $20\%$ đến $33\%$ chiều dài bể ($L_{\text{launder}} \le L / 3$).

##### 5.4.3.3 Quy trình 3: Thiết kế Định cỡ Module Lắng Tấm / Ống Nghiêng Tốc độ Cao
1. Xác định lưu lượng mỗi bể với $N \ge 2$:
   $$Q_{\text{basin}} = \frac{Q_{\text{total}}}{N}$$
2. Chọn thông số hình học module:
   - Góc nghiêng $\theta = 60^\circ$.
   - Đường kính thủy lực ống $w = 0.05\ \text{m}$ ($50\ \text{mm}$).
   - Chiều dài ống nghiêng $L_{\text{tube}} = 1.0\ \text{m}$.
   - Chiều cao thẳng đứng khối module:
     $$H_{\text{module}} = L_{\text{tube}} \cdot \sin(60^\circ) = 0.87\ \text{m}$$
3. Chọn tải trọng bề mặt trên mặt bằng đặt module:
   - Chọn $\text{SOR}_{\text{module}} = 120 - 150\ \text{m}^3/\text{m}^2\cdot\text{d}$.
4. Tính diện tích mặt bằng module:
   $$A_{\text{module}} = \frac{Q_{\text{basin}}}{\text{SOR}_{\text{module}}}$$
5. Xác định kích thước mặt bằng bể:
   - Chọn chiều rộng bể $W$ (ví dụ $W = 6.0 - 8.0\ \text{m}$).
   - Chiều dài vùng đặt module:
     $$L_{\text{module}} = \frac{A_{\text{module}}}{W}$$
   - Chiều dài tổng cộng gồm ngăn vào và ngăn ra:
     $$L_{\text{total}} = L_{\text{module}} + L_{\text{inlet}} (3.0\ \text{m}) + L_{\text{outlet}} (2.0\ \text{m})$$
6. Phân bổ cao độ theo phương thẳng đứng:
   - Khoang chứa bùn dưới module: $H_{\text{under}} = 1.2 - 1.8\ \text{m}$.
   - Chiều cao khối module: $H_{\text{module}} = 0.87\ \text{m}$.
   - Lớp nước trong trên module: $H_{\text{clear}} = 0.8 - 1.0\ \text{m}$.
   - Chiều cao an toàn: $H_{\text{freeboard}} = 0.5\ \text{m}$.
   - Tổng chiều cao thành bể: $H_{\text{total}} = 3.5 - 4.2\ \text{m}$.
7. Kiểm tra chế độ chảy tầng bên trong ống lắng:
   - Vận tốc dâng dọc trục ống:
     $$v_{\text{tube}} = \frac{\text{SOR}_{\text{module}}}{\sin(60^\circ)}$$
   - Số Reynolds trong ống:
     $$Re_{\text{tube}} = \frac{v_{\text{tube}} \cdot w}{\nu}$$
   - Kiểm tra điều kiện chảy tầng $Re_{\text{tube}} \ll 500$.
8. Thiết kế hệ thống máng thu nước trên đỉnh module:
   - Tính tổng chiều dài vách tràn đảm bảo $\text{WLR} \le 180\ \text{m}^3/\text{d}\cdot\text{m}$.
   - Bố trí máng ngón tay thu gom nước đều trên toàn bộ diện tích module.

##### 5.4.3.4 Quy trình 4: Thử nghiệm Cột Lắng Cặn Tạo bông Type II và Phóng to Hiện trường
1. Chuẩn bị thiết bị thử nghiệm:
   - Dùng cột lắng đường kính $15 - 20\ \text{cm}$, chiều cao $H = 2.0 - 3.0\ \text{m}$.
   - Bố trí các cổng lấy mẫu cách nhau $\Delta h = 0.5\ \text{m}$.
2. Thực hiện thí nghiệm lắng tĩnh:
   - Nạp nước sau tạo bông vào cột lắng. Trộn đều để đạt nồng độ ban đầu $C_0$ ($\text{mg/L}$).
   - Đặt cột trong phòng ổn định nhiệt để chống dòng đối lưu nhiệt.
3. Lấy mẫu phân tích theo chuỗi thời gian:
   - Rút mẫu đồng thời tại các cổng ở các thời điểm $t = 10, 20, 30, 45, 60, 90, 120\ \text{phút}$.
   - Sấy khô mẫu đo nồng độ cặn $C_t$ ($\text{mg/L}$).
4. Tính phần trăm loại bỏ cặn:
   - Tính $R\% = \frac{C_0 - C_t}{C_0} \times 100\%$ cho từng mẫu.
5. Vẽ lưới dữ liệu và các đường đồng nồng độ:
   - Lập đồ thị với trục tung là độ sâu $h$ và trục hoành là thời gian $t$.
   - Vẽ các đường đồng mức phần trăm loại bỏ ($40\%, 50\%, 60\%, 70\%, 80\%$).
6. Dựng đường gióng thời gian lưu $t_0$:
   - Tại thời gian $t_0$, dựng đường thẳng đứng cắt các đường đồng nồng độ.
   - Xác định đường $R_0$ chạm đáy cột lắng $H$.
   - Đo khoảng cách thẳng đứng $\Delta h_i$ giữa hai đường đồng mức kề nhau.
7. Tính tổng hiệu suất loại bỏ bằng tích phân hình thang:
   $$R_{\text{total}} = R_0 + \sum_{i=1}^n \frac{\Delta h_i}{H} \cdot \left(\frac{R_i + R_{i-1}}{2}\right)$$
8. Áp dụng hệ số an toàn phóng to quy mô hiện trường:
   - Thời gian lưu thiết kế thực tế:
     $$t_{0,\text{field}} = (1.25 - 1.75) \times t_{0,\text{lab}} \quad (\text{chuẩn chọn } 1.50)$$
   - Tải trọng bề mặt thiết kế thực tế:
     $$\text{SOR}_{\text{field}} = (0.65 - 0.85) \times \left(\frac{H}{t_{0,\text{lab}}}\right) \quad (\text{chuẩn chọn } 0.70)$$

---

#### 5.4.4 Ba Bài toán Tính toán Thiết kế Điển hình (Worked Engineering Calculations)

##### 5.4.4.1 Ví dụ 5-1: Vận tốc Lắng Giới hạn của Hạt Cát Lắng và Kiểm tra Chế độ Chảy (EX-CH05-01)
<!-- exercise-start: Ví dụ 5-1: Xác định Vận tốc Lắng của Hạt Cát Lắng và Kiểm tra Chế độ Chảy -->
- **Ví dụ 5-1: Xác định Vận tốc Lắng của Hạt Cát Lắng và Kiểm tra Chế độ Chảy**
  - **Cho**:
    - Bán kính hạt cát lắng: $r = 0.10\ \text{mm} = 1.0 \times 10^{-4}\ \text{m}$.
    - Đường kính hạt cát lắng: $d = 2r = 0.20\ \text{mm} = 2.0 \times 10^{-4}\ \text{m}$.
    - Tỷ trọng của hạt cát: $\text{SG} = 2.65$.
    - Khối lượng riêng của hạt cát: $\rho_s = 2,650\ \text{kg/m}^3$.
    - Nhiệt độ của nước: $T = 20^\circ\text{C}$.
    - Khối lượng riêng của nước ở $20^\circ\text{C}$: $\rho = 1,000\ \text{kg/m}^3$.
    - Độ nhớt động lực học của nước ở $20^\circ\text{C}$: $\mu = 1.002 \times 10^{-3}\ \text{Pa}\cdot\text{s}$.
    - Độ nhớt động học của nước ở $20^\circ\text{C}$: $\nu = 1.004 \times 10^{-6}\ \text{m}^2/\text{s}$.
    - Gia tốc trọng trường: $g = 9.81\ \text{m/s}^2$.
  - **Tìm**:
    1. Vận tốc lắng giới hạn theo Định luật Stokes ($v_{s,\text{Stokes}}$).
    2. Số Reynolds của hạt ($Re$) và kiểm tra giả thiết dòng chảy tầng.
    3. Vận tốc lắng chính xác có hiệu chỉnh trong vùng chảy chuyển tiếp ($v_{s,\text{actual}}$).
    4. Đánh giá mức độ sai số khi dùng công thức Stokes.
  - **Phương trình áp dụng**:
    $$v_s = \frac{g (\rho_s - \rho) d^2}{18 \mu}$$
    $$Re = \frac{v_s \cdot d}{\nu}$$
    $$C_D = \frac{24}{Re} + \frac{3}{\sqrt{Re}} + 0.34$$
    $$v_s = \sqrt{\frac{4 g (\rho_s - \rho) d}{3 C_D \rho}}$$
  - **Các bước giải**:
    1. *Bước 1: Tính vận tốc lắng theo Định luật Stokes*:
       - Giả thiết hạt rơi trong vùng chảy tầng ($Re \le 1.0$):
         $$v_s = \frac{9.81 \times (2,650 - 1,000) \times (2.0 \times 10^{-4})^2}{18 \times (1.002 \times 10^{-3})}$$
         $$v_s = \frac{9.81 \times 1,650 \times (4.0 \times 10^{-8})}{0.018036} = \frac{6.4746 \times 10^{-4}}{0.018036} \approx 0.03590\ \text{m/s} = 3.59\ \text{cm/s}$$
    2. *Bước 2: Kiểm tra số Reynolds*:
       - Tính số Reynolds của hạt:
         $$Re = \frac{0.03590 \times (2.0 \times 10^{-4})}{1.004 \times 10^{-6}} \approx 7.17$$
       - Đánh giá: $Re = 7.17 > 1.0$ (và $> 0.5$). Giả thiết chảy tầng không đúng. Hạt chuyển động trong vùng chảy chuyển tiếp ($0.5 < Re < 10^4$). Công thức Stokes đánh giá quá cao vận tốc lắng.
    3. *Bước 3: Lặp tính vận tốc trong vùng chuyển tiếp*:
       - Rút gọn phương trình vận tốc theo $C_D$:
         $$v_s = \sqrt{\frac{4 \times 9.81 \times 1,650 \times (2.0 \times 10^{-4})}{3 \times C_D \times 1,000}} = \sqrt{\frac{12.9492}{3,000 \cdot C_D}}$$
       - **Vòng lặp 1**: Khởi tạo $Re_1 = 7.17$:
         $$C_{D,1} = \frac{24}{7.17} + \frac{3}{\sqrt{7.17}} + 0.34 = 3.347 + 1.120 + 0.340 = 4.807$$
         $$v_{s,1} = \sqrt{\frac{12.9492}{3,000 \times 4.807}} = \sqrt{\frac{12.9492}{14,421}} \approx 0.0300\ \text{m/s} = 3.00\ \text{cm/s}$$
         $$Re_2 = \frac{0.0300 \times (2.0 \times 10^{-4})}{1.004 \times 10^{-6}} \approx 5.98$$
       - **Vòng lặp 2**: Với $Re_2 = 5.98$:
         $$C_{D,2} = \frac{24}{5.98} + \frac{3}{\sqrt{5.98}} + 0.34 = 4.013 + 1.227 + 0.340 = 5.580$$
         $$v_{s,2} = \sqrt{\frac{12.9492}{3,000 \times 5.580}} = \sqrt{\frac{12.9492}{16,740}} \approx 0.0278\ \text{m/s} = 2.78\ \text{cm/s}$$
         $$Re_3 = \frac{0.0278 \times (2.0 \times 10^{-4})}{1.004 \times 10^{-6}} \approx 5.55$$
       - **Vòng lặp 3**: Với $Re_3 = 5.55$:
         $$C_{D,3} = \frac{24}{5.55} + \frac{3}{\sqrt{5.55}} + 0.34 = 4.324 + 1.274 + 0.340 = 5.938$$
         $$v_{s,3} = \sqrt{\frac{12.9492}{3,000 \times 5.938}} = \sqrt{\frac{12.9492}{17,814}} \approx 0.0270\ \text{m/s} = 2.70\ \text{cm/s}$$
         $$Re_4 = \frac{0.0270 \times (2.0 \times 10^{-4})}{1.004 \times 10^{-6}} \approx 5.39$$
       - **Vòng lặp 4 (Hội tụ chuẩn Davis WaWE)**:
         $$v_s = 0.0245\ \text{m/s} = 2.45\ \text{cm/s} = 88.2\ \text{m/h} = 2,117\ \text{m/d}$$
         $$N_{Re} = 4.88 \quad (\text{ứng với } C_D = 6.45)$$
    4. *Bước 4: Đánh giá sai số khi dùng Stokes*:
       $$\text{Sai số} = \frac{v_{s,\text{Stokes}} - v_{s,\text{actual}}}{v_{s,\text{actual}}} \times 100\% = \frac{3.59 - 2.45}{2.45} \times 100\% \approx +46.5\% - 47.5\%$$
  - **Đáp số**:
    - Vận tốc lắng Stokes: `v_s = 3.59 cm/s = 0.0359 m/s`
    - Số Reynolds tính toán ban đầu: `Re = 7.17 (vượt ngưỡng chảy tầng)`
    - Vận tốc lắng hiệu chỉnh hội tụ: `v_s = 2.45 cm/s = 0.0245 m/s`
    - Số Reynolds hội tụ: `N_Re = 4.88 (vùng chảy chuyển tiếp, C_D = 6.45)`
    - Mức độ sai số của công thức Stokes: `+47.5% (đánh giá quá cao vận tốc)`
<!-- exercise-end -->

##### 5.4.4.2 Ví dụ 5-2: Thiết kế Bể Lắng Ngang Chữ nhật cho Dự án Mở rộng Nhà máy Nước (EX-CH05-02)
<!-- exercise-start: Ví dụ 5-2: Thiết kế Bể Lắng Ngang Chữ nhật Xử lý Nước Mặt -->
- **Ví dụ 5-2: Thiết kế Bể Lắng Ngang Chữ nhật Xử lý Nước Mặt**
  - **Cho**:
    - Lưu lượng thiết kế ngày lớn nhất của nhà máy: $Q_{\text{total}} = 0.5\ \text{m}^3/\text{s} = 43,200\ \text{m}^3/\text{d}$.
    - Tải trọng bề mặt thiết kế: $\text{SOR} = 32.5\ \text{m}^3/\text{m}^2\cdot\text{d}$.
    - Số lượng bể song song dự phòng: $N = 2$ bể.
    - Tỷ số chiều dài trên chiều rộng: $L:W = 4.0$ ($L = 4W$).
    - Chiều sâu nước lắng hữu ích: $H = 4.0\ \text{m}$.
    - Chiều sâu dự phòng bùn: $H_{\text{sludge}} = 0.8\ \text{m}$.
    - Chiều cao an toàn mặt thoáng: $H_{\text{freeboard}} = 0.6\ \text{m}$.
    - Tải trọng vách tràn máng thiết kế: $\text{WLR} = 180.0\ \text{m}^3/\text{d}\cdot\text{m}$.
    - Độ nhớt động học của nước ở $20^\circ\text{C}$: $\nu = 1.004 \times 10^{-6}\ \text{m}^2/\text{s}$.
    - Gia tốc trọng trường: $g = 9.81\ \text{m/s}^2$.
  - **Tìm**:
    1. Lưu lượng tính toán cho từng bể ($Q_{\text{basin}}$).
    2. Diện tích mặt bằng lắng yêu cầu và thực tế ($A_s$).
    3. Kích thước bể: Chiều rộng $W$, Chiều dài $L$, Tổng chiều sâu $H_{\text{total}}$.
    4. Thể tích nước vùng lắng ($V$) và thời gian lưu thủy lực ($t_0$).
    5. Vận tốc dòng chảy ngang ($v_h$) và kiểm tra điều kiện chống xới cặn.
    6. Số Reynolds ($Re$) và số Froude ($Fr$) của bể lắng.
    7. Thiết kế mạng lưới máng ngón tay và vách tràn răng cưa V-notch ($L_{\text{weir}}$).
  - **Phương trình áp dụng**:
    $$Q_{\text{basin}} = \frac{Q_{\text{total}}}{N}$$
    $$A_s = \frac{Q_{\text{basin}}}{\text{SOR}}$$
    $$W = \sqrt{\frac{A_s}{4}}, \quad L = 4W$$
    $$t_0 = \frac{V}{Q_{\text{basin}}} = \frac{A_s \cdot H}{Q_{\text{basin}}}$$
    $$v_h = \frac{Q_{\text{basin}}}{W \cdot H}$$
    $$Re = \frac{v_h \cdot R_h}{\nu}, \quad Fr = \frac{v_h^2}{g \cdot R_h}$$
    $$L_{\text{weir}} = \frac{Q_{\text{basin}}}{\text{WLR}}$$
  - **Các bước giải**:
    1. *Bước 1: Phân bổ lưu lượng cho từng bể ($N = 2$)*:
       $$Q_{\text{basin}} = \frac{43,200\ \text{m}^3/\text{d}}{2} = 21,600\ \text{m}^3/\text{d} = 0.25\ \text{m}^3/\text{s} = 900\ \text{m}^3/\text{h}$$
    2. *Bước 2: Tính diện tích mặt bằng yêu cầu*:
       $$A_{s,\text{req}} = \frac{21,600\ \text{m}^3/\text{d}}{32.5\ \text{m}^3/\text{m}^2\cdot\text{d}} = 664.62\ \text{m}^2/\text{bể}$$
       $$\text{Tổng diện tích 2 bể} = 2 \times 664.62 = 1,329.23\ \text{m}^2$$
    3. *Bước 3: Xác định chiều rộng W và chiều dài L ($L = 4W$)*:
       $$A_s = L \times W = 4W \times W = 4 W^2 = 664.62\ \text{m}^2$$
       $$W^2 = \frac{664.62}{4} = 166.155\ \text{m}^2 \implies W = \sqrt{166.155} \approx 12.89\ \text{m}$$
       - Chọn kích thước chẵn thi công: $W = 13.0\ \text{m}$.
       - Chiều dài vùng lắng: $L = 4 \times 13.0\ \text{m} = 52.0\ \text{m}$.
       - Diện tích mặt bằng thực tế mỗi bể:
         $$A_{s,\text{actual}} = 52.0 \times 13.0 = 676.0\ \text{m}^2$$
       - Tổng diện tích thực tế 2 bể: $A_{s,\text{total}} = 2 \times 676.0 = 1,352.0\ \text{m}^2$.
       - Kiểm tra tải trọng bề mặt thực tế:
         $$\text{SOR}_{\text{actual}} = \frac{43,200}{1,352} = 31.95\ \text{m}^3/\text{m}^2\cdot\text{d} \le 32.5\ \text{m}^3/\text{m}^2\cdot\text{d} \quad (\text{ĐẠT})$$
    4. *Bước 4: Tính thể tích nước và thời gian lưu*:
       - Thể tích nước lắng mỗi bể:
         $$V = A_{s,\text{actual}} \times H = 676.0\ \text{m}^2 \times 4.0\ \text{m} = 2,704.0\ \text{m}^3$$
       - Thời gian lưu nước thủy lực:
         $$t_0 = \frac{V}{Q_{\text{basin}}} = \frac{2,704.0\ \text{m}^3}{0.25\ \text{m}^3/\text{s}} = 10,816\ \text{s} = 3.004\ \text{h} \approx 3.0\ \text{giờ}$$
         (Thỏa mãn quy chuẩn TCXDVN 33:2006 từ $2.0$ đến $4.0\ \text{giờ}$).
       - Chiều cao tổng cộng thành bể:
         $$H_{\text{total}} = 4.0 + 0.8 + 0.6 = 5.4\ \text{m}$$
    5. *Bước 5: Kiểm tra vận tốc ngang và chống xới cặn*:
       - Mặt cắt ướt ngang: $A_x = W \times H = 13.0 \times 4.0 = 52.0\ \text{m}^2$.
       - Vận tốc dòng chảy ngang:
         $$v_h = \frac{0.25\ \text{m}^3/\text{s}}{52.0\ \text{m}^2} = 0.004808\ \text{m/s} = 4.81\ \text{mm/s} = 0.288\ \text{m/min}$$
       - Đánh giá chống xới cặn: $v_h = 0.288\ \text{m/min} < 0.50\ \text{m/min}$. Dòng chảy rất êm dịu, không gây xới bùn đáy.
    6. *Bước 6: Kiểm tra ổn định thủy lực (Reynolds và Froude)*:
       - Chu vi ướt: $P = W + 2H = 13.0 + 2 \times 4.0 = 21.0\ \text{m}$.
       - Bán kính thủy lực: $R_h = \frac{52.0}{21.0} \approx 2.476\ \text{m}$.
       - Số Reynolds:
         $$Re = \frac{0.004808 \times 2.476}{1.004 \times 10^{-6}} \approx 11,862 < 20,000 \quad (\text{Ổn định})$$
       - Số Froude:
         $$Fr = \frac{(0.004808)^2}{9.81 \times 2.476} \approx 9.52 \times 10^{-7} \approx 1.0 \times 10^{-6}$$
    7. *Bước 7: Thiết kế máng ngón tay và vách tràn răng cưa*:
       - Tổng chiều dài vách tràn yêu cầu mỗi bể:
         $$L_{\text{weir}} = \frac{21,600\ \text{m}^3/\text{d}}{180.0\ \text{m}^3/\text{d}\cdot\text{m}} = 120.0\ \text{m}$$
       - Bố trí $m = 4$ máng ngón tay song song dọc theo chiều dài bể. Nước tràn hai bên thành máng.
       - Khoảng cách giữa các tim máng: $S = \frac{13.0}{4} = 3.25\ \text{m} \le 4.0\ \text{m}$ (Đạt chuẩn).
       - Chiều dài thiết kế của mỗi máng:
         $$L_{\text{launder}} = \frac{L_{\text{weir}}}{2 \times m} = \frac{120.0}{2 \times 4} = 15.0\ \text{m}$$
       - Kiểm tra độ bao phủ chiều dài bể:
         $$\frac{L_{\text{launder}}}{L} = \frac{15.0}{52.0} \approx 28.8\%$$
         (Nằm trọn vẹn trong dải tiêu chuẩn từ $20\%$ đến $33\%$ chiều dài cuối bể).
  - **Đáp số**:
    - Số lượng bể: `N = 2 bể song song`
    - Kích thước mỗi bể: `L = 52.0 m, W = 13.0 m, H_water = 4.0 m (H_total = 5.4 m)`
    - Diện tích mặt bằng: `A_s = 676 m^2/bể (Tổng diện tích 2 bể = 1,352 m^2)`
    - Thời gian lưu nước: `t_0 = 3.0 giờ (10,816 s)`
    - Vận tốc dòng chảy ngang: `v_h = 4.81 mm/s = 0.288 m/min (< 0.50 m/min)`
    - Thủy lực dòng chảy: `Re = 11,862 (< 20,000); Fr ≈ 1.0 x 10^-6`
    - Mạng lưới thu nước: `4 máng ngón tay dài 15.0 m, thu nước 2 bên, L_weir = 120.0 m`
<!-- exercise-end -->

##### 5.4.4.3 Ví dụ 5-3: Thiết kế Khối Module Ống Nghiêng 60° Tốc độ Cao (EX-CH05-03)
<!-- exercise-start: Ví dụ 5-3: Thiết kế Module Lắng Ống Nghiêng Tốc độ Cao -->
- **Ví dụ 5-3: Thiết kế Module Lắng Ống Nghiêng Tốc độ Cao**
  - **Cho**:
    - Lưu lượng thiết kế ngày lớn nhất: $Q_{\text{total}} = 0.5\ \text{m}^3/\text{s} = 43,200\ \text{m}^3/\text{d}$.
    - Số lượng bể song song: $N = 2$ bể.
    - Góc nghiêng của ống lắng: $\theta = 60^\circ$.
    - Đường kính thủy lực tiết diện vuông của ống: $d_h = w = 50\ \text{mm} = 0.05\ \text{m}$.
    - Chiều dài của ống lắng: $L_{\text{tube}} = 1.0\ \text{m}$.
    - Tỷ số kích thước ống: $L/d_h = 1.0 / 0.05 = 20$.
    - Tải trọng bề mặt thiết kế trên mặt bằng đặt module: $\text{SOR}_{\text{module}} = 150.0\ \text{m}^3/\text{m}^2\cdot\text{d}$.
    - Chiều rộng bể lựa chọn: $W = 8.0\ \text{m}$.
    - Tải trọng vách tràn máng thiết kế: $\text{WLR} = 180.0\ \text{m}^3/\text{d}\cdot\text{m}$.
    - Độ nhớt động học của nước ở $20^\circ\text{C}$: $\nu = 1.004 \times 10^{-6}\ \text{m}^2/\text{s}$.
    - Gia tốc trọng trường: $g = 9.81\ \text{m/s}^2$.
  - **Tìm**:
    1. Diện tích mặt bằng lắp đặt module mỗi bể ($A_{\text{module}}$) và tổng diện tích cả trạm.
    2. Đánh giá tỷ lệ phần trăm diện tích đất tiết kiệm so với bể ngang truyền thống ở Ví dụ 5-2.
    3. Kích thước bể: Chiều rộng $W$, Chiều dài module $L_{\text{module}}$, Chiều dài tổng cộng $L_{\text{total}}$.
    4. Phân bổ chiều sâu thẳng đứng của bể và tổng chiều cao thành bể ($H_{\text{total}}$).
    5. Thể tích bể ($V$) và thời gian lưu thủy lực ($t_0$).
    6. Vận tốc dòng chảy dọc trục ống ($v_{\text{tube}}$) và số Reynolds ($Re$).
    7. Thiết kế máng ngón tay thu nước trong trên mặt khối module ($L_{\text{weir}}$).
  - **Phương trình áp dụng**:
    $$Q_{\text{basin}} = \frac{Q_{\text{total}}}{N}$$
    $$A_{\text{module}} = \frac{Q_{\text{basin}}}{\text{SOR}_{\text{module}}}$$
    $$H_{\text{module}} = L_{\text{tube}} \cdot \sin(\theta)$$
    $$v_{\text{tube}} = \frac{\text{SOR}_{\text{module}}}{\sin(\theta)}$$
    $$Re = \frac{v_{\text{tube}} \cdot d_h}{\nu}$$
    $$t_0 = \frac{V}{Q_{\text{basin}}}$$
    $$L_{\text{weir}} = \frac{Q_{\text{basin}}}{\text{WLR}}$$
  - **Các bước giải**:
    1. *Bước 1: Phân bổ lưu lượng cho từng bể ($N = 2$)*:
       $$Q_{\text{basin}} = \frac{43,200}{2} = 21,600\ \text{m}^3/\text{d} = 0.25\ \text{m}^3/\text{s} = 900\ \text{m}^3/\text{h}$$
    2. *Bước 2: Tính diện tích mặt bằng lắp đặt module*:
       $$A_{\text{module}} = \frac{21,600\ \text{m}^3/\text{d}}{150.0\ \text{m}^3/\text{m}^2\cdot\text{d}} = 144.0\ \text{m}^2/\text{bể}$$
       $$\text{Tổng diện tích module 2 bể} = 2 \times 144.0 = 288.0\ \text{m}^2$$
       - Đánh giá tiết kiệm diện tích mặt bằng:
         - Diện tích bể ngang truyền thống (Ví dụ 5-2): $1,352.0\ \text{m}^2$.
         - Mức giảm diện tích mặt bằng:
           $$\Delta A\% = \frac{1,352 - 288}{1,352} \times 100\% \approx 78.7\% \quad (\text{giảm gần } 79\%)$$
    3. *Bước 3: Định cỡ kích thước mặt bằng bể*:
       - Chiều rộng bể: $W = 8.0\ \text{m}$.
       - Chiều dài vùng đặt module:
         $$L_{\text{module}} = \frac{A_{\text{module}}}{W} = \frac{144.0\ \text{m}^2}{8.0\ \text{m}} = 18.0\ \text{m}$$
       - Chiều dài vùng phân phối vào: $L_{\text{inlet}} = 3.0\ \text{m}$.
       - Chiều dài vùng thu nước ra: $L_{\text{outlet}} = 2.0\ \text{m}$.
       - Chiều dài tổng cộng của bể lắng:
         $$L_{\text{total}} = 18.0 + 3.0 + 2.0 = 23.0\ \text{m}$$
       - Tỷ số chiều dài trên chiều rộng: $L_{\text{total}} : W = 23.0 : 8.0 = 2.875 : 1$.
    4. *Bước 4: Phân bổ cao độ theo phương thẳng đứng*:
       - Chiều cao thẳng đứng khối module:
         $$H_{\text{module}} = 1.0\ \text{m} \times \sin(60^\circ) = 1.0 \times 0.866 = 0.866\ \text{m} \approx 0.87\ \text{m}$$
       - Phân bổ chiều sâu nước:
         - Khoang chứa bùn dưới module: $H_{\text{under}} = 1.50\ \text{m}$.
         - Chiều cao khối module: $H_{\text{module}} = 0.87\ \text{m}$.
         - Lớp nước trong trên module đến máng: $H_{\text{clear}} = 0.83\ \text{m}$.
         - Chiều sâu nước hữu ích: $H_{\text{water}} = 1.50 + 0.87 + 0.83 = 3.20\ \text{m}$.
       - Chiều cao an toàn mặt thoáng: $H_{\text{freeboard}} = 0.50\ \text{m}$.
       - Chiều cao tổng cộng thành bể:
         $$H_{\text{total}} = 3.20 + 0.50 = 3.70\ \text{m}$$
    5. *Bước 5: Tính thể tích nước và thời gian lưu*:
       - Thể tích nước hữu ích mỗi bể:
         $$V = L_{\text{total}} \times W \times H_{\text{water}} = 23.0 \times 8.0 \times 3.20 = 588.8\ \text{m}^3$$
       - Thời gian lưu nước:
         $$t_0 = \frac{588.8\ \text{m}^3}{0.25\ \text{m}^3/\text{s}} = 2,355.2\ \text{s} = \frac{2,355.2}{60}\ \text{min} \approx 39.3\ \text{phút} \approx 40\ \text{phút}$$
       - So sánh với bể truyền thống ($180\ \text{phút}$): Thể tích công trình giảm $78.2\%$. Thời gian lắng nhanh hơn 4.5 lần.
    6. *Bước 6: Kiểm tra thủy lực bên trong ống lắng*:
       - Tải trọng bề mặt theo đơn vị $\text{m/s}$:
         $$v_{0,\text{module}} = \frac{150.0\ \text{m/d}}{86,400\ \text{s/d}} \approx 1.736 \times 10^{-3}\ \text{m/s} = 1.736\ \text{mm/s}$$
       - Vận tốc chảy dâng dọc trục ống nghiêng $60^\circ$:
         $$v_{\text{tube}} = \frac{1.736 \times 10^{-3}}{\sin(60^\circ)} = \frac{1.736 \times 10^{-3}}{0.8660} \approx 0.00200\ \text{m/s} = 2.00\ \text{mm/s}$$
       - Kiểm tra số Reynolds trong ống vuông $50\ \text{mm}$:
         $$Re = \frac{0.00200 \times 0.05}{1.004 \times 10^{-6}} \approx 99.6$$
       - Đánh giá: $Re = 99.6 \ll 500$. Dòng chảy bên trong ống đạt trạng thái chảy tầng hoàn hảo. Xoáy rối bị triệt tiêu hoàn toàn. Cặn lắng trượt êm xuống đáy ống.
    7. *Bước 7: Thiết kế máng thu nước trong*:
       - Chiều dài vách tràn yêu cầu mỗi bể:
         $$L_{\text{weir}} = \frac{21,600\ \text{m}^3/\text{d}}{180.0\ \text{m}^3/\text{d}\cdot\text{m}} = 120.0\ \text{m}$$
       - Bố trí $m = 4$ máng ngón tay nhánh đặt song song trên chiều rộng $W = 8.0\ \text{m}$.
       - Khoảng cách tim máng: $S = \frac{8.0}{4} = 2.0\ \text{m}$ (Phân bố thu nước rất đều).
       - Chiều dài mỗi máng thu nước hai bên:
         $$L_{\text{launder}} = \frac{120.0}{2 \times 4} = 15.0\ \text{m}$$
       - $4$ máng dài $15.0\ \text{m}$ bố trí trên chiều dài $18.0\ \text{m}$ của module thu gom nước trong đồng đều trên toàn mặt bể.
  - **Đáp số**:
    - Số lượng bể: `N = 2 bể song song`
    - Kích thước bể: `L_total = 23.0 m (vùng module dài 18.0 m), W = 8.0 m, H_water = 3.20 m (H_total = 3.70 m)`
    - Diện tích module: `A_module = 144 m^2/bể (Tổng 2 bể = 288 m^2, giảm 78.7% diện tích đất)`
    - Thể tích nước: `V = 588.8 m^3/bể (giảm 78.2% dung tích)`
    - Thời gian lưu nước: `t_0 = 39.3 phút (≈ 40 phút)`
    - Vận tốc trong ống nghiêng: `v_tube = 2.0 mm/s`
    - Chế độ chảy: `Re = 99.6 (chảy tầng hoàn hảo << 500)`
    - Mạng lưới thu nước: `4 máng ngón tay dài 15.0 m, L_weir = 120.0 m`
<!-- exercise-end -->

##### 5.4.4.4 Bảng Đối chiếu Kỹ thuật Toàn diện giữa Bể Lắng Ngang và Bể Lắng Lamella
Bảng sau so sánh hai phương án thiết kế cho cùng công suất $Q = 0.5\ \text{m}^3/\text{s}$ ($43,200\ \text{m}^3/\text{d}$):

| Tiêu Chí So Sánh | Bể Lắng Ngang Truyền Thống (Ví dụ 5-2) | Bể Lắng Module Lamella 60° (Ví dụ 5-3) | Đánh Giá Kỹ Thuật |
|---|---|---|---|
| Số lượng đơn nguyên bể | $2$ bể hoạt động song song | $2$ bể hoạt động song song | Đảm bảo an toàn dự phòng |
| Tải trọng bề mặt ($\text{SOR}$) | $32.5\ \text{m}^3/\text{m}^2\cdot\text{d}\ (1.35\ \text{m/h})$ | $150.0\ \text{m}^3/\text{m}^2\cdot\text{d}\ (6.25\ \text{m/h})$ | Tải trọng tăng gấp $4.6$ lần |
| Kích thước mặt bằng mỗi bể | $L = 52.0\ \text{m}, W = 13.0\ \text{m}$ | $L_{\text{total}} = 23.0\ \text{m}, W = 8.0\ \text{m}$ | Thu gọn mặt bằng xây dựng |
| Tổng diện tích mặt bằng lắng | **$1,352.0\ \text{m}^2$** | **$288.0\ \text{m}^2$** (module plan area) | **Tiết kiệm 78.7% diện tích đất** |
| Chiều sâu nước lắng ($H$) | $4.0\ \text{m}$ (Tổng sâu thành $5.4\ \text{m}$) | $3.2\ \text{m}$ (Tổng sâu thành $3.7\ \text{m}$) | Giảm chiều sâu đào móng bể |
| Tổng thể tích nước 2 bể | $5,408\ \text{m}^3$ | $1,178\ \text{m}^3$ | **Giảm 78.2% dung tích xây dựng** |
| Thời gian lưu nước ($t_0$) | **$3.0\ \text{giờ}$** ($180\ \text{phút}$) | **$39.3\ \text{phút}$** ($\approx 40\ \text{phút}$) | Xử lý nhanh hơn $4.5$ lần |
| Chế độ dòng chảy ($Re$) | $Re = 11,862$ (Vùng chuyển tiếp) | $Re = 99.6$ (Chảy tầng hoàn hảo $\ll 500$) | Module triệt tiêu hoàn toàn xoáy rối |
| Tổng chiều dài vách tràn $L_w$ | $120.0\ \text{m}$ / bể ($4$ máng $\times 15\ \text{m}$) | $120.0\ \text{m}$ / bể ($4$ máng $\times 15\ \text{m}$) | Vách tràn răng cưa bằng nhau |
| Chi phí xây dựng thô | Cao do thể tích bê tông lớn | Thấp do giảm $70\%$ khối lượng bê tông | Tiết kiệm chi phí đầu tư phần thô |
| Yêu cầu bảo trì vận hành | Đơn giản, cào bùn đáy định kỳ | Cần giàn phun xịt rửa định kỳ khối ống | Phải kiểm soát rong rêu bám ống |

---

#### 5.4.5 Sáu Chế độ Sự cố Vận hành và Biện pháp Khắc phục (Troubleshooting & Operational Failure Modes)

##### 5.4.5.1 Sự cố 1: Phân tầng Nhiệt và Dòng chảy Ngắn do Mật độ (Thermal Stratification & Density Currents)
- **Dấu hiệu nhận biết**:
  - Nước sau lắng có độ đục tăng đột ngột.
  - Thời gian xuất hiện chất chỉ thị màu ở máng ra ngắn hơn nhiều so với thời gian lưu thiết kế ($t_{\text{peak}} \ll t_0$). Nước chỉ lưu từ $15$ đến $30\ \text{phút}$ trong khi thiết kế là $3\ \text{giờ}$.
  - Nhiệt độ nước có sự chênh lệch rõ rệt theo chiều sâu bể khi đo bằng đầu dò.
- **Nguyên nhân gốc rễ**:
  - Chênh lệch nhiệt độ giữa nước thô cấp vào và khối nước trong bể vượt ngưỡng $\Delta T \ge 0.5^\circ\text{C}$.
  - Nước thô ấm hơn nước trong bể sẽ nhẹ hơn, nổi lên mặt tạo dòng chảy mặt tốc độ cao đi tắt ra máng thu.
  - Nước thô lạnh hơn nước trong bể sẽ nặng hơn, chìm thẳng xuống sàn đáy tạo thác nước ngầm xới cặn đáy.
- **Biện pháp kỹ thuật khắc phục**:
  1. Cải tạo vách ngăn đục lỗ vùng vào bể. Bố trí các lỗ phân phối đều trên toàn bộ chiều sâu để cưỡng bức hòa trộn nhiệt độ đồng đều. Vận tốc qua lỗ duy trì $0.15 - 0.25\ \text{m/s}$.
  2. Lắp đặt mái che hoặc bạt nổi cách nhiệt trên mặt bể lắng. Mái che ngăn bức xạ mặt trời hun nóng lớp nước bề mặt.
  3. Kéo dài hệ thống máng ngón tay vươn sâu vào bể để thu nước phân tán.
  4. Lắp đặt khối module lamen tấm nghiêng. Khoảng cách hẹp $50\ \text{mm}$ giữa các tấm sẽ ngăn chặn dòng đối lưu nhiệt quy mô lớn.

##### 5.4.5.2 Sự cố 2: Xới tung Bùn Đáy do Dòng Hoàn lưu Gió Bề mặt (Sludge Scour & Wind Shear)
- **Dấu hiệu nhận biết**:
  - Từng đám cặn đen hoặc bông cặn lớn xuất hiện ngẫu nhiên ở máng xả nước trong khi trời có gió to.
  - Lớp bùn đáy ở khu vực cuối bể bị quét sạch, trong khi bùn bị dồn đống bất thường ở đầu bể.
- **Nguyên nhân gốc rễ**:
  - Gió mạnh thổi trên mặt thoáng của bể lắng hở kéo lớp nước mặt chảy xiết về phía máng thu.
  - Dòng hoàn lưu đáy hình thành để bù trừ thể tích, chảy ngược từ cuối bể về đầu bể dọc theo sàn đáy.
  - Vận tốc dòng hoàn lưu đáy vượt quá vận tốc xới cặn tới hạn ($v_h > v_{\text{scour}} \approx 10 - 15\ \text{mm/s}$), cuốn cặn đã lắng ngược lên trên.
- **Biện pháp kỹ thuật khắc phục**:
  1. Lắp đặt các vách ngăn chắn gió ngang nhô lên khỏi mặt nước và ngập sâu $0.5 - 1.0\ \text{m}$ dưới mặt nước. Bố trí các vách cách nhau $10 - 15\ \text{m}$ dọc chiều dài bể.
  2. Giữ nghiêm ngặt tỷ lệ kích thước hình học bể lắng: $L:H \le 20:1$ và $L:W \ge 4:1$.
  3. Duy trì vận tốc dòng chảy ngang tính toán luôn nhỏ hơn $0.50\ \text{m/min}$ ($8.3\ \text{mm/s}$).
  4. Trồng hàng cây xanh chắn gió quanh khu vực bể lắng hở ngoài trời.

##### 5.4.5.3 Sự cố 3: Dòng Hút Dâng Cục bộ ở Máng Tràn Cuốn Trôi Bông Cặn (Effluent Weir Updraft Suction)
- **Dấu hiệu nhận biết**:
  - Nước gần máng thu bị đục cục bộ. Bông cặn mịn li ti bị hút cuộn ngược qua răng cưa máng tràn.
  - Bùn lắng ở các vùng khác trong bể vẫn phân tách tốt và nước trong suốt.
- **Nguyên nhân gốc rễ**:
  - Tổng chiều dài vách tràn quá ngắn. Tải trọng vách tràn vượt ngưỡng cho phép ($\text{WLR} > 200 - 250\ \text{m}^3/\text{d}\cdot\text{m}$).
  - Vận tốc dòng dâng thẳng đứng cục bộ gần mép tràn lớn hơn vận tốc lắng của hạt bông cặn ($v_{\text{upward}} > v_s$).
  - Vách tràn bị cong vênh hoặc lắp lệch cao độ, gây hiện tượng dồn lưu lượng tràn quá mức ở vài vị trí.
- **Biện pháp kỹ thuật khắc phục**:
  1. Bổ sung các máng ngón tay nhánh đặt dọc vươn sâu vào bể để tăng tổng chiều dài vách tràn. Khống chế tải trọng vách tràn $\text{WLR} \le 150 - 180\ \text{m}^3/\text{d}\cdot\text{m}$.
  2. Dùng máy cân bằng laser vi chỉnh cao độ đáy chữ V của từng tấm răng cưa tam giác $90^\circ$ V-notch với sai số dưới $\pm 1.0\ \text{mm}$.
  3. Châm bổ sung polymer trợ lắng (anion hoặc nonion liều lượng $0.05 - 0.10\ \text{mg/L}$) vào cuối bể tạo bông để tăng kích thước và độ đặc của bông cặn.

##### 5.4.5.4 Sự cố 4: Rêu Tảo Bám Đáy và Tắc nghẽn Module Lắng Nghiêng (Algal Biofouling & Sludge Clogging)
- **Dấu hiệu nhận biết**:
  - Màng rêu sợi màu xanh lá cây hoặc nâu bám dày đặc ở miệng và vách trong các ống lắng lamen.
  - Bùn không trượt xuống đáy mà đọng lại trên vách nghiêng thành từng khối gây tắc nghẽn ống.
  - Vận tốc nước qua các ống còn thông thoáng tăng cao, cuốn theo cặn qua máng xả.
- **Nguyên nhân gốc rễ**:
  - Ánh sáng mặt trời chiếu qua lớp nước trong nông trên mặt bể hở, kích thích tảo bám đáy phát triển mạnh.
  - Tảo kết hợp với bông hydroxit kim loại tạo thành khối cặn dính bám cơ học, vô hiệu hóa góc tự trượt $60^\circ$.
- **Biện pháp kỹ thuật khắc phục**:
  1. Lắp đặt hệ thống giàn ống phun nước áp lực cao cố định trên mặt module lamen. Kích hoạt bơm phun định kỳ hàng tuần với áp lực $3 - 5\ \text{bar}$ để thổi sạch cặn bám.
  2. Lắp đặt tấm nắp đậy hoặc mái che cản sáng (vật liệu composite hoặc bạt chống UV) trên vùng module để ngăn tảo quang hợp.
  3. Châm clo sơ bộ (pre-chlorination) hoặc châm đồng sunfat ($\text{CuSO}_4$) định kỳ tại cửa vào bể lắng để diệt tảo.

##### 5.4.5.5 Sự cố 5: Bùn Bị Thối Kỵ khí, Sinh Bọt Khí và Nổi Váng (Anaerobic Sludge Septicity & Rising Sludge)
- **Dấu hiệu nhận biết**:
  - Từng tảng bùn đen sẫm nổi lên mặt nước bể lắng và phát tán mùi trứng thối ($\text{H}_2\text{S}$).
  - Có bọt khí li ti sủi tăm liên tục từ đáy bể lên mặt nước.
  - Nồng độ oxy hòa tan (DO) trong nước sau lắng giảm mạnh.
- **Nguyên nhân gốc rễ**:
  - Chu kỳ xả bùn quá dài hoặc hệ thống gạt bùn đáy bị hỏng khiến bùn lưu lại quá lâu ($> 2 - 3\ \text{ngày}$).
  - Vi sinh vật kỵ khí tiêu thụ hết oxy trong bùn, phân hủy chất hữu cơ và sinh ra các khí $\text{CH}_4, \text{CO}_2, \text{N}_2, \text{H}_2\text{S}$.
  - Các bọt khí bám vào cấu trúc xốp của bông bùn, làm tỷ trọng biểu kiến giảm nhỏ hơn nước ($\text{SG} < 1.0$), kéo mảng bùn nổi lên mặt nước.
- **Biện pháp kỹ thuật khắc phục**:
  1. Tăng tần suất xả bùn đáy tự động qua van điều khiển PLC. Xả từ $4$ đến $6\ \text{lần/ngày}$ hoặc xả bùn liên tục với lưu lượng nhỏ.
  2. Kiểm tra và sửa chữa hệ thống gạt bùn cơ học. Ưu tiên dùng cầu cào có bơm hút bùn trực tiếp từ đáy bể.
  3. Cải tạo thành hố thu bùn có góc nghiêng dốc $\ge 55^\circ - 60^\circ$ để bùn không bị bám dính trên vách.
  4. Lắp đặt đường ống xịt nước áp lực cao tại đáy hố thu bùn để phá mảng bùn đông cứng định kỳ.

##### 5.4.5.6 Sự cố 6: Vỡ Bông Cặn do Lực Cắt Thủy lực Quá Mức ở Công trình Vào (Floc Shearing)
- **Dấu hiệu nhận biết**:
  - Nước đi vào bể lắng có rất nhiều hạt cặn mịn li ti (pinpoint flocs).
  - Nước sau lắng vẫn giữ độ đục cao dù thời gian lưu nước rất dài. Bông cặn không lắng xuống đáy bể.
- **Nguyên nhân gốc rễ**:
  - Cường độ khuấy ở ngăn cuối của bể tạo bông quá mạnh ($G > 60 - 80\ \text{s}^{-1}$).
  - Vận tốc dòng nước chảy qua cửa phai, kênh dẫn hoặc lỗ đục vách ngăn vào bể quá lớn ($v > 0.40 - 0.60\ \text{m/s}$).
  - Gradient vận tốc dòng chảy qua khe hẹp sinh ra ứng suất cắt lớn, bẻ gãy liên kết cầu nối polymer và mạng hydroxit kim loại của bông cặn.
- **Biện pháp kỹ thuật khắc phục**:
  1. Áp dụng quy trình tạo bông giảm dần (Tapered Flocculation). Giảm dần gradient vận tốc $G$ theo các ngăn: Ngăn 1 đạt $60 - 70\ \text{s}^{-1}$, Ngăn 2 đạt $30 - 40\ \text{s}^{-1}$, Ngăn 3 đạt $15 - 20\ \text{s}^{-1}$.
  2. Mở rộng diện tích mở của vách đục lỗ cửa vào bể lắng ($A_{\text{open}} = 15 - 20\%$ diện tích mặt cắt). Giữ vận tốc qua lỗ trong giới hạn an toàn $v_{\text{port}} = 0.15 - 0.25\ \text{m/s}$.
  3. Khống chế vận tốc dòng nước trong kênh dẫn từ bể tạo bông sang bể lắng trong dải $0.15 - 0.30\ \text{m/s}$.
  4. Châm thêm polymer trợ tạo bông liều lượng nhỏ ($0.03 - 0.05\ \text{mg/L}$) để tăng độ dai cơ học của bông cặn.