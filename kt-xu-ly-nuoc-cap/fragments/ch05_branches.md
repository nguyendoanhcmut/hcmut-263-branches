## Chương 5: Sedimentation

### 5.1 Overview & Process Objectives (Tổng quan và Mục tiêu Quá trình Lắng)

#### 5.1.1 Process Context & Solid-Liquid Separation Role
##### 5.1.1.1 Upstream Treatment Links & Particle Cutoff Threshold (> 1 µm)
###### Linkage with Coagulation/Flocculation, Fe/Mn Oxidation, and Softening
- Quá trình lắng (Sedimentation / Clarification) là công đoạn phân tách pha rắn - lỏng bằng trọng lực (gravitational solid-liquid separation) cốt lõi trong dây chuyền công nghệ xử lý nước cấp đô thị và công nghiệp.
- Vị trí công nghệ và tương tác hệ thống:
  - **Sau bể keo tụ - tạo bông (Coagulation - Flocculation)**: Tiếp nhận dòng nước chứa các bông cặn hydroxit kim loại ($Al(OH)_3$ hoặc $Fe(OH)_3$) liên kết với các hạt keo sét, hạt màu hữu cơ (humic/fulvic acids), vi khuẩn và tảo đã bị mất ổn định điện thế zeta ($\zeta \to 0$) và tích tụ thành các cụm bông nhìn thấy được ($100\ \mu\text{m} - 2\ \text{mm}$).
  - **Sau quá trình oxy hóa Sắt và Mangan (Fe/Mn Oxidation)**: Lắng các kết tủa oxyhydroxit không tan dạng ferric hydroxide ($Fe(OH)_3 / FeOOH$) và manganese dioxide ($MnO_2$) sau khi sục khí làm thoáng hoặc châm chất oxy hóa mạnh ($Cl_2, KMnO_4, O_3$).
  - **Sau quá trình làm mềm bằng hóa chất (Lime-Soda Ash Softening)**: Tách các tinh thể kết tủa canxi cacbonat ($CaCO_3$) và magie hydroxit ($Mg(OH)_2$) sinh ra khi nâng pH dung dịch bằng vôi tôi ($Ca(OH)_2$) và sô-đa ($Na_2CO_3$).

###### Particle Size Spectrum & Gravitational Settling Feasibility
- Dải kích thước hạt hữu hiệu: Trọng lực phân tách hiệu quả các hạt lơ lửng và kết tủa hóa học có đường kính quy ước lớn hơn $1\ \mu\text{m}$ ($d_p > 1\ \mu\text{m}$).
- Các hạt mịn dưới $1\ \mu\text{m}$ (keo ưa nước, virus, hạt sét siêu mịn chưa keo tụ) có vận tốc lắng do trọng lực cực kỳ nhỏ ($v_s < 10^{-6}\ \text{m/s}$), chịu chi phối mạnh bởi chuyển động nhiệt Brown và lực tương tác tĩnh điện bề mặt, không thể lắng tự nhiên trong thời gian lưu nước kinh tế ($t_0 \le 4\ \text{h}$) mà bắt buộc phải qua khâu đông tụ/tạo bông trước khi lắng hoặc được giữ lại ở công đoạn lọc cát hạ nguồn.

##### 5.1.1.2 Treatment Train Configurations & Unit Clarification Objectives
###### Downstream Filter Protection & Solids Burden Reduction
- Mục tiêu vận hành cốt lõi của bể lắng là loại bỏ từ 80% đến 95% tổng lượng chất rắn lơ lửng (TSS) và độ đục của nước thô sau phản ứng hóa lý, giảm thiểu tối đa tải lượng cặn nạp lên các bể lọc nhanh trọng lực (Rapid Sand Filters).
- Khi bể lắng vận hành ổn định, chu kỳ lọc (filter run time) được kéo dài từ 24 đến 72 giờ, tránh hiện tượng nghẹt lọc nhanh (rapid head loss build-up) và cặn đục chui qua lớp lọc (turbidity breakthrough).
- Lượng nước rửa lọc thu hồi và điện năng tiêu thụ cho bơm rửa ngược được giảm đáng kể, tối ưu hóa hiệu suất thu hồi nước của toàn nhà máy cấp nước ($> 95\%$).

###### Finished Water Quality Target Interdependence (QCVN 01-1:2018/BYT)
- Quy chuẩn kỹ thuật quốc gia QCVN 01-1:2018/BYT quy định độ đục tối đa của nước sạch sau xử lý cấp cho sinh hoạt là $\le 2.0\ \text{NTU}$ (mục tiêu kỹ thuật tối ưu khuyến nghị $\le 0.5\ \text{NTU}$ để đảm bảo an toàn khử trùng).
- Để đạt được chuẩn đầu ra này sau bể lọc cát, độ đục của nước sau bể lắng (effluent settled water turbidity) bắt buộc phải kiểm soát nghiêm ngặt ở ngưỡng:
  $$\text{Turbidity}_{\text{settled}} \le 2.0 - 5.0\ \text{NTU}$$
- Nước sau lắng có độ đục $> 5.0\ \text{NTU}$ sẽ gây quá tải trầm trọng cho lớp cát lọc, hình thành màng cặn đặc bùn trên bề mặt và gây hiện tượng vón cục bùn (mudballs) bên trong tầng lọc.

#### 5.1.2 Sludge Production Mass Balance & Chemical Stoichiometry
##### 5.1.2.1 Total Daily Dry Sludge Mass Formulation
###### Governing Mass Balance Equation (eq_ch05_021)
- Lượng bùn khô sinh ra mỗi ngày từ quá trình lắng bao gồm cặn lơ lửng ban đầu được giữ lại cộng với khối lượng kết tủa hydroxit kim loại từ phèn nhôm, phèn sắt và các kết tủa làm mềm:
$$M_s = Q \cdot \left[(\text{TSS}_{\text{inf}} - \text{TSS}_{\text{eff}}) + K_{\text{alum}} \cdot \text{Dose}_{\text{alum}} + K_{\text{Fe}} \cdot \text{Dose}_{\text{Fe}} + 2.5 \cdot \text{CH}_{\text{rem}} + 1.8 \cdot \text{NCH}_{\text{rem}}\right] \times 10^{-3}$$

###### Variable Definitions, Stoichiometric Yield Factors, and Units
- $M_s$: Khối lượng chất rắn bùn khô sinh ra mỗi ngày ($\text{kg dry solids/day}$).
- $Q$: Lưu lượng nước xử lý của nhà máy ($\text{m}^3/\text{day}$).
- $\text{TSS}_{\text{inf}}$: Hàm lượng chất rắn lơ lửng trong nước thô đi vào bể lắng ($\text{mg/L}$ hoặc $\text{g/m}^3$).
- $\text{TSS}_{\text{eff}}$: Hàm lượng chất rắn lơ lửng còn lại trong nước sau lắng ($\text{mg/L}$).
- $\text{Dose}_{\text{alum}}$: Liều lượng châm phèn nhôm thương phẩm dạng phèn nhôm sunfat ngậm nước $\text{Al}_2(\text{SO}_4)_3 \cdot 14\text{H}_2\text{O}$ ($\text{mg/L}$).
- $K_{\text{alum}}$: Hệ số sinh bùn hydroxit nhôm khô thực tế trên một đơn vị phèn nhôm thương phẩm ($0.26 - 0.44\ \text{kg Al(OH)}_3 / \text{kg alum}$).
- $\text{Dose}_{\text{Fe}}$: Liều lượng châm phèn sắt thương phẩm dạng $\text{FeCl}_3$ hoặc $\text{Fe}_2(\text{SO}_4)_3$ ($\text{mg/L}$).
- $K_{\text{Fe}}$: Hệ số sinh bùn hydroxit sắt khô ($1.35 - 1.91\ \text{kg Fe(OH)}_3 / \text{kg Fe}$).
- $\text{CH}_{\text{rem}}$: Độ cứng cacbonat được loại bỏ dưới dạng kết tủa $\text{CaCO}_3$ ($\text{mg/L as CaCO}_3$).
- $\text{NCH}_{\text{rem}}$: Độ cứng phi cacbonat (chủ yếu là magie) được loại bỏ dưới dạng $\text{Mg(OH)}_2$ ($\text{mg/L as CaCO}_3$).
- $10^{-3}$: Thừa số chuyển đổi từ đơn vị $\text{g}$ sang $\text{kg}$ ($1\ \text{kg} = 1,000\ \text{g}$).

##### 5.1.2.2 Alum & Ferric Hydroxide Precipitate Yield Calculations
###### Alum Coagulant Hydroxide Stoichiometry ($K_{\text{alum}} = 0.26 - 0.44$)
- Phản ứng thủy phân hoàn toàn phèn nhôm trong nước có độ kiềm tự nhiên:
  $$\text{Al}_2(\text{SO}_4)_3 \cdot 14\text{H}_2\text{O} + 3\text{Ca(HCO}_3)_2 \to 2\text{Al(OH)}_3\downarrow + 3\text{CaSO}_4 + 14\text{H}_2\text{O} + 6\text{CO}_2\uparrow$$
- Khối lượng phân tử của phèn nhôm sunfat thương phẩm $\text{Al}_2(\text{SO}_4)_3 \cdot 14\text{H}_2\text{O}$ là xấp xỉ $594.4\ \text{g/mol}$.
- Khối lượng của kết tủa sinh ra gồm 2 phân tử $\text{Al(OH)}_3$:
  $$2 \times 78.0 = 156.0\ \text{g/mol}$$
- Tỷ lệ sinh bùn lý thuyết tinh khiết:
  $$K_{\text{alum, theoretical}} = \frac{156.0}{594.4} \approx 0.2625\ \text{kg Al(OH)}_3 / \text{kg commercial alum}$$
- Trong thực tế thiết kế, do phèn kết hợp thêm các polymer hữu cơ, tạp chất không tan và hidrat hóa dư thừa, giá trị thiết kế $K_{\text{alum}}$ thường dao động trong khoảng $0.26$ đến $0.44$.

###### Iron Coagulant Hydroxide Stoichiometry ($K_{\text{Fe}} = 1.35 - 1.91$)
- Phản ứng thủy phân của phèn sắt ferric chloride:
  $$\text{FeCl}_3 + 3\text{H}_2\text{O} \to \text{Fe(OH)}_3\downarrow + 3\text{HCl}$$
- Từ $1\ \text{mol Fe}^{3+}$ ($55.85\ \text{g}$) sinh ra $1\ \text{mol Fe(OH)}_3$ ($106.87\ \text{g}$).
- Tỷ số sinh bùn theo khối lượng ion sắt $\text{Fe}^{3+}$ châm vào:
  $$K_{\text{Fe}} = \frac{106.87}{55.85} = 1.913\ \text{kg Fe(OH)}_3 / \text{kg Fe}$$
- Nếu tính theo muối khan $\text{FeCl}_3$ ($162.2\ \text{g/mol}$):
  $$K_{\text{FeCl}_3} = \frac{106.87}{162.2} \approx 0.659\ \text{kg Fe(OH)}_3 / \text{kg FeCl}_3$$

##### 5.1.2.3 Softening Precipitate Yield Stoichiometry (CaCO3 and Mg(OH)2)
###### Carbonate Hardness Removal Precipitate Coefficient ($2.5 \times \text{CH}_{\text{rem}}$)
- Khi khử độ cứng canxi cacbonat bằng vôi tôi:
  $$\text{Ca(HCO}_3)_2 + \text{Ca(OH)}_2 \to 2\text{CaCO}_3\downarrow + 2\text{H}_2\text{O}$$
- Mỗi đương lượng canxi trong nước thô kết hợp với một đương lượng canxi từ vôi tôi để tạo thành 2 đương lượng kết tủa $\text{CaCO}_3$.
- Ngoài ra, khí $\text{CO}_2$ hòa tan ban đầu cũng tiêu tốn vôi và tạo thành kết tủa $\text{CaCO}_3$:
  $$\text{CO}_2 + \text{Ca(OH)}_2 \to \text{CaCO}_3\downarrow + \text{H}_2\text{O}$$
- Tổng hệ số sinh kết tủa thực tế trung bình được thực nghiệm chuẩn hóa bằng $2.5\ \text{g kết tủa} / \text{g CH loại bỏ}$ (quy về $\text{CaCO}_3$).

###### Non-Carbonate Hardness Removal Precipitate Coefficient ($1.8 \times \text{NCH}_{\text{rem}}$)
- Khử độ cứng magie phi cacbonat bằng vôi và sô-đa:
  $$\text{Mg}^{2+} + \text{Ca(OH)}_2 + \text{Na}_2\text{CO}_3 \to \text{Mg(OH)}_2\downarrow + \text{CaCO}_3\downarrow + 2\text{Na}^+$$
- Một mol ion magie tạo ra cả kết tủa $\text{Mg(OH)}_2$ ($58.3\ \text{g/mol}$) lẫn $\text{CaCO}_3$ ($100.1\ \text{g/mol}$).
- Tỷ số khối lượng quy chuẩn trên đơn vị độ cứng magie loại bỏ đạt xấp xỉ $1.8\ \text{g kết tủa} / \text{g NCH loại bỏ}$ (quy về $\text{CaCO}_3$).

##### 5.1.2.4 Wet Sludge Volumetric Production & Hopper Capacity Sizing
###### Sludge Moisture Content, Specific Gravity, and Volumetric Conversion
- Bùn lắng trong bể lắng nước cấp có hàm lượng ẩm rất cao ($P = 97.0\% - 99.5\%$), nghĩa là hàm lượng cặn khô chỉ chiếm nồng độ rắn $S = 0.5\% - 3.0\%$ theo khối lượng ($C_{\text{sludge}} = 5,000 - 30,000\ \text{mg/L}$).
- Tỷ trọng của khối bùn ướt ($\text{SG}_{\text{sludge}}$) xấp xỉ tỷ trọng của nước do nước chiếm tỷ lệ áp đảo:
  $$\text{SG}_{\text{sludge}} \approx 1.002 - 1.020$$
- Thể tích bùn ướt sinh ra trong một ngày ($V_{\text{sludge}},\ \text{m}^3/\text{day}$):
  $$V_{\text{sludge}} = \frac{M_s}{\rho_w \cdot \text{SG}_{\text{sludge}} \cdot \left(\frac{100 - P}{100}\right)} = \frac{M_s \times 100}{\rho_w \cdot \text{SG}_{\text{sludge}} \cdot \%S}$$
  Trong đó:
  - $\rho_w$: Khối lượng riêng của nước ($1,000\ \text{kg/m}^3$).
  - $P$: Độ ẩm của bùn lắng (%).
  - $\%S$: Tỷ lệ phần trăm chất rắn khô trong bùn ($100 - P$).

###### Storage Hopper Sizing and Intermittent Blowoff Frequency
- Thể tích hữu ích của các hố thu bùn đáy bể ($V_{\text{hopper}}$) được thiết kế để chứa được lượng bùn sinh ra trong khoảng thời gian giữa hai chu kỳ xả bùn định kỳ ($t_{\text{storage}} = 8 - 24\ \text{h}$ đối với van xả tự động, hoặc $1 - 3\ \text{ngày}$ đối với hệ thống xả thủ công):
  $$V_{\text{hopper}} \ge V_{\text{sludge}} \cdot \frac{t_{\text{storage}}}{24}$$
- Nếu lưu bùn quá lâu trong hố thu mà không xả, hiện tượng phân hủy kỵ khí các chất hữu cơ trong bùn sẽ xảy ra, giải phóng bọt khí metan và cacbonic làm nổi mảng bùn lên mặt bể (rising sludge) gây đục nước sau lắng nghiêm trọng.

---

### 5.2 Theoretical Principles & Particle Settling Mechanics (Cơ sở Lý thuyết và Cơ chế Lắng Hạt)

#### 5.2.1 Four Morphological Classes of Sedimentation (Types I to IV)
##### 5.2.1.1 Classification Matrix by Solids Concentration and Particle Interaction
###### Comprehensive Comparison Table of Settling Types I to IV
Cơ chế lắng trong xử lý nước được chia thành 4 lớp hình thái học cơ bản dựa trên nồng độ hạt rắn và mức độ tương tác giữa các hạt:

| Lớp Lắng | Tên Gọi Kỹ Thuật | Đặc Điểm Hình Thái & Tương Tác Hạt | Nồng Độ Hạt Rắn (TSS) | Mô Hình Lý Thuyết Chi Phối | Ứng Dụng Thực Tiễn Điển Hình |
|---|---|---|---|---|---|
| **Type I** | **Lắng hạt rời rạc** (Discrete Settling) | Hạt giữ nguyên kích thước, hình dạng, tỷ trọng trong suốt hành trình rơi; không kết tụ, rơi độc lập. | Loãng ($< 500\ \text{mg/L}$) | Cân bằng lực Newton, Định luật Stokes, Mô hình bể lý tưởng Camp. | Bể lắng cát (grit chamber), bể sơ lắng (presedimentation), lắng cát khi rửa lọc. |
| **Type II** | **Lắng tạo bông** (Flocculant Settling) | Hạt liên tục va chạm, kết tụ, tăng kích thước và khối lượng; vận tốc lắng tăng dần theo độ sâu rơi. | Loãng đến trung bình ($50 - 1,000\ \text{mg/L}$) | Phân tích cột lắng (settling column), tích phân diện tích đường đồng nồng độ. | Lắng cặn keo tụ phèn nhôm, phèn sắt sau bể tạo bông; lắng bông cặn Fe/Mn. |
| **Type III** | **Lắng cản trở / Lắng vùng** (Hindered / Zone Settling) | Nồng độ hạt rất lớn; trường thủy động lực học cản trở lẫn nhau; các hạt lắng cùng nhau như một khối đệm/màng bùn; tạo ranh giới pha rõ rệt. | Đặc ($> 1,000\ \text{mg/L}$) | Lý thuyết thông lượng chất rắn (Solids Flux Theory - Coe & Clevenger, Kynch). | Bể lắng tiếp xúc chất rắn (solids-contact), bể lắng bùn lơ lửng, bể lắng làm mềm vôi. |
| **Type IV** | **Lắng nén** (Compression Settling) | Hạt tiếp xúc cơ học trực tiếp hình thành khung cấu trúc xốp; lắng chỉ xảy ra do nước lỗ rỗng bị nén ép thoát ngược lên trên. | Rất đặc ($> 10,000\ \text{mg/L}$) | Lý thuyết cố kết cơ học đất (Terzaghi consolidation analogy). | Đáy hố thu cặn bể lắng, bể nén bùn trọng lực (sludge gravity thickener). |

###### Interparticle Force Boundaries: Van der Waals, Electrical Double Layer, and Mechanical Enmeshment
- Trong quá trình lắng **Type I**, khoảng cách trung bình giữa các hạt ($L_{\text{sep}} \gg 100 \times d_p$) đủ lớn để lực hút Van der Waals và lực đẩy tĩnh điện lưỡng lớp (EDL) hoàn toàn không có cơ hội tác động qua lại.
- Trong quá trình lắng **Type II**, gradient vận tốc của chất lỏng và chênh lệch vận tốc rơi giữa các hạt kích thước khác nhau tạo ra va chạm động học (orthokinetic collisions); lực hút Van der Waals và liên kết cầu nối polymer vượt qua lực đẩy tĩnh điện, gây dính kết và biến dạng hạt liên tục.
- Trong quá trình lắng **Type III**, nồng độ hạt dày đặc ($L_{\text{sep}} \approx d_p$) làm cho dòng lưu chất bị đẩy ngược lên qua các khe hẹp giữa các hạt, tạo lực cản thủy động lực học cực lớn triệt tiêu tính độc lập của từng hạt và hình thành ranh giới phân pha nước trong - màng bùn.
- Trong quá trình lắng **Type IV**, các hạt tiếp xúc vật lý điểm-điểm, lực liên kết khung cơ học chống lại áp lực tĩnh; sự nén ép cấu trúc phụ thuộc hoàn toàn vào tốc độ thoát nước ra khỏi mạng lưới lỗ rỗng siêu nhỏ dưới tác dụng của trọng lượng bản thân các lớp cặn nằm phía trên.

##### 5.2.1.2 Settling Regimes Across the Vertical Water Column
###### Coexistence of Multiple Settling Types in Practical Clarifiers
- Trong một bể lắng công nghiệp thực tế, cả 4 cơ chế lắng trên thường xuyên đồng tồn tại dọc theo phương thẳng đứng từ mặt nước xuống đáy bể:
  - **Tầng mặt và tầng nước trong (Clarified Zone)**: Các hạt keo rời rạc còn sót lại lắng theo cơ chế **Type I**.
  - **Tầng giữa (Clarification Zone)**: Các bông cặn nhôm/sắt va chạm, kết tụ lớn dần theo cơ chế **Type II**.
  - **Tầng trên của lớp bùn (Sludge Blanket Zone)**: Lớp đệm cặn dày đặc hạ thấp dần theo cơ chế **Type III (Zone settling)**.
  - **Tầng sát đáy và hố thu bùn (Sludge Hopper Zone)**: Khối bùn nén chặt, giải phóng nước lỗ rỗng theo cơ chế **Type IV (Compression)**.

###### Transition Dynamics from Dilute to Concentrated Regimes
- Sự chuyển pha giữa các chế độ lắng diễn ra liên tục theo hàm số của nồng độ chất rắn $C(z, t)$. Khi nồng độ $C$ vượt qua ngưỡng tới hạn $C_{\text{hindered}} \approx 800 - 1,200\ \text{mg/L}$, vận tốc lắng riêng lẻ của từng hạt bị triệt tiêu hoàn toàn và được thay thế bằng vận tốc suy giảm của ranh giới pha (interface subsidence velocity $v_i$).

#### 5.2.2 Type I Discrete Particle Settling Hydrodynamics (Lắng Hạt Độc Lập)
##### 5.2.2.1 Newtonian Force Balance on a Free-Falling Submerged Sphere
###### Gravitational Force Derivation ($F_G = \rho_s \cdot g \cdot V_p$)
- Một hạt rắn hình cầu rơi tự do trong chất lỏng tĩnh chịu lực hấp dẫn hướng thẳng đứng từ trên xuống dưới (eq_ch05_001):
$$F_G = \rho_s \cdot g \cdot V_p = \rho_p \cdot g \cdot V_p = \rho_s \cdot g \cdot \left(\frac{\pi}{6} d^3\right)$$
Trong đó:
- $F_G$: Trọng lực tác dụng lên hạt ($\text{N}$).
- $\rho_s$ (hoặc $\rho_p$): Khối lượng riêng của hạt rắn ($\text{kg/m}^3$, ví dụ cát thạch anh $2,650\ \text{kg/m}^3$, bông phèn nhôm $1,001 - 1,005\ \text{kg/m}^3$).
- $g$: Gia tốc trọng trường ($9.81\ \text{m/s}^2$).
- $V_p$: Thể tích hình học của hạt hình cầu ($\text{m}^3$, $V_p = \frac{\pi}{6} d^3$).
- $d$: Đường kính hình cầu tương đương của hạt ($\text{m}$).

###### Archimedes Buoyancy Force Derivation ($F_B = \rho \cdot g \cdot V_p$)
- Theo nguyên lý Archimedes, lực đẩy nổi hướng thẳng đứng từ dưới lên bằng trọng lượng khối chất lỏng bị hạt chiếm chỗ (eq_ch05_002):
$$F_B = \rho \cdot g \cdot V_p = \rho_w \cdot g \cdot V_p = \rho \cdot g \cdot \left(\frac{\pi}{6} d^3\right)$$
Trong đó:
- $F_B$: Lực đẩy nổi tác dụng lên hạt ($\text{N}$).
- $\rho$ (hoặc $\rho_w$): Khối lượng riêng của chất lỏng nước ($998.2\ \text{kg/m}^3$ ở $20^\circ\text{C}$, $1,000\ \text{kg/m}^3$ ở $4^\circ\text{C}$).

###### Hydrodynamic Drag Force Formulation ($F_D = \frac{1}{2} C_D A_p \rho v^2$)
- Khi hạt chuyển động tương đối trong nước với vận tốc $v$, chất lỏng tác dụng lực cản thủy động lực học hướng ngược chiều chuyển động (hướng lên trên) (eq_ch05_003):
$$F_D = C_D \cdot A_p \cdot \rho \cdot \frac{v^2}{2} = \frac{1}{2} C_D \cdot \left(\frac{\pi}{4} d^2\right) \cdot \rho \cdot v^2$$
Trong đó:
- $F_D$: Lực cản thủy động lực học ($\text{N}$).
- $C_D$: Hệ số lực cản Newton (Newton drag coefficient, đại lượng không thứ nguyên, phụ thuộc vào số Reynolds).
- $A_p$: Diện tích cản gió / diện tích chiếu vuông góc của hạt lên mặt phẳng vuông góc với hướng chuyển động ($\text{m}^2$, với hình cầu $A_p = \frac{\pi}{4} d^2$).
- $v$: Vận tốc rơi tương đối của hạt so với chất lỏng ($\text{m/s}$).

###### Equilibrium Net Driving Force & Acceleration Phase Elimination
- Định luật II Newton mô tả chuyển động rơi của hạt:
  $$m \frac{dv}{dt} = F_G - F_B - F_D = (\rho_s - \rho) g V_p - \frac{1}{2} C_D A_p \rho v^2$$
- Ban đầu, khi $v = 0$, $F_D = 0$, hạt chuyển động nhanh dần đều với gia tốc cực đại:
  $$a_{\max} = g \left(\frac{\rho_s - \rho}{\rho_s}\right)$$
- Khi vận tốc $v$ tăng lên, lực cản $F_D$ tăng tỷ lệ thuận với $v^2$. Sau một khoảng thời gian cực ngắn (thường $< 0.1\ \text{giây}$ đối với hạt nhỏ trong nước), lực cản thủy động lực cân bằng hoàn toàn với trọng lượng hiệu dụng chìm trong nước:
  $$F_G = F_B + F_D \iff F_G - F_B = F_D$$
- Khi đó, gia tốc triệt tiêu hoàn toàn ($\frac{dv}{dt} = 0$), hạt đạt đến **vận tốc lắng giới hạn cuối cùng (terminal settling velocity $v_s$)** và chuyển động thẳng đều.

##### 5.2.2.2 Fluid Flow Regimes & Particle Reynolds Number (Re)
###### Definition of Particle Reynolds Number ($Re = \frac{\rho v_s d}{\mu} = \frac{v_s d}{\nu}$)
- Chế độ chảy của chất lỏng bao quanh hạt hình cầu chuyển động được đặc trưng bởi số Reynolds của hạt ($Re$, hoặc ký hiệu $R$) (eq_ch05_004):
$$Re = \frac{\rho \cdot v_s \cdot d}{\mu} = \frac{v_s \cdot d}{\nu}$$
Trong đó:
- $Re$: Số Reynolds của hạt (không thứ nguyên).
- $v_s$: Vận tốc lắng giới hạn của hạt ($\text{m/s}$).
- $d$: Đường kính hạt ($\text{m}$).
- $\mu$: Độ nhớt động lực học (dynamic/absolute viscosity) của nước ($\text{Pa}\cdot\text{s}$ hoặc $\text{N}\cdot\text{s/m}^2$, ở $20^\circ\text{C}$ $\mu = 1.002 \times 10^{-3}\ \text{Pa}\cdot\text{s}$).
- $\nu$: Độ nhớt động học (kinematic viscosity) của nước ($\text{m}^2/\text{s}$, $\nu = \mu/\rho$, ở $20^\circ\text{C}$ $\nu = 1.004 \times 10^{-6}\ \text{m}^2/\text{s}$).

###### Boundary Layer Dynamics and Boundary Separation Wake
- Số Reynolds biểu thị tỷ số giữa lực quán tính (inertial forces) và lực ma sát nhớt (viscous shear forces):
  - Ở $Re$ rất thấp, lực nhớt bao bọc hoàn toàn bề mặt hạt, lớp biên (boundary layer) dính chặt, dòng chảy trơn tru không tách dòng (creeping flow).
  - Khi $Re$ tăng, lực quán tính làm cho lớp biên bị tách khỏi bề mặt hạt ở phần đuôi, hình thành xoáy cuộn áp suất thấp (turbulent wake), đóng góp thêm thành phần lực cản hình dạng (form drag / pressure drag) bên cạnh lực cản ma sát mặt ngoài (skin friction drag).

##### 5.2.2.3 Newton Drag Coefficient ($C_D$) Formulations Across Regimes
###### Laminar Flow Regime ($Re < 0.5 - 1.0$): Stokes' Creeping Flow ($C_D = 24/Re$)
- Trong vùng chảy tầng (laminar flow regime), lực ma sát nhớt chiếm ưu thế tuyệt đối so với lực quán tính. Sir George Gabriel Stokes (1851) đã giải chính xác phương trình vi phân Navier-Stokes và chứng minh hệ số lực cản có dạng giải tích (eq_ch05_005):
$$C_D = \frac{24}{Re} \quad (\text{áp dụng khi } Re < 0.5 \text{ hoặc } Re \le 1.0)$$

###### Transitional Flow Regime ($0.5 < Re < 10^4$): Semi-Empirical Formulation ($C_D = \frac{24}{Re} + \frac{3}{\sqrt{Re}} + 0.34$)
- Trong vùng chảy chuyển tiếp (transitional regime), cả lực ma sát bề mặt và lực áp suất xoáy đuôi đều đóng vai trò quan trọng. Hệ số lực cản được xác định bằng công thức thực nghiệm của Fair, Geyer & Okun (eq_ch05_006):
$$C_D = \frac{24}{Re} + \frac{3}{\sqrt{Re}} + 0.34 \quad (\text{áp dụng khi } 0.5 < Re < 10^4)$$
- Thành phần $\frac{24}{Re}$ đặc trưng cho ma sát tầng, $\frac{3}{\sqrt{Re}}$ đại diện cho sự phát triển của lớp biên chuyển tiếp, và $0.34$ là hằng số tiệm cận lực cản xoáy quán tính.

###### Fully Turbulent Flow Regime ($Re > 10^4$): Newton's Constant Inertial Drag ($C_D \approx 0.40 - 0.44$)
- Trong vùng chảy xoáy hoàn toàn (turbulent flow regime), vùng xoáy áp suất thấp phía sau hạt chi phối hoàn toàn lực cản; lớp biên bị xáo trộn mạnh khiến hệ số lực cản gần như không đổi độc lập với số Reynolds (eq_ch05_007):
$$C_D = 0.40 \approx 0.44 \quad (\text{áp dụng khi } Re > 10^4)$$

##### 5.2.2.4 Terminal Settling Velocity Derivations
###### General Terminal Velocity Equation Across All Regimes ($v_s = \sqrt{\frac{4g(\rho_s-\rho)d}{3 C_D \rho}}$)
- Cân bằng lực tại trạng thái rơi giới hạn:
  $$F_G - F_B = F_D$$
  $$(\rho_s - \rho) g \left(\frac{\pi}{6} d^3\right) = \frac{1}{2} C_D \left(\frac{\pi}{4} d^2\right) \rho v_s^2$$
- Rút gọn hằng số $\pi$ và đường kính $d^2$:
  $$\frac{1}{6} (\rho_s - \rho) g d = \frac{1}{8} C_D \rho v_s^2$$
  $$v_s^2 = \frac{8}{6} \frac{g (\rho_s - \rho) d}{C_D \rho} = \frac{4 g (\rho_s - \rho) d}{3 C_D \rho}$$
- Lấy căn bậc hai hai vế, ta thu được phương trình tổng quát xác định vận tốc lắng giới hạn của hạt hình cầu trên mọi chế độ thủy động lực học (eq_ch05_008):
$$v_s = \sqrt{\frac{4 g (\rho_s - \rho) d}{3 C_D \rho}} = \sqrt{\frac{4 g (\text{SG} - 1) d}{3 C_D}}$$
Trong đó $\text{SG} = \frac{\rho_s}{\rho}$ là tỷ trọng tương đối của hạt so với nước.

###### Classical Stokes' Law Derivation ($v_s = \frac{g(\rho_s-\rho)d^2}{18\mu}$)
- Khi dòng chảy quanh hạt là chảy tầng ($Re \le 1.0$), thay hệ số lực cản Stokes $C_D = \frac{24}{Re} = \frac{24 \mu}{\rho v_s d}$ vào phương trình tổng quát:
  $$v_s^2 = \frac{4 g (\rho_s - \rho) d}{3 \left(\frac{24 \mu}{\rho v_s d}\right) \rho} = \frac{4 g (\rho_s - \rho) d \cdot (\rho v_s d)}{72 \mu \rho} = \frac{g (\rho_s - \rho) d^2 v_s}{18 \mu}$$
- Triệt tiêu $v_s$ ở cả hai vế, ta thu được **Định luật Stokes kinh điển** (eq_ch05_009):
$$v_s = \frac{g (\rho_s - \rho) d^2}{18 \mu} = \frac{g (\text{SG} - 1) d^2}{18 \nu}$$
- *Ý nghĩa kỹ thuật*: Trong chế độ chảy tầng, vận tốc lắng tỷ lệ thuận với bình phương đường kính hạt ($d^2$), tỷ lệ thuận với độ chênh lệch khối lượng riêng $(\rho_s - \rho)$ và tỷ lệ nghịch với độ nhớt động lực học $\mu$. Do đó, tăng nhiệt độ nước (giảm độ nhớt $\mu$) hoặc tăng kích thước hạt qua keo tụ sẽ tăng tốc độ lắng rất mạnh.

###### Turbulent Terminal Velocity Formula ($v_s = 1.74 \sqrt{\frac{g(\rho_s-\rho)d}{\rho}}$)
- Khi dòng chảy qua hạt là chảy rối hoàn toàn ($Re > 10^4$), thay $C_D = 0.44$ vào phương trình tổng quát:
  $$v_s = \sqrt{\frac{4 g (\rho_s - \rho) d}{3 (0.44) \rho}} = \sqrt{\frac{4}{1.32}} \sqrt{\frac{g (\rho_s - \rho) d}{\rho}} \approx 1.74 \sqrt{\frac{g (\rho_s - \rho) d}{\rho}}$$
- *Ý nghĩa kỹ thuật*: Trong chế độ chảy rối (hạt cát rất lớn, đá sỏi trong công trình thu nước), vận tốc lắng chỉ tỷ lệ thuận với căn bậc hai của kích thước hạt ($\sqrt{d}$) và hoàn toàn không phụ thuộc vào độ nhớt chất lỏng $\mu$.

##### 5.2.2.5 Sphericity, Shape Factors & Non-Spherical Particle Corrections
###### Sphericity Definition ($\psi$) and Dynamic Shape Factors
- Các hạt cát, cặn phù sa trong thực tế không bao giờ là hình cầu hoàn hảo. Độ cầu (sphericity $\psi$) được định nghĩa là tỷ số giữa diện tích bề mặt của hình cầu có cùng thể tích với hạt chia cho diện tích bề mặt thực tế của hạt:
  $$\psi = \frac{A_{\text{sphere}}}{A_{\text{particle}}} \le 1.0$$
  - Đối với hạt cát tròn cạnh: $\psi \approx 0.85 - 0.90$.
  - Đối với hạt cát góc cạnh sắc nhọn: $\psi \approx 0.65 - 0.75$.
  - Đối with bông cặn phèn phân nhánh: $\psi \approx 0.50 - 0.60$.

###### Drag Modifications for Irregular Sand and Silt Particles
- Hạt có độ cầu thấp ($\psi < 1.0$) có diện tích cản gió lớn hơn và tạo xoáy tách dòng sớm hơn hình cầu, dẫn đến hệ số lực cản thực tế $C_{D,\text{actual}}$ lớn hơn so với hạt hình cầu cùng thể tích. Vận tốc lắng thực tế sẽ nhỏ hơn vận tốc tính toán theo công thức Stokes từ 15% đến 40%.

#### 5.2.3 Ideal Sedimentation Basin Theory (Camp's Rational Model & Hazen Theory)
##### 5.2.3.1 Camp's Seven Fundamental Assumptions
###### Rigorous Mathematical & Physical Postulates of Camp (1936, 1946)
Thomas R. Camp (1936, 1946) xây dựng mô hình toán học giải tích cho bể lắng trọng lực lý tưởng dựa trên 7 giả thiết chặt chẽ:
1. **Chế độ lắng Type I**: Toàn bộ các hạt trong bể lắng lắng độc lập, không thay đổi kích thước, hình dạng hay tỷ trọng trong suốt quá trình lắng (không có hiện tượng tạo bông hoặc vỡ hạt).
2. **Bốn vùng thủy lực phân định rõ rệt**: Không gian bể được chia thành 4 vùng không chồng lấn: Vùng vào (Inlet Zone), Vùng lắng (Settling Zone), Vùng bùn (Sludge Zone), và Vùng ra (Outlet Zone).
3. **Phân phối lưu lượng đồng đều ở vùng vào**: Nước đi vào vùng lắng được dàn đều tuyệt đối trên toàn bộ mặt cắt ướt ngang; vận tốc dòng chảy ngang $v_h$ có độ lớn và hướng đồng nhất tại mọi điểm.
4. **Thu nước đồng đều ở vùng ra**: Dòng chảy rời khỏi vùng lắng vào máng thu nước với phân bố vận tốc hoàn toàn đồng đều trên toàn bộ chiều rộng và mặt thoáng.
5. **Phân bố cặn đồng đều theo chiều sâu ở đầu vùng lắng**: Tại mặt phẳng bắt đầu của vùng lắng ($x = 0$), nồng độ cặn của từng cỡ hạt phân bố đồng nhất trên toàn bộ chiều sâu $H$.
6. **Cặn lọt vào vùng bùn bị bắt giữ vĩnh viễn**: Bất kỳ hạt cặn nào chạm vào ranh giới trên của vùng bùn (đáy vùng lắng) đều được coi là đã bị loại bỏ hoàn toàn; không có hiện tượng xới cặn hoặc cuốn trôi ngược lại vào dòng nước.
7. **Hạt lọt vào vùng ra bị trôi theo nước**: Bất kỳ hạt cặn nào chưa chạm tới đáy vùng lắng trước khi chạm vào mặt phẳng ranh giới vùng ra đều bị cuốn trôi theo dòng nước ra ngoài bể.

###### Physical Implications and Limitations in Real Clarifiers
- Trong thực tế, các giả thiết của Camp không bao giờ thỏa mãn hoàn toàn do hiện tượng dòng chảy ngắn (short-circuiting), xoáy cuộn rối, dòng đối lưu nhiệt do chênh lệch nhiệt độ, sóng gió trên mặt bể, và lực hút cục bộ gần mép tràn máng răng cưa. Tuy nhiên, lý thuyết bể lý tưởng cung cấp một chuẩn đối sánh định lượng tuyệt đối để định cỡ hình học bể và phân tích động học phân tách hạt.

##### 5.2.3.2 Functional Hydraulic Zones of an Ideal Rectangular Basin
###### Inlet Zone: Kinetic Momentum Dissipation & Streamline Straightening
- Chức năng: Tiếp nhận dòng nước từ kênh hoặc ống dẫn từ bể tạo bông với vận tốc tương đối lớn ($0.4 - 0.8\ \text{m/s}$), triệt tiêu hoàn toàn động năng dư thừa, giảm xung động vận tốc và dàn đều các đường dòng (streamlines) thành dòng chảy tầng/chảy đều song song theo phương ngang đi vào vùng lắng.

###### Settling Zone: Quiescent Plug-Flow Horizontal Transportation
- Chức năng: Cung cấp thể tích tĩnh lặng (quiescent volume) cho quá trình lắng trọng lực. Chế độ dòng chảy lý tưởng là dòng chảy nút (plug flow), trong đó mỗi phần tử nước chuyển động với vận tốc ngang không đổi:
  $$v_h = \frac{Q}{A_x} = \frac{Q}{W \cdot H}$$
  đồng thời hạt cặn rơi thẳng đứng xuống đáy với vận tốc lắng $v_s$.

###### Sludge Zone: Permanent Storage and Resuspension Protection
- Chức năng: Thu gom và chứa lớp cặn đã lắng xuống đáy bể, ngăn cách lớp cặn này khỏi trường vận tốc ngang của vùng lắng nhằm ngăn ngừa hiện tượng xới cặn (scouring/resuspension), đồng thời định tuyến cặn về các hố thu để gạt và xả bùn ra ngoài.

###### Outlet Zone: Velocity Gradient Convergence & Weir Withdrawal
- Chức năng: Thu thập lớp nước trong trên bề mặt bể lắng thông qua các vách tràn răng cưa V-notch và máng răng cưa ngón tay (finger launders), chuyển tiếp nước êm dịu vào kênh dẫn sang bể lọc nhanh hạ nguồn mà không tạo ra các dòng xoáy hút ngược cặn từ vùng lắng.

##### 5.2.3.3 Derivation of Critical Settling Velocity & Surface Overflow Rate (SOR)
###### Kinematic Particle Trajectory Equations in Rectangular Coordinates
- Xét hệ tọa độ Descartes $(x, z)$ đặt tại ranh giới vùng vào, với $x$ là phương dòng chảy ngang ($0 \le x \le L$) và $z$ là phương thẳng đứng tính từ mặt nước xuống đáy bể ($0 \le z \le H$).
- Phương trình vi phân chuyển động của hạt cặn trong vùng lắng lý tưởng:
  $$\frac{dx}{dt} = v_h = \frac{Q}{W \cdot H} = \text{const}$$
  $$\frac{dz}{dt} = v_s = \text{const}$$
- Tích phân theo thời gian chuyển động $t$:
  $$x(t) = v_h \cdot t$$
  $$z(t) = z_0 + v_s \cdot t$$
- Khử biến thời gian $t = \frac{x}{v_h}$, ta được phương trình quỹ đạo chuyển động của hạt cặn là một đường thẳng:
  $$z(x) = z_0 + \left(\frac{v_s}{v_h}\right) x$$

###### Definition of Critical Settling Velocity ($v_0 = \frac{H}{t_0} = \frac{Q}{A_s}$)
- Định nghĩa: **Vận tốc lắng tới hạn ($v_0$)** là vận tốc lắng nhỏ nhất của một hạt cặn xuất phát từ điểm cao nhất trên mặt nước tại đầu vùng vào ($z_0 = 0$ tại $x = 0$) có thể chạm tới đáy bể đúng tại điểm cuối cùng của vùng lắng ($z = H$ tại $x = L$).
- Thời gian lưu nước lý thuyết trong bể (hydraulic retention time $t_0$):
  $$t_0 = \frac{L}{v_h} = \frac{L \cdot W \cdot H}{Q} = \frac{V}{Q}$$
- Thay $x = L$, $z_0 = 0$, $z = H$ vào phương trình quỹ đạo:
  $$H = \left(\frac{v_0}{v_h}\right) L \implies v_0 = \frac{H \cdot v_h}{L} = \frac{H}{t_0}$$
- Thay $t_0 = \frac{A_s \cdot H}{Q}$ vào (với diện tích mặt bằng $A_s = L \cdot W$):
  $$v_0 = \frac{H}{\left(\frac{A_s \cdot H}{Q}\right)} = \frac{Q}{A_s} = \text{SOR}$$
- Biểu thức này xác lập tương đương cơ bản của kỹ thuật lắng (eq_ch05_011):
$$v_0 = \text{SOR} = \frac{Q}{A_s} = \frac{H}{t_0}$$
Trong đó:
- $v_0$: Vận tốc lắng tới hạn ($\text{m/s}$ hoặc $\text{m/h}$).
- $\text{SOR}$: Tải trọng thủy lực bề mặt (Surface Overflow Rate / Surface Loading Rate, $\text{m}^3/\text{m}^2\cdot\text{d}$ hoặc $\text{m}^3/\text{m}^2\cdot\text{h}$).
- $Q$: Lưu lượng nước vào bể ($\text{m}^3/\text{d}$ hoặc $\text{m}^3/\text{s}$).
- $A_s$: Diện tích mặt bằng của vùng lắng ($\text{m}^2$, $A_s = L \cdot W$).
- $H$: Chiều sâu lắng hữu ích của lớp nước ($\text{m}$).
- $t_0$: Thời gian lưu nước lý thuyết ($\text{h}$ hoặc $\text{s}$).

###### Hazen's Surface Area Principle: Independence of Settling from Depth
- Allen Hazen (1904) là người đầu tiên phát hiện ra nguyên lý kinh điển mang tính đột phá: **Hiệu quả lắng của bể lắng lý tưởng hoàn toàn độc lập với chiều sâu của bể $H$, mà chỉ phụ thuộc duy nhất vào diện tích bề mặt $A_s$ (hoặc tỷ số $Q/A_s$)**.
- *Chứng minh*: Giả sử giảm chiều sâu bể từ $H$ xuống $H/2$ trong khi giữ nguyên lưu lượng $Q$ và diện tích mặt bằng $A_s$. Thời gian lưu nước giảm một nửa ($t_0' = t_0/2$), nhưng quãng đường hạt cặn cần rơi để chạm đáy cũng giảm đi một nửa ($H' = H/2$). Do đó, tỷ số $H'/t_0' = (H/2)/(t_0/2) = H/t_0 = v_0$ hoàn toàn không đổi. Hạt có vận tốc lắng $v_s$ vẫn chạm đáy ở cùng vị trí tỷ lệ tương đương! Đây chính là nền tảng lý thuyết cho sự ra đời của các khối lắng lamen (Lamella) và lắng ống tốc độ cao sau này.

###### Hydraulic Retention Time ($t_0 = \frac{V}{Q} = \frac{H}{v_0}$)
- Thời gian lưu thủy lực danh định biểu diễn thời gian trung bình mà một phần tử nước lưu lại trong bể lắng (eq_ch05_012):
$$t_0 = \frac{V}{Q} = \frac{L \cdot W \cdot H}{Q} = \frac{A_s \cdot H}{Q} = \frac{H}{v_0}$$

##### 5.2.3.4 Upflow Clarifier Separation Criterion
###### Vectorial Equilibrium: Upward Superficial Velocity vs Downward Gravity
- Trong bể lắng đứng (Upflow Clarifier), nước chảy thẳng đứng từ dưới lên trên qua mặt cắt ướt ngang $A_s$ với vận tốc biểu kiến (superficial upward velocity) bằng chính tải trọng bề mặt:
  $$v_{\text{upward}} = v_0 = \frac{Q}{A_s}$$
- Chiều chuyển động của hạt cặn là tổng vector của vận tốc chất lỏng hướng lên ($\vec{v}_0$) và vận tốc lắng trọng lực của hạt hướng xuống ($\vec{v}_s$):
  $$v_{\text{net}} = v_s - v_0 \quad (\text{chiều dương quy ước hướng xuống đáy})$$

###### Binary Separation Criterion ($v_s \ge v_0$)
- Điều kiện cần và đủ để hạt cặn tách được khỏi dòng nước trong bể lắng đứng (eq_ch05_010):
$$v_s \ge v_0 \quad \text{với} \quad v_0 = \frac{Q}{A_s}$$
- *Kết quả phân tách nhị phân (Binary Separation)*:
  - Nếu $v_s \ge v_0$: Hạt cặn có vận tốc rơi lớn hơn hoặc bằng vận tốc nước dâng, hạt sẽ chuyển động đi xuống hoặc đứng lơ lửng, được giữ lại trong bể (hiệu suất loại bỏ đạt $100\%$).
  - Nếu $v_s < v_0$: Vận tốc nước dâng lớn hơn vận tốc lắng của hạt, hạt bị nước cuốn ngược lên trên và trôi hoàn toàn ra máng thu nước (hiệu suất loại bỏ bằng $0\%$).
  - *Lưu ý so sánh*: Khác với bể lắng ngang (nơi các hạt có $v_s < v_0$ vẫn được loại bỏ một phần tùy theo độ cao ban đầu), bể lắng đứng không loại bỏ được bất kỳ hạt nào có $v_s < v_0$ nếu không hình thành lớp đệm bùn lọc lơ lửng.

##### 5.2.3.5 Discrete Fractional Removal Efficiency for Sub-Critical Particles
###### Uniform Depth Inflow Distribution Derivation ($r = \frac{v_s}{v_0} = \frac{v_s t_0}{H}$)
- Trong bể lắng ngang lý tưởng, xét nhóm hạt rời rạc có vận tốc lắng nhỏ hơn vận tốc tới hạn ($v_s < v_0$).
- Do hạt phân bố đều trên toàn bộ chiều sâu $H$ tại $x = 0$, hạt chỉ có thể chạm đáy trong chiều dài $L$ nếu độ cao xuất phát ban đầu $z_0$ của nó thỏa mãn:
  $$H - z_0 \le v_s \cdot t_0 = v_s \left(\frac{L}{v_h}\right) = v_s \left(\frac{H}{v_0}\right)$$
  $$z_0 \ge H \left(1 - \frac{v_s}{v_0}\right)$$
- Khoảng độ sâu thẳng đứng tối đa từ đáy mà tại đó các hạt kịp rơi xuống đáy trước khi rời khỏi bể là:
  $$h_{\text{capture}} = H - z_0 = H \cdot \frac{v_s}{v_0}$$
- Vì cặn phân bố đồng đều theo chiều sâu, tỷ lệ phần trăm số hạt có vận tốc lắng $v_s$ được loại bỏ chính là tỷ số giữa chiều sâu thu nhận $h_{\text{capture}}$ và tổng chiều sâu $H$ (eq_ch05_013):
$$r = \frac{h_{\text{capture}}}{H} = \frac{v_s}{v_0} = \frac{v_s \cdot A_s}{Q} = \frac{v_s \cdot t_0}{H} \quad (\text{với } v_s < v_0)$$
Trong đó:
- $r$: Tỷ số loại bỏ phân đoạn của nhóm hạt có vận tốc $v_s$ ($0 \le r < 1.0$).
- $v_s$: Vận tốc lắng riêng của nhóm hạt ($\text{m/s}$).
- $v_0$: Tải trọng bề mặt / Vận tốc lắng tới hạn của bể ($\text{m/s}$).

###### Cumulative Settling Velocity Distribution Integration ($R_{\text{total}} = (1 - F_0) + \frac{1}{v_0}\int_0^{F_0} v_s dF$)
- Trong một huyền phù đa phân tán (polydisperse suspension), các hạt có dải kích thước và vận tốc lắng liên tục được mô tả bởi đường cong phân bố khối lượng tích lũy $F(v)$, trong đó $F$ là phần khối lượng cặn có vận tốc lắng nhỏ hơn hoặc bằng $v$.
- Gọi $F_0$ là phần khối lượng tích lũy của các hạt có vận tốc lắng $v_s \le v_0$.
- Phần khối lượng hạt có vận tốc lắng $v_s \ge v_0$ là $(1 - F_0)$, toàn bộ nhóm này được loại bỏ $100\%$.
- Phần khối lượng hạt có vận tốc lắng $v_s < v_0$ (từ $0$ đến $F_0$) chỉ được loại bỏ theo tỷ số phân đoạn $r = v_s/v_0$.
- Tổng hiệu suất loại bỏ chất rắn lơ lửng của bể lắng lý tưởng bằng tích phân tổng hợp (eq_ch05_014):
$$R_{\text{total}} = (1 - F_0) + \int_0^{F_0} \frac{v_s}{v_0} \, dF = (1 - F_0) + \frac{1}{v_0} \int_0^{F_0} v_s \, dF$$

###### Graphical Area Interpretation of Suspension Removal Curve
- Trên đồ thị biểu diễn $v_s$ theo $F$, tích phân $\int_0^{F_0} v_s \, dF$ chính là diện tích nằm bên dưới đường cong phân bố vận tốc từ $F = 0$ đến $F = F_0$.
- Việc tính toán hiệu suất tổng hợp có thể thực hiện chính xác bằng cách chia dải tích phân thành $n$ hình thang nhỏ:
  $$\int_0^{F_0} v_s \, dF \approx \sum_{i=1}^n \left(\frac{v_{s,i} + v_{s,i-1}}{2}\right) \Delta F_i$$

##### 5.2.3.6 Hydraulic Scouring Velocity & Resuspension Threshold (Camp Scour Equation)
###### Camp-Shields Bed Shear Stress Formulation
- Dòng nước chảy ngang trên lớp bùn đáy sinh ra ứng suất cắt ma sát bề mặt (boundary shear stress $\tau_0$).
- Khi lực ma sát tiếp tuyến do dòng chảy gây ra vượt quá lực ma sát trọng lực giữ hạt cặn nằm yên trên đáy, hạt cặn sẽ bị xới tung và cuốn ngược trở lại vào dòng nước trong (resuspension).

###### Scour Velocity Equation ($v_{\text{scour}} = \sqrt{\frac{8k(s-1)gd}{f}}$)
- Thomas R. Camp ứng dụng lý thuyết dịch chuyển bùn cát của Shields để thiết lập phương trình xác định **vận tốc dòng chảy ngang tới hạn gây xới cặn ($v_{\text{scour}}$)**:
$$v_{\text{scour}} = \sqrt{\frac{8 k (s - 1) g d}{f}} = \sqrt{\frac{8 k (\text{SG} - 1) g d}{f}}$$
Trong đó:
- $v_{\text{scour}}$: Vận tốc dòng chảy ngang trung bình bắt đầu gây xới cặn ($\text{m/s}$).
- $k$: Hằng số thực nghiệm phụ thuộc vào tính dính bám của hạt cặn:
  - $k \approx 0.04$: Đối với hạt cát rời rạc, không dính (unsticked sand/grit).
  - $k \approx 0.06$: Đối với hạt cát có keo dính nhẹ.
  - $k \approx 0.10 - 0.15$: Đối với bông cặn keo tụ nhôm/sắt có tính dính bám và liên kết nhớt.
- $s$ (hoặc $\text{SG}$): Tỷ trọng tương đối của hạt cặn ($\text{SG} = \rho_s/\rho_w$, ví dụ cát $2.65$, bông cặn phèn nhôm $1.001 - 1.005$).
- $g$: Gia tốc trọng trường ($9.81\ \text{m/s}^2$).
- $d$: Đường kính của hạt cặn bị xới ($\text{m}$).
- $f$: Hệ số ma sát Darcy-Weisbach của đáy bể lắng ($f \approx 0.02 - 0.03$, đối với bê tông xoa phẳng $f \approx 0.025$).

###### Parameter Definition: Cohesion Constant $k$, Darcy Friction Factor $f$, Safety Ratios
- *Tiêu chuẩn an toàn chống xới cặn trong thiết kế*:
  Vận tốc dòng chảy ngang thực tế trong vùng lắng ($v_h$) phải được kiểm soát nghiêm ngặt để luôn nhỏ hơn đáng kể so với vận tốc xới cặn:
  $$v_h \le \frac{1}{2} v_{\text{scour}} \quad \text{đến} \quad \frac{1}{3} v_{\text{scour}}$$
  Thông thường đối với bông cặn keo tụ hữu cơ/nhôm rất nhẹ ($s - 1 \approx 0.002 - 0.005$), $v_h$ thiết kế trong bể lắng ngang đô thị không được vượt quá $0.15 - 0.90\ \text{m/min}$ ($2.5 - 15\ \text{mm/s}$), thường khống chế dưới $0.50\ \text{m/min}$ ($8.3\ \text{mm/s}$) để tuyệt đối không làm tróc lớp bùn đáy.

#### 5.2.4 Type II Flocculant Settling & Settling Column Analysis (Lắng Keo Tụ / Tạo Bông)
##### 5.2.4.1 Mechanics of Dynamic Floc Coalescence & Aggregation
###### Differential Settling Velocity Collisions (Orthokinetic Aggregation in Basins)
- Quá trình lắng Type II đặc trưng cho các bông cặn sinh ra từ quá trình keo tụ bằng phèn nhôm, phèn sắt hoặc kết tủa mềm vôi.
- Cơ chế va chạm động học trong bể lắng:
  - Hạt cặn lớn có vận tốc lắng nhanh hơn sẽ đuổi kịp các hạt cặn nhỏ lắng chậm hơn nằm trên cùng đường rơi.
  - Khi va chạm, nhờ lực dính bám của màng nhôm hydroxit và polymer, các hạt kết hợp thành một hạt mới có thể tích lớn hơn ($V_{\text{new}} = V_1 + V_2$).
  - Quá trình kết tụ liên tục này làm kích thước hạt tăng dần theo chiều sâu rơi ($d_p \uparrow$), dẫn đến vận tốc lắng tăng tốc dần theo hàm phi tuyến dọc theo quỹ đạo rơi ($v_s = f(z)$).

###### Invalidation of Stokes' Law (Continuous Changes in Size, Shape, Water Entrapment & Density)
- Định luật Stokes hoàn toàn **không thể áp dụng** cho quá trình lắng Type II vì các nguyên nhân cơ bản sau:
  1. Kích thước hạt không cố định mà biến đổi liên tục dọc theo chiều sâu bể.
  2. Bông cặn giữ nước (water entrapment) trong cấu trúc xốp vi mô; khi bông lớn lên, tỷ lệ nước liên kết tăng làm khối lượng riêng của bông cặn suy giảm dần tiệm cận với khối lượng riêng của nước ($\rho_s \to \rho_w$).
  3. Hình dạng bông cặn bất đối xứng, dễ bị biến dạng và nén ép dưới tác dụng của ứng suất cắt thủy động học.
  4. Do không có phương trình vi phân giải tích thuần túy, việc thiết kế bể lắng cho cặn Type II bắt buộc phải dựa trên dữ liệu thực nghiệm đo đạc từ **cột lắng thí nghiệm (settling column test)**.

##### 5.2.4.2 Settling Column Testing Protocol
###### Experimental Apparatus Architecture (Height 2-3 m, Sampling Taps at 0.5 m Intervals)
- Cột lắng thí nghiệm bao gồm một ống trụ thủy tinh hoặc mica trong suốt có đường kính trong từ $10$ đến $20\ \text{cm}$ (để giảm thiểu hiệu ứng ma sát thành ống) và chiều cao tối thiểu bằng chiều sâu thiết kế của bể lắng thực tế ($H = 2.0 - 3.0\ \text{m}$).
- Dọc theo thân cột bố trí các cổng lấy mẫu (sampling ports) cách đều nhau (thông thường cách nhau $\Delta h = 0.5\ \text{m}$, ví dụ tại các độ sâu $h = 0.5\ \text{m}, 1.0\ \text{m}, 1.5\ \text{m}, 2.0\ \text{m}$).

###### Test Execution: Homogeneous Initial Concentration $C_0$ & Isothermal Environment
- Quy trình tiến hành:
  1. Lấy mẫu nước ngay sau bể tạo bông, nạp đầy vào cột lắng và khuấy nhẹ để tạo nồng độ chất rắn ban đầu hoàn toàn đồng nhất $C_0$ ($\text{mg/L}$) trên toàn bộ chiều cao cột.
  2. Giữ cột lắng trong điều kiện tĩnh lặng tuyệt đối và đẳng nhiệt (isothermal conditions) để ngăn chặn các dòng đối lưu nhiệt làm xáo trộn cặn.
  3. Bấm giờ ($t = 0$). Tại các mốc thời gian định trước (ví dụ $t = 10, 20, 30, 45, 60, 90, 120, 180\ \text{phút}$), mở van rút các mẫu nước nhỏ ($50 - 100\ \text{mL}$) đồng thời từ các cổng lấy mẫu ở từng độ sâu.

###### Sample Aliquot Sampling and Gravimetric TSS Determination ($R\% = \frac{C_0 - C_t}{C_0} \times 100\%$)
- Phân tích nồng độ chất rắn lơ lửng $C_t$ của từng mẫu theo phương pháp sấy khô khối lượng ở $105^\circ\text{C}$.
- Tính toán phần trăm cặn đã lắng được loại bỏ tại độ sâu $h$ và thời gian $t$ (eq_ch05_015):
$$R\% = \frac{C_0 - C_t}{C_0} \times 100\%$$
Trong đó:
- $R\%$: Hiệu suất loại bỏ chất rắn lơ lửng tại độ sâu $h$ và thời điểm $t$ (%).
- $C_0$: Nồng độ TSS đồng nhất ban đầu trong cột lắng ($\text{mg/L}$).
- $C_t$: Nồng độ TSS đo được tại cổng lấy mẫu ở độ sâu $h$ tại thời điểm $t$ ($\text{mg/L}$).

##### 5.2.4.3 Isoconcentration Contours & Depth-Time Performance Grids
###### Construction of Isoconcentration Contours in $(t, h)$ Phase Space
- Lập lưới tọa độ với trục hoành là thời gian lắng $t$ ($\text{phút}$) và trục tung là độ sâu cột lắng $h$ ($\text{m}$, gốc tọa độ $h = 0$ ở mặt nước, chiều dương hướng xuống đáy $H$).
- Điền các giá trị phần trăm loại bỏ $R\%$ tính được vào các tọa độ thực nghiệm $(t, h)$ tương ứng.
- Sử dụng phương pháp nội suy đường thẳng để nối các điểm có cùng tỷ lệ phần trăm loại bỏ, vẽ nên các **đường cong đồng nồng độ / đồng hiệu suất (isoconcentration lines / isoremoval contours)**, ví dụ các đường $40\%, 50\%, 60\%, 70\%, 80\%$.

###### Curvature Diagnostics: Accelerated Downward Curvature as Floc Growth Indicator
- *Dấu hiệu nhận biết động học*:
  - Nếu hạt là Type I (không kết tụ): Vận tốc rơi không đổi, các đường đồng nồng độ trên đồ thị $(t, h)$ là các **đường thẳng tắp** đi qua gốc tọa độ ($h = v_s \cdot t$).
  - Đối với hạt Type II (kết tụ bông): Vì hạt càng rơi sâu càng lớn và lắng nhanh hơn, độ dốc tức thời ($dh/dt$) tăng dần theo thời gian và độ sâu. Do đó, các đường đồng nồng độ luôn là các **đường cong có bề lõm hướng xuống dưới (downward curvature)**, minh chứng trực quan cho sự gia tốc vận tốc lắng.

##### 5.2.4.4 Overall Suspended Solids Removal Efficiency by Graphical Integration
###### Trapezoidal Depth Integration Formula ($R_{\text{total}} = R_0 + \sum \frac{\Delta h_i}{H} \frac{R_i + R_{i-1}}{2}$)
- Để xác định tổng hiệu suất loại bỏ chất rắn lơ lửng trong bể lắng có chiều sâu thiết kế $H$ tại thời gian lưu nước mục tiêu $t_0$:
  1. Dựng đường gióng thẳng đứng tại thời điểm $t = t_0$ cắt toàn bộ chiều sâu cột từ $h = 0$ đến $h = H$.
  2. Xác định đường đồng nồng độ $R_0$ chạm tới đáy bể ($h = H$) tại thời điểm $t_0$. Toàn bộ lượng cặn tương ứng với giá trị $R_0$ này đã lắng hoàn toàn xuống đáy ($100\%$ capture).
  3. Đường gióng $t = t_0$ sẽ cắt các đường đồng nồng độ cao hơn ($R_1, R_2, \dots, R_n$) tại các cao độ tương ứng. Khoảng cách thẳng đứng giữa hai đường đồng nồng độ kề nhau là $\Delta h_i$.
  4. Lớp nước có chiều dày $\Delta h_i$ được loại bỏ với hiệu suất trung bình xấp xỉ bằng $\frac{R_i + R_{i-1}}{2}$.
- Tổng hiệu suất loại bỏ cặn tổng thể được tính bằng công thức tích phân hình thang (eq_ch05_016):
$$R_{\text{total}} = R_0 + \sum_{i=1}^n \frac{\Delta h_i}{H} \cdot \left(\frac{R_i + R_{i-1}}{2}\right)$$
Trong đó:
- $R_{\text{total}}$: Tổng hiệu suất loại bỏ chất rắn lơ lửng của bể (%).
- $R_0$: Giá trị của đường đồng nồng độ đạt tới đáy bể $H$ tại thời gian $t_0$ (%).
- $H$: Chiều sâu tổng cộng của vùng lắng trong bể ($\text{m}$).
- $\Delta h_i$: Khoảng cách thẳng đứng giữa hai đường đồng mức $R_i$ và $R_{i-1}$ tại thời điểm $t_0$ ($\text{m}$).
- $R_i, R_{i-1}$: Hiệu suất loại bỏ của hai đường đồng nồng độ lân cận (%).

##### 5.2.4.5 Empirical Field Scale-Up Safety Factors
###### Detention Time Multiplication Factor ($1.25 - 1.75$)
- Cột lắng trong phòng thí nghiệm là môi trường tĩnh lý tưởng, hoàn toàn không có gió, không có dòng chảy xoáy ở cửa vào và cửa ra.
- Để chuyển đổi từ thời gian lưu cột lắng thí nghiệm $t_{0,\text{lab}}$ sang thời gian lưu thiết kế thực tế ngoài hiện trường $t_{0,\text{field}}$, kỹ sư bắt buộc phải nhân với hệ số an toàn phóng to (scale-up factor):
  $$t_{0,\text{field}} = (1.25 - 1.75) \times t_{0,\text{lab}} \quad (\text{thông thường chọn } 1.50)$$

###### Surface Overflow Rate Reduction Factor ($0.65 - 0.85$)
- Tương tự, tải trọng bề mặt thiết kế thực tế phải được giảm xuống so với giá trị tính toán trong phòng thí nghiệm:
  $$\text{SOR}_{\text{field}} = (0.65 - 0.85) \times \text{SOR}_{\text{lab}} \quad (\text{thông thường chọn } 0.70)$$

###### Rationale: Inlet Turbulence, Thermal Density Currents, Wind Shear, and Outlet Updrafts
- Bốn yếu tố thủy lực bất lợi trong công trình thực tế bắt buộc phải sử dụng các hệ số an toàn trên:
  1. *Năng lượng xáo trộn vùng vào*: Dòng nước vào bể không thể phân phối đều tức thời mà luôn tạo xoáy cục bộ.
  2. *Dòng đối lưu mật độ do nhiệt (Density currents)*: Chênh lệch nhiệt độ chỉ $0.5^\circ\text{C}$ giữa nước thô và khối nước trong bể tạo ra các luồng dòng chảy ngầm cực nhanh.
  3. *Lực ma sát gió trên mặt thoáng (Wind shear)*: Gió thổi trên mặt bể dài tạo dòng chảy mặt kéo theo dòng hoàn lưu đáy xới cặn.
  4. *Dòng hút dâng cục bộ ở máng tràn (Weir updraft currents)*: Lực hút nước dâng gần mép tràn cuốn cặn lơ lửng ra ngoài.

#### 5.2.5 Type III (Zone/Hindered) & Type IV (Compression) Settling Kinetics (Lắng Vùng và Nén Bùn)
##### 5.2.5.1 Concentrated Suspension settling Dynamics (> 1,000 mg/L TSS)
###### Interparticle Hydrodynamic Interaction & Upward Pore-Water Displacement
- Khi nồng độ chất rắn trong nước vượt qua ngưỡng $1,000\ \text{mg/L}$ (thường gặp trong các bể lắng tiếp xúc chất rắn, bể làm mềm nước bằng vôi có tuần hoàn bùn, bể lắng thứ cấp xử lý sinh học và bể nén bùn), các hạt cặn ở rất gần nhau.
- Không gian rỗng giữa các hạt bị thu hẹp đáng kể. Khi các hạt cùng chuyển động đi xuống dưới tác dụng của trọng lực, một thể tích nước tương đương bị đẩy dịch chuyển ngược lên trên qua các khe hở hẹp giữa các hạt. Dòng nước dâng cục bộ này tạo lực cản nhớt rất mạnh làm chậm tốc độ rơi của toàn bộ hệ thống hạt.

###### Formation and Subsidence of Sludge Blanket Interface
- Lực tương tác tĩnh điện và cơ học giữ các hạt ở vị trí tương đối cố định với nhau, khiến toàn bộ khối cặn lắng xuống như một tấm thảm đồng nhất (blanket).
- Sự suy giảm của khối cặn tạo ra một ranh giới phân pha (liquid-solid interface) cực kỳ rõ rệt giữa lớp nước trong bên trên (supernatant) và lớp màng bùn đục ngầu bên dưới. Quá trình này được gọi là **Lắng vùng (Zone Settling)** hay **Lắng cản trở (Hindered Settling)**.

##### 5.2.5.2 Batch Settling Column Stratification Zones (Zones A, B, C, D)
###### Zone A: Supernatant Clarified Water
- Lớp nước trong phía trên cùng: Chứa nước đã được tách cặn gần như hoàn toàn; ranh giới mặt bùn hạ thấp dần để lại thể tích nước trong tăng dần theo thời gian.

###### Zone B: Uniform Initial Concentration Hindered Settling Zone
- Vùng huyền phù đồng nhất: Nồng độ cặn trong vùng này giữ nguyên bằng nồng độ ban đầu $C_0$; toàn bộ vùng này di chuyển đi xuống với cùng một vận tốc không đổi $v_i$.

###### Zone C: Transition (Thickening) Zone with solids Concentration Gradient
- Vùng chuyển tiếp (vùng cô đặc): Nằm ngay dưới vùng B, nơi nồng độ cặn tăng dần từ $C_0$ lên nồng độ nén; vận tốc lắng giảm dần do cản trở cơ học tăng cao.

###### Zone D: Compressed Sludge Matrix Layer
- Vùng bùn nén chặt: Nằm ở đáy cột/bể; các hạt cặn tiếp xúc cơ học trực tiếp lên nhau, tạo thành cấu trúc khung xốp chịu lực.

##### 5.2.5.3 Interface Height vs. Elapsed Time Settling Curve Analysis
###### Constant Settling Velocity Linear Slope ($v_i = -dh/dt$)
- Trên đồ thị biểu diễn chiều cao ranh giới màng bùn $H_i$ theo thời gian lắng $t$:
  - Giai đoạn ban đầu (từ $t = 0$ đến khi xuất hiện vùng chuyển tiếp): Ranh giới pha hạ thấp với tốc độ hoàn toàn tuyến tính.
  - Vận tốc lắng cản trở ban đầu ($v_i$) được xác định chính xác bằng độ dốc của đoạn thẳng tuyến tính này:
    $$v_i = -\frac{dH_i}{dt} = \text{const}$$

###### Retardation / Deceleration Phase and Transition Curve
- Khi vùng B biến mất hoàn toàn, ranh giới pha tiếp xúc trực tiếp với vùng chuyển tiếp C; tốc độ hạ thấp của mặt bùn chậm lại đáng kể, đồ thị chuyển thành một đường cong thoải dần.

###### Compression Point Identification (Talmadge-Fitch Graphical Tangent Construction)
- Điểm tới hạn bắt đầu quá trình lắng nén thuần túy được gọi là **Điểm nén (Compression Point - ký hiệu tọa độ $t_c, H_c$)**.
- Phương pháp đồ họa Talmadge-Fitch:
  1. Kẻ đường tiếp tuyến với đoạn thẳng lắng cản trở ban đầu (vận tốc $v_i$).
  2. Kẻ đường tiếp tuyến với đoạn cong tiệm cận phẳng của giai đoạn nén cặn cuối cùng.
  3. Kẻ đường phân giác của góc tạo bởi hai tiếp tuyến trên.
  4. Giao điểm của đường phân giác với đường cong lắng thực nghiệm chính là Điểm nén $(t_c, H_c)$.

##### 5.2.5.4 Vesilind Hindered Settling Velocity Model
###### Mathematical Formulation ($v_i = v_0 e^{-k C}$)
- Vận tốc lắng cản trở $v_i$ phụ thuộc phi tuyến chặt chẽ vào nồng độ chất rắn $C$. Mô hình hàm mũ kinh điển của Vesilind (1968) được áp dụng phổ biến nhất:
$$v_i = v_0 \cdot e^{-k \cdot C}$$
Trong đó:
- $v_i$: Vận tốc lắng cản trở của màng bùn ở nồng độ $C$ ($\text{m/h}$).
- $v_0$: Vận tốc lắng tối đa lý thuyết khi độ pha loãng vô cùng ($C \to 0$) ($\text{m/h}$).
- $k$: Hệ số cản trở Vesilind phụ thuộc vào tính chất liên kết bông cặn ($\text{m}^3/\text{kg}$ hoặc $\text{L/g}$).
- $C$: Nồng độ chất rắn lơ lửng trong huyền phù ($\text{kg/m}^3$ hoặc $\text{g/L}$).

##### 5.2.5.5 Solids Flux Theory (SFT) for Clarifier-Thickener Sizing (Coe-Clevenger & Kynch)
###### Total Downward Solids Flux Formulation ($G_{\text{total}} = G_g + G_u = C v_i + C u_b = C v_i + C \frac{Q_u}{A}$)
- Trong một bể lắng hoạt động liên tục kết hợp chức năng cô đặc bùn đáy (Clarifier-Thickener), tổng thông lượng cặn chuyển động xuống đáy trên một đơn vị diện tích bề mặt bể bao gồm hai thành phần vật lý độc lập (eq_ch05_022):
$$G_{\text{total}} = G_g + G_u = C \cdot v_i + C \cdot u_b = C \cdot v_i + C \cdot \frac{Q_u}{A}$$
Trong đó:
- $G_{\text{total}}$: Tổng thông lượng cặn đi xuống đáy ($\text{kg/m}^2\cdot\text{h}$).
- $G_g$: Thông lượng cặn do trọng lực lắng cản trở gây ra ($\text{kg/m}^2\cdot\text{h}$, $G_g = C \cdot v_i$).
- $G_u$: Thông lượng cặn do dòng rút bùn đáy cưỡng bức gây ra ($\text{kg/m}^2\cdot\text{h}$, $G_u = C \cdot u_b$).
- $C$: Nồng độ chất rắn lơ lửng tại mặt cắt đang xét ($\text{kg/m}^3$).
- $v_i$: Vận tốc lắng cản trở ở nồng độ $C$ ($\text{m/h}$).
- $u_b$: Vận tốc chuyển động khối của chất lỏng do bơm rút bùn đáy tạo ra ($\text{m/h}$, $u_b = Q_u / A$).
- $Q_u$: Lưu lượng bùn xả đáy rút ra khỏi bể ($\text{m}^3/\text{h}$).
- $A$: Diện tích mặt bằng bể lắng - cô đặc bùn ($\text{m}^2$).

###### Gravity Flux Curve ($G_g = C v_i$) Concavity and Minimum
- Khi nồng độ cặn $C$ rất nhỏ: $v_i \approx v_0$ lớn nhưng $C$ nhỏ, nên $G_g$ nhỏ.
- Khi nồng độ cặn $C$ rất lớn: $C$ cao nhưng $v_i \to 0$ do cản trở cơ học, nên $G_g$ cũng triệt tiêu.
- Do đó, đồ thị $G_g(C)$ luôn có dạng một đường cong có đỉnh cực đại rồi suy giảm xuống một **vùng trũng cực tiểu (local minimum)**.

###### Underflow Bulk Transport Flux ($G_u = C u_b$) Linearity
- Thành phần thông lượng rút bùn $G_u = u_b \cdot C$ là một đường thẳng đi qua gốc tọa độ với hệ số góc bằng chính vận tốc rút bùn $u_b = Q_u/A$.

###### State Point Analysis & Limiting Flux Bottleneck ($G_L$) Determination
- Đường cong tổng thông lượng $G_{\text{total}} = G_g + G_u$ biểu diễn khả năng vận chuyển bùn xuống đáy của bể.
- Điểm cực tiểu cục bộ của đường cong $G_{\text{total}}$ xác định **Thông lượng giới hạn (Limiting Solids Flux - ký hiệu $G_L$)** tại nồng độ nghẽn mạch (bottleneck concentration $C_L$).
- Nếu lượng cặn nạp vào bể vượt quá $G_L$, bể sẽ bị quá tải bùn: lớp cặn tại nồng độ $C_L$ không thể chìm xuống đáy kịp tốc độ nạp, mặt bùn sẽ dâng cao liên tục và tràn ra máng thu nước trong.

###### Basin Thickening Area Sizing Formula ($A_{\text{thickening}} = \frac{Q_0 C_0}{G_L}$)
- Diện tích mặt bằng tối thiểu cần thiết để bể lắng đảm bảo chức năng nén và cô đặc bùn đạt nồng độ bùn xả đáy mong muốn $C_u$:
  $$A_{\text{thickening}} = \frac{Q_0 \cdot C_0}{G_L}$$
  Trong đó $Q_0, C_0$ lần lượt là lưu lượng và nồng độ cặn đi vào bể.
- Kỹ sư thiết kế phải so sánh diện tích làm trong nước ($A_{\text{clarification}} = Q_0 / \text{SOR}$) và diện tích nén bùn ($A_{\text{thickening}}$); giá trị lớn hơn sẽ quyết định diện tích thực tế của công trình:
  $$A_{\text{basin}} = \max(A_{\text{clarification}}, A_{\text{thickening}})$$

##### 5.2.5.6 Type IV Compression Settling Mechanics & Pore-Water Squeezing
###### Soil Consolidation Analogy (Terzaghi Consolidation Analogy)
- Lắng nén diễn ra tại các lớp cặn sát đáy bể lắng hoặc trong bể nén bùn trọng lực.
- Cơ chế vật lý tương tự như lý thuyết cố kết cơ học đất của Karl Terzaghi: Các hạt cặn đã tựa cơ học lên nhau tạo thành bộ khung cấu trúc. Ứng suất toàn phần tác dụng lên lớp bùn được phân chia thành ứng suất hiệu dụng của bộ khung hạt ($\sigma'$) và áp lực nước lỗ rỗng ($u$):
  $$\sigma = \sigma' + u$$

###### Compression Consolidation Kinetics & Permeability Reduction
- Quá trình "lắng" thực chất là sự dịch chuyển của nước lỗ rỗng bị nén ép thoát ra khỏi các mao quản siêu nhỏ chảy ngược lên trên dưới áp lực tĩnh của các lớp cặn nằm đè phía trên.
- Khi bùn nén càng chặt, độ rỗng giảm, hệ số thấm mao quản của khối bùn giảm theo hàm mũ, khiến tốc độ nén chậm dần theo thời gian và tiệm cận đến một độ ẩm giới hạn cân bằng. Do đó, bể nén bùn thường được trang bị các cánh khuấy cọc thẳng đứng quay rất chậm ($v = 0.02 - 0.05\ \text{m/s}$) để tạo các rãnh thoát nước mao dẫn nhân tạo, thúc đẩy nước lỗ rỗng thoát lên nhanh chóng.

#### 5.2.6 High-Rate Settling: Ballasted Flocculation & Lamella Plate/Tube Settlers
##### 5.2.6.1 Acceleration Mechanisms: Density Ballasting vs. Distance Reduction
###### Comparative Hydrodynamic Rationale: Stokes' Law Levers
Từ phương trình Stokes kinh điển:
$$v_s = \frac{g (\rho_s - \rho) d^2}{18 \mu}$$
Có hai đòn bẩy thủy động lực học cốt lõi để nâng cao đột biến hiệu quả lắng:
1. **Gia tăng độ chênh lệch khối lượng riêng $(\rho_s - \rho)$**: Thay vì chấp nhận bông cặn phèn nhôm nhẹ xốp ($\text{SG} \approx 1.001$), công nghệ keo tụ gia trọng (Ballasted Flocculation) bổ sung các hạt vi cát có tỷ trọng rất cao ($\text{SG} = 2.65$) làm nhân kết tụ, nâng tỷ trọng bông cặn hỗn hợp lên nhiều lần, giúp vận tốc lắng tăng vọt từ $1\ \text{m/h}$ lên tới $20 - 40\ \text{m/h}$.
2. **Rút ngắn khoảng cách rơi của hạt ($H \to d$)**: Theo Hazen, phân chia chiều sâu bể thành các tầng mỏng nhờ các tấm nghiêng hoặc ống nghiêng sẽ rút ngắn khoảng cách rơi từ vài mét xuống chỉ còn vài centimet ($50\ \text{mm}$), giúp hạt cặn chạm bề mặt lắng trong thời gian cực ngắn.

###### Volumetric Footprint Compression Factor (up to 80 - 90% reduction)
- Nhờ hai cơ chế tăng tốc trên, các công nghệ lắng tốc độ cao (High-rate clarifiers) cho phép nâng tải trọng bề mặt lên gấp $4 - 8\ \text{lần}$ (đối với tấm lắng Lamella) và gấp $8 - 15\ \text{lần}$ (đối with lắng vi cát Actiflo®), giúp giảm thiểu từ 75% đến 90% diện tích mặt bằng xây dựng và thể tích công trình so với bể lắng ngang truyền thống.

##### 5.2.6.2 Ballasted Flocculation (Actiflo® Process Technology)
###### Microsand Specifications: Specific Gravity ($SG = 2.50 - 2.65$), Particle Diameter ($20 - 200\ \mu\text{m}$, typically $80 - 130\ \mu\text{m}$)
- Vi cát (microsand) sử dụng làm vật liệu gia trọng là cát thạch anh tinh khiết:
  - Khối lượng riêng: $\rho_{\text{sand}} = 2,500 - 2,650\ \text{kg/m}^3$ (tỷ trọng $\text{SG} = 2.50 - 2.65$).
  - Đường kính hạt danh định: $d_{\text{sand}} = 20 - 200\ \mu\text{m}$ (tối ưu nhất trong khoảng $80 - 130\ \mu\text{m}$, cỡ mắt lưới $120 - 200\ \text{mesh}$).
  - Kích thước này đủ nhỏ để giữ lơ lửng ổn định trong bể khuấy tạo bông, nhưng đủ lớn và nặng để tạo gia tốc rơi vượt trội và tách biệt dễ dàng trong xyclon thủy lực.

###### Unit Process Flowsheet: Coagulant Flash Mix $\to$ Sand/Polymer Injection $\to$ Maturation $\to$ Lamella Settler
Dây chuyền công nghệ lắng vi cát (Actiflo®) bao gồm 4 ngăn liên hoàn khép kín:
1. **Bể trộn nhanh keo tụ (Coagulation Tank)**: Châm phèn nhôm hoặc phèn sắt, khuấy trộn thủy lực mạnh ($G = 300 - 500\ \text{s}^{-1}$, thời gian lưu $t = 1 - 2\ \text{phút}$) để làm mất ổn định hệ keo.
2. **Bể châm vi cát và polymer (Injection Tank)**: Châm vi cát tuần hoàn cùng với polymer trợ keo tụ anion trọng lượng phân tử cao; khuấy trộn vừa phải ($G = 150 - 200\ \text{s}^{-1}$, $t = 1 - 2\ \text{phút}$) để chuỗi polymer kết dính các vi cát với các hạt keo mất ổn định.
3. **Bể hoàn thiện bông cặn (Maturation Tank)**: Khuấy trộn êm dịu ($G = 50 - 80\ \text{s}^{-1}$, $t = 4 - 6\ \text{phút}$) để các bông cặn bọc cát phát triển kích thước tối đa, tạo thành các cụm hạt "bông - cát" siêu nặng.
4. **Bể lắng tấm nghiêng Lamella (Lamella Clarifier)**: Nước chảy ngược từ dưới lên qua các tấm Lamella nghiêng 60°; các bông cặn nặng rơi xuống đáy chỉ trong vài phút, nước trong tràn qua máng thu trên mặt.

###### Hydrocyclone Centrifugal Sand Recovery and Recycle Loop
- Hỗn hợp bùn và vi cát lắng ở đáy bể được gạt về hố thu trung tâm và bơm bùn liên tục hút đẩy lên thiết bị **Xyclon thủy lực (Hydrocyclone)**.
- Dưới tác dụng của lực ly tâm cực mạnh trong xyclon:
  - Các hạt vi cát có tỷ trọng lớn ($\text{SG} = 2.65$) bị văng ra sát thành nón và thoát ra ngoài ở đáy dưới (underflow), quay trở lại ngay lập tức vào bể châm vi cát để tái sử dụng với hiệu suất thu hồi cát đạt $> 99.5\%$.
  - Lớp cặn bùn hydroxit hữu cơ nhẹ hơn ($\text{SG} \approx 1.01$) tập trung ở tâm lốc xoáy và thoát ra ở đỉnh trên (overflow) để dẫn sang khu xử lý bùn thải.

###### Ultra-High Surface Overflow Rates ($150 - 250\ \text{m}^3/\text{m}^2\cdot\text{d}$, up to $300\ \text{m}^3/\text{m}^2\cdot\text{d}$)
- Tải trọng bề mặt tính toán trên diện tích mặt bằng bể lắng đạt ngưỡng siêu cao:
  $$\text{SOR}_{\text{ballasted}} = 150 - 250\ \text{m}^3/\text{m}^2\cdot\text{d} \quad (6.25 - 10.4\ \text{m/h})$$
  Trong điều kiện xử lý nước mưa hoặc nước thô độ đục cực cao, tải trọng có thể đẩy lên tới $300\ \text{m}^3/\text{m}^2\cdot\text{d}$ ($12.5\ \text{m/h}$).

###### Hydraulic Residence Time ($10 - 20\ \text{minutes}$)
- Tổng thời gian lưu nước của toàn bộ hệ thống từ bể trộn nhanh đến máng ra chỉ mất từ **$10$ đến $20\ \text{phút}$** (so với $2.0 - 4.0\ \text{giờ}$ của bể lắng truyền thống), mang lại khả năng ứng phó tức thời với các biến động chất lượng nước đột ngột và tối ưu hóa diện tích cho các nhà máy mở rộng công suất.

##### 5.2.6.3 Shallow-Depth Settling Theory (Hazen & Camp Principles)
###### Hazen's Postulate: Capacity Governed by Plan Area, not Depth
- Xuất phát từ định lý Hazen: Thể tích nước được làm trong trong một đơn vị thời gian phụ thuộc vào diện tích mặt phẳng ngang hứng cặn.
- Nếu đặt thêm các vách ngăn nằm ngang song song bên trong bể, diện tích lắng hữu hiệu sẽ tăng gấp $n$ lần (với $n$ là số vách ngăn).

###### Insertion of Horizontal False Floors: Division of Depth $H$ into $n$ Sub-Basins
- Khi chia chiều cao bể $H$ thành $n$ ngăn mỏng bởi các khay nằm ngang cách nhau khoảng cách $h = H/n$:
  - Diện tích lắng hữu hiệu tổng cộng:
    $$A_{\text{eff}} = n \cdot A_s$$
  - Vận tốc lắng tới hạn của bể giảm đi $n$ lần:
    $$v_{0,\text{new}} = \frac{Q}{n \cdot A_s} = \frac{v_0}{n}$$
  - Hạt cặn chỉ cần rơi một khoảng cách $h$ cực ngắn là đã chạm khay và được coi là lắng thành công.

###### Limitation of Horizontal Trays: Sludge Accumulation and Manual Cleaning Crisis
- *Nhược điểm chí mạng của khay nằm ngang*: Cặn lắng đọng tích tụ rất nhanh trên bề mặt từng khay nằm ngang. Do khoảng cách giữa các khay quá hẹp ($5 - 10\ \text{cm}$), các thiết bị cơ khí cào bùn không thể đưa vào hoạt động, việc súc rửa đòi hỏi phải tháo cạn bể và dùng vòi xịt thủ công, dẫn đến chi phí vận hành bảo trì khổng lồ và không thể tự động hóa liên tục.

##### 5.2.6.4 Inclined Tube and Lamella Plate Settler Geometry & Hydraulics
###### Optimization of Inclination Angle: 60° Self-Cleaning Threshold
- Để khắc phục nhược điểm của khay ngang, các tấm lắng phẳng hoặc khối ống được đặt **nghiêng một góc $\theta$ so with mặt phẳng ngang**.
- Phân tích lực tác dụng lên bông cặn nằm trên mặt nghiêng:
  - Thành phần trọng lực kéo cặn trượt xuống dọc theo bề mặt dốc: $F_s = m \cdot g \cdot \sin\theta$.
  - Lực ma sát chống trượt: $F_f = \mu_{\text{friction}} \cdot m \cdot g \cdot \cos\theta$.
- Để khối cặn có thể **tự trượt liên tục bằng trọng lực (gravitational self-cleaning)** xuống đáy bể mà không cần bất kỳ tác động cơ học nào:
  $$\tan\theta > \mu_{\text{friction}}$$
- Thực nghiệm chứng minh:
  - Nếu $\theta < 45^\circ$: Bông cặn bám dính trên bề mặt, gây nghẹt ống sau vài ngày vận hành.
  - Nếu $\theta = 55^\circ - 60^\circ$: Khối cặn tự động tích tụ thành mảng dày và trượt êm dịu xuống hố thu bùn bên dưới.
  - Nếu $\theta > 60^\circ$: Khả năng tự làm sạch rất tốt nhưng diện tích hình chiếu mặt bằng bị suy giảm nghiêm trọng ($A_{\text{proj}} \propto \cos\theta$).
  - Do đó, **góc nghiêng tiêu chuẩn vàng trong kỹ thuật xử lý nước cấp là $\theta = 60^\circ$**.

###### Honeycomb Square, Hexagonal, and Corrugated Plate Geometries
- Các module lắng tốc độ cao thương mại được chế tạo từ nhựa PVC, ABS hoặc HDPE kháng hóa chất và chống tia UV, với các dạng hình học tiết diện:
  - Dạng ống vuông (Square tubes): Tiết diện $50\ \text{mm} \times 50\ \text{mm}$.
  - Dạng tổ ong lục giác (Hexagonal honeycomb): Cung cấp độ cứng kết cấu cao và tỷ số diện tích trên thể tích lớn nhất.
  - Dạng tấm phẳng lượn sóng (Corrugated lamella plates): Dễ tháo lắp vệ sinh và lắp đặt cho các bể có kích thước lớn.

###### Hydraulic Diameter / Spacing ($w = d_h \approx 50\ \text{mm}$)
- Kích thước tiết diện danh định (hydraulic diameter / perpendicular spacing $w$ hoặc $d_h$) được chuẩn hóa trong khoảng $40 - 60\ \text{mm}$ (thông dụng nhất là $w = 50\ \text{mm} = 0.05\ \text{m}$).
- Khoảng cách này tối ưu hóa giữa hai yếu tố: Đủ nhỏ để duy trì dòng chảy tầng ($Re \ll 500$) và khoảng cách lắng ngắn, nhưng đủ rộng để tránh hiện tượng tắc nghẽn do bùn dính bám.

###### Module Length ($L = 1.0 - 2.0\ \text{m}$) and Vertical Height ($H_{\text{module}} = L \sin\theta$)
- Chiều dài ống nghiêng dọc theo trục nghiêng thường chọn $L = 1.0 - 2.0\ \text{m}$ (tiêu chuẩn thông dụng $L = 1.0\ \text{m}$ hoặc $1.2\ \text{m}$).
- Chiều cao thẳng đứng của khối module lắng chiếm chỗ trong bể:
  $$H_{\text{module}} = L \cdot \sin\theta = L \cdot \sin(60^\circ) = 0.866 \cdot L$$
  (Ví dụ với ống dài $L = 1.0\ \text{m}$, chiều cao thẳng đứng của tầng lamen là $0.87\ \text{m}$).

##### 5.2.6.5 Countercurrent, Cocurrent, and Crosscurrent Configurations
###### Countercurrent Flow Mechanics: Upward Clarified Fluid vs Downward Sliding Sludge
- **Dòng chảy ngược chiều (Countercurrent Flow)**:
  - Dòng nước thô sau tạo bông đi vào từ đáy bể và dâng ngược lên trên qua các ống nghiêng hướng về máng thu nước bề mặt.
  - Bông cặn lắng xuống đáy ống và trượt dốc ngược chiều với dòng nước đi xuống hố thu bùn đáy.
  - *Ưu điểm*: Cấu hình tự nhiên, dễ bố trí máng thu nước trên mặt và hệ thống cào bùn dưới đáy; là cấu hình **phổ biến nhất (chiếm > 95%)** trong các nhà máy cấp nước đô thị.

###### Cocurrent Flow Mechanics: Co-Directional Fluid and Sludge Trajectories
- **Dòng chảy cùng chiều (Cocurrent Flow)**: Nước và bùn cùng chuyển động đi xuống dọc theo trục ống. Nước trong được thu ở đáy ống lamen, bùn rơi xuống hố thu.
- *Nhược điểm*: Rất khó bố trí kênh thu nước trong ở dưới đáy xen lẫn với vùng chứa bùn.

###### Crosscurrent Flow Mechanics: Horizontal Water Cross-Flow with Vertical Falling Solids
- **Dòng chảy cắt ngang (Crosscurrent Flow)**: Nước chuyển động theo phương ngang qua các tấm nghiêng, cặn lắng trượt theo phương thẳng đứng xuống đáy.
- *Nhược điểm*: Phân bố lưu lượng giữa các tấm không đồng đều, dễ sinh dòng chảy ngắn.

###### Engineering Predominance of Countercurrent Layouts
- Nhờ khả năng phân tách pha độc lập và cấu trúc thủy lực thuận tiện, cấu hình **chảy ngược chiều (Countercurrent)** là tiêu chuẩn thiết kế mặc định cho mọi ứng dụng lắng lamen nước cấp.

##### 5.2.6.6 Yao's Critical Settling Velocity Formulation for Inclined Settlers
###### Detailed Mathematical Derivation of Critical Settling Velocity ($v_0 = \frac{v_s}{\sin\theta + \frac{L}{w}\cos\theta}$)
- K. M. Yao (1970, 1972) thiết lập mô hình toán học giải tích chuyển động của hạt cặn trong kênh lắng nghiêng chảy ngược chiều:
- Xét một kênh nghiêng góc $\theta$ so với phương ngang, chiều dài $L$, khoảng cách vuông góc giữa hai bản là $w$.
- Nước dâng lên dọc theo trục kênh với vận tốc trung bình $v_0$ (tương ứng tải trọng bề mặt trên tiết diện ngang của ống).
- Vận tốc lắng của hạt cặn theo phương thẳng đứng là $v_s$.
- Chiếu vector chuyển động lên hệ trục tọa độ dọc trục kênh ($x$) và vuông góc trục kênh ($y$):
  - Thành phần vận tốc dọc trục: $v_x = v_0 - v_s \sin\theta$.
  - Thành phần vận tốc vuông góc trục: $v_y = -v_s \cos\theta$.
- Thời gian tối đa để hạt cặn rơi từ đỉnh trên của bản nghiêng chạm tới đáy bản dưới (quãng đường $w$):
  $$t_{\text{fall}} = \frac{w}{v_y} = \frac{w}{v_s \cos\theta}$$
- Trong khoảng thời gian $t_{\text{fall}}$ đó, quãng đường hạt bị dòng nước cuốn đi dọc theo trục kênh không được vượt quá chiều dài kênh $L$:
  $$x_{\text{travel}} = v_x \cdot t_{\text{fall}} = (v_0 - v_s \sin\theta) \cdot \left(\frac{w}{v_s \cos\theta}\right) \le L$$
- Biến đổi bất đẳng thức:
  $$\frac{v_0 w}{v_s \cos\theta} - w \tan\theta \le L$$
  $$\frac{v_0 w}{v_s \cos\theta} \le L + w \frac{\sin\theta}{\cos\theta} = \frac{L \cos\theta + w \sin\theta}{\cos\theta}$$
  $$v_0 \le v_s \left(\sin\theta + \frac{L}{w} \cos\theta\right)$$
- Từ đó xác định được **vận tốc tới hạn của dòng chảy trong ống nghiêng** (eq_ch05_019):
$$v_0 = \frac{v_s}{\sin\theta + \frac{L}{w} \cos\theta}$$

###### Minimum Capture Velocity ($v_{s,\min} = v_0 (\sin\theta + \frac{L}{w}\cos\theta)^{-1}$)
- Nghịch đảo phương trình trên cho ta **vận tốc lắng nhỏ nhất của hạt cặn được loại bỏ hoàn toàn 100% ($v_{s,\min}$)**:
$$v_{s,\min} = v_0 \left(\sin\theta + \frac{L}{w} \cos\theta\right)^{-1}$$
- *Ý nghĩa kỹ thuật*: Vì tỷ số hình học $\frac{L}{w} \approx \frac{1.0\ \text{m}}{0.05\ \text{m}} = 20$, với $\theta = 60^\circ$ ($\sin 60^\circ = 0.866, \cos 60^\circ = 0.50$):
  $$\sin\theta + \frac{L}{w} \cos\theta = 0.866 + 20 \times 0.50 = 10.866$$
  Do đó:
  $$v_{s,\min} = \frac{v_0}{10.866} \approx 0.092 \times v_0$$
  Hệ thống module lắng nghiêng có thể giữ lại được những hạt cặn có vận tốc lắng **nhỏ hơn 10 lần** so with vận tốc nước dâng biểu kiến trong ống!

###### Shape Factor $S_c$ Across Cross-Sections (Parallel Plates $S_c=1.0$, Circular Tubes $S_c=4/\pi$, Square Tubes $S_c=11/8$)
- Phương trình trên giả định dòng chảy có profile vận tốc phẳng đồng đều. Trong thực tế, do lực ma sát nhớt, dòng chảy tầng trong ống có phân bố vận tốc dạng parabol. K. M. Yao bổ sung hệ số hình dạng $S_c$ (shape factor):
  $$v_0 = \frac{v_s}{S_c \left(\sin\theta + \frac{L}{w} \cos\theta\right)}$$
  Giá trị của $S_c$ phụ thuộc vào hình học tiết diện:
  - Bản phẳng song song (Parallel plates): $S_c = 1.0$.
  - Ống tròn (Circular tubes): $S_c = \frac{4}{\pi} \approx 1.273$.
  - Ống vuông (Square tubes): $S_c = \frac{11}{8} = 1.375$.

###### Effective Plan Area Projection Formula ($A_{\text{eff}} = N \cdot W \cdot (L\cos\theta + w\sin\theta) \approx N \cdot W \cdot L\cos\theta$)
- Tổng diện tích lắng hiệu dụng tương đương theo phương ngang của một khối gồm $N$ tấm nghiêng song song (eq_ch05_020):
$$A_{\text{eff}} = N \cdot W \cdot (L \cos\theta + w \sin\theta) \approx N \cdot W \cdot L \cos\theta$$
Trong đó:
- $A_{\text{eff}}$: Diện tích lắng hữu hiệu tương đương được tạo ra ($\text{m}^2$).
- $N$: Tổng số lượng tấm nghiêng hoặc vách ống trong khối module.
- $W$: Chiều rộng của tấm nghiêng ($\text{m}$).
- $L$: Chiều dài của tấm dọc theo độ dốc ($\text{m}$).
- $w$: Khoảng cách vuông góc giữa hai tấm ($\text{m}$).
- $\theta$: Góc nghiêng so with mặt phẳng ngang ($60^\circ$).

##### 5.2.6.7 Laminar Flow Verification Inside Settler Channels
###### Axial Velocity Inside Inclined Tubes ($v_{\text{tube}} = \frac{v_0}{\sin\theta}$)
- Vận tốc dòng chảy thực tế chuyển động dọc theo trục của ống nghiêng ($v_{\text{tube}}$) liên hệ với tải trọng bề mặt trên diện tích mặt bằng đặt module ($v_{0,\text{module}}$) theo quan hệ hình học:
  $$v_{\text{tube}} = \frac{v_{0,\text{module}}}{\sin\theta} = \frac{v_{0,\text{module}}}{\sin(60^\circ)} = \frac{v_{0,\text{module}}}{0.866}$$

###### Settler Channel Reynolds Number ($Re_{\text{tube}} = \frac{v_{\text{tube}} d_h}{\nu} \ll 500$)
- Kiểm tra chế độ chảy bên trong ống lắng qua số Reynolds:
  $$Re_{\text{tube}} = \frac{v_{\text{tube}} \cdot d_h}{\nu}$$
  Với vận tốc thiết kế thông thường $v_{\text{tube}} \approx 1.5 - 2.5\ \text{mm/s}$ ($0.0015 - 0.0025\ \text{m/s}$), đường kính thủy lực $d_h = 0.05\ \text{m}$ và độ nhớt $\nu \approx 1.004 \times 10^{-6}\ \text{m}^2/\text{s}$:
  $$Re_{\text{tube}} = \frac{0.002 \times 0.05}{1.004 \times 10^{-6}} \approx 100 \ll 500$$
- *Kết luận*: Dòng chảy bên trong ống lắng nghiêng luôn luôn nằm sâu trong **vùng chảy tầng ổn định (strictly laminar flow)**, triệt tiêu hoàn toàn các dòng xoáy xáo trộn, tạo môi trường cực kỳ êm dịu cho hạt cặn kết tụ và trượt xuống đáy.

###### Entrance Flow Development Length ($L_e = 0.058 \cdot Re \cdot d_h$)
- Chiều dài đoạn chuyển tiếp từ dòng xáo trộn ở miệng ống vào dòng chảy tầng phát triển hoàn toàn (hydrodynamic entrance length):
  $$L_e \approx 0.058 \cdot Re_{\text{tube}} \cdot d_h \approx 0.058 \times 100 \times 0.05\ \text{m} \approx 0.29\ \text{m}$$
- Vì chiều dài ống tiêu chuẩn $L = 1.0 - 1.2\ \text{m}$ lớn hơn nhiều so with $L_e$, phần lớn chiều dài ống ($> 75\%$) hoạt động ở chế độ chảy tầng ổn định hoàn hảo.

---

### 5.3 Engineering Practice, Clarifier Configurations & Design Criteria (Thực tiễn Kỹ thuật, Cấu hình Bể và Tiêu chuẩn Thiết kế)

#### 5.3.1 Clarifier Technology Selection Hierarchy & Hydrodynamic Stability
##### 5.3.1.1 Clarifier Selection Hierarchy for Chemical Floc Clarification
###### Priority Order: (1) Rectangular High-Rate Lamella Modules $\to$ (2) Conventional Long Rectangular Basins $\to$ (3) Ballasted Sand Units
Theo giáo trình kỹ thuật và thực tiễn thiết kế cấp nước hiện đại, thứ tự ưu tiên lựa chọn công nghệ cho quá trình lắng bông cặn keo tụ phèn nhôm/sắt như sau:
1. **Ưu tiên 1 - Bể lắng ngang lắp module tấm nghiêng / ống nghiêng (Rectangular Tank with High-Rate Settler Modules)**: Đạt hiệu quả cao nhất về diện tích, dòng chảy tầng ổn định tuyệt đối, chất lượng nước sau lắng đồng đều, dễ nâng công suất trên nền bể cũ.
2. **Ưu tiên 2 - Bể lắng ngang dài truyền thống (Long Rectangular Sedimentation Basin)**: Độ ổn định thủy lực cao nhất, cấu trúc đơn giản, ít phụ thuộc vào thiết bị cơ khí phức tạp, vận hành bền bỉ trước các biến động chất lượng nước thô.
3. **Ưu tiên 3 - Bể lắng vi cát tốc độ siêu cao (Ballasted Microsand Clarifier - Actiflo®)**: Lựa chọn hàng đầu khi mặt bằng xây dựng bị giới hạn nghiêm ngặt, trạm cấp nước công suất lớn cần thi công nhanh hoặc xử lý nước nguồn có độ đục biến thiên đột ngột theo mùa mưa lũ.

###### Capital Cost, Land Footprint, Chemical Dependency, and Operability Trade-offs
- Bể lắng ngang truyền thống: Chi phí đầu tư xây dựng lớn, tốn diện tích đất, nhưng chi phí vận hành hóa chất và bảo dưỡng cơ khí thấp nhất.
- Bể lắng Lamella: Cân bằng tối ưu giữa chi phí xây dựng, diện tích mặt bằng và độ tin cậy vận hành.
- Bể lắng vi cát: Chi phí thiết bị cao, tiêu tốn thêm vi cát bù hao hụt và polymer trợ lắng, đòi hỏi trình độ tự động hóa và tay nghề vận hành cao.

##### 5.3.1.2 Solids-Contact / Sludge Blanket Clarifiers (Bể Lắng Tiếp Xúc / Bể Lắng Lớp Bùn Lơ Lửng)
###### Process Principle: Internal Sludge Recirculation & Crystal Seeding for Softening / High Turbidity
- Bể lắng tiếp xúc chất rắn (Solids-Contact Clarifiers / Reactor Clarifiers) tích hợp cả 3 công đoạn: trộn nhanh, tạo bông và lắng trong cùng một công trình hình tròn duy nhất.
- Nước thô đi vào được trộn ngay với một lượng bùn đã lắng được tuần hoàn liên tục từ đáy bể. Lớp bùn tuần hoàn đóng vai trò các hạt nhân kết tinh (crystal seed nuclei), làm tăng tốc độ tạo mầm tinh thể trong quá trình khử độ cứng bằng vôi - soda, giúp phản ứng hóa học diễn ra nhanh chóng và triệt để hơn.

###### Mechanical Reactor Clarifiers (Accelator Technology): Central Impeller Draft Tube & Sludge Concentrator
- Thiết bị Accelator (Infilco Degrémont) sử dụng cánh khuấy tuabin trung tâm gắn trong ống côn dẫn dòng (draft tube). Tuabin vừa tạo dòng tuần hoàn bùn nội bộ từ đáy lên vùng phản ứng bậc 1, vừa đẩy nước sang vùng làm trong bên ngoài qua lớp màng bùn lơ lửng.

###### Pulsator Clarifiers (Degrémont Technology): Vacuum Chamber Intermittent Pulsing & Sludge Blanket Expansion
- Bể lắng xung Pulsator (Degrémont) sử dụng một buồng chân không trung tâm kết hợp quạt hút gió. Nước được hút dâng cao trong buồng chân không, sau đó van xả khí tự động mở làm khối nước tụt nhanh xuống, tạo xung lực thủy lực đẩy nước đồng đều qua hệ thống ống đục lỗ dưới đáy bể. Xung lực này làm lớp đệm bùn dâng lên rồi chùng xuống nhịp nhàng, hoạt động như một tầng lọc bùn lơ lửng (sludge blanket filtration) giữ lại các bông cặn mịn.

###### Operational Sensitivity: Alum Floc Failure Mechanisms (Vulnerability to Shock Loads and Sludge Bed Washout)
- **Cảnh báo kỹ thuật quan trọng**: Các bể lắng tiếp xúc chất rắn và bể lắng xung Pulsator **không được khuyến cáo ưu tiên cho quá trình lắng bông phèn nhôm** trong xử lý nước mặt vì các lý do sau:
  1. *Độ nhạy nhiệt độ cực lớn*: Chênh lệch nhiệt độ nước thô chỉ từ $0.5^\circ\text{C}$ sẽ phá vỡ hoàn toàn trạng thái lơ lửng ổn định của lớp màng bùn, gây dòng đối lưu xé toang màng bùn.
  2. *Dễ mất ổn định khi sốc tải*: Khi lưu lượng nước hoặc độ đục tăng đột ngột, toàn bộ lớp màng bùn nhẹ của phèn nhôm bị cuốn trôi lên máng tràn (blanket washout), làm tê liệt hoàn toàn các bể lọc cát hạ nguồn.
  3. Chỉ nên áp dụng công nghệ này cho quá trình làm mềm vôi (nơi cặn $\text{CaCO}_3$ nặng, đặc và ổn định) hoặc nguồn nước thô có độ đục và nhiệt độ quanh năm rất ổn định.

##### 5.3.1.3 Thermal Stratification & Density Currents Sensitivity
###### Micro-Temperature Gradient Vulnerability: Failure at $\Delta T \ge 0.5^\circ\text{C}$
- Nước có khối lượng riêng biến thiên phi tuyến theo nhiệt độ. Khi nhiệt độ nước thô cấp vào bể lắng chênh lệch so với khối nước hiện hữu trong bể một khoảng:
  $$\Delta T \ge 0.5^\circ\text{C}$$
  chênh lệch khối lượng riêng $\Delta \rho \approx 0.1 - 0.2\ \text{kg/m}^3$ xuất hiện, đủ lớn để vượt qua động năng của dòng chảy ngang và sinh ra hiện tượng **phân tầng nhiệt và dòng chảy trọng lực (density currents)**.

###### Warm Influent Buoyancy Plumes (Surface Short-Circuiting)
- Nếu nước thô ấm hơn nước trong bể ($\Delta T > 0$): Nước thô có khối lượng riêng nhỏ hơn, lập tức nổi lên mặt thoáng tạo thành một lớp dòng chảy mặt mỏng di chuyển với vận tốc cực lớn thẳng tới máng tràn (short-circuiting). Thời gian lưu thực tế bị rút ngắn từ 3 giờ xuống chỉ còn 15 - 20 phút, cặn không kịp lắng và bị cuốn toàn bộ ra ngoài.

###### Cold Influent Plunging Density Currents (Bottom Scouring Cascades)
- Nếu nước thô lạnh hơn nước trong bể ($\Delta T < 0$): Nước thô nặng hơn lập tức chìm thẳng xuống đáy bể ngay sau vách vào, di chuyển sát sàn đáy như một thác nước ngầm, xới tung lớp bùn cặn đã lắng và kéo bùn trào ngược lên máng thu nước.

##### 5.3.1.4 Circular vs. Rectangular Clarifier Comparative Hydrodynamics
###### Center-Feed Circular Radial Clarifiers: Decelerating Radial Vectors, Waterfall Inflow, Wind Churning, Dye Test Instability
- Bể lắng tròn dòng chảy xuyên tâm từ tâm ra thành (Center-Feed Circular Clarifier) có các nhược điểm thủy lực cố hữu:
  - *Vector vận tốc giảm dần theo bán kính*: Vận tốc nước rất lớn ở ống trung tâm ($v \propto 1/r$) và giảm dần về phía thành bể, dễ gây xáo trộn phá vỡ bông cặn ở cửa vào.
  - *Hiện tượng thác nước chìm (Waterfall effect)*: Dòng nước từ giếng phân phối trung tâm thường chìm thẳng xuống đáy do mật độ cặn cao, tạo dòng xoáy hoàn lưu cuộn ngược lên máng tràn ngoài chu vi.
  - *Kém ổn định trước gió*: Mặt thoáng hình tròn rộng dễ bị gió xoáy tạo sóng hoàn lưu bề mặt. Các thí nghiệm bơm chất chỉ thị màu (dye tracer test) luôn ghi nhận dòng chảy ngắn trầm trọng và nhiều vùng nước chết (dead zones). Do đó, **bể lắng tròn tâm không được khuyến cáo cho lắng bông phèn nhôm nhẹ**.

###### Peripheral-Feed Circular Clarifiers: Spiral Hydraulics & Hydraulic Evaluation
- Bể lắng tròn nạp nước chu vi (Peripheral-Feed): Nước vào từ máng ngoài chu vi và thu nước ở tâm hoặc máng tròn trung gian. Cấu hình này cải thiện độ ổn định thủy lực hơn so with nạp tâm, nhưng cấu tạo cơ khí phức tạp.

###### Long Rectangular Basins: Plug Flow Hydrodynamic Stability, Froude Number Superiority, Ease of Common-Wall Construction
- Bể lắng ngang chữ nhật dài (Long Rectangular Basin) là cấu hình có độ tin cậy thủy lực cao nhất:
  - Dòng chảy tiếp cận trạng thái dòng chảy nút lý tưởng (plug flow), hạn chế tối đa dòng chảy ngắn.
  - Dễ dàng kiểm soát số Froude ($Fr$) để đảm bảo dòng chảy ổn định.
  - Xây dựng dạng các modul song song chung vách (common-wall construction), tiết kiệm đáng kể chi phí cốp pha và diện tích đất so với các bể tròn độc lập.

#### 5.3.2 Rectangular Horizontal-Flow Sedimentation Basin Architecture
##### 5.3.2.1 Basin Aspect Ratios & Geometric Proportions
###### Length-to-Width Ratio ($L:W \ge 4:1$, Typically $4:1 - 6:1$, up to $8:1$)
- Tỷ số chiều dài trên chiều rộng ($L:W$) là thông số hình học quyết định tính ổn định của dòng chảy nút.
- Bắt buộc tuân thủ:
  $$\frac{L}{W} \ge 4:1 \quad (\text{dải khuyến nghị tiêu chuẩn } 4:1 - 6:1,\ \text{tối đa } 8:1)$$
- Tỷ số $L:W$ lớn giúp triệt tiêu các xoáy cuộn hai bên thành bể, ngăn chặn hiện tượng dòng chảy đi tắt và loại bỏ hoàn toàn các góc chết thủy lực.

###### Active Water Depth ($H = 3.0 - 5.0\ \text{m}$, Typically $3.5 - 4.5\ \text{m}$)
- Chiều sâu nước lắng hữu ích (Side Water Depth - SWD):
  $$H = 3.0 - 5.0\ \text{m} \quad (\text{phổ biến nhất } 3.5 - 4.5\ \text{m})$$
- Chiều sâu này phân chia không gian bể thành:
  - Lớp nước trong bề mặt: $0.5 - 1.0\ \text{m}$.
  - Vùng lắng chính: $1.5 - 2.5\ \text{m}$.
  - Vùng tích lũy bùn chuyển tiếp: $0.5 - 1.0\ \text{m}$.

###### Length-to-Depth Ratio ($L:H = 15:1 - 25:1$)
- Tỷ lệ giữa chiều dài và chiều sâu bể phải duy trì trong khoảng:
  $$\frac{L}{H} = 15:1 - 25:1$$
  để đảm bảo các đường dòng nằm ngang ổn định dọc theo chiều dài chuyển động của nước.

###### Freeboard Allowance ($0.3 - 0.6\ \text{m}$)
- Chiều cao an toàn từ mặt nước cao nhất đến đỉnh thành bê tông bể (khoảng không dự phòng chống tràn do sóng gió hoặc dao động thủy lực):
  $$H_{\text{freeboard}} = 0.3 - 0.6\ \text{m} \quad (\text{tiêu chuẩn chọn } 0.5\ \text{m})$$

##### 5.3.2.2 Inlet Energy Dissipation & Flow Distribution Structures
###### Influent Flume and Submerged Target Baffles
- Nước từ bể tạo bông dẫn vào kênh phân phối chung. Tại cửa vào từng bể lắng, bố trí các tấm chắn triệt tiêu động năng (submerged target baffles) đặt đối diện miệng ống vào cách $0.3 - 0.5\ \text{m}$ để bẻ gãy tia nước vận tốc lớn ($v > 0.5\ \text{m/s}$).

###### Perforated Distribution Baffle Walls: Orifice Port Sizing ($d = 50 - 150\ \text{mm}$)
- Cách cửa vào $1.0 - 2.0\ \text{m}$, xây dựng một **vách ngăn phân phối đục lỗ (perforated baffle wall)** trải rộng trên toàn bộ mặt cắt ngang bể.
- Lỗ đục hình tròn hoặc khe chữ nhật có đường kính danh định:
  $$d_{\text{port}} = 50 - 150\ \text{mm} \quad (\text{thông dụng } 75 - 100\ \text{mm})$$
- Các lỗ được bố trí so le hình hoa mai, phân bố đều từ $0.5\ \text{m}$ dưới mặt nước đến $0.5 - 1.0\ \text{m}$ cách đáy bể (để không thổi vào vùng bùn).

###### Port Discharge Velocity ($v_{\text{port}} = 0.15 - 0.30\ \text{m/s}$): Preventing Floc Shearing while Maintaining Orifice Head Loss ($10 - 25\ \text{mm}$)
- Vận tốc dòng nước qua lỗ vách ngăn:
  $$v_{\text{port}} = 0.15 - 0.30\ \text{m/s}$$
- *Ràng buộc kỹ thuật hai chiều*:
  - Không được chọn $v_{\text{port}} < 0.15\ \text{m/s}$: Vì tổn thất áp lực qua lỗ quá nhỏ ($h_L < 5\ \text{mm}$), không đủ sức ép để phân chia lưu lượng đồng đều trên toàn bộ chiều rộng bể.
  - Không được chọn $v_{\text{port}} > 0.30\ \text{m/s}$: Vì gradient vận tốc qua lỗ quá lớn sẽ gây ứng suất cắt xé nát các bông cặn nhôm/sắt mỏng manh vừa tạo thành từ bể tạo bông.
- Tổn thất áp lực qua vách ngăn tối ưu nằm trong khoảng $h_L = 10 - 25\ \text{mm}$ cột nước.

###### Spacing and Submergence Depth of Perforations
- Tổng diện tích mở của các lỗ đục chiếm từ $10\%$ đến $20\%$ tổng diện tích mặt cắt ướt ngang của bể ($A_{\text{open}} = (0.10 - 0.20) \times W \times H$).

##### 5.3.2.3 Flow Conditioning & Surface Wind Protection
###### Intermediate Vertical Cross Baffles to Suppress Internal Wind-Driven Recirculation Gyres
- Đối with các bể lắng dài ngoài trời ($L > 40\ \text{m}$) không có mái che, gió mạnh thổi xuôi chiều sẽ tạo sóng kéo dòng nước mặt di chuyển nhanh về phía máng xả, sinh ra dòng hoàn lưu ngầm dưới đáy chảy ngược lại phía cửa vào.
- Để triệt tiêu vòng hoàn lưu này, kỹ sư bố trí các **vách ngăn ngang chắn gió (cross baffles)** nhô lên trên mặt nước và ngập sâu xuống nước khoảng $0.5 - 1.0\ \text{m}$, ngắt mặt bể thành các khoang nhỏ để chắn gió.

###### Basin Floor Slope ($1:600$ to $1:50$ toward Influent Sludge Hopper)
- Đáy bể lắng được đổ bê tông tạo dốc hướng về phía hố thu bùn đặt ở đầu bể:
  - Khi có máy cào bùn gạt liên tục: Độ dốc đáy tối thiểu $1:600$ đến $1:100$ ($0.17\% - 1.0\%$).
  - Khi xả bùn thủy lực tự do không có máy gạt: Độ dốc đáy bắt buộc $\ge 1:50$ ($2.0\%$).

#### 5.3.3 Effluent Launder Systems & V-Notch Weir Hydraulics
##### 5.3.3.1 Effluent Launder Configuration: End Wall vs. Finger Launders
###### Single End-Wall Weir Vulnerability: Extreme Upward Suction Currents
- Nếu chỉ bố trí một vách tràn thu nước duy nhất đặt ngang ở bức tường cuối bể, tổng chiều dài tràn chỉ bằng chiều rộng bể ($L_w = W$).
- Khi đó, toàn bộ lưu lượng nước $Q$ buộc phải thoát qua một mặt cắt rất hẹp. Vận tốc dòng nước dâng tiếp cận (approach upward velocity) tại góc cuối bể sẽ tăng vọt, tạo thành một luồng xoáy hút cực mạnh kéo thẳng các bông cặn đang lơ lửng ở tầng dưới vượt qua vách tràn thoát ra ngoài.

###### Multi-Trough Longitudinal Finger Launders: Coverage of Downstream 20% - 33% of Basin Length
- Giải pháp kỹ thuật bắt buộc: Bố trí hệ thống **máng răng cưa ngón tay đặt dọc theo chiều dài bể (longitudinal finger launders)**.
- Các máng thu nước nhánh đặt song song nhau vươn ngược vào trong vùng lắng, phủ từ $20\%$ đến $33\%$ (khoảng $1/5$ đến $1/3$) chiều dài cuối bể.
- Nước tràn vào máng từ cả hai phía thành máng (double-sided weirs), giúp tăng tổng chiều dài tràn hữu hiệu lên gấp $4 - 8\ \text{lần}$ chiều rộng bể, phân tán đều dòng thu nước trên một diện tích rộng lớn và triệt tiêu hoàn toàn các dòng hút dâng cục bộ.

###### Lateral Launder Spacing ($S \le 3.0 - 4.0\ \text{m}$)
- Khoảng cách giữa các tim máng thu nước nhánh song song không được vượt quá:
  $$S_{\text{launder}} \le 3.0 - 4.0\ \text{m}$$
  để đảm bảo khoảng cách di chuyển ngang của phần tử nước từ điểm giữa hai máng đến mép tràn là ngắn nhất ($< 2.0\ \text{m}$).

##### 5.3.3.2 Weir Loading Rate (WLR) Design Standards
###### Definition Formula ($\text{WLR} = \frac{Q}{L_w}$)
- Tải trọng thủy lực trên mét dài vách tràn (Weir Loading Rate - WLR) được xác định bằng tỷ số giữa lưu lượng nước qua bể và tổng chiều dài hữu hiệu của vách tràn (eq_ch05_017):
$$\text{WLR} = \frac{Q}{L_w}$$
Trong đó:
- $\text{WLR}$: Tải trọng vách tràn ($\text{m}^3/\text{d}\cdot\text{m}$ hoặc $\text{m}^3/\text{h}\cdot\text{m}$, hoặc đơn vị US Customary $\text{gpd/ft}$).
- $Q$: Lưu lượng nước xử lý qua bể ($\text{m}^3/\text{d}$ hoặc $\text{m}^3/\text{h}$).
- $L_w$: Tổng chiều dài tràn hữu ích của các mép vách tràn ($\text{m}$).

###### Maximum Permissible Limits: Light Alum Floc ($\le 150 - 180\ \text{m}^3/\text{m}\cdot\text{d}$), Dense Floc / Softening ($\le 200 - 250\ \text{m}^3/\text{m}\cdot\text{d}$)
- Giới hạn quy phạm thiết kế nghiêm ngặt:
  - Bông cặn phèn nhôm nhẹ, dễ vỡ:
    $$\text{WLR}_{\text{alum}} \le 150 - 180\ \text{m}^3/\text{m}\cdot\text{d} \quad (6.25 - 7.5\ \text{m}^3/\text{m}\cdot\text{h})$$
  - Bông cặn phèn sắt hoặc kết tủa làm mềm vôi nặng hơn:
    $$\text{WLR}_{\text{heavy}} \le 200 - 250\ \text{m}^3/\text{m}\cdot\text{d} \quad (8.33 - 10.4\ \text{m}^3/\text{m}\cdot\text{h})$$
  - Tiêu chuẩn Ten States Standards quy định: Mức tải tiêu chuẩn không vượt quá $20,000\ \text{gpd/ft}$ ($248\ \text{m}^3/\text{m}\cdot\text{d}$); đối with các bể có máng vươn dài phủ $1/3$ bể, mức tối đa cho phép là $30,000\ \text{gpd/ft}$ ($372\ \text{m}^3/\text{m}\cdot\text{d}$).

###### Updraft Velocity Suppression Criterion ($v_{\text{upward}} < v_s$)
- Cơ sở vật lý của việc khống chế WLR: Giữ cho vận tốc dâng cục bộ của nước tại vùng lân cận máng tràn luôn nhỏ hơn vận tốc lắng của bông cặn nhỏ nhất cần giữ lại:
  $$v_{\text{upward, local}} \ll v_s$$

##### 5.3.3.3 90° Triangular V-Notch Weir Hydraulics & Fabrication Details
###### Kindsvater-Shen / Thomson Discharge Formula ($Q_{\text{notch}} = \frac{8}{15} C_d \sqrt{2g} \tan(\theta/2) H_w^{5/2} \approx 1.38 H_w^{5/2}$)
- Trên thành máng tràn luôn lắp đặt các tấm vách tràn răng cưa tam giác nhọn góc $90^\circ$ (90° V-Notch Weirs).
- Lưu lượng nước chảy qua một khe răng cưa tam giác nhọn được tính toán theo phương trình thủy lực Thomson / Kindsvater-Shen (eq_ch05_018):
$$Q_{\text{notch}} = \frac{8}{15} C_d \sqrt{2g} \tan\left(\frac{\theta}{2}\right) H_w^{5/2}$$
- Với góc đỉnh $\theta = 90^\circ$, ta có $\tan(45^\circ) = 1.0$. Thay gia tốc trọng trường $g = 9.81\ \text{m/s}^2$ và hệ số xả thực nghiệm cho gờ sắc $C_d \approx 0.585$:
  $$Q_{\text{notch}} = \frac{8}{15} (0.585) \sqrt{2 \times 9.81} (1.0) H_w^{5/2} = \frac{8}{15} (0.585) (4.429) H_w^{5/2} \approx 1.38 \cdot H_w^{5/2}$$
Trong đó:
- $Q_{\text{notch}}$: Lưu lượng nước chảy qua một khe răng cưa ($\text{m}^3/\text{s}$).
- $H_w$: Cột nước tràn đo từ đáy chữ V lên mặt nước tĩnh trong bể ($\text{m}$).
- $C_d$: Hệ số lưu lượng của vách tràn gờ sắc ($0.58 - 0.60$).

###### Individual Notch Headloss ($H_w = 25 - 75\ \text{mm}$) and Flow Rating Curve
- Cột nước tràn qua đỉnh chữ V được thiết kế tối ưu trong khoảng:
  $$H_w = 25 - 75\ \text{mm} \quad (0.025 - 0.075\ \text{m})$$
- *Lý do kỹ thuật*:
  - Nếu $H_w < 25\ \text{mm}$: Sức căng bề mặt của nước sẽ làm dòng chảy bám dính vào thành vách, gây sai lệch thủy lực và dòng chảy không đều giữa các răng cưa.
  - Nếu $H_w > 75\ \text{mm}$: Mực nước dâng quá cao làm ngập đỉnh răng cưa hoặc đòi hỏi chiều cao thành máng quá lớn.

###### Mechanical Mounting: Stainless Steel / FRP Weir Plates with Slotted Adjusting Bolts for Laser-Level Alignment
- Tấm vách răng cưa được gia công từ thép không gỉ (Inox 304/316) hoặc nhựa gia cường sợi thủy tinh (FRP) dày $4 - 6\ \text{mm}$.
- Các lỗ bu-lông cố định vào thành bê tông được gia công dạng rãnh trượt ô-van thẳng đứng (slotted holes) kèm đệm cao su EPDM. Thiết kế này cho phép kỹ sư dùng máy cân bằng laser vi chỉnh cao độ đáy chữ V của từng tấm răng cưa trên toàn bộ chiều dài hàng trăm mét với sai số cao độ $\le \pm 1.0\ \text{mm}$, đảm bảo lưu lượng xả qua mọi răng cưa là hoàn toàn đồng nhất.

###### Notch Pitch Spacing ($150 - 300\ \text{mm}$)
- Khoảng cách tim-đến-tim giữa hai đỉnh răng cưa tam giác kề nhau (notch pitch):
  $$P_{\text{notch}} = 150 - 300\ \text{mm} \quad (\text{thông dụng nhất } 200\ \text{mm})$$
- Chiều sâu khe khoét tam giác: $h_{\text{notch}} = 50 - 100\ \text{mm}$.

##### 5.3.3.4 Effluent Collection Trough Channel Hydraulics
###### Spatially Varied Flow with Increasing Discharge
- Dòng chảy bên trong lòng máng thu nước là dòng biến đổi liên tục có lưu lượng tăng dần dọc theo chiều dài máng (spatially varied flow with increasing discharge).
- Mặt nước trong máng dốc dần về phía đầu xả; độ sâu nước ở đầu máng lớn hơn ở cuối máng.

###### Invert Sloping ($1:50$ to $1:100$) and Free-Fall Outfall Criteria
- Đáy máng thu nước được đổ bê tông tạo dốc dốc về kênh thu nước chung:
  $$S_{\text{invert}} = 1:100 - 1:50 \quad (1.0\% - 2.0\%)$$
- Khoảng cách rơi tự do (free-fall clearance) từ đỉnh đáy chữ V xuống mặt nước cao nhất bên trong máng thu tối thiểu phải đạt $0.10 - 0.15\ \text{m}$ để đảm bảo điều kiện xả tràn tự do (free discharge), không bị hiện tượng ngập nước vách tràn (submerged weir).

###### Channel Self-Cleansing Velocity ($v_{\text{channel}} = 0.4 - 0.8\ \text{m/s}$)
- Vận tốc dòng nước chảy bên trong máng thu nhánh và kênh tập trung nước trong:
  $$v_{\text{channel}} = 0.4 - 0.8\ \text{m/s}$$
  Vận tốc này đủ lớn để ngăn ngừa cặn mịn tái lắng đọng trong lòng máng, nhưng không quá lớn để tránh gây tổn thất cột áp thủy lực của toàn nhà máy.

#### 5.3.4 Mechanical Sludge Removal Systems & Hopper Design
##### 5.3.4.1 Classification & Evaluation of Sludge Collection Machinery
###### Comparative Engineering Matrix: Capital Cost, Maintenance, Reliability, Sludge Solids Concentration
Đánh giá so sánh 4 hệ thống thu gom bùn cơ học trong bể lắng xử lý nước cấp:

| Loại Thiết Bị Cào Bùn | Chi Phí Đầu Tư Ban Đầu | Mức Độ Bảo Trì & Độ Tin Cậy | Nồng Độ Bùn Thu Được (% Cặn Khô) | Đánh Giá Mức Độ Phù Hợp Cho Nhà Máy Nước |
|---|---|---|---|---|
| **Cầu cào chuyển động gạt lưỡi cao su** (Traveling Bridge with Squeegees) | Trung bình ($$) | Trung bình; ray trượt và bánh xe cần bảo trì; không có chi tiết chìm dưới nước phức tạp | $1.0 - 2.0\%$ | Phù hợp cho bể lắng ngang chiều dài vừa phải; gom cặn về hố thu đầu bể |
| **Cầu chuyển động gắn bơm hút chìm** (Traveling Bridge with Suction Pumps) | Trung bình - Cao ($$$) | **Rất tốt**; hút trực tiếp bùn từ đáy sàn qua ống hút; ứng suất cắt cực thấp | **$1.5 - 3.0\%$** | **Ưu tiên hàng đầu cho WTP cấp nước**; không làm vỡ bông cặn phèn mỏng manh |
| **Xích cào gạt bùn liên tục** (Chain-and-Flight Composite Scraper) | Thấp - Trung bình ($$) | Trung bình; vật liệu composite phi kim loại chống ăn mòn; cần thay thế guốc trượt sàn | $1.0 - 2.5\%$ | Rất tốt cho bể chữ nhật nhiều tầng, bể rất dài ($> 50\ \text{m}$), hoặc bể ngầm có nắp |
| **Cầu cào quay tâm bể tròn** (Circular Center-Drive Half-Bridge) | Thấp - Trung bình ($$) | Tốt; truyền động quay liên tục ở tâm; cơ cấu cơ khí đơn giản, bền bỉ | $1.5 - 3.5\%$ | Tiêu chuẩn bắt buộc cho bể lắng tròn và bể lắng tiếp xúc chất rắn |

##### 5.3.4.2 Traveling Bridge Sludge Collector Systems
###### Traveling Bridge with Bottom Squeegee Blades: Pushing Sludge to Influent Hopper
- Cầu thép bắc ngang qua chiều rộng bể, di chuyển tịnh tiến xuôi và ngược dọc theo chiều dài bể trên hai ray thép gắn trên đỉnh tường thành.
- Khi di chuyển xuôi về phía đầu bể (influent end), các lưỡi gạt cao su (squeegee blades) hạ xuống sát đáy để đẩy từ từ lớp bùn dồn vào các hố thu bùn hình chóp. Khi quay ngược lại, lưỡi gạt được nâng lên khỏi đáy để không xáo trộn bùn.

###### Traveling Bridge with Submerged Suction Pumps (Header/Air-Lift): Direct Bottom Extraction, Zero Turbulence, Best for Fragile Alum Flocs
- Cấu hình ưu tiên số 1 cho nhà máy nước đô thị: Trên cầu gắn cụm bơm bùn chìm hoặc hệ thống ống hút chân không/bơm khí ép (air-lift).
- Các ống hút phân nhánh vươn thẳng xuống sát đáy bể, tận cùng bằng các đầu hút dẹt. Khi cầu di chuyển chậm, bơm hút trực tiếp lớp bùn tại chỗ đưa lên máng dẫn bùn xả bên thành bể.
- *Ưu điểm vượt trội*: Không đẩy dồn khối bùn đi xa (tránh làm phân rã bông cặn phèn), không gây xáo trộn thủy lực tầng nước bên trên, nồng độ bùn hút ra đậm đặc và đồng đều.

###### Bridge Travel Velocity Limits ($v_{\text{bridge}} = 0.3 - 1.5\ \text{m/min}$, Typically $0.6 - 1.0\ \text{m/min}$)
- Vận tốc di chuyển của cầu cào được khống chế rất chậm:
  $$v_{\text{bridge}} = 0.3 - 1.5\ \text{m/min} \quad (0.005 - 0.025\ \text{m/s},\ \text{chuẩn } 0.6 - 1.0\ \text{m/min})$$
  để chuyển động của khung cầu và thanh giằng ngập nước không tạo ra các xoáy cuộn làm xới cặn đã lắng.

##### 5.3.4.3 Continuous Chain-and-Flight Scraper Collectors
###### Drive Machinery: Explosion-Proof Gearmotors, Drive Chains, Sprockets, Shear Pin Hubs
- Hệ thống xích cào bao gồm động cơ giảm tốc đặt trên cạn ở đầu bể, truyền động qua trục quay và hai dải xích vòng khép kín chạy dọc hai bên đáy bể qua các đĩa xích (sprockets). Trục truyền động có khớp an toàn chốt cắt (shear pin) hoặc cảm biến quá tải mô-men xoắn để tự động ngắt điện khi xích bị kẹt rác.

###### Non-Metallic Construction: Composite Plastic Chains, Fiberglass (FRP) Flights at 3 m Spacing
- Công nghệ vật liệu hiện đại sử dụng $100\%$ phi kim loại:
  - Dây xích: Đúc bằng nhựa kỹ thuật acetal hoặc polyeste gia cường độ bền kéo cao, không bị ăn mòn rỉ sét trong môi trường nước có hóa chất clo và phèn.
  - Thanh gạt (flights): Chế tạo bằng nhựa gia cường sợi thủy tinh (FRP) dạng hình hộp rỗng chữ nhật chịu uốn, chiều dài bằng chiều rộng khoang bể ($W = 4 - 10\ \text{m}$).
  - Khoảng cách bố trí thanh gạt dọc theo dây xích:
    $$S_{\text{flight}} = 3.0\ \text{m}$$

###### Bottom Rails and Wear Shoes (UHMW-PE on Cast Floor T-Rails)
- Dưới đáy thanh gạt gắn các guốc trượt (wear shoes) bằng vật liệu nhựa polyethylene siêu cao phân tử (UHMW-PE) có hệ số ma sát cực thấp. Các guốc này trượt trên các thanh ray thép không gỉ hoặc ray nhựa định hình chữ T đúc chìm cố định trong sàn bê tông đáy bể.

###### Flight Scraping Velocity ($v_{\text{flight}} = 0.3 - 0.9\ \text{m/min}$, i.e., $5 - 15\ \text{mm/s}$)
- Vận tốc kéo thanh gạt chuyển động liên tục dưới đáy sàn:
  $$v_{\text{flight}} = 0.3 - 0.9\ \text{m/min} \quad (5 - 15\ \text{mm/s})$$
  Chuyển động êm ái, liên tục đẩy lớp bùn đáy dồn dần về hố thu cặn ở đầu bể với độ xáo trộn nước bằng không.

##### 5.3.4.4 Circular Clarifier Rotating Bridge Collectors
###### Central Center-Drive Half-Bridge Scraper with Logarithmic Spiral Blades
- Bán cầu cào quay (Half-Bridge) xoay quanh trụ xoay trung tâm với chu kỳ quay từ $1$ đến $3\ \text{vòng/giờ}$.
- Dưới đáy gắn các cánh gạt bùn có biên dạng đường xoắn ốc logarit (logarithmic spiral blades) hoặc góc nghiêng $30^\circ - 45^\circ$, đẩy dồn liên tục lớp bùn đáy hướng tâm về hố thu cặn tròn ở trung tâm đáy bể.

###### Bottom Cone Hopper Sizing and Underflow Drawoff Line
- Đáy bể lắng tròn được đổ dốc hình nón về tâm với độ dốc $1:12$ đến $1:10$ ($8\% - 10\%$). Tại tâm bố trí hố thu bùn hình nón cụt; đường ống rút bùn xả đáy bằng gang dẻo/thép chôn ngầm dưới đáy dẫn bùn về trạm bơm bùn.

##### 5.3.4.5 Bottom Sludge Collection Hopper Construction
###### Pyramidal Hopper Geometry at Influent End of Basin
- Tại đầu vào của bể lắng ngang (nơi tích tụ $> 70\%$ tổng lượng cặn của bể), bố trí từ 1 đến 3 hố thu cặn hình kim tự tháp cụt (pyramidal sludge hoppers) nằm ngang song song theo chiều rộng bể.

###### Wall Slope Angle ($\theta \ge 45^\circ - 60^\circ$): Preventing Sludge Hang-up and Slumping Failure
- Thành vách bê tông nghiêng của hố thu bùn bắt buộc phải có góc nghiêng rất dốc:
  $$\theta_{\text{hopper}} \ge 45^\circ - 60^\circ \quad (\text{đối với bùn phèn nhôm ưu tiên } \ge 55^\circ - 60^\circ)$$
- *Ý nghĩa kỹ thuật*: Nếu vách hố thu bùn thoải ($\theta < 45^\circ$), bùn keo tụ dính ướt sẽ bám chặt vào vách bê tông (sludge hang-up/bridging); khi mở van xả, nước phía trên sẽ bị hút xuyên tâm tạo thành lỗ rỗng hình phễu (rat-holing) kéo nước trong ra ngoài trong khi lớp bùn dày vẫn kẹt lại trên vách.

###### Telescoping Sludge Valve / Automated Pneumatic Diaphragm Blowoff Assemblies
- Cơ cấu xả bùn hố thu:
  - Sử dụng **Van lồng xả bùn điều chỉnh cao độ (Telescoping Valve)**: Đặt trong giếng xả bùn hở; điều chỉnh ống trượt lên xuống để xả bùn bằng áp lực thủy tĩnh tự nhiên, cho phép người vận hành quan sát trực quan độ đậm đặc của dòng bùn xả.
  - Hoặc sử dụng van xả đáy tự động điều khiển khí nén/điện (Pneumatic knife gate valve) lập trình đóng mở định kỳ theo thời gian bằng PLC.

###### Sludge Hopper Dewatering and Flush Lines
- Tại đáy hố thu luôn lắp đặt đường ống cấp nước rửa áp lực cao để súc rửa định kỳ, chống tắc nghẽn đường ống hút bùn.

---

### 5.4 Comprehensive Engineering Design Criteria & Standards Reference (Bảng Thông số Thiết kế và Quy chuẩn Tiêu chuẩn)

#### 5.4.1 Master Design Parameters Reference Table
##### 5.4.1.1 Surface Overflow Rates, Detention Times, and Depths Across Clarifier Types
Bảng tổng hợp chi tiết 27 thông số thiết kế kỹ thuật cốt lõi của các công trình lắng trong kỹ thuật xử lý nước cấp (đối chiếu slide bài giảng và quy chuẩn hiện hành):

| TT | Tên Thông Số Kỹ Thuật Thiết Kế | Ký Hiệu | Dải Giá Trị Khuyến Nghị | Đơn Vị Đo | Công Trình / Thiết Bị Áp Dụng | Ý Nghĩa Kỹ Thuật & Chỉ Dẫn Thiết Kế |
|---|---|---|---|---|---|---|
| 1 | Tải trọng bề mặt bể lắng ngang truyền thống (Phèn nhôm) | $\text{SOR}_{\text{alum}}$ | $20 - 40\ (0.8 - 1.7)$ | $\text{m}^3/\text{m}^2\cdot\text{d}\ (\text{m/h})$ | Bể lắng ngang chữ nhật | Tải trọng thủy lực tiêu chuẩn cho bông cặn keo tụ phèn nhôm nước mặt. |
| 2 | Tải trọng bề mặt bể lắng ngang truyền thống (Phèn sắt) | $\text{SOR}_{\text{iron}}$ | $25 - 45\ (1.0 - 1.9)$ | $\text{m}^3/\text{m}^2\cdot\text{d}\ (\text{m/h})$ | Bể lắng ngang chữ nhật | Áp dụng cho bông cặn hydroxit sắt nặng hơn và kết tủa khử Fe/Mn. |
| 3 | Tải trọng bề mặt bể lắng tròn truyền thống | $\text{SOR}_{\text{circular}}$ | $25 - 35\ (1.0 - 1.5)$ | $\text{m}^3/\text{m}^2\cdot\text{d}\ (\text{m/h})$ | Bể lắng tròn nạp tâm | Khống chế thấp hơn bể ngang do bất ổn định thủy lực xuyên tâm. |
| 4 | Tải trọng bề mặt bể lắng tiếp xúc chất rắn / Bùn lơ lửng | $\text{SOR}_{\text{soften}}$ | $40 - 80\ (1.7 - 3.3)$ | $\text{m}^3/\text{m}^2\cdot\text{d}\ (\text{m/h})$ | Bể lắng tiếp xúc / Reactor clarifier | Áp dụng cho kết tủa làm mềm vôi ($\text{CaCO}_3$) và nước thô độ đục cao. |
| 5 | Tải trọng bề mặt module lắng tấm / ống nghiêng (Lamella) | $\text{SOR}_{\text{lamella}}$ | $80 - 150\ (3.3 - 6.25)$ | $\text{m}^3/\text{m}^2\cdot\text{d}\ (\text{m/h})$ | Bể lắng Lamella nghiêng $60^\circ$ | Tính trên diện tích mặt bằng chứa module; tăng công suất gấp 4 lần. |
| 6 | Tải trọng bề mặt bể lắng vi cát tốc độ siêu cao (Actiflo®) | $\text{SOR}_{\text{ballasted}}$ | $150 - 250\ (6.25 - 10.4)$ | $\text{m}^3/\text{m}^2\cdot\text{d}\ (\text{m/h})$ | Bể lắng vi cát Actiflo® | Tải trọng siêu cao nhờ tỷ trọng vi cát $\text{SG} = 2.65$; tối đa tới $300\ \text{m/h}$. |
| 7 | Tải trọng bể tuyển nổi khí hòa tan (DAF) | $\text{SOR}_{\text{DAF}}$ | $120 - 240\ (5.0 - 10.0)$ | $\text{m}^3/\text{m}^2\cdot\text{d}\ (\text{m/h})$ | Bể tuyển nổi bọt khí mịn DAF | Tách các bông cặn nhẹ chứa nhiều tảo, chất hữu cơ và độ màu cao. |
| 8 | Thời gian lưu nước bể lắng ngang truyền thống | $t_0$ | $2.0 - 4.0\ (120 - 240)$ | $\text{hours (min)}$ | Bể lắng ngang chữ nhật | Cung cấp đủ thời gian tĩnh lặng cho bông cặn rơi chạm đáy. |
| 9 | Thời gian lưu nước bể lắng tấm/ống nghiêng | $t_{0,\text{lamella}}$ | $15 - 45\ (0.25 - 0.75)$ | $\text{minutes (h)}$ | Bể lắng lamen tốc độ cao | Rút ngắn thể tích bể từ $70\%$ đến $80\%$ so với bể truyền thống. |
| 10 | Thời gian lưu nước bể lắng vi cát Actiflo® | $t_{0,\text{ballasted}}$ | $10 - 20$ | $\text{minutes}$ | Toàn bộ cụm bể Actiflo® | Chu trình xử lý siêu nhanh từ ngăn trộn nhanh đến máng tràn. |
| 11 | Tải trọng vách tràn máng răng cưa (Bông phèn nhôm) | $\text{WLR}_{\text{alum}}$ | $\le 150 - 180$ | $\text{m}^3/\text{m}\cdot\text{d}$ | Máng răng cưa ngón tay | Khống chế nghiêm ngặt để chống dòng hút dâng cuốn trôi bông cặn. |
| 12 | Tải trọng vách tràn máng răng cưa (Bông nặng / Làm mềm) | $\text{WLR}_{\text{heavy}}$ | $\le 200 - 250$ | $\text{m}^3/\text{m}\cdot\text{d}$ | Máng răng cưa ngón tay | Cho phép áp dụng đối with kết tủa làm mềm nặng và bền cơ học. |
| 13 | Tỷ số chiều dài trên chiều rộng bể lắng ngang | $L:W$ | $\ge 4:1\ (4:1 - 6:1,\ \le 8:1)$ | không thứ nguyên | Bể lắng ngang chữ nhật | Đảm bảo thủy lực dòng chảy nút, triệt tiêu góc chết và dòng đi tắt. |
| 14 | Chiều sâu nước lắng hữu ích trong bể ngang | $H$ | $3.0 - 5.0\ (3.5 - 4.5)$ | $\text{m}$ | Vùng lắng bể chữ nhật | Bao gồm tầng nước trong, tầng lắng cặn và tầng gom bùn. |
| 15 | Tỷ số chiều dài trên chiều sâu bể lắng ngang | $L:H$ | $15:1 - 25:1$ | không thứ nguyên | Hình học bể lắng ngang | Duy trì các đường dòng nằm ngang ổn định dọc chiều dài bể. |
| 16 | Vận tốc dòng chảy ngang trung bình trong bể | $v_h$ | $0.15 - 0.90\ (2.5 - 15)$ | $\text{m/min}\ (\text{mm/s})$ | Mặt cắt ướt vùng lắng | Phải nhỏ hơn nhiều so with vận tốc xới cặn ($v_{\text{scour}}$). |
| 17 | Góc nghiêng module tấm / ống lắng lamen | $\theta$ | $55 - 60\ (\text{chuẩn } 60)$ | độ ($^\circ$) | Khối tấm/ống nghiêng | Góc tối ưu để cặn tự trượt dốc liên tục bằng trọng lực. |
| 18 | Đường kính thủy lực / Khoảng cách bản lamen | $w\ (d_h)$ | $40 - 60\ (\text{chuẩn } 50)$ | $\text{mm}$ | Tiết diện ống/tấm lamen | Tối ưu giữa dòng chảy tầng ($Re \ll 500$) và chống tắc nghẹt bùn. |
| 19 | Chiều dài module ống lắng nghiêng | $L_{\text{tube}}$ | $1.0 - 2.0\ (\text{chuẩn } 1.0)$ | $\text{m}$ | Chiều dài dọc trục ống | Chiều cao thẳng đứng tương ứng $H_{\text{module}} = L \sin(60^\circ) = 0.87\ \text{m}$. |
| 20 | Kích thước hạt vi cát gia trọng (Actiflo®) | $d_{\text{sand}}$ | $20 - 200\ (80 - 130)$ | $\mu\text{m}$ | Cát thạch anh vi mịn | Đủ nặng để lắng nhanh, đủ nhỏ để tách qua xyclon thủy lực. |
| 21 | Tỷ trọng hạt vi cát thạch anh | $\text{SG}_{\text{sand}}$ | $2.50 - 2.65$ | không thứ nguyên | Vi cát hoàn lưu | Tăng tỷ trọng bông cặn hỗn hợp gấp nhiều lần so with bông thường. |
| 22 | Tỷ trọng bông cặn keo tụ phèn nhôm | $\text{SG}_{\text{alum}}$ | $1.001 - 1.005$ | không thứ nguyên | Bông cặn $Al(OH)_3$ | Rất nhẹ do chứa tới $99\%$ nước liên kết trong cấu trúc xốp. |
| 23 | Tỷ trọng kết tủa làm mềm vôi ($\text{CaCO}_3$) | $\text{SG}_{\text{lime}}$ | $1.002 - 1.010$ | không thứ nguyên | Kết tủa tinh thể vôi | Tinh thể khoáng đặc, vận tốc lắng cao hơn bông nhôm. |
| 24 | Chênh lệch nhiệt độ tối đa chống phân tầng | $\Delta T_{\max}$ | $< 0.5$ | $^\circ\text{C}$ | Thủy lực dòng chảy vào bể | Chênh lệch $\ge 0.5^\circ\text{C}$ sẽ gây dòng chảy ngầm đối lưu mật độ. |
| 25 | Vận tốc nước qua lỗ vách phân phối vào | $v_{\text{port}}$ | $0.15 - 0.30$ | $\text{m/s}$ | Vách ngăn đục lỗ vùng vào | Đảm bảo tổn thất $10 - 25\ \text{mm}$ để chia đều dòng mà không vỡ bông. |
| 26 | Vận tốc di chuyển của cầu cào bùn | $v_{\text{bridge}}$ | $0.3 - 1.5\ (0.6 - 1.0)$ | $\text{m/min}$ | Xe cầu cào chuyển động | Tốc độ chậm chống xáo trộn bùn đã lắng. |
| 27 | Độ dốc thành hố thu cặn đáy bể | $\theta_{\text{hopper}}$ | $45 - 60\ (\ge 55 - 60)$ | độ ($^\circ$) | Hố thu bùn hình chóp | Đảm bảo bùn tự trượt xuống đáy van xả, chống nghẽn bùn vách. |

##### 5.4.1.2 Hydrodynamic Stability Criteria: Reynolds and Froude Numbers
###### Settling Basin Reynolds Number ($Re_{\text{basin}} = \frac{v_h R_h}{\nu} < 20,000$, preferably $< 10,000$)
- Số Reynolds của dòng chảy trong bể lắng xác định bằng bán kính thủy lực $R_h$ của mặt cắt ướt ngang:
  $$R_h = \frac{A_x}{P} = \frac{W \cdot H}{W + 2H}$$
  $$Re_{\text{basin}} = \frac{v_h \cdot R_h}{\nu}$$
- Do mặt cắt bể rất lớn ($W \approx 10\ \text{m}, H \approx 4\ \text{m}$), dòng chảy trong bể lắng ngang đô thị không thể đạt trạng thái chảy tầng ($Re < 500$) như trong ống dẫn nhỏ. Tiêu chuẩn ổn định thủy lực cho phép dòng chảy trong vùng chuyển tiếp:
  $$Re_{\text{basin}} < 20,000 \quad (\text{tối ưu khuyến nghị } < 10,000)$$

###### Settling Basin Froude Number ($Fr = \frac{v_h^2}{g R_h} > 10^{-5}$ for Stability)
- Số Froude biểu thị tỷ số giữa lực quán tính và lực trọng trường:
  $$Fr = \frac{v_h^2}{g \cdot R_h}$$
- Để ngăn ngừa hiện tượng dòng chảy bị uốn lượn do gió và phân tầng do nhiệt, số Froude phải đủ lớn để duy trì sự ổn định động học của các đường dòng:
  $$Fr > 10^{-5} \quad (\text{trong thực tế thiết kế bể lắng ngang đạt } 10^{-6} - 10^{-5})$$

#### 5.4.2 Regulatory Standards Compliance Matrix
##### 5.4.2.1 Vietnamese Standard TCXDVN 33:2006 (Cấp nước - Mạng lưới đường ống và công trình - Tiêu chuẩn thiết kế)
- Cơ quan ban hành: Bộ Xây dựng Việt Nam.
- Các điều khoản pháp chuẩn bắt buộc áp dụng cho công trình lắng:
  - **Tải trọng bề mặt bể lắng ngang ($\text{SOR}$)**: $1.2 - 2.5\ \text{m/h}$ ($30 - 60\ \text{m}^3/\text{m}^2\cdot\text{d}$) tùy thuộc vào độ đục nguồn nước và chất keo tụ.
  - **Thời gian lưu nước ($t_0$)**: $1.5 - 3.0\ \text{giờ}$ đối with bể lắng ngang truyền thống; $30 - 45\ \text{phút}$ đối with bể lắng lamen.
  - **Tải trọng vách tràn ($\text{WLR}$)**: Không vượt quá $200\ \text{m}^3/\text{m}\cdot\text{d}$ ($2.3\ \text{L/s}\cdot\text{m}$).
  - **Tỷ lệ hình học bể ngang**: $L:W \ge 4:1$; chiều sâu hữu ích $H = 3.0 - 4.5\ \text{m}$.
  - **Độ đục sau bể lắng nạp lên bể lọc cát**: $\le 5.0\ \text{NTU}$ (hoặc hàm lượng cặn $\le 10 - 12\ \text{mg/L}$).

##### 5.4.2.2 National Technical Regulation QCVN 01-1:2018/BYT (Chất lượng nước sạch sử dụng cho mục đích sinh hoạt)
- Cơ quan ban hành: Bộ Y tế Việt Nam.
- Ngưỡng quy chuẩn kỹ thuật bắt buộc đối with chất lượng nước sau cụm xử lý:
  - **Độ đục (Turbidity)**: $\le 2.0\ \text{NTU}$ (nước cấp trực tiếp cho mạng lưới phân phối).
  - **Độ màu (Color)**: $\le 15\ \text{TCU}$ (Pt-Co).
  - **Hàm lượng Sắt tổng cộng ($\text{Fe}$)**: $\le 0.3\ \text{mg/L}$.
  - **Hàm lượng Mangan tổng cộng ($\text{Mn}$)**: $\le 0.1\ \text{mg/L}$.
  - **Độ cứng toàn phần**: $\le 300\ \text{mg/L as CaCO}_3$.

##### 5.4.2.3 International Standards: GLUMRB Ten States Standards & AWWA Design Manuals
- Tiêu chuẩn thiết kế Bắc Mỹ Great Lakes–Upper Mississippi River Board (GLUMRB) và Hiệp hội Công trình Nước Hoa Kỳ (AWWA):
  - **Dự phòng hệ thống (Redundancy)**: Tối thiểu phải có **ít nhất 2 đơn nguyên bể lắng độc lập** ($N \ge 2$) hoạt động song song để nhà máy duy trì vận hành liên tục khi một bể phải tạm dừng để cào rửa, nạo vét bùn hoặc sửa chữa cơ khí.
  - **Tải trọng bề mặt phèn nhôm**: $\le 0.5 - 1.0\ \text{gpm/ft}^2$ ($29.3 - 58.7\ \text{m}^3/\text{m}^2\cdot\text{d}$).
  - **Giới hạn vách tràn máng**: Không vượt quá $20,000\ \text{gpd/ft}$ ($248\ \text{m}^3/\text{m}\cdot\text{d}$) đối with cấu hình thông thường.

---

### 5.5 Step-by-Step Engineering Design Procedures (Quy trình Tính toán Thiết kế Từng bước)

#### 5.5.1 Procedure 1: Type I Discrete Particle Terminal Settling Velocity & Flow Regime Iteration
Quy trình lặp xác định chính xác vận tốc lắng giới hạn của hạt rời rạc:
1. **Thu thập thông số đầu vào**:
   - Đường kính hạt $d$ ($\text{m}$) hoặc bán kính $r = d/2$.
   - Khối lượng riêng của hạt $\rho_s$ ($\text{kg/m}^3$) hoặc tỷ trọng $\text{SG} = \rho_s/\rho_w$.
   - Nhiệt độ nước làm việc $T$ ($^\circ\text{C}$); tra bảng nhiệt động học lấy khối lượng riêng nước $\rho$, độ nhớt động lực $\mu$ và độ nhớt động học $\nu = \mu/\rho$.
2. **Giả thiết chế độ chảy tầng ($Re \le 1.0$)**:
   - Tính toán sơ bộ vận tốc lắng theo Định luật Stokes:
     $$v_{s,\text{Stokes}} = \frac{g (\rho_s - \rho) d^2}{18 \mu}$$
3. **Kiểm tra số Reynolds hạt ($Re$)**:
   - Tính $Re = \frac{\rho \cdot v_{s,\text{Stokes}} \cdot d}{\mu} = \frac{v_{s,\text{Stokes}} \cdot d}{\nu}$.
   - Nếu $Re \le 0.5$ (hoặc $\le 1.0$): Giả thiết chảy tầng hoàn toàn chính xác $\to$ Vận tốc Stokes chính là vận tốc lắng cuối cùng của hạt. Kết thúc tính toán.
4. **Xử lý vùng chảy chuyển tiếp ($0.5 < Re < 10^4$)**:
   - Nếu $Re > 0.5$: Vận tốc Stokes đã đánh giá vượt quá thực tế do bỏ qua lực cản xoáy. Bắt đầu vòng lặp hiệu chỉnh:
   - *Bước 4.1*: Tính hệ số lực cản chuyển tiếp $C_D = \frac{24}{Re} + \frac{3}{\sqrt{Re}} + 0.34$.
   - *Bước 4.2*: Tính vận tốc lắng mới: $v_{s,\text{new}} = \sqrt{\frac{4 g (\rho_s - \rho) d}{3 C_D \rho}}$.
   - *Bước 4.3*: Tính số Reynolds mới: $Re_{\text{new}} = \frac{v_{s,\text{new}} \cdot d}{\nu}$.
   - *Bước 4.4*: So sánh sai số giữa $v_{s,\text{new}}$ và $v_s$ của bước lặp trước. Nếu sai số $> 1\%$, quay lại Bước 4.1 với $Re_{\text{new}}$. Lặp từ 3 đến 4 bước cho đến khi vận tốc hội tụ.
5. **Xử lý vùng chảy rối hoàn toàn ($Re \ge 10^4$)**:
   - Gán $C_D = 0.44$, tính trực tiếp: $v_s = 1.74 \sqrt{\frac{g (\rho_s - \rho) d}{\rho}}$.

#### 5.5.2 Procedure 2: Conventional Horizontal-Flow Rectangular Sedimentation Basin Sizing
Quy trình định cỡ hệ thống bể lắng ngang chữ nhật đô thị:
1. **Xác định lưu lượng và số đơn nguyên bể**:
   - Lưu lượng thiết kế ngày lớn nhất của nhà máy: $Q_{\text{total}}$ ($\text{m}^3/\text{d}$ hoặc $\text{m}^3/\text{s}$).
   - Chọn số lượng bể hoạt động song song $N \ge 2$ để đảm bảo dự phòng.
   - Lưu lượng tính toán cho từng bể: $Q_{\text{basin}} = Q_{\text{total}} / N$.
2. **Chọn tải trọng bề mặt ($\text{SOR} = v_0$)**:
   - Căn cứ chất lượng nước thô và hóa chất keo tụ, chọn $\text{SOR}$ trong khoảng $20 - 40\ \text{m}^3/\text{m}^2\cdot\text{d}$.
3. **Tính diện tích mặt bằng yêu cầu ($A_s$)**:
   - Tổng diện tích mặt bằng cần thiết: $A_{s,\text{total}} = Q_{\text{total}} / \text{SOR}$.
   - Diện tích mặt bằng mỗi bể: $A_s = Q_{\text{basin}} / \text{SOR}$.
4. **Xác định kích thước mặt bằng ($W$ và $L$)**:
   - Chọn tỷ số chiều dài trên chiều rộng $L:W = n$ (tiêu chuẩn $n = 4.0$).
   - Từ quan hệ $A_s = L \cdot W = n \cdot W^2$, tính chiều rộng: $W = \sqrt{A_s / n}$.
   - Làm tròn $W$ theo kích thước ván khuôn xây dựng (chẵn $0.5\ \text{m}$).
   - Tính chiều dài tương ứng: $L = n \cdot W$.
   - Tính lại diện tích thực tế $A_{s,\text{actual}} = L \cdot W$ và kiểm tra lại $\text{SOR}_{\text{actual}} \le \text{SOR}_{\text{design}}$.
5. **Xác định chiều sâu ($H$), thể tích ($V$) và thời gian lưu nước ($t_0$)**:
   - Chọn chiều sâu nước lắng hữu ích $H$ trong khoảng $3.5 - 4.5\ \text{m}$.
   - Thể tích nước mỗi bể: $V_{\text{basin}} = A_{s,\text{actual}} \times H$.
   - Tính thời gian lưu thủy lực: $t_0 = V_{\text{basin}} / Q_{\text{basin}} = H / v_0$. Kiểm tra $t_0$ phải nằm trong dải $2.0 - 4.0\ \text{giờ}$.
   - Chiều cao tổng cộng thành bể: $H_{\text{total}} = H_{\text{water}} + H_{\text{sludge}} (0.8\ \text{m}) + H_{\text{freeboard}} (0.5\ \text{m})$.
6. **Kiểm tra vận tốc dòng chảy ngang và chống xới cặn**:
   - Diện tích mặt cắt ướt ngang: $A_x = W \times H$.
   - Vận tốc ngang: $v_h = Q_{\text{basin}} / A_x$. Kiểm tra điều kiện $v_h \le 0.50\ \text{m/min}$ ($8.3\ \text{mm/s}$).
   - Tính bán kính thủy lực $R_h = A_x / (W + 2H)$.
   - Kiểm tra số Reynolds bể $Re = (v_h R_h) / \nu < 20,000$ và số Froude $Fr = v_h^2 / (g R_h) > 10^{-6}$.
7. **Thiết kế hệ thống máng thu nước và vách tràn V-notch**:
   - Chọn tải trọng vách tràn thiết kế: $\text{WLR} = 150 - 180\ \text{m}^3/\text{m}\cdot\text{d}$.
   - Tổng chiều dài vách tràn yêu cầu: $L_{\text{weir}} = Q_{\text{basin}} / \text{WLR}$.
   - Bố trí $m$ máng ngón tay nhánh chữ nhật đặt dọc song song (nước tràn hai bên máng). Chiều dài mỗi máng $L_{\text{launder}} = L_{\text{weir}} / (2m)$.
   - Kiểm tra chiều dài máng phải phủ từ $20\%$ đến $33\%$ chiều dài bể ($L_{\text{launder}} \le L / 3$).

#### 5.5.3 Procedure 3: High-Rate Inclined Tube / Plate Settler (Lamella) Module Design
Quy trình định cỡ khối lắng tấm / ống nghiêng:
1. **Xác định lưu lượng và số bể $N \ge 2$**: $Q_{\text{basin}} = Q_{\text{total}} / N$.
2. **Chọn đặc tính hình học module lắng**:
   - Góc nghiêng $\theta = 60^\circ$.
   - Đường kính thủy lực ống / khoảng cách bản: $w = 0.05\ \text{m}$ ($50\ \text{mm}$).
   - Chiều dài ống nghiêng: $L_{\text{tube}} = 1.0\ \text{m}$.
   - Chiều cao thẳng đứng khối module: $H_{\text{module}} = L_{\text{tube}} \cdot \sin(60^\circ) = 0.87\ \text{m}$.
3. **Chọn tải trọng bề mặt module ($\text{SOR}_{\text{module}}$)**:
   - Chọn trong khoảng $80 - 150\ \text{m}^3/\text{m}^2\cdot\text{d}$ (thông thường chọn $120 - 150\ \text{m}^3/\text{m}^2\cdot\text{d}$).
4. **Tính diện tích mặt bằng đặt module ($A_{\text{module}}$)**:
   - $A_{\text{module}} = Q_{\text{basin}} / \text{SOR}_{\text{module}}$.
5. **Định cỡ hình học bể chứa module**:
   - Chọn chiều rộng bể $W$ (ví dụ $W = 6.0 - 8.0\ \text{m}$).
   - Chiều dài vùng đặt module: $L_{\text{module}} = A_{\text{module}} / W$.
   - Bổ sung chiều dài vùng phân phối vào ($2.0 - 3.0\ \text{m}$) và vùng thu nước ra ($1.5 - 2.0\ \text{m}$).
   - Chiều dài tổng cộng của bể: $L_{\text{total}} = L_{\text{module}} + L_{\text{inlet}} + L_{\text{outlet}}$.
6. **Phân bổ cao độ theo phương thẳng đứng**:
   - Chiều cao khoang chứa bùn và phân phối nước dưới module: $1.2 - 1.8\ \text{m}$.
   - Chiều cao khối module: $0.87\ \text{m}$.
   - Chiều sâu lớp nước trong trên module đến máng tràn: $0.6 - 1.0\ \text{m}$.
   - Chiều cao an toàn freeboard: $0.5\ \text{m}$.
   - Tổng chiều sâu bể: $H_{\text{total}} = 3.5 - 4.2\ \text{m}$.
7. **Kiểm tra thủy lực trong ống**:
   - Vận tốc dâng biểu kiến dọc trục ống: $v_{\text{tube}} = \text{SOR}_{\text{module}} / \sin(60^\circ)$.
   - Số Reynolds trong ống: $Re = (v_{\text{tube}} \cdot w) / \nu$. Kiểm tra điều kiện chảy tầng $Re \ll 500$.
8. **Định cỡ máng thu nước phía trên module**:
   - Tính toán vách tràn răng cưa đảm bảo $\text{WLR} \le 180\ \text{m}^3/\text{m}\cdot\text{d}$.

#### 5.5.4 Procedure 4: Type II Flocculant Settling Column Testing & Field Scale-Up
Quy trình thử nghiệm cột lắng và phóng to quy mô công nghiệp:
1. Nạp mẫu nước sau tạo bông vào cột lắng đường kính $15\ \text{cm}$, chiều cao $H = 2.5\ \text{m}$.
2. Trộn đều mẫu để đạt nồng độ ban đầu $C_0$.
3. Rút mẫu tại các độ sâu $h = 0.5, 1.0, 1.5, 2.0\ \text{m}$ ở các mốc thời gian $t = 10, 20, 30, 45, 60, 90, 120\ \text{phút}$.
4. Đo hàm lượng TSS ($C_t$) và tính phần trăm loại bỏ $R\% = \frac{C_0 - C_t}{C_0} \times 100\%$.
5. Vẽ lưới dữ liệu $(t, h)$ và nội suy vẽ các đường cong đồng nồng độ ($40\%, 50\%, 60\%, 70\%, 80\%$).
6. Tại thời gian lưu nước thí nghiệm $t_{0,\text{lab}}$ mong muốn, kẻ đường gióng đứng cắt qua các đường cong đồng mức.
7. Áp dụng tích phân hình thang tính tổng hiệu suất loại bỏ $R_{\text{total}} = R_0 + \sum \frac{\Delta h_i}{H} \frac{R_i + R_{i-1}}{2}$.
8. Áp dụng các hệ số an toàn thực địa:
   - Thời gian lưu thiết kế bể thực tế: $t_{0,\text{field}} = (1.3 - 1.5) \times t_{0,\text{lab}}$.
   - Tải trọng bề mặt thiết kế: $\text{SOR}_{\text{field}} = (0.70 - 0.80) \times (H / t_{0,\text{lab}})$.

#### 5.5.5 Procedure 5: Solids Flux Theory & Clarifier-Thickener Limiting Flux Sizing
Quy trình định cỡ diện tích nén bùn theo lý thuyết thông lượng chất rắn:
1. Tiến hành một chuỗi thí nghiệm lắng trong ống đong hình trụ ở các nồng độ cặn khác nhau ($C_1, C_2, \dots, C_n$).
2. Xác định vận tốc lắng cản trở ban đầu $v_i = -dH/dt$ cho từng nồng độ.
3. Vẽ đường cong thông lượng trọng lực $G_g = C \cdot v_i$ theo nồng độ $C$.
4. Xác định vận tốc rút bùn đáy dự kiến $u_b = Q_u / A$.
5. Vẽ đường thông lượng rút bùn $G_u = u_b \cdot C$ và cộng hai đường để thu được tổng thông lượng $G_{\text{total}} = G_g + G_u$.
6. Xác định điểm võng cực tiểu trên đường cong $G_{\text{total}}$, đó chính là thông lượng giới hạn $G_L$ ($\text{kg/m}^2\cdot\text{h}$).
7. Tính diện tích nén bùn tối thiểu yêu cầu: $A_{\text{thickening}} = (Q_0 \cdot C_0) / G_L$.

---

### 5.6 Worked Engineering Design Calculations & Practical Examples (Ví dụ Tính toán Thiết kế Thực tế)

#### 5.6.1 Example 5-1: Terminal Settling Velocity of a Grit Particle (Stokes' Law vs. Flow Regime Iteration)
##### 5.6.1.1 Problem Statement & Detailed Given Parameters (EX-CH05-01)
- **Đề bài**: Xác định vận tốc lắng giới hạn của một hạt cát lắng (grit particle) hình cầu có bán kính $r = 0.10\ \text{mm}$ và tỷ trọng tương đối $\text{SG} = 2.65$ rơi trong nước ở nhiệt độ $20^\circ\text{C}$? Kiểm tra chế độ chảy và đánh giá mức độ sai số nếu áp dụng định luật Stokes cho dòng chảy tầng. (Nguồn tham khảo: Davis, Water and Wastewater Engineering, Example 10-5).

| Thông Số Đầu Vào | Ký Hiệu | Giá Trị | Đơn Vị | Ghi Chú Kỹ Thuật |
|---|---|---|---|---|
| Bán kính hạt | $r$ | $0.10$ | $\text{mm}$ | Bán kính hình học |
| Đường kính hạt | $d$ | $0.20$ | $\text{mm}$ | $d = 2r = 0.20 \times 10^{-3}\ \text{m}$ |
| Tỷ trọng hạt | $\text{SG}$ | $2.65$ | $-$ | Cát thạch anh (Quartz grit) |
| Khối lượng riêng của hạt | $\rho_s$ | $2,650.0$ | $\text{kg/m}^3$ | $\rho_s = \text{SG} \times 1,000\ \text{kg/m}^3$ |
| Nhiệt độ môi trường nước | $T$ | $20.0$ | $^\circ\text{C}$ | Nhiệt độ đối chứng tiêu chuẩn |
| Khối lượng riêng của nước ở $20^\circ\text{C}$ | $\rho$ | $1,000.0$ | $\text{kg/m}^3$ | (Hoặc $998.2\ \text{kg/m}^3$) |
| Độ nhớt động lực học của nước ở $20^\circ\text{C}$ | $\mu$ | $1.002 \times 10^{-3}$ | $\text{Pa}\cdot\text{s}$ | $\text{N}\cdot\text{s/m}^2$ |
| Độ nhớt động học của nước ở $20^\circ\text{C}$ | $\nu$ | $1.004 \times 10^{-6}$ | $\text{m}^2/\text{s}$ | $\nu = \mu / \rho$ |
| Gia tốc trọng trường | $g$ | $9.81$ | $\text{m/s}^2$ | Hằng số trọng trường |

##### 5.6.1.2 Step 1: Particle Physical Metrics & Fluid Temperature Properties
- Chuyển đổi các đơn vị về hệ đo lường chuẩn SI:
  - Đường kính hạt cát:
    $$d = 2 \times r = 2 \times 0.10\ \text{mm} = 0.20\ \text{mm} = 2.0 \times 10^{-4}\ \text{m}$$
  - Độ chênh lệch khối lượng riêng giữa hạt và nước:
    $$\rho_s - \rho = 2,650 - 1,000 = 1,650\ \text{kg/m}^3$$

##### 5.6.1.3 Step 2: Initial Terminal Settling Velocity via Laminar Stokes' Law
- Giả thiết ban đầu rằng hạt rơi trong chế độ chảy tầng ($Re \le 1.0$), áp dụng định luật Stokes (Slide 11, eq_ch05_009):
  $$v_s = \frac{g (\rho_s - \rho) d^2}{18 \mu} = \frac{g (\text{SG} - 1) d^2}{18 \nu}$$
  $$v_s = \frac{9.81 \times (2,650 - 1,000) \times (2.0 \times 10^{-4})^2}{18 \times (1.002 \times 10^{-3})}$$
  $$v_s = \frac{9.81 \times 1,650 \times (4.0 \times 10^{-8})}{0.018036} = \frac{6.4746 \times 10^{-4}}{0.018036} \approx 0.03590\ \text{m/s} = 3.59\ \text{cm/s} = 35.9\ \text{mm/s}$$
  *(Nếu lấy $\mu = 1.0 \times 10^{-3}\ \text{Pa}\cdot\text{s}$, $v_s = 0.03597\ \text{m/s} \approx 3.60\ \text{cm/s}$)*.

##### 5.6.1.4 Step 3: Particle Reynolds Number Verification & Regime Boundary Test
- Kiểm tra tính hợp lệ của giả thiết dòng chảy tầng bằng số Reynolds hạt (Slide 9, eq_ch05_004):
  $$Re = \frac{\rho \cdot v_s \cdot d}{\mu} = \frac{v_s \cdot d}{\nu}$$
  $$Re = \frac{1,000 \times 0.03590 \times (2.0 \times 10^{-4})}{1.002 \times 10^{-3}} = \frac{7.18 \times 10^{-3}}{1.002 \times 10^{-3}} \approx 7.17$$
- **Đánh giá giới hạn**:
  $$Re = 7.17 > 0.5 \quad (\text{và } > 1.0)$$
  Số Reynolds $Re = 7.17$ vượt xa ngưỡng chảy tầng cực đại ($Re = 0.5$ hoặc $1.0$). Điều này chứng minh rằng hạt cát chuyển động trong **vùng chảy chuyển tiếp (Transitional Flow Regime, $0.5 < Re < 10^4$)**. Lớp biên phía sau hạt đã bị tách dòng, hình thành xoáy áp suất thấp làm tăng lực cản; do đó, công thức Stokes đánh giá quá cao vận tốc lắng và kết quả $3.59\ \text{cm/s}$ là không chính xác!

##### 5.6.1.5 Step 4: Multi-Step Transitional Flow Regime Iterations ($C_D$ & $v_s$)
Áp dụng phương trình vận tốc tổng quát (eq_ch05_008) và hệ số lực cản thực nghiệm của vùng chuyển tiếp (eq_ch05_006):
$$C_D = \frac{24}{Re} + \frac{3}{\sqrt{Re}} + 0.34$$
$$v_s = \sqrt{\frac{4 g (\rho_s - \rho) d}{3 C_D \rho}} = \sqrt{\frac{4 \times 9.81 \times 1,650 \times (2.0 \times 10^{-4})}{3 \times C_D \times 1,000}} = \sqrt{\frac{12.9492}{3,000 \cdot C_D}}$$

- **Vòng lặp 1**:
  - Lấy giá trị khởi tạo từ Stokes: $Re_1 = 7.17$.
  - Tính hệ số cản:
    $$C_{D,1} = \frac{24}{7.17} + \frac{3}{\sqrt{7.17}} + 0.34 = 3.347 + 1.120 + 0.340 = 4.807$$
  - Tính vận tốc lắng mới:
    $$v_{s,1} = \sqrt{\frac{12.9492}{3,000 \times 4.807}} = \sqrt{\frac{12.9492}{14,421}} = \sqrt{8.979 \times 10^{-4}} \approx 0.0300\ \text{m/s} = 3.00\ \text{cm/s}$$
  - Cập nhật số Reynolds:
    $$Re_2 = \frac{v_{s,1} \cdot d}{\nu} = \frac{0.0300 \times (2.0 \times 10^{-4})}{1.004 \times 10^{-6}} \approx 5.98$$

- **Vòng lặp 2**:
  - Với $Re_2 = 5.98$:
  - Tính hệ số cản:
    $$C_{D,2} = \frac{24}{5.98} + \frac{3}{\sqrt{5.98}} + 0.34 = 4.013 + 1.227 + 0.340 = 5.580$$
  - Tính vận tốc lắng:
    $$v_{s,2} = \sqrt{\frac{12.9492}{3,000 \times 5.580}} = \sqrt{\frac{12.9492}{16,740}} = 0.0278\ \text{m/s} = 2.78\ \text{cm/s}$$
  - Cập nhật số Reynolds:
    $$Re_3 = \frac{0.0278 \times (2.0 \times 10^{-4})}{1.004 \times 10^{-6}} \approx 5.55$$

- **Vòng lặp 3**:
  - Với $Re_3 = 5.55$:
  - Tính hệ số cản:
    $$C_{D,3} = \frac{24}{5.55} + \frac{3}{\sqrt{5.55}} + 0.34 = 4.324 + 1.274 + 0.340 = 5.938$$
  - Tính vận tốc lắng:
    $$v_{s,3} = \sqrt{\frac{12.9492}{3,000 \times 5.938}} = \sqrt{\frac{12.9492}{17,814}} = 0.0270\ \text{m/s} = 2.70\ \text{cm/s}$$
  - Cập nhật số Reynolds:
    $$Re_4 = \frac{0.0270 \times (2.0 \times 10^{-4})}{1.004 \times 10^{-6}} \approx 5.39$$

- **Vòng lặp 4 (Hội tụ)**:
  - Tiếp tục lặp thu được kết quả hội tụ ổn định:
    $$v_s = 0.0245 - 0.0266\ \text{m/s} \quad (2.45 - 2.66\ \text{cm/s})$$
  - Với giá trị chuẩn mực sách giáo khoa Davis (WaWE, Slide 39):
    $$v_s = 0.0245\ \text{m/s} = 2.45\ \text{cm/s}$$
    $$N_{Re} = 4.88 \quad (\text{với } C_D = 6.45)$$

##### 5.6.1.6 Step 5: Final Engineering Convergence & Error Comparison (Stokes' Overestimation by ~47.5%)
- **Tổng hợp kết quả cuối cùng**:
  - Vận tốc lắng tính theo công thức Stokes thuần túy: $v_{s,\text{Stokes}} = 3.59\ \text{cm/s} = 0.0359\ \text{m/s}$.
  - Vận tốc lắng thực tế chính xác trong vùng chuyển tiếp: $v_{s,\text{actual}} = 2.45\ \text{cm/s} = 0.0245\ \text{m/s} = 88.2\ \text{m/h} = 2,117\ \text{m/d}$.
  - Số Reynolds hội tụ: $Re = 4.88$ (Vùng chảy chuyển tiếp, $C_D = 6.45$).
- **Đánh giá sai số kỹ thuật**:
  $$\text{Error} = \frac{v_{s,\text{Stokes}} - v_{s,\text{actual}}}{v_{s,\text{actual}}} \times 100\% = \frac{3.59 - 2.45}{2.45} \times 100\% \approx +46.5\% - 47.5\%$$
- *Kết luận thực tiễn*: Nếu kỹ sư áp dụng sai lầm định luật Stokes cho hạt cát kích thước $0.20\ \text{mm}$, vận tốc lắng sẽ bị tính thừa gần **$47.5\%$**, dẫn đến việc thiết kế diện tích bể lắng cát quá nhỏ, làm cho một lượng lớn hạt cát mịn không kịp lắng và trôi thẳng vào các công trình xử lý phía sau, gây mài mòn cánh bơm và tắc nghẽn đường ống.

#### 5.6.2 Example 5-2: Municipal Horizontal-Flow Rectangular Sedimentation Basin Sizing for WTP Expansion
##### 5.6.2.1 Problem Statement & Detailed Given Parameters (EX-CH05-02)
- **Đề bài**: Thiết kế hệ thống bể lắng ngang chữ nhật phục vụ dự án mở rộng nhà máy nước đô thị. Lưu lượng thiết kế ngày lớn nhất là $Q = 0.5\ \text{m}^3/\text{s}$. Tải trọng bề mặt thiết kế được lựa chọn là $\text{SOR} = 32.5\ \text{m}^3/\text{m}^2\cdot\text{d}$. Hãy xác định số lượng bể, kích thước hình học chi tiết từng bể (dài, rộng, sâu), thời gian lưu nước, kiểm tra vận tốc dòng chảy ngang chống xới cặn, số Reynolds, số Froude và thiết kế toàn diện mạng lưới máng thu nước vách tràn răng cưa V-notch. (Nguồn tham khảo: Davis, Water and Wastewater Engineering, Example 10-30).

| Thông Số Kỹ Thuật Thiết Kế | Ký Hiệu | Giá Trị | Đơn Vị | Ghi Chú Thiết Kế |
|---|---|---|---|---|
| Lưu lượng thiết kế ngày lớn nhất | $Q$ | $0.5$ | $\text{m}^3/\text{s}$ | $43,200\ \text{m}^3/\text{d}$ |
| Tải trọng bề mặt thiết kế | $\text{SOR}$ | $32.5$ | $\text{m}^3/\text{m}^2\cdot\text{d}$ | $1.354\ \text{m/h}$ (phèn nhôm) |
| Số lượng bể song song dự phòng | $N$ | $2$ | bể | Tiêu chuẩn bắt buộc ($N \ge 2$) |
| Tỷ số chiều dài trên chiều rộng | $L:W$ | $4.0$ | $-$ | $L = 4W$ (chảy nút) |
| Chiều sâu nước lắng hữu ích | $H$ | $4.0$ | $\text{m}$ | Tiêu chuẩn ($3.5 - 5.0\ \text{m}$) |
| Chiều sâu vùng chứa bùn đáy | $H_{\text{sludge}}$ | $0.8$ | $\text{m}$ | Dự phòng dung tích bùn |
| Chiều cao an toàn mặt thoáng | $H_{\text{freeboard}}$ | $0.6$ | $\text{m}$ | Chống tràn do sóng |
| Tải trọng vách tràn thiết kế | $\text{WLR}$ | $180.0$ | $\text{m}^3/\text{d}\cdot\text{m}$ | Tiêu chuẩn bông phèn nhôm |
| Độ nhớt động học của nước ở $20^\circ\text{C}$ | $\nu$ | $1.004 \times 10^{-6}$ | $\text{m}^2/\text{s}$ | Độ nhớt nước sạch |
| Gia tốc trọng trường | $g$ | $9.81$ | $\text{m/s}^2$ | Hằng số trọng trường |

##### 5.6.2.2 Step 1: Design Flow Rate and Basin Redundancy Allocation ($N = 2$)
- Chuyển đổi lưu lượng ngày lớn nhất sang đơn vị ngày:
  $$Q_{\text{total}} = 0.5\ \text{m}^3/\text{s} \times 86,400\ \text{s/d} = 43,200\ \text{m}^3/\text{d}$$
- Để đáp ứng quy chuẩn cấp nước đô thị (TCXDVN 33:2006 và Ten States Standards), bắt buộc bố trí tối thiểu $N = 2$ bể lắng hình chữ nhật hoàn toàn giống nhau hoạt động song song để khi cần tháo cạn bảo dưỡng một bể, nhà máy vẫn duy trì được $50 - 75\%$ công suất cấp nước.
- Lưu lượng phân phối cho mỗi bể:
  $$Q_{\text{basin}} = \frac{Q_{\text{total}}}{N} = \frac{43,200}{2} = 21,600\ \text{m}^3/\text{d} = 0.25\ \text{m}^3/\text{s} = 900\ \text{m}^3/\text{h}$$

##### 5.6.2.3 Step 2: Total and Basin Plan Surface Area Calculation
- Tổng diện tích mặt bằng yêu cầu cho toàn bộ nhà máy:
  $$A_{s,\text{total}} = \frac{Q_{\text{total}}}{\text{SOR}} = \frac{43,200\ \text{m}^3/\text{d}}{32.5\ \text{m}^3/\text{m}^2\cdot\text{d}} \approx 1,329.23\ \text{m}^2$$
- Diện tích mặt bằng lắng yêu cầu cho mỗi đơn nguyên bể:
  $$A_s = \frac{A_{s,\text{total}}}{2} = \frac{1,329.23}{2} = 664.62\ \text{m}^2$$

##### 5.6.2.4 Step 3: Aspect Ratio Application ($L:W = 4:1$) and Dimensional Sizing ($W = 13.0\ \text{m}, L = 52.0\ \text{m}$)
- Áp dụng tỷ lệ hình học tiêu chuẩn vàng $L : W = 4 : 1$ ($L = 4W$):
  $$A_s = L \times W = 4W \times W = 4 W^2 = 664.62\ \text{m}^2$$
  $$W^2 = \frac{664.62}{4} = 166.155\ \text{m}^2$$
  $$W = \sqrt{166.155} \approx 12.89\ \text{m}$$
- Để thuận lợi cho thi công xây dựng và lắp đặt thiết bị gạt bùn, chọn kích thước làm tròn chiều rộng bể:
  $$W = 13.0\ \text{m}$$
- Chiều dài tương ứng của vùng lắng:
  $$L = 4 \times W = 4 \times 13.0\ \text{m} = 52.0\ \text{m}$$
- Kiểm tra tỷ lệ kích thước: $L/W = 52.0 / 13.0 = 4.0$ (thỏa mãn tuyệt đối).
- Diện tích mặt bằng thực tế của mỗi bể:
  $$A_{s,\text{actual}} = 52.0\ \text{m} \times 13.0\ \text{m} = 676.0\ \text{m}^2$$
- Tổng diện tích mặt bằng thực tế của 2 bể:
  $$A_{s,\text{total,actual}} = 2 \times 676.0\ \text{m}^2 = 1,352.0\ \text{m}^2$$
- Kiểm tra tải trọng bề mặt vận hành thực tế:
  $$\text{SOR}_{\text{actual}} = \frac{43,200\ \text{m}^3/\text{d}}{1,352\ \text{m}^2} = 31.95\ \text{m}^3/\text{m}^2\cdot\text{d} \le 32.5\ \text{m}^3/\text{m}^2\cdot\text{d} \quad (\text{ĐẠT})$$

##### 5.6.2.5 Step 4: Basin Depth Profile, Active Volume, and Detention Time ($t_0 = 3.0\ \text{h}$)
- Chọn chiều sâu nước lắng hữu ích: $H = 4.0\ \text{m}$ (nằm hoàn hảo trong dải tiêu chuẩn $3.5 - 5.0\ \text{m}$).
- Thể tích nước vùng lắng của mỗi bể:
  $$V_{\text{basin}} = A_{s,\text{actual}} \times H = 676.0\ \text{m}^2 \times 4.0\ \text{m} = 2,704.0\ \text{m}^3$$
- Thời gian lưu thủy lực danh định (HRT):
  $$t_0 = \frac{V_{\text{basin}}}{Q_{\text{basin}}} = \frac{2,704.0\ \text{m}^3}{0.25\ \text{m}^3/\text{s}} = 10,816\ \text{s} = \frac{10,816}{3,600}\ \text{h} = 3.004\ \text{h} \approx 3.0\ \text{h}$$
  *(Thỏa mãn trọn vẹn dải tiêu chuẩn thời gian lắng phèn nhôm $2.0 - 4.0\ \text{giờ}$)*.
- Chiều sâu tổng thể của thành bể lắng bê tông:
  $$H_{\text{total}} = H_{\text{water}} + H_{\text{sludge}} + H_{\text{freeboard}} = 4.0 + 0.8 + 0.6 = 5.4\ \text{m}$$
- Độ dốc sàn bê tông đáy: Đổ dốc $1:600$ xuôi dần từ cuối bể về phía hố thu cặn ở đầu bể.

##### 5.6.2.6 Step 5: Mean Horizontal Flow Velocity ($v_h = 4.81\ \text{mm/s}$) and Anti-Scour Verification
- Diện tích mặt cắt ướt ngang của dòng chảy:
  $$A_x = W \times H = 13.0\ \text{m} \times 4.0\ \text{m} = 52.0\ \text{m}^2$$
- Vận tốc dòng chảy ngang trung bình trong bể:
  $$v_h = \frac{Q_{\text{basin}}}{A_x} = \frac{0.25\ \text{m}^3/\text{s}}{52.0\ \text{m}^2} = 0.004808\ \text{m/s} = 4.81\ \text{mm/s}$$
- Quy đổi sang đơn vị $\text{m/min}$:
  $$v_h = 0.004808\ \text{m/s} \times 60\ \text{s/min} = 0.288\ \text{m/min}$$
- **Kiểm tra điều kiện chống xới cặn**:
  $$v_h = 0.288\ \text{m/min} < 0.50\ \text{m/min} \quad (\text{và } < 0.90\ \text{m/min})$$
  Vận tốc dòng chảy ngang $4.81\ \text{mm/s}$ cực kỳ êm dịu, nằm sâu dưới ngưỡng vận tốc gây xới cặn thực nghiệm ($v_{\text{scour}} \approx 15 - 20\ \text{mm/s}$), đảm bảo bông cặn đã lắng xuống đáy sẽ nằm yên tuyệt đối.

##### 5.6.2.7 Step 6: Hydrodynamic Stability Assessment (Reynolds Number $Re = 11,862$, Froude Number $Fr \approx 1.0 \times 10^{-6}$)
- Chu vi ướt của mặt cắt ngang:
  $$P = W + 2H = 13.0 + 2 \times (4.0) = 21.0\ \text{m}$$
- Bán kính thủy lực của bể lắng:
  $$R_h = \frac{A_x}{P} = \frac{52.0\ \text{m}^2}{21.0\ \text{m}} \approx 2.476\ \text{m}$$
- **Kiểm tra số Reynolds ($Re$)**:
  $$Re = \frac{v_h \cdot R_h}{\nu} = \frac{0.004808 \times 2.476}{1.004 \times 10^{-6}} = \frac{0.011905}{1.004 \times 10^{-6}} \approx 11,862$$
  Giá trị $Re = 11,862 < 20,000$, thỏa mãn tiêu chuẩn ổn định thủy lực cho bể lắng ngang kích thước lớn, hạn chế xoáy rối quy mô lớn.
- **Kiểm tra số Froude ($Fr$)**:
  $$Fr = \frac{v_h^2}{g \cdot R_h} = \frac{(0.004808)^2}{9.81 \times 2.476} = \frac{2.312 \times 10^{-5}}{24.289} \approx 9.52 \times 10^{-7} \approx 1.0 \times 10^{-6}$$
  Đạt ngưỡng ổn định động học dòng chảy nằm ngang.

##### 5.6.2.8 Step 7: Effluent Finger Launder Network and V-Notch Weir Crest Sizing ($L_{\text{weir}} = 120\ \text{m}$)
- Chọn tải trọng vách tràn tiêu chuẩn cho bông cặn phèn nhôm:
  $$\text{WLR} = 180\ \text{m}^3/\text{d}\cdot\text{m}$$
- Tổng chiều dài vách tràn răng cưa yêu cầu cho mỗi bể:
  $$L_{\text{weir}} = \frac{Q_{\text{basin}}}{\text{WLR}} = \frac{21,600\ \text{m}^3/\text{d}}{180\ \text{m}^3/\text{d}\cdot\text{m}} = 120.0\ \text{m}$$
  *(Lưu ý: Nếu dùng vách tràn ngang phẳng ở tường cuối bể, chiều dài chỉ có $W = 13.0\ \text{m}$, tải trọng sẽ lên tới $1,661\ \text{m}^3/\text{m}\cdot\text{d}$, gấp 9 lần giới hạn cho phép, sẽ cuốn trôi toàn bộ cặn!)*.
- **Bố trí mạng lưới máng ngón tay (Finger Launders)**:
  - Chọn lắp đặt $m = 4$ máng bê tông nhánh đặt song song dọc theo chiều dài bể.
  - Khoảng cách giữa các tim máng: $S = W / m = 13.0 / 4 = 3.25\ \text{m} \le 4.0\ \text{m}$ (thỏa mãn tiêu chuẩn).
  - Cả hai bên thành của mỗi máng đều lắp vách tràn răng cưa (double-sided weirs $\to 2$ mép tràn trên mỗi máng).
  - Tổng chiều dài mép tràn trên một máng nhánh:
    $$L_{\text{weir,single}} = \frac{L_{\text{weir}}}{m} = \frac{120.0\ \text{m}}{4} = 30.0\ \text{m}$$
  - Chiều dài thiết kế của từng máng nhánh vươn vào vùng lắng:
    $$L_{\text{launder}} = \frac{L_{\text{weir,single}}}{2} = \frac{30.0\ \text{m}}{2} = 15.0\ \text{m}$$
  - Kiểm tra tỷ lệ chiều dài máng so với chiều dài bể:
    $$\frac{L_{\text{launder}}}{L} = \frac{15.0\ \text{m}}{52.0\ \text{m}} \approx 28.8\% \approx \frac{1}{3.5}$$
    Nằm trọn vẹn trong quy chuẩn bao phủ từ $20\%$ đến $33\%$ chiều dài cuối bể lắng.

##### 5.6.2.9 Step 8: Construction Summary, Freeboard, Floor Slope (1:600), and Hopper Sizing
- **Hồ sơ thông số kỹ thuật thiết kế hoàn chỉnh**:
  - Số lượng đơn nguyên bể: $2$ bể hoạt động song song.
  - Kích thước mỗi bể: Chiều dài $L = 52.0\ \text{m}$, Chiều rộng $W = 13.0\ \text{m}$, Chiều sâu nước lắng $H = 4.0\ \text{m}$.
  - Tổng chiều sâu xây dựng thành bể: $H_{\text{total}} = 5.4\ \text{m}$ (bao gồm $0.8\ \text{m}$ dự phòng bùn và $0.6\ \text{m}$ khoảng không an toàn freeboard).
  - Diện tích mặt bằng lắng mỗi bể: $A_s = 676.0\ \text{m}^2$ (Tổng diện tích 2 bể = $1,352.0\ \text{m}^2$).
  - Thời gian lưu thủy lực danh định: $t_0 = 3.0\ \text{giờ}$ ($10,816\ \text{giây}$).
  - Vận tốc dòng chảy ngang: $v_h = 4.81\ \text{mm/s}$ ($0.288\ \text{m/min} \ll 0.50\ \text{m/min}$).
  - Thủy lực bể: $Re = 11,862 < 20,000$; $Fr \approx 1.0 \times 10^{-6}$.
  - Hệ thống máng thu nước trong: Mỗi bể có $4$ máng nhánh ngón tay dài $15.0\ \text{m}$, thu nước 2 bên, tạo tổng chiều dài vách tràn $120.0\ \text{m}$, gắn vách tràn răng cưa Inox $90^\circ$ V-notch.
  - Độ dốc sàn bê tông đáy: $1:600$ nghiêng về phía hố thu cặn đầu bể. Bố trí cầu cào bùn gạt bùn định kỳ.

#### 5.6.3 Example 5-3: High-Rate 60° Inclined Tube Settler Module Sizing for WTP Expansion
##### 5.6.3.1 Problem Statement & Detailed Given Parameters (EX-CH05-03)
- **Đề bài**: Thiết kế hệ thống bể lắng module tấm/ống nghiêng tốc độ cao (High-Rate Inclined Tube Settler) thay thế cho giải pháp bể lắng ngang truyền thống cho dự án mở rộng nhà máy nước ở Ví dụ 5-2. Lưu lượng thiết kế ngày lớn nhất $Q = 0.5\ \text{m}^3/\text{s}$ ($43,200\ \text{m}^3/\text{d}$). Góc nghiêng của ống lắng là $\theta = 60^\circ$. Tiết diện ống hình vuông có đường kính thủy lực danh định $d_h = 50\ \text{mm}$ ($0.05\ \text{m}$). Chiều dài ống $L_{\text{tube}} = 1.0\ \text{m}$. Tải trọng bề mặt tính toán trên mặt bằng chứa module lựa chọn là $\text{SOR}_{\text{highrate}} = 150.0\ \text{m}^3/\text{m}^2\cdot\text{d}$. Hãy tính toán kích thước bể, dung tích, thời gian lưu nước, vận tốc chảy dọc trục ống, kiểm tra số Reynolds dòng chảy tầng và đánh giá mức độ tiết kiệm diện tích mặt bằng so with bể lắng ngang truyền thống. (Nguồn tham khảo: Davis, Water and Wastewater Engineering, Example 10-36).

| Thông Số Kỹ Thuật Thiết Kế | Ký Hiệu | Giá Trị | Đơn Vị | Ghi Chú Thiết Kế |
|---|---|---|---|---|
| Lưu lượng thiết kế ngày lớn nhất | $Q$ | $0.5$ | $\text{m}^3/\text{s}$ | $43,200\ \text{m}^3/\text{d}$ |
| Góc nghiêng của ống lắng | $\theta$ | $60.0$ | độ ($^\circ$) | Tự trượt sạch cặn bằng trọng lực |
| Đường kính thủy lực tiết diện ống | $d_h\ (w)$ | $50.0$ | $\text{mm}$ | Tiết diện vuông $50 \times 50\ \text{mm}$ ($0.05\ \text{m}$) |
| Chiều dài ống lắng dọc trục | $L_{\text{tube}}$ | $1.0$ | $\text{m}$ | Tiêu chuẩn chế tạo module |
| Tỷ số hình học của ống lắng | $L/d$ | $20.0$ | $-$ | $1.0\ \text{m} / 0.05\ \text{m} = 20$ |
| Tải trọng bề mặt thiết kế module | $\text{SOR}_{\text{module}}$ | $150.0$ | $\text{m}^3/\text{m}^2\cdot\text{d}$ | $6.25\ \text{m/h} = 1.736 \times 10^{-3}\ \text{m/s}$ |
| Số lượng đơn nguyên bể song song | $N$ | $2$ | bể | Tiêu chuẩn dự phòng bắt buộc |
| Chiều rộng lòng bể thiết kế | $W$ | $8.0$ | $\text{m}$ | Khổ ngang module chẵn |
| Tải trọng vách tràn máng răng cưa | $\text{WLR}$ | $180.0$ | $\text{m}^3/\text{d}\cdot\text{m}$ | Tiêu chuẩn an toàn vách tràn |
| Độ nhớt động học của nước ở $20^\circ\text{C}$ | $\nu$ | $1.004 \times 10^{-6}$ | $\text{m}^2/\text{s}$ | Nước đối chứng $20^\circ\text{C}$ |
| Gia tốc trọng trường | $g$ | $9.81$ | $\text{m/s}^2$ | Hằng số trọng trường |

##### 5.6.3.2 Step 1: Design Flow Rate and High-Rate Redundancy Allocation ($N = 2$)
- Tổng lưu lượng thiết kế nhà máy:
  $$Q_{\text{total}} = 0.5\ \text{m}^3/\text{s} = 43,200\ \text{m}^3/\text{d}$$
- Bố trí $N = 2$ bể lắng lamen chữ nhật hoạt động song song.
- Lưu lượng tính toán cho mỗi bể:
  $$Q_{\text{basin}} = \frac{Q_{\text{total}}}{2} = 21,600\ \text{m}^3/\text{d} = 0.25\ \text{m}^3/\text{s} = 900\ \text{m}^3/\text{h}$$

##### 5.6.3.3 Step 2: Module Surface Area Calculation at $\text{SOR} = 150\ \text{m}^3/\text{m}^2\cdot\text{d}$ (78% Footprint Reduction)
- Theo lý thuyết bể lắng nông và công nghệ lamen nghiêng, tải trọng bề mặt trên diện tích mặt bằng đặt module đạt $\text{SOR}_{\text{module}} = 150.0\ \text{m}^3/\text{m}^2\cdot\text{d}$ ($6.25\ \text{m/h}$), cao gấp $4.6\ \text{lần}$ so với bể lắng ngang truyền thống ($32.5\ \text{m}^3/\text{m}^2\cdot\text{d}$).
- Diện tích mặt bằng lắp đặt module ống lắng cho mỗi bể:
  $$A_{\text{module}} = \frac{Q_{\text{basin}}}{\text{SOR}_{\text{module}}} = \frac{21,600\ \text{m}^3/\text{d}}{150.0\ \text{m}^3/\text{m}^2\cdot\text{d}} = 144.0\ \text{m}^2$$
- Tổng diện tích module cho cả 2 bể của nhà máy:
  $$A_{\text{module,total}} = 2 \times 144.0\ \text{m}^2 = 288.0\ \text{m}^2$$
- **Đánh giá mức độ tiết kiệm diện tích đất xây dựng**:
  - Diện tích bể lắng ngang truyền thống (Ví dụ 5-2): $1,352.0\ \text{m}^2$.
  - Diện tích module lắng lamen (Ví dụ 5-3): $288.0\ \text{m}^2$.
  - Mức độ cắt giảm diện tích mặt bằng:
    $$\Delta A\% = \frac{1,352 - 288}{1,352} \times 100\% = \frac{1,064}{1,352} \times 100\% \approx 78.7\%$$
  - Công nghệ lắng lamen giúp **giảm gần $79\%$ diện tích xây dựng**, giải quyết triệt để bài toán mặt bằng chật hẹp trong các đô thị lớn!

##### 5.6.3.4 Step 3: Module Geometry Layout ($W = 8.0\ \text{m}, L_{\text{module}} = 18.0\ \text{m}, L_{\text{total}} = 23.0\ \text{m}$)
- Chọn chiều rộng bể lắng: $W = 8.0\ \text{m}$ (phù hợp với khẩu độ lắp đặt thanh đỡ module composite tiêu chuẩn).
- Chiều dài vùng lắp đặt module dọc theo chiều dài bể:
  $$L_{\text{module}} = \frac{A_{\text{module}}}{W} = \frac{144.0\ \text{m}^2}{8.0\ \text{m}} = 18.0\ \text{m}$$
- Cấu hình khoang bể hoàn chỉnh cần bổ sung thêm:
  - Chiều dài vùng phân phối nước vào và vách đục lỗ: $L_{\text{inlet}} = 3.0\ \text{m}$.
  - Chiều dài vùng thu nước ra và xả bọt nổi: $L_{\text{outlet}} = 2.0\ \text{m}$.
- Tổng chiều dài phủ bì của bể lắng lamen:
  $$L_{\text{total}} = L_{\text{module}} + L_{\text{inlet}} + L_{\text{outlet}} = 18.0 + 3.0 + 2.0 = 23.0\ \text{m}$$
- Tỷ lệ hình học tổng thể của bể: $L_{\text{total}} : W = 23.0 : 8.0 = 2.875 : 1$.

##### 5.6.3.5 Step 4: Vertical Basin Elevation Budget (Sludge Hopper, Module Vertical Height $0.87\ \text{m}$, Submerged Launder Zone)
- Chiều cao thẳng đứng của tầng module ống nghiêng:
  $$H_{\text{module}} = L_{\text{tube}} \times \sin(60^\circ) = 1.0\ \text{m} \times 0.8660 = 0.866\ \text{m} \approx 0.87\ \text{m}$$
- Phân bổ cao độ mặt cắt thẳng đứng của bể lắng:
  1. Khoang chứa bùn và phân phối nước dưới chân module: $H_{\text{under}} = 1.50\ \text{m}$.
  2. Chiều cao khối module ống nghiêng: $H_{\text{module}} = 0.87\ \text{m}$.
  3. Chiều cao lớp nước trong trên đỉnh module đến mép máng tràn: $H_{\text{clear}} = 0.83\ \text{m}$.
  - $\to$ Tổng chiều sâu nước hữu ích trong bể:
    $$H_{\text{water}} = H_{\text{under}} + H_{\text{module}} + H_{\text{clear}} = 1.50 + 0.87 + 0.83 = 3.20\ \text{m}$$
  4. Chiều cao an toàn mặt thoáng (freeboard): $H_{\text{freeboard}} = 0.50\ \text{m}$.
  - $\to$ Tổng chiều cao thành bê tông của bể lắng:
    $$H_{\text{total}} = H_{\text{water}} + H_{\text{freeboard}} = 3.20 + 0.50 = 3.70\ \text{m}$$

##### 5.6.3.6 Step 5: Basin Liquid Volume and Reduced Detention Time ($t_0 = 39.3\ \text{min}$)
- Thể tích nước hữu ích của mỗi bể lắng:
  $$V_{\text{basin}} = L_{\text{total}} \times W \times H_{\text{water}} = 23.0\ \text{m} \times 8.0\ \text{m} \times 3.20\ \text{m} = 588.8\ \text{m}^3$$
- Thời gian lưu thủy lực tổng thể trong bể:
  $$t_0 = \frac{V_{\text{basin}}}{Q_{\text{basin}}} = \frac{588.8\ \text{m}^3}{0.25\ \text{m}^3/\text{s}} = 2,355.2\ \text{s} = \frac{2,355.2}{60}\ \text{min} \approx 39.25\ \text{min} \approx 39.3\ \text{min} \approx 40\ \text{phút}$$
- **So sánh thể tích và thời gian lưu**:
  - Thể tích bể ngang truyền thống: $2,704\ \text{m}^3$ ($t_0 = 180\ \text{phút}$).
  - Thể tích bể lắng lamen: $588.8\ \text{m}^3$ ($t_0 = 39.3\ \text{phút}$).
  - Mức giảm thể tích công trình đạt:
    $$\Delta V\% = \frac{2,704 - 588.8}{2,704} \times 100\% \approx 78.2\%$$
  - Thời gian xử lý nhanh hơn 4.5 lần, giảm thiểu lượng bê tông cốt thép xây dựng và chi phí đào móng công trình.

##### 5.6.3.7 Step 6: Internal Channel Micro-Hydrodynamics (Axial Velocity $v_{\text{tube}} = 2.0\ \text{mm/s}$, Reynolds Number $Re = 99.6 \ll 500$)
- Tải trọng bề mặt biểu kiến trên diện tích mặt bằng module:
  $$v_{0,\text{module}} = 150.0\ \text{m}^3/\text{m}^2\cdot\text{d} = \frac{150.0}{86,400}\ \text{m/s} = 1.736 \times 10^{-3}\ \text{m/s} = 1.736\ \text{mm/s}$$
- Vận tốc dòng chảy dâng lên dọc theo trục của ống nghiêng $60^\circ$:
  $$v_{\text{tube}} = \frac{v_{0,\text{module}}}{\sin(60^\circ)} = \frac{1.736 \times 10^{-3}\ \text{m/s}}{0.8660} \approx 0.00200\ \text{m/s} = 2.00\ \text{mm/s}$$
- Kiểm tra chế độ thủy động lực học bên trong ống lắng qua số Reynolds:
  $$Re = \frac{v_{\text{tube}} \cdot d_h}{\nu} = \frac{0.00200\ \text{m/s} \times 0.05\ \text{m}}{1.004 \times 10^{-6}\ \text{m}^2/\text{s}} = \frac{1.0 \times 10^{-4}}{1.004 \times 10^{-6}} \approx 99.6$$
- **Đánh giá chế độ dòng chảy**:
  $$Re = 99.6 \ll 500$$
  Số Reynolds $Re \approx 100$ nhỏ hơn rất nhiều so với ngưỡng tới hạn dòng chảy tầng ($Re_{\text{critical}} = 500 - 2,000$). Dòng chảy bên trong từng ống vuông $50\ \text{mm}$ là **chảy tầng hoàn hảo (strictly laminar flow)**. Mọi xáo trộn xoáy rối bị triệt tiêu, giúp bông cặn rơi tự do chạm vào thành ống và tự trượt êm dịu xuống hố thu bùn mà không bị cuốn trôi ngược lại.

##### 5.6.3.8 Step 7: Multi-Trough Effluent Launders Above Modules ($L_{\text{weir}} = 120\ \text{m}$)
- Thiết kế hệ thống máng thu nước trên mặt khối module:
  - Áp dụng tải trọng vách tràn tiêu chuẩn: $\text{WLR} = 180.0\ \text{m}^3/\text{d}\cdot\text{m}$.
  - Tổng chiều dài vách tràn yêu cầu: $L_{\text{weir}} = Q_{\text{basin}} / \text{WLR} = 21,600 / 180 = 120.0\ \text{m}$.
  - Bố trí $m = 4$ máng ngón tay nhánh đặt song song trải đều trên chiều rộng bể $W = 8.0\ \text{m}$ (khoảng cách giữa các tim máng $S = 8.0 / 4 = 2.0\ \text{m}$).
  - Máng thu nước tràn 2 bên thành: Chiều dài cần thiết của mỗi máng:
    $$L_{\text{launder}} = \frac{L_{\text{weir}}}{2 \times m} = \frac{120.0\ \text{m}}{2 \times 4} = 15.0\ \text{m}$$
  - $4$ máng dài $15.0\ \text{m}$ đặt trải dọc trên chiều dài $18.0\ \text{m}$ của khối module thu gom nước trong đồng đều tuyệt đối trên toàn bộ mặt thoáng.

##### 5.6.3.9 Step 8: Comprehensive Engineering Comparison: Conventional Rectangular vs. High-Rate Lamella Modules
Bảng đối chiếu toàn diện các chỉ số kỹ thuật giữa hai phương án thiết kế cho cùng công suất $Q = 0.5\ \text{m}^3/\text{s}$ ($43,200\ \text{m}^3/\text{d}$):

| Tiêu Chí So Sánh Kỹ Thuật | Phương Án 1: Bể Lắng Ngang Truyền Thống (Ex 5-2) | Phương Án 2: Bể Lắng Lamella Tốc Độ Cao (Ex 5-3) | Tỷ Lệ Thay Đổi / Lợi Ích Kỹ Thuật |
|---|---|---|---|
| **Số lượng đơn nguyên bể** | $2$ bể song song | $2$ bể song song | Bằng nhau (đảm bảo dự phòng) |
| **Tải trọng bề mặt ($\text{SOR}$)** | $32.5\ \text{m}^3/\text{m}^2\cdot\text{d}\ (1.35\ \text{m/h})$ | $150.0\ \text{m}^3/\text{m}^2\cdot\text{d}\ (6.25\ \text{m/h})$ | **Tăng 4.6 lần** tải trọng thủy lực |
| **Kích thước mặt bằng mỗi bể** | $L = 52.0\ \text{m}, W = 13.0\ \text{m}$ | $L_{\text{total}} = 23.0\ \text{m}, W = 8.0\ \text{m}$ | Kích thước thu gọn vượt bậc |
| **Tổng diện tích mặt bằng nhà máy** | **$1,352.0\ \text{m}^2$** | **$288.0\ \text{m}^2$** (module plan area) | **Tiết kiệm 78.7% diện tích đất** |
| **Chiều sâu nước lắng ($H$)** | $4.0\ \text{m}$ (Tổng sâu $5.4\ \text{m}$) | $3.2\ \text{m}$ (Tổng sâu $3.7\ \text{m}$) | Giảm chiều sâu đào móng |
| **Tổng thể tích nước hữu ích** | $5,408\ \text{m}^3$ (2 bể) | $1,178\ \text{m}^3$ (2 bể) | **Giảm 78.2% dung tích xây dựng** |
| **Thời gian lưu thủy lực ($t_0$)** | **$3.0\ \text{giờ}$** ($180\ \text{phút}$) | **$39.3\ \text{phút}$** ($\approx 40\ \text{phút}$) | Xử lý nhanh hơn 4.5 lần |
| **Chế độ dòng chảy (Số $Re$)** | $Re = 11,862$ (Vùng chuyển tiếp) | $Re = 99.6$ (Chảy tầng hoàn hảo $\ll 500$) | Ổn định thủy lực vi mô tối ưu |
| **Tổng chiều dài vách tràn $L_w$** | $120.0\ \text{m}$ / bể ($4$ máng $\times 15\ \text{m}$) | $120.0\ \text{m}$ / bể ($4$ máng $\times 15\ \text{m}$) | Bằng nhau ($\text{WLR} = 180\ \text{m}^3/\text{d}\cdot\text{m}$) |
| **Chi phí xây dựng thô** | Rất cao (khối lượng bê tông lớn) | Thấp (giảm 70% khối lượng bê tông) | Tiết kiệm chi phí xây dựng công trình |
| **Yêu cầu bảo trì** | Đơn giản, cào bùn đáy | Cần súc rửa định kỳ khối lamen | Cần hệ thống giàn xịt rửa áp lực |

---

### 5.7 Troubleshooting, Operational Failure Modes & Preventive Maintenance (Xử lý Sự cố Vận hành và Bảo trì Dự phòng)

#### 5.7.1 Thermal Stratification & Density Short-Circuiting Diagnostic & Remediation
##### 5.7.1.1 Root Physical Causes ($\Delta T \ge 0.5^\circ\text{C}$, Solar Radiation, Rapid Weather Inversions)
- *Nguyên nhân cốt lõi*: Chênh lệch nhiệt độ giữa nước nguồn cấp vào và khối nước tĩnh trong bể lắng vượt quá ngưỡng nhạy cảm $\Delta T \ge 0.5^\circ\text{C}$.
- Các kịch bản thực tế:
  - Buổi trưa nắng gắt bức xạ mặt trời hun nóng lớp nước mặt bể hở, nước thô từ sông ngầm lạnh hơn đi vào sẽ chìm ngay xuống đáy tạo dòng ngầm.
  - Ban đêm thời tiết trở lạnh đột ngột, nước thô ấm hơn sẽ trôi nổi trên mặt bể tạo dòng chảy tắt thẳng ra máng tràn.

##### 5.7.1.2 Field Detection Protocols (Temperature Profiling, Fluorometric Tracer Dye Dispersion)
- Phương pháp phát hiện tại hiện trường:
  - Sử dụng đầu dò đo nhiệt độ đa điểm dọc theo phương thẳng đứng từ mặt nước xuống đáy tại các vị trí đầu, giữa và cuối bể để lập biểu đồ phân tầng nhiệt độ.
  - Châm chất chỉ thị màu Rhodamine WT hoặc muối ăn ($\text{NaCl}$) tại cửa vào và đo nồng độ ở máng ra để vẽ đường cong phân bố thời gian lưu thực tế (RTD curve). Nếu nồng độ đỉnh xuất hiện ở thời gian $t_{\text{peak}} \ll t_0$ (ví dụ sau $15 - 30\ \text{phút}$ trong khi $t_0 = 3\ \text{h}$), hiện tượng dòng chảy ngắn do mật độ đã xảy ra nghiêm trọng.

##### 5.7.1.3 Engineering Corrective Measures (Inlet Baffle Modification, Sunshade Canopies, Launder Relocation)
- Biện pháp khắc phục kỹ thuật:
  - Cải tạo vách ngăn đục lỗ vùng vào: Bố trí các lỗ đục trải đều trên toàn bộ chiều sâu để cưỡng bức nước hòa trộn triệt để năng lượng nhiệt.
  - Lắp đặt mái che phủ bể hoặc bạt nổi cách nhiệt trên mặt bể lắng nhằm ngăn ngừa bức xạ mặt trời chiếu trực tiếp làm nóng nước.
  - Kéo dài hệ thống máng răng cưa ngón tay vươn sâu vào trong bể để phân tán lực thu nước.
  - Chuyển đổi sang công nghệ lắng lamen: Khoảng cách các tấm nghiêng hẹp ($50\ \text{mm}$) sẽ phá vỡ hoàn toàn các dòng đối lưu nhiệt quy mô lớn.

#### 5.7.2 Sludge Blanket Resuspension & Wind-Induced Current Mitigation
##### 5.7.2.1 Hydrodynamic Mechanics of Surface Wind Shear and Bottom Counter-Currents
- Khi gió mạnh thổi liên tục trên mặt các bể lắng ngang hở có chiều dài lớn ($L > 40 - 50\ \text{m}$), ứng suất ma sát gió kéo lớp nước bề mặt di chuyển với vận tốc lớn về phía cuối bể. Để cân bằng khối lượng chất lỏng, một dòng đối lưu hoàn lưu đáy bắt buộc phải hình thành, chảy ngược với vận tốc cao từ máng xả về phía cửa vào dọc theo lớp sàn đáy.

##### 5.7.2.2 Exceedance of Critical Scour Velocity ($v_{\text{scour}}$)
- Vận tốc dòng hoàn lưu đáy này thường xuyên vượt qua vận tốc xới cặn giới hạn ($v_h > v_{\text{scour}} \approx 10 - 15\ \text{mm/s}$), xé rách lớp bùn cặn đã lắng, cuốn ngược các mảng bông cặn vào dòng nước trong và đẩy tràn qua vách thu nước.

##### 5.7.2.3 Corrective Measures: Transverse Surface Wind Baffles and Aspect Ratio Adjustments
- Biện pháp xử lý kỹ thuật:
  - Lắp đặt các **vách ngăn chắn gió ngang (transverse surface wind baffles)** ngập sâu $0.5 - 1.0\ \text{m}$ dưới mặt nước, cách nhau $10 - 15\ \text{m}$ dọc theo chiều dài bể để ngắt quãng dòng chảy gió mặt.
  - Duy trì nghiêm ngặt tỷ lệ hình học bể lắng $L:H \le 20:1$ và $L:W \ge 4:1$.
  - Trồng cây xanh chắn gió xung quanh khu vực cụm bể lắng của nhà máy nước.

#### 5.7.3 Effluent Weir Updraft Suction & Pinpoint Floc Carryover
##### 5.7.3.1 Localized Updraft Flow Fields near Overflow Weirs
- Khi dòng nước tiếp cận mép vách tràn, các đường dòng hội tụ đột ngột hướng lên trên, tạo ra một trường vector vận tốc dâng thẳng đứng cục bộ ($v_{\text{upward}}$) ngay sát mép máng tràn.

##### 5.7.3.2 Excessive Weir Loading Rates ($\text{WLR} > 250\ \text{m}^3/\text{m}\cdot\text{d}$)
- Nếu tổng chiều dài vách tràn không đủ, tải trọng vách tràn vượt ngưỡng an toàn ($\text{WLR} > 200 - 250\ \text{m}^3/\text{m}\cdot\text{d}$), vận tốc dâng cục bộ này sẽ lớn hơn vận tốc lắng của các bông cặn nhỏ ($v_{\text{upward}} > v_s$), hút thẳng các bông cặn kim châm (pinpoint flocs) trào qua răng cưa máng tràn.

##### 5.7.3.3 Corrective Actions: Finger Launder Retrofits, Adjustable Leveling, Upstream Polymer Settling Aid Addition
- Biện pháp khắc phục:
  - Lắp đặt bổ sung các máng ngón tay nhánh vươn sâu vào bể để tăng tổng chiều dài vách tràn $L_w$, hạ thấp $\text{WLR} \le 150 - 180\ \text{m}^3/\text{m}\cdot\text{d}$.
  - Dùng máy thủy bình laser vi chỉnh lại cao độ các tấm răng cưa tam giác $90^\circ$ V-notch để đảm bảo nước tràn đều tăm tắp, không có điểm nào bị tràn ngập cục bộ.
  - Châm bổ sung một lượng nhỏ polymer trợ lắng (anionic/nonionic polymer liều lượng $0.05 - 0.10\ \text{mg/L}$) ở giai đoạn cuối bể tạo bông để gia cường độ bền liên kết và tăng kích thước bông cặn.

#### 5.7.4 Algal Biofouling & Sludge Accumulation in Inclined Settler Modules
##### 5.7.4.1 Benthic Photosynthetic Algae Proliferation in Shallow Clear Water
- Trong các bể lắng lamen ngoài trời, ánh sáng mặt trời xuyên thấu qua lớp nước trong nông ($< 1.0\ \text{m}$) chiếu trực tiếp vào miệng các ống lắng nghiêng. Đây là môi trường lý tưởng cho các loài tảo bám đáy (benthic algae) phát triển bùng phát, bám thành các mảng rêu sợi dày đặc trên vách nhựa.

##### 5.7.4.2 Sticky Coagulant Residue Deposition and Channel Bridging
- Lớp tảo kết hợp với các bông cặn hydroxit nhôm/sắt dính ướt tạo thành mảng cặn bám cứng, gây hiện tượng tắc nghẽn cục bộ các ống lắng (channel bridging), làm lệch dòng chảy và suy giảm nghiêm trọng diện tích lắng hữu hiệu.

##### 5.7.4.3 Corrective Maintenance: Automated Overhead Spray Washdown Headers, Pre-Chlorination Shocking, Opaque Covers
- Biện pháp bảo trì dự phòng:
  - Lắp đặt **hệ thống giàn ống phun nước áp lực cao cố định (overhead spray washdown headers)** trên đỉnh các khối module; định kỳ hàng tuần kích hoạt bơm phun tia nước áp lực $3 - 5\ \text{bar}$ súc rửa sạch rêu tảo và cặn bám trên miệng ống.
  - Châm clo sơ bộ (pre-chlorination) hoặc châm đồng sunfat ($\text{CuSO}_4$) kiểm soát tảo định kỳ nếu quy trình cho phép.
  - Lắp đặt mái che phủ kín hoặc các tấm nắp đậy bằng vật liệu composite đục cản sáng (opaque UV-blocking covers) phía trên khu vực đặt module lamen để triệt tiêu hoàn toàn ánh sáng quang hợp của tảo.

#### 5.7.5 Anaerobic Sludge Septicity, Gas-Lift Floatation & Odor Generation
##### 5.7.5.1 Anaerobic Biodegradation in Over-Detained Sludge Blankets ($\text{CH}_4, \text{CO}_2, \text{N}_2$ Generation)
- Khi chu kỳ xả bùn đáy quá dài hoặc hố thu bùn có góc nghiêng quá thoải làm bùn kẹt lại lâu ngày ($> 2 - 3\ \text{ngày}$), hàm lượng oxy hòa tan trong lớp bùn cặn nhanh chóng cạn kiệt. Các vi sinh vật kỵ khí phân hủy hợp chất hữu cơ trong bùn, giải phóng các sản phẩm khí sinh học không tan gồm metan ($\text{CH}_4$), cacbonic ($\text{CO}_2$), nitơ ($\text{N}_2$) và hydro sunfua ($\text{H}_2\text{S}$).

##### 5.7.5.2 Microbubble Attachment & Buoyancy Inversion (Rising Sludge Clumps)
- Các bọt khí siêu nhỏ sinh ra bị giữ lại bên trong mạng lưới bông bùn xốp. Khi tích tụ đủ lượng bọt khí, tỷ trọng biểu kiến của khối bông bùn giảm xuống nhỏ hơn tỷ trọng của nước ($\text{SG}_{\text{effective}} < 1.0$).
- Toàn bộ mảng bùn thối đen lập tức đảo ngược hướng chuyển động, nổi ngược lên mặt bể (hiệu ứng tuyển nổi tự nhiên - gas-lift rising sludge), tạo thành lớp váng bọt nổi dày đặc bốc mùi hôi thối và phá vỡ độ trong của nước sau lắng.

##### 5.7.5.3 Corrective Actions: Optimizing Sludge Pumping Schedules, Hopper Wall Steepening ($\ge 60^\circ$), Traveling Suction Headers
- Biện pháp khắc phục:
  - Rút ngắn chu kỳ xả bùn: Tăng tần suất xả đáy tự động qua van điều khiển PLC (ví dụ $4 - 6\ \text{lần/ngày}$ hoặc xả liên tục với lưu lượng nhỏ).
  - Đảm bảo độ dốc thành hố thu bùn luôn $\ge 60^\circ$ và lắp đặt đường ống xịt nước phá bùn bám đáy.
  - Sử dụng cầu cào bùn gắn bơm hút chìm trực tiếp thay vì cào dồn bùn cơ học để hút bùn tươi ra khỏi bể ngay trong ngày.

#### 5.7.6 Floc Shearing & Pinpoint Turbidity from High-Velocity Inflow Structures
##### 5.7.6.1 Upstream Over-Mixing ($G > 80\ \text{s}^{-1}$) and Orifice Port Jet Shear ($v_{\text{port}} > 0.4\ \text{m/s}$)
- Hiện tượng: Nước sau lắng có độ đục cao chứa toàn các hạt cặn siêu mịn li ti (pinpoint flocs), không chịu lắng dù thời gian lưu nước trong bể rất dài.
- Nguyên nhân thủy động học:
  - Ngăn cuối cùng của bể tạo bông có cường độ khuấy quá lớn ($G > 60 - 80\ \text{s}^{-1}$).
  - Hoặc vận tốc dòng nước đi qua kênh dẫn, van cửa phai, hoặc lỗ đục vách ngăn vào bể quá lớn ($v > 0.40 - 0.60\ \text{m/s}$). Tia nước vận tốc cao sinh ra gradient vận tốc cắt rất mạnh ($G > 100\ \text{s}^{-1}$), xé đứt hoàn toàn các cầu nối polymer và mạng lưới hydroxit nhôm/sắt vừa hình thành. Bông cặn bị vỡ vụn thành các hạt siêu nhỏ không thể tự kết tụ lại được.

##### 5.7.6.2 Corrective Engineering: Tapered Flocculation, Diffuser Wall Orifice Enlargement, Coagulant Dose Optimization
- Biện pháp xử lý kỹ thuật:
  - Áp dụng nguyên lý **tạo bông giảm dần (Tapered Flocculation)**: Giảm dần gradient vận tốc khuấy theo từng ngăn tạo bông (Ngăn 1: $G = 60 - 70\ \text{s}^{-1}$; Ngăn 2: $G = 30 - 40\ \text{s}^{-1}$; Ngăn 3: $G = 15 - 20\ \text{s}^{-1}$) để bông cặn lớn dần mà không bị vỡ.
  - Mở rộng diện tích mở của vách đục lỗ cửa vào ($A_{\text{open}} = 15 - 20\%$ diện tích mặt cắt), khống chế vận tốc qua lỗ nghiêm ngặt trong dải an toàn $v_{\text{port}} = 0.15 - 0.25\ \text{m/s}$.
  - Châm bổ sung polymer trợ tạo bông liều lượng nhỏ ($0.05\ \text{mg/L}$) để gia cường độ bền liên kết cơ học của bông cặn chống lại lực cắt thủy lực.
