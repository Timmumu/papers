# SLR Summary Matrix — 3rd Round (429 papers)

Review: *A Self-Improving Cognitive Digital Twin for Design-for-Safety and Design-for-Quality in the Built Environment.*
Screening follows `2 stage PRISMA guideline.md` — Prompt A (Step 1, title/abstract screening, columns G–K).
Data source: `429 papers.txt` (Endnote RIS export; Scopus / Web of Science / Lens.org).

**Step-1 decision rule:** Include only if G–K are all "Yes". Conservative: unsure → "No".

**Result: 165 Include / 264 Exclude** (incl. 6 cross-database duplicates excluded)

## Step 1 Screening — all 429 papers

| #   | ID   | Source         | Title (short)                                                           | G   | H   | I   | J   | K   | Decision    | Note                                                                                |
| --- | ---- | -------------- | ----------------------------------------------------------------------- | --- | --- | --- | --- | --- | ----------- | ----------------------------------------------------------------------------------- |
| 1   | 3566 | Scopus         | An association rule mining model for the application of construction t… | Yes | No  | No  | Yes | Yes | Exclude     | Tech-adoption survey (ARM); no DT, no DfS/DfQ focus                                 |
| 2   | 3741 | Scopus         | Digital twin and AI-driven smart adaptive walls for energy, comfort an… | Yes | Yes | No  | Yes | Yes | Exclude     | Energy/comfort/carbon optimization; safety shield is control constraint (edge 5)    |
| 3   | 3665 | Scopus         | Enhancing attack resilience of cyber-physical systems through state de… | No  | No  | No  | Yes | Yes | Exclude     | Cybersecurity of industrial CPS/SCADA; not AECO                                     |
| 4   | 3657 | Scopus         | IoT-Driven Resilience Monitoring: Case Study of a Cyber-Physical Syste… | No  | Yes | No  | Yes | Yes | Exclude     | Smart energy systems CI; not built environment                                      |
| 5   | 3685 | Scopus         | Virtual Fencing for Safety-Critical Cyber-Physical Systems: Computer-V… | No  | Yes | No  | Yes | Yes | Exclude     | Crowd management/surveillance; no built asset DfS/DfQ                               |
| 6   | 3756 | Scopus         | Lessons Learned from the Real-World Deployment of Multisensor Fusion f… | Yes | Yes | Yes | Yes | Yes | **Include** | Work-zone safety; predictive DT framework for conflict detection                    |
| 7   | 3978 | Web of Science | TOWARDS NEXT GENERATION CYBER-PHYSICAL SYSTEMS AND DIGITAL TWINS FOR C… | Yes | Yes | Yes | Yes | Yes | **Include** | Concept/scenario paper; DT+CPS for construction safety & health                     |
| 8   | 3527 | Scopus         | A methodological approach to hybrid AI systems for real-time infrastru… | Yes | No  | Yes | Yes | Yes | Exclude     | SHM hybrid AI; no DT built/proposed                                                 |
| 9   | 3963 | Web of Science | Neural network-based metamodel for scaffolding behavior: Application f… | Yes | No  | Yes | Yes | Yes | Exclude     | FEM+NN metamodel; authors state not a full digital twin                             |
| 10  | 3917 | Web of Science | Enhancing resilience through environmental data integration in early c… | Yes | No  | No  | Yes | Yes | Exclude     | BIM-ICDD semantic linking; no DT; compliance not DfQ                                |
| 11  | 3541 | Scopus         | Automation levels for nuclear reactor operations: A revised perspectiv… | No  | No  | No  | Yes | Yes | Exclude     | Nuclear power domain                                                                |
| 12  | 3903 | Web of Science | BIM-GIS integrated hydrodynamic modeling for road flood risk assessmen… | Yes | No  | Yes | Yes | Yes | Exclude     | BIM-HDM framework; DT only future early warning                                     |
| 13  | 3915 | Web of Science | Digital-Twin-Based Fire Safety Management Framework for Smart Building… | Yes | Yes | Yes | Yes | Yes | **Include** | DT-based fire safety management framework; conceptual + survey                      |
| 14  | 3668 | Scopus         | GUIDE2FR: A smart monitoring platform with a digital twin of a firefig… | Yes | Yes | Yes | Yes | Yes | **Include** | Building DT for emergency response & evacuation safety                              |
| 15  | 4053 | Web of Science | Practical Application of Digital Twins for Transportation Asset Data M… | Yes | Yes | Yes | Yes | Yes | **Include** | DT for guiderail safety-hardware condition & preventive maintenance                 |
| 16  | 3579 | Scopus         | State regulation of the IoT in the Russian Federation: Fundamentals an… | No  | No  | No  | Yes | Yes | Exclude     | Legal/regulatory IoT paper; not AECO                                                |
| 17  | 3838 | Scopus         | The Role of Artificial Intelligence in Shaping Intelligent Motorways: … | Yes | No  | No  | Yes | Yes | Exclude     | AI-in-motorways review; DT one of many topics                                       |
| 18  | 4020 | Web of Science | FingerCI: Writing industrial process specifications from network traff… | No  | Yes | No  | Yes | Yes | Exclude     | Cybersecurity; airport baggage system industrial testbed                            |
| 19  | 3842 | Scopus         | Seeking a Definition of Digital Twins for Construction and Infrastruct… | Yes | Yes | Yes | Yes | Yes | **Include** | DT definition/standardisation for construction; safety in scope                     |
| 20  | 4028 | Web of Science | Proposal of a conceptual model of digital twins for construction sites  | Yes | Yes | Yes | Yes | Yes | **Include** | DT conceptual model for site resource control incl. quality                         |
| 21  | 3828 | Scopus         | Serverless 3D Reconstruction and Spatial Anchoring for Cloud-Native In… | Yes | Yes | Yes | Yes | Yes | **Include** | Cloud DT for infrastructure inspection; defects as georeferenced anchors            |
| 22  | 3662 | Scopus         | Integration of Railway Bridge Structural Health Monitoring into the In… | Yes | Yes | Yes | Yes | Yes | **Include** | DT SHM, anomaly detection, damage warnings; 2-yr pilot                              |
| 23  | 3975 | Web of Science | Methodological framework for integrating structural health monitoring … | Yes | Yes | Yes | Yes | Yes | **Include** | SHM-DT framework, damage levels, early warning; heritage basilica                   |
| 24  | 3996 | Web of Science | Driving Factors for the Adoption of Digital Twin Technology Implementa… | Yes | Yes | Yes | Yes | Yes | **Include** | Adoption drivers incl. safety & quality factors; survey                             |
| 25  | 4030 | Web of Science | Excavator 3D pose estimation using deep learning and hybrid datasets    | Yes | No  | Yes | Yes | Yes | Exclude     | CV pose estimation; DT only synthesizes training data                               |
| 26  | 3982 | Web of Science | Integrating Web-Based Weather Data into Building Information Modeling … | Yes | No  | Yes | Yes | Yes | Exclude     | BIM+RPA weather alerts; static BIM, no live DT                                      |
| 27  | 3940 | Web of Science | Circular economy in construction: The digital transformation perspecti… | Yes | No  | No  | Yes | Yes | Exclude     | CE/digitalisation review; DT peripheral                                             |
| 28  | 4037 | Web of Science | Intelligent technologies for tunnel construction and maintenance: A st… | Yes | Yes | Yes | Yes | Yes | **Include** | Review incl. geological DT, real-time risk analysis, construction safety            |
| 29  | 3551 | Scopus         | Improving Organizational and Engineering Reliability during Dismantlin… | Yes | No  | Yes | Yes | No  | Exclude     | Russian journal; BIM/DT mentioned, full text non-English                            |
| 30  | 3571 | Scopus         | The Process of Digitalization of the Urban Environment for the Develop… | Yes | No  | No  | Yes | Yes | Exclude     | Urban regeneration protocol; DT as future archive                                   |
| 31  | 3707 | Scopus         | Construction and application of digital twin system for coal ports      | No  | Yes | Yes | Yes | No  | Exclude     | Industrial port ops; Chinese journal, non-English                                   |
| 32  | 3613 | Scopus         | Incorporation of pre-existing longitudinal cracks in finite element an… | Yes | No  | Yes | Yes | Yes | Exclude     | Pure FEM structural analysis; no DT                                                 |
| 33  | 3645 | Scopus         | The evolution of BIM work standards: current, best, and future practic… | Yes | No  | No  | Yes | Yes | Exclude     | BIM-manager narrative review; no DT core                                            |
| 34  | 3807 | Scopus         | Railway condition information modelling in a BIM framework for mainten… | Yes | No  | Yes | Yes | Yes | Exclude     | I-BIM maintenance framework; DT aspirational                                        |
| 35  | 3595 | Scopus         | Digital Twin conceptual framework for improving critical infrastructur… | Yes | Yes | Yes | Yes | Yes | **Include** | DT framework for critical infrastructure resilience & crisis mgmt                   |
| 36  | 3888 | Web of Science | From BIM to Web3: A critical interpretive synthesis of present and eme… | Yes | No  | No  | Yes | Yes | Exclude     | Data-management review; no DT core, no safety/quality                               |
| 37  | 3869 | Scopus         | Affective computing in smart city spaces: Research on emotion recognit… | No  | No  | No  | Yes | Yes | Exclude     | Emotion recognition; no built asset, no safety/quality                              |
| 38  | 3702 | Scopus         | TunnelSDF-FilterNet: A Domain-Aware Neural Framework for High-Fidelity… | Yes | No  | Yes | Yes | Yes | Exclude     | Neural-SDF reconstruction; DT only downstream use                                   |
| 39  | 3901 | Web of Science | Methodology for 3D Management of University Faculties Using Integrated… | Yes | No  | No  | Yes | Yes | Exclude     | Static GIS-BIM/CMMS-3D; no live DT                                                  |
| 40  | 3889 | Web of Science | Integration of BIM Tools for the Facility Management of Railway Bridge… | Yes | No  | Yes | Yes | Yes | Exclude     | BIM-Dynamo automation; initial step towards DT only                                 |
| 41  | 3555 | Scopus         | Climate Change Impacts on Reinforced Concrete Structures: A Bibliometr… | Yes | No  | No  | Yes | Yes | Exclude     | Bibliometric; DT only a keyword trend                                               |
| 42  | 3658 | Scopus         | AI based surrogate model for digital twins in structural health monito… | Yes | Yes | Yes | Yes | Yes | **Include** | ANN surrogate within DT for bridge SHM, safety info, life-cycle                     |
| 43  | 3958 | Web of Science | Integration of Emerging Technologies with Construction Practices in Au… | Yes | No  | No  | Yes | Yes | Exclude     | Tech-adoption survey; DT one of many                                                |
| 44  | 3936 | Web of Science | Digital twinning of building construction processes. Case study: A rei… | Yes | Yes | Yes | Yes | Yes | **Include** | Real DT prototype on office-building site; health & safety potential                |
| 45  | 3795 | Scopus         | Risk Mitigation of a Heritage Bridge Using Noninvasive Sensors          | Yes | Yes | Yes | Yes | Yes | **Include** | DT structural model validated on field data; what-if risk scenarios                 |
| 46  | 3998 | Web of Science | Autonomous dimensional inspection and issue tracking of rebar using se… | Yes | Yes | Yes | Yes | Yes | **Include** | DT generation module + CV inspection; quality defect tracking                       |
| 47  | 3984 | Web of Science | A transformer-based surrogate modeling strategy for tunnel digital twi… | Yes | Yes | Yes | Yes | Yes | **Include** | DT framework for settlement/deformation prediction; safety & risk                   |
| 48  | 3601 | Scopus         | Digital twin-based experimental method for construction loads of adjac… | Yes | Yes | Yes | Yes | No  | Exclude     | Chinese journal; full text non-English                                              |
| 49  | 3911 | Web of Science | Digital Twin-Based and Knowledge Graph-Enhanced Emergency Response in … | Yes | Yes | Yes | Yes | Yes | **Include** | Real-time risk assessment, hazard inference, tunnel project applied                 |
| 50  | 3953 | Web of Science | Digital Twin-Enabled Robust Parallel Control of Construction Engineeri… | Yes | Yes | Yes | Yes | Yes | **Include** | DT for gin-pole lifting; safety risk reduced 32%                                    |
| 51  | 3873 | Scopus         | Construction and application of Digital Twin model of pipeline          | No  | Yes | Yes | Yes | No  | Exclude     | Oil/gas pipeline industry; Chinese journal, non-English                             |
| 52  | 3745 | Scopus         | Monitoring Construction and System Development of Bridge Horizontal Ro… | Yes | Yes | Yes | Yes | No  | Exclude     | Chinese journal; non-English full text                                              |
| 53  | 3509 | Scopus         | Multi-Modal Excavator Activity Recognition Using Two-Stream CNN-LSTM w… | Yes | No  | Yes | Yes | Yes | Exclude     | CV activity recognition; DT integration future work                                 |
| 54  | 3529 | Scopus         | Guidance for Materials 4.0 to interact with a digital twin              | No  | Yes | No  | Yes | Yes | Exclude     | Materials/manufacturing component DT; not AECO                                      |
| 55  | 3660 | Scopus         | On-Site Safety Inspections Through Marker-Less Augmented Reality and B… | Yes | No  | Yes | Yes | Yes | Exclude     | BIM+AR safety inspection; no DT (duplicate of #56)                                  |
| 56  | 3931 | Web of Science | On-Site Safety Inspections Through Marker-Less Augmented Reality and B… | Yes | No  | Yes | Yes | Yes | Exclude     | Duplicate of ID 3660 (WoS copy); BIM-based, no DT                                   |
| 57  | 3679 | Scopus         | Intelligent Transportation Systems Using Roadside Infrastructure: A Li… | No  | No  | No  | Yes | Yes | Exclude     | Traffic ITS survey; DT only future distribution topic                               |
| 58  | 3651 | Scopus         | The role of the foundation flexibility on the seismic response of a mo… | Yes | No  | Yes | Yes | Yes | Exclude     | Pure FE soil-structure interaction study; no DT                                     |
| 59  | 3830 | Scopus         | For how large soil shear wave velocity the soil-structure interaction … | Yes | No  | Yes | Yes | Yes | Exclude     | Pure FE seismic SSI analysis; no DT                                                 |
| 60  | 3793 | Scopus         | Online traffic load identification of high-speed railway bridge using … | Yes | No  | Yes | Yes | Yes | Exclude     | Load-identification method; DT only data consumer                                   |
| 61  | 3802 | Scopus         | Digital Twin System of Bridges Group Based on Machine Vision Fusion Mo… | Yes | Yes | Yes | Yes | Yes | **Include** | Regional bridge-group DT; condition perception & safety warning                     |
| 62  | 4007 | Web of Science | Assessing the Suitability of Damage Indexes for Digital Twin Applicati… | Yes | No  | Yes | Yes | Yes | Exclude     | Damage-index benchmarking; DT only future use                                       |
| 63  | 3708 | Scopus         | The role of the marine research infrastructures in the European marine… | No  | No  | No  | Yes | Yes | Exclude     | Marine science RIs; not AECO                                                        |
| 64  | 3631 | Scopus         | Enhancing Operational Resilience of Critical Infrastructure Processes … | No  | Yes | No  | Yes | Yes | Exclude     | Oil-refinery process CPS; industrial                                                |
| 65  | 3626 | Scopus         | Interconnected digital twins of subway stations for decision support s… | Yes | Yes | Yes | Yes | Yes | **Include** | Station DTs for incident decision support; response -17.4%                          |
| 66  | 3967 | Web of Science | Structural Analysis of Construction Risk Management Assessment Model B… | Yes | Yes | Yes | Yes | Yes | **Include** | DTCRAM for construction risk prediction/control                                     |
| 67  | 4036 | Web of Science | Real-time bridge disaster management: Enabling technology and applicat… | Yes | Yes | Yes | Yes | Yes | **Include** | RtBDM framework; real-time monitoring & decision for bridge safety                  |
| 68  | 3760 | Scopus         | Integrating LLMs and Digital Twins for Adaptive Multi-Robot Task Alloc… | Yes | Yes | Yes | Yes | Yes | **Include** | Closed-loop site DT + LLM; productivity & safety motivation                         |
| 69  | 3521 | Scopus         | Application Benefit Analysis of Digital Twin Technology in Tunnel Cons… | Yes | Yes | Yes | Yes | No  | Exclude     | Chinese journal (Tunnel Construction); non-English                                  |
| 70  | 4002 | Web of Science | Smart building evacuation by tracking multi-camera network and explain… | Yes | No  | Yes | Yes | Yes | Exclude     | CV tracking framework; DT as end-goal only                                          |
| 71  | 3528 | Scopus         | Digital twin system construction method for evaluating load carrying c… | Yes | Yes | Yes | Yes | No  | Exclude     | Chinese journal (CIMS); non-English full text                                       |
| 72  | 3736 | Scopus         | Stakeholder-informed renovation digital twin for multi-domain monitori… | Yes | Yes | Yes | Yes | Yes | **Include** | Renovation DT tracking quality & safety KPIs; pilot + TAM                           |
| 73  | 3625 | Scopus         | Digital twin-driven on-line monitoring method of metal selective laser… | No  | Yes | Yes | Yes | No  | Exclude     | Additive manufacturing; Chinese journal, non-English                                |
| 74  | 3906 | Web of Science | Digital Twins for Construction Assets Using BIM Standard Specification… | Yes | Yes | Yes | Yes | Yes | **Include** | SLR (229 pubs) + ISO 19650-based DT framework for construction assets               |
| 75  | 3921 | Web of Science | Predictive digital monitoring of construction resources: an integrated… | Yes | Yes | No  | Yes | Yes | Exclude     | DTSRM for cost/time/resources; safety only as extension                             |
| 76  | 4046 | Web of Science | Exploring Data for Construction Digital Twins: Building Health and Saf… | Yes | Yes | Yes | Yes | Yes | **Include** | Highway project DT demonstrators incl. health & safety twin                         |
| 77  | 3912 | Web of Science | Seismic Failure Mechanism Shift in RC Buildings Revealed by NDT-Suppor… | Yes | No  | Yes | Yes | Yes | Exclude     | Level-2 static twin = calibrated BIM; no live data link                             |
| 78  | 4029 | Web of Science | Intervention and management of construction workers' unsafe behavior: … | Yes | Yes | Yes | Yes | Yes | **Include** | Closed-loop simulation DT for unsafe-behavior intervention                          |
| 79  | 3782 | Scopus         | A scientometric analysis of drone-based structural health monitoring a… | Yes | No  | Yes | Yes | Yes | Exclude     | Scientometric review; DT only integration trend                                     |
| 80  | 3955 | Web of Science | Development of a BIM and IoT-Based Smart Lighting Maintenance System P… | Yes | Yes | No  | Yes | Yes | Exclude     | FM reactive maintenance; safety incidental                                          |
| 81  | 3632 | Scopus         | Machine learning for design and analysis of steel frame halls           | Yes | No  | No  | Yes | Yes | Exclude     | AI design co-pilot; no DT                                                           |
| 82  | 4048 | Web of Science | Maschinelles Lernen beim Entwurf und der Bemessung von Stahlrahmenhall… | Yes | No  | No  | Yes | No  | Exclude     | German duplicate of ID 3632; non-English                                            |
| 83  | 3824 | Scopus         | Preliminary architecture design for human-in-the-loop control of robot… | No  | Yes | No  | Yes | Yes | Exclude     | Fusion-reactor maintenance robotics; not AECO                                       |
| 84  | 3493 | Scopus         | Digital twins in bridge engineering for streamlined maintenance and en… | Yes | Yes | Yes | Yes | Yes | **Include** | Adaptable bridge DT; what-if simulations; safety & lifespan                         |
| 85  | 4032 | Web of Science | Resilient ventilation network construction in complex underground mini… | No  | Yes | Yes | Yes | Yes | Exclude     | Mining ventilation; not AECO built environment                                      |
| 86  | 3775 | Scopus         | Digital twin-based vibration displacement sensing and recognition tech… | Yes | Yes | Yes | Yes | Yes | **Include** | DT safety-management model; stress prediction 99.1% (verify Step 3)                 |
| 87  | 3826 | Scopus         | Cooperative Localization in Transportation 5.0                          | No  | No  | No  | Yes | Yes | Exclude     | Vehicle localization framework; not AECO                                            |
| 88  | 3876 | Web of Science | Bridge Digital Twin for Practical Bridge Operation and Maintenance by … | Yes | Yes | Yes | Yes | Yes | **Include** | Integrated WebGIS+WebBIM DT; defect modeling, maintenance, safety                   |
| 89  | 3786 | Scopus         | Virtual and Augmented Reality Use Cases for Fusion Design Engineering   | No  | No  | No  | Yes | Yes | Exclude     | Fusion-energy facility design; not AECO                                             |
| 90  | 3778 | Scopus         | Digital twin for smart coal mining workface: Technological frame and c… | No  | Yes | Yes | Yes | No  | Exclude     | Mining; Chinese journal, non-English                                                |
| 91  | 3797 | Scopus         | Construction of Autonomous Collaborative Resource Control System for E… | No  | Yes | No  | Yes | Yes | Exclude     | EV charging/IoV scheduling; not AECO                                                |
| 92  | 3979 | Web of Science | Integrating multi-source data for life-cycle risk assessment of bridge… | Yes | Yes | Yes | Yes | Yes | **Include** | BN-based system DT; multi-source data; bridge-network risk                          |
| 93  | 3962 | Web of Science | Federation of non-destructive testing data for bridge asset management  | Yes | No  | Yes | Yes | Yes | Exclude     | NDT data federation in Revit; DT as future tool                                     |
| 94  | 3542 | Scopus         | Construction of damage-free digital twin of damaged aero-engine blades… | No  | Yes | No  | Yes | Yes | Exclude     | Aerospace remanufacturing                                                           |
| 95  | 3580 | Scopus         | The Conventional Construction Scenario and the Emergence of Advance Te… | Yes | No  | No  | Yes | Yes | Exclude     | Tech-adoption survey; DT one item in a list                                         |
| 96  | 3611 | Scopus         | Digital twin driven airflow intelligent control system for the air out… | No  | Yes | Yes | Yes | No  | Exclude     | Mining ventilation; Chinese journal, non-English                                    |
| 97  | 4005 | Web of Science | Mixed Reality for Safe and Reliable Human-Robot Collaboration in Timbe… | Yes | Yes | Yes | Yes | Yes | **Include** | Robot DT for motion preview & safe workspace entry; construction HRC                |
| 98  | 3652 | Scopus         | Protecting critical infrastructure against cascading effects: The PREC… | No  | Yes | No  | Yes | Yes | Exclude     | Cyber-physical security of CI generally; not AECO-specific                          |
| 99  | 3942 | Web of Science | Robotic devices for Structural Health Monitoring                        | Yes | No  | Yes | Yes | Yes | Exclude     | Robotics-for-SHM review; DT creation only attempts                                  |
| 100 | 4026 | Web of Science | Data-Driven Condition Assessment and Life Cycle Analysis Methods for D… | Yes | Yes | Yes | Yes | Yes | **Include** | 4-stage concept incl. FE-based DT; safety concept & remaining-life                  |
| 101 | 4031 | Web of Science | Dynamic train-bridge compatibility: the reference method as a new form… | Yes | No  | Yes | Yes | Yes | Exclude     | Train-bridge dynamic compatibility verification; no DT                              |
| 102 | 3577 | Scopus         | A Metaverse-Based Teaching Building Evacuation Training System With De… | Yes | Yes | Yes | Yes | Yes | **Include** | Metaverse+DRL evacuation training; building fire safety                             |
| 103 | 3908 | Web of Science | The Challenge of Machine Learning and Artificial Intelligence in the C… | Yes | Yes | No  | Yes | Yes | Exclude     | AI/DT challenges perspective; energy transition focus, safety peripheral            |
| 104 | 3977 | Web of Science | AN INTELLIGENT CONSTRUCTION SYSTEM BASED ON DIGITAL TWIN AND FOUNDATIO… | Yes | Yes | Yes | Yes | Yes | **Include** | DT×Transformer closed-loop for SCP operations; risk prediction, AR execution        |
| 105 | 3609 | Scopus         | Study on the Construction and Application of Digital Twins on High Vol… | No  | Yes | Yes | Yes | Yes | Exclude     | High-voltage live-line work; power industry, not AECO                               |
| 106 | 3924 | Web of Science | A methodology for sky-space-ground integrated remote sensing monitorin… | Yes | Yes | Yes | Yes | Yes | **Include** | Data-BIM DT framework for residential quality monitoring                            |
| 107 | 3980 | Web of Science | Digital twin-enabled cooperative autonomous truck platooning framework… | No  | Yes | No  | Yes | Yes | Exclude     | Truck platooning logistics; not AECO                                                |
| 108 | 4045 | Web of Science | Exploring the Impact of Construction 4.0 on Industrial Relations: A Co… | Yes | No  | No  | Yes | Yes | Exclude     | Construction 4.0 industrial-relations SLR; DT one theme                             |
| 109 | 3770 | Scopus         | Participatory Sensing and Digital Twin City: Updating Virtual City Mod… | Yes | Yes | Yes | Yes | Yes | **Include** | Participatory sensing DT city for risk-informed decisions; physical vulnerability   |
| 110 | 3926 | Web of Science | Construction Path of Shanghai Oriental Hub Municipal Pipeline Full Cyc… | Yes | Yes | Yes | Yes | Yes | **Include** | Full-cycle municipal pipeline DT platform; safe operation focus                     |
| 111 | 3959 | Web of Science | Enhancing worker monitoring and management on large-scale construction… | Yes | Yes | Yes | Yes | Yes | **Include** | UAV+DT worker monitoring & authorization; operational safety                        |
| 112 | 3765 | Scopus         | Digital twin-driven pose estimation and trajectory prediction for modu… | Yes | Yes | Yes | Yes | Yes | **Include** | DT-driven pose/trajectory prediction for MiC stacking; collision prevention         |
| 113 | 3913 | Web of Science | A Method for Building a Mixed-Reality Digital Twin of a Roadheader Mon… | No  | Yes | Yes | Yes | Yes | Exclude     | Coal-mine roadheader MR-DT; mining domain                                           |
| 114 | 3636 | Scopus         | A TOOL-BASED SYSTEM ARCHITECTURE FOR A DIGITAL TWIN: A CASE STUDY IN A… | Yes | Yes | No  | Yes | Yes | Exclude     | Healthcare OR air-quality DT; FM/IAQ, no DfS/DfQ                                    |
| 115 | 3973 | Web of Science | Augmented reality and digital twin system for interaction with constru… | Yes | Yes | Yes | Yes | Yes | **Include** | AR+DT CPS for construction machinery; precision & safety                            |
| 116 | 3735 | Scopus         | ANCHOR-Grid: Authenticating Smart Grid Digital Twins Using Real-World … | No  | Yes | No  | Yes | Yes | Exclude     | Smart-grid DT authentication; power/cybersecurity                                   |
| 117 | 3537 | Scopus         | Navigating the Future: Developing Smart Fairways for Enhanced Maritime… | No  | Yes | Yes | Yes | Yes | Exclude     | Maritime smart fairways; not AECO                                                   |
| 118 | 3813 | Scopus         | Toward intelligent tunnel construction: The universal discontinuity in… | Yes | Yes | Yes | Yes | Yes | **Include** | UDi probabilistic rock-block failure prediction in DT workflow; tunnel safety       |
| 119 | 4018 | Web of Science | Toward intelligent tunnel construction: The universal discontinuity in… | Yes | Yes | Yes | Yes | Yes | Exclude     | Duplicate of ID 3813 (WoS copy)                                                     |
| 120 | 3556 | Scopus         | Exploring the Construction of a Composite Risk Prevention and Control … | Yes | Yes | Yes | Yes | No  | Exclude     | Chinese journal (Underground Space); non-English full text                          |
| 121 | 3558 | Scopus         | An Integrated Intelligent Approach for Monitoring and Management of a … | Yes | Yes | Yes | Yes | Yes | **Include** | Deep foundation pit DT platform; multi-source sensing + ML prediction               |
| 122 | 3886 | Web of Science | Digital construction site layout planning and real-time trajectory ana… | Yes | Yes | Yes | Yes | Yes | **Include** | DTCS RAM module; struck-by hazard trajectory analysis; SIF prevention               |
| 123 | 3949 | Web of Science | Advancing Smart Construction Management: A Comprehensive Analysis of D… | Yes | Yes | Yes | Yes | Yes | **Include** | SLR of 395 DT-construction papers incl. safety management                           |
| 124 | 3501 | Scopus         | Construction of Digital Twin System for Cold Chain Logistics Stereo Wa… | No  | Yes | Yes | Yes | Yes | Exclude     | Cold-chain warehouse logistics; not AECO                                            |
| 125 | 3956 | Web of Science | Multi-dimensional framework for assessing digital twin maturity in con… | Yes | Yes | Yes | Yes | Yes | **Include** | DT maturity model for construction machinery; safety & efficiency                   |
| 126 | 3971 | Web of Science | Construction of a digital twin system for the blended-wing-body underw… | No  | Yes | No  | Yes | Yes | Exclude     | Underwater glider DT; marine robotics                                               |
| 127 | 3642 | Scopus         | Design verification and in-service performance evaluation model for hi… | Yes | Yes | Yes | Yes | No  | Exclude     | Chinese journal (J. Building Structures); non-English full text                     |
| 128 | 3575 | Scopus         | An intelligent BIM-enabled digital twin framework for real-time struct… | Yes | Yes | Yes | Yes | Yes | **Include** | BIM-enabled DT for real-time SHM; IoT+DSP+structural analysis                       |
| 129 | 3666 | Scopus         | Research on an intelligent monitoring system for the entire tunnel con… | Yes | Yes | Yes | Yes | Yes | **Include** | IoT+DT whole-process tunnel construction monitoring; collapse capture               |
| 130 | 3976 | Web of Science | Parametric modeling and safety simulation of pit excavation affecting … | Yes | No  | Yes | Yes | Yes | Exclude     | BIM-FEM excavation analysis; no live DT data link                                   |
| 131 | 3790 | Scopus         | Research and design of intelligent mine ventilation construction archi… | No  | No  | Yes | Yes | Yes | Exclude     | Mine ventilation intelligence; mining, no DT built                                  |
| 132 | 3821 | Scopus         | Smart Monitoring System of Bridge Erecting Machine Operation Status In… | Yes | Yes | Yes | Yes | No  | Exclude     | Chinese journal (China J. Highway Transport); non-English                           |
| 133 | 3987 | Web of Science | A REVIEW OF DRIVERS AND BARRIERS OF DIGITAL TWIN ADOPTION IN BUILDING … | Yes | Yes | No  | Yes | Yes | Exclude     | DT adoption drivers/barriers review; safety not in scope focus                      |
| 134 | 4050 | Web of Science | Investigating the Applicability of Industry 4.0 Technologies in Road C… | Yes | No  | No  | Yes | Yes | Exclude     | C4.0 readiness survey in road projects; DT one of 16 techs                          |
| 135 | 3563 | Scopus         | Building digital-twin virtual machining for milling chatter detection … | No  | Yes | Yes | Yes | Yes | Exclude     | Milling chatter detection; manufacturing                                            |
| 136 | 3592 | Scopus         | Dynamic Cost Control of Construction Engineering Projects Using Multi-… | Yes | Yes | No  | Yes | Yes | Exclude     | DT for dynamic cost control; no safety/quality angle                                |
| 137 | 3930 | Web of Science | Underpass clearance checking in highway widening projects using digita… | Yes | Yes | Yes | Yes | Yes | **Include** | DT clearance checking for underpasses; collision prevention at design               |
| 138 | 3784 | Scopus         | Monitoring System for the Construction of Arch Cover Method Subway Sta… | Yes | Yes | Yes | Yes | Yes | **Include** | DT+IoT monitoring of arch-cover subway station construction; early warning          |
| 139 | 3630 | Scopus         | Building facility virtual inspection system design and implementation … | Yes | Yes | Yes | Yes | No  | Exclude     | Chinese journal (J. Civil & Environmental Eng.); non-English                        |
| 140 | 4054 | Web of Science | Application of the multimodal model for predicting rock mechanical par… | Yes | No  | Yes | Yes | Yes | Exclude     | MWD rock-parameter prediction; no DT                                                |
| 141 | 3605 | Scopus         | Intelligent control of building fire protection system using digital t… | Yes | Yes | Yes | Yes | Yes | **Include** | DT+semantic web intelligent control of building fire protection                     |
| 142 | 3794 | Scopus         | Digital twin driven intelligent assessment method for structural safet… | Yes | Yes | Yes | Yes | No  | Exclude     | Chinese journal (China Civil Eng. Journal); non-English                             |
| 143 | 3572 | Scopus         | Digital twin: Stability analysis for tower crane hoisting safety with … | Yes | Yes | Yes | Yes | Yes | **Include** | DT of tower-crane hoisting stability; scale-model experiments                       |
| 144 | 3872 | Scopus         | Early-warning of unsafe hoisting operations: An integration of digital… | Yes | Yes | Yes | Yes | Yes | **Include** | DT+KG early-warning of unsafe hoisting operations                                   |
| 145 | 3599 | Scopus         | Enhancing Autonomous Vehicle Localization Through Cooperative LiDAR an… | No  | No  | No  | Yes | Yes | Exclude     | AV localization via roadside LiDAR; not AECO                                        |
| 146 | 3832 | Scopus         | Intelligent Transition of Automotive Industry Driven by Autonomous Dri… | No  | Yes | No  | Yes | No  | Exclude     | Autonomous-driving simulation; Chinese journal, non-English                         |
| 147 | 3789 | Scopus         | Automated quantification of construction workers’ exposure to falling … | Yes | No  | Yes | Yes | Yes | Exclude     | BIM+AI+sensor hazard exposure quantification; no DT                                 |
| 148 | 4027 | Web of Science | Knowledge graph exploitation to enhance the usability of risk assessme… | Yes | Yes | Yes | Yes | Yes | **Include** | KG exploitation on DTs for construction safety planning usability                   |
| 149 | 4023 | Web of Science | The influence of information from digital buildings on fire service op… | Yes | No  | Yes | Yes | Yes | Exclude     | Fire-service information needs; no DT system built                                  |
| 150 | 3854 | Scopus         | Mathematical Framework for Airport as Cognitive Digital Twin of Aviati… | No  | Yes | No  | Yes | Yes | Exclude     | Airport as cognitive DT of aviation ecosystem; not AECO asset                       |
| 151 | 4012 | Web of Science | Constructing a Reliable Health Indicator for Bearings Using Convolutio… | No  | No  | No  | Yes | Yes | Exclude     | Bearing RUL health indicator; manufacturing                                         |
| 152 | 3731 | Scopus         | The overlooked frontier of AI in construction: conversational, documen… | Yes | No  | No  | Yes | Yes | Exclude     | Document-native AI for admin workflows; no DT                                       |
| 153 | 3584 | Scopus         | Station biophilia–assessing the perception of greenery on railway plat… | Yes | Yes | No  | Yes | Yes | Exclude     | Station greenery perception via DT; well-being, not DfS/DfQ                         |
| 154 | 4024 | Web of Science | AI-based risk assessment for construction site disaster preparedness t… | Yes | Yes | Yes | Yes | Yes | **Include** | Vision-based DT for wind-borne debris risk; hurricane preparedness                  |
| 155 | 3644 | Scopus         | Analyzing Safety Risk Imposed by Jobsite Debris to Nearby Built Enviro… | Yes | Yes | Yes | Yes | Yes | **Include** | Geometric DTs of jobsite debris; glazing failure risk of nearby buildings           |
| 156 | 3643 | Scopus         | Digital Twin-Enabled Incident Detection and Response: A Systematic Rev… | No  | Yes | No  | Yes | Yes | Exclude     | CI cybersecurity incident detection SLR; not AECO-specific                          |
| 157 | 3523 | Scopus         | Intelligent digital methods for extending the service life of the Nibe… | Yes | No  | Yes | Yes | No  | Exclude     | German journal (Beton- und Stahlbetonbau); non-English full text                    |
| 158 | 3792 | Scopus         | Effective Underground Facilities Management in Virtual Reality by Appl… | Yes | Yes | Yes | Yes | Yes | **Include** | VR+DT training simulator for underground utility tunnel management safety           |
| 159 | 3608 | Scopus         | Generation and Verification of CFD-based ROM for Real-Time Thermal Flo… | No  | Yes | Yes | Yes | No  | Exclude     | Nuclear containment ROM; Korean journal, non-English                                |
| 160 | 4008 | Web of Science | Reinforcement learning for control and optimization of real buildings:… | Yes | No  | No  | Yes | Yes | Exclude     | RL control of building energy; safety of RL only, not DfS                           |
| 161 | 3750 | Scopus         | A Digital Twin Framework Utilizing Machine Learning for Robust Predict… | No  | Yes | Yes | Yes | Yes | Exclude     | Tire health DT; automotive                                                          |
| 162 | 3604 | Scopus         | ADVANCING CIVIL INFRASTRUCTURE WITH DIGITAL TWINS: A REVIEW OF APPLICA… | Yes | Yes | Yes | Yes | Yes | **Include** | DT survey: SHM, predictive maintenance, infrastructure safety                       |
| 163 | 3517 | Scopus         | Digital Twin for Safety and Security: Perspectives on Building Lifecyc… | Yes | Yes | Yes | Yes | Yes | **Include** | DT for building safety & security lifecycle; fire + anomaly use cases               |
| 164 | 3883 | Web of Science | Automation of shape quality control for precast concrete members using… | Yes | No  | Yes | Yes | Yes | Exclude     | 3D-scan+BIM precast shape QC; no live DT                                            |
| 165 | 3916 | Web of Science | Constructing a digital twin for estimating the response and load of a … | Yes | Yes | Yes | Yes | Yes | **Include** | DT estimating piping response/load under seismic; real-time ROM                     |
| 166 | 3548 | Scopus         | Active gravity-aligned reference Axis for high-precision verticality a… | Yes | No  | Yes | Yes | Yes | Exclude     | Verticality sensing device; DT only beneficiary (edge 3)                            |
| 167 | 3938 | Web of Science | Spatio-temporal heat risk analysis in construction: Digital twin-enabl… | Yes | Yes | Yes | Yes | Yes | **Include** | DT-enabled spatio-temporal heat risk monitoring for workers                         |
| 168 | 3999 | Web of Science | Advanced fire emergency management based on potential fire risk assess… | Yes | Yes | Yes | Yes | Yes | **Include** | Informative DT fire emergency management; evacuation risk                           |
| 169 | 3808 | Scopus         | Digital twin for natural gas infrastructure operation and management v… | No  | Yes | Yes | Yes | Yes | Exclude     | Natural gas pipeline DMD-DT; energy utility ops                                     |
| 170 | 3827 | Scopus         | Digital twin of a building as the basis for the application of nanotec… | Yes | Yes | No  | Yes | No  | Exclude     | Russian journal (Nanotechnologies in Construction); non-English                     |
| 171 | 3738 | Scopus         | Detection of Defects in Polyethylene and Polyamide Flat Panels Using A… | No  | No  | Yes | Yes | Yes | Exclude     | Ultrasound defect detection in plastic panels; manufacturing NDT                    |
| 172 | 3897 | Web of Science | A PLS-SEM based framework for enabling digital twin systems for real-t… | Yes | Yes | No  | Yes | Yes | Exclude     | PLS-SEM framework for DT monitoring; productivity focus, no DfS/DfQ                 |
| 173 | 3859 | Scopus         | A Study on the Prioritization and Combination Strategies of Smart Safe… | Yes | No  | Yes | Yes | No  | Exclude     | Korean journal (JAIK); non-English full text                                        |
| 174 | 3507 | Scopus         | State-of-Art review of resilience of bridges and bridge networks        | Yes | No  | Yes | Yes | Yes | Exclude     | Bridge resilience review; DT only in proposed future framework                      |
| 175 | 4051 | Web of Science | Automatic Object Detection in Radargrams of Multi-Antenna GPR Systems … | Yes | No  | Yes | Yes | Yes | Exclude     | GPR antenna DT for data simulation; no asset DT                                     |
| 176 | 3591 | Scopus         | Building a Lightweight Digital Twin of a Crane Boom for Structural Saf… | Yes | Yes | Yes | Yes | Yes | **Include** | Lightweight multifidelity-surrogate DT of crane boom; structural safety             |
| 177 | 3748 | Scopus         | Reconstruction of the road bridge on Monte Cassino Avenue in Koszalin   | Yes | No  | Yes | Yes | Yes | Exclude     | Bridge reconstruction case; verified FE "element of a DT" only                      |
| 178 | 3712 | Scopus         | Post-Earthquake Building Evaluation Using UAVs: A BIM-Based Digital Tw… | Yes | Yes | Yes | Yes | Yes | **Include** | BIM-based DT framework for post-earthquake building evaluation                      |
| 179 | 3612 | Scopus         | Intelligent Monitoring Platform and Application for Building Energy Us… | Yes | Yes | No  | Yes | Yes | Exclude     | Building energy monitoring DT; energy focus (edge 5)                                |
| 180 | 3728 | Scopus         | Applications of artificial intelligence in the AEC industry: a review … | Yes | No  | No  | Yes | Yes | Exclude     | AI-in-AEC review; DT only future direction                                          |
| 181 | 3661 | Scopus         | Automated generation and semantic segmentation of roof orthophoto for … | Yes | Yes | Yes | Yes | Yes | **Include** | DT-based roof monitoring; orthophoto + segmentation; deterioration hazards          |
| 182 | 3937 | Web of Science | Rapid integration strategy for oblique photogrammetry terrain and high… | Yes | No  | No  | Yes | Yes | Exclude     | OPDM-BIM integration method; DT as context only                                     |
| 183 | 3839 | Scopus         | 3D laser point cloud-based geometric digital twin for condition assess… | Yes | Yes | Yes | Yes | Yes | **Include** | Geometric DT for pipeline deformation/blockage defect assessment                    |
| 184 | 3581 | Scopus         | Research on the Construction of a Digital Twin Model for a 3D Measurem… | No  | Yes | No  | Yes | Yes | Exclude     | Gear measurement DT; manufacturing metrology                                        |
| 185 | 3947 | Web of Science | Digital twin-driven virtual sensor approach for safe construction oper… | Yes | Yes | Yes | Yes | Yes | **Include** | DT-driven virtual sensors for dredger construction safety                           |
| 186 | 3610 | Scopus         | A Multi-Sensor Fusion Approach Combined with RandLA-Net for Large-Scal… | No  | No  | Yes | Yes | Yes | Exclude     | Power-grid tower point-cloud segmentation; not AECO                                 |
| 187 | 3587 | Scopus         | Construction and application of CMF design service model for industria… | No  | Yes | No  | Yes | No  | Exclude     | Industrial product CMF design; Chinese journal, non-English                         |
| 188 | 3554 | Scopus         | Key Technologies for Health Management and Intelligent Operation and M… | No  | Yes | Yes | Yes | No  | Exclude     | Power equipment O&M; Chinese journal, non-English                                   |
| 189 | 3767 | Scopus         | A lightweight and attention-enhanced framework for robust pavement def… | Yes | No  | Yes | Yes | Yes | Exclude     | Pavement defect YOLO; DT only dataset name                                          |
| 190 | 4016 | Web of Science | Teaching robots to perform quasi-repetitive construction tasks through… | Yes | No  | No  | Yes | Yes | Exclude     | LfD robot training; DT as perceived workspace only                                  |
| 191 | 4011 | Web of Science | Framework for Operational Resilience Management of Critical Infrastruc… | No  | Yes | Yes | Yes | Yes | Exclude     | CI resilience framework; district heating plant case                                |
| 192 | 3617 | Scopus         | Review on the Non-Destructive Test (NDT) Approaches on Concrete Crack … | Yes | No  | Yes | Yes | Yes | Exclude     | NDT crack-mapping review; DT linkage aspirational                                   |
| 193 | 3510 | Scopus         | A deep feature fusion network based on multi-scale kernel construction… | No  | No  | Yes | Yes | No  | Exclude     | Aircraft wing stress field; Chinese journal, non-English                            |
| 194 | 3899 | Web of Science | Creation and application of a geometric digital twin model for constru… | Yes | Yes | Yes | Yes | Yes | **Include** | Dynamic geometric DT for cable-net construction; shape/force prediction             |
| 195 | 3974 | Web of Science | Digital twin-enabled safety monitoring system for seamless worker-robo… | Yes | Yes | Yes | Yes | Yes | **Include** | DT safety monitoring for worker-robot collaboration; collision mitigation           |
| 196 | 3945 | Web of Science | Developing WSN/BIM-Based Environmental Monitoring Management System fo… | Yes | Yes | Yes | Yes | Yes | **Include** | WSN/BIM DT for parking garage environmental hazard monitoring                       |
| 197 | 3990 | Web of Science | Human-Robot collaboration in construction: Robot design, perception an… | Yes | No  | Yes | Yes | Yes | Exclude     | HRC review; DT-based HRC only future priority                                       |
| 198 | 3729 | Scopus         | Multi-scale evolution mechanism and knowledge construction of a digita… | No  | Yes | Yes | Yes | Yes | Exclude     | Machining quality DT; manufacturing                                                 |
| 199 | 3898 | Web of Science | Supply chain management for modular construction using building inform… | Yes | Yes | No  | Yes | Yes | Exclude     | BIM+IoT+GIS logistics DT; efficiency/cost, no safety/quality core                   |
| 200 | 3514 | Scopus         | Portal-Frame Piers to Spare Space for Two Piers of Jingkou Double-Trac… | Yes | Yes | Yes | Yes | No  | Exclude     | Chinese journal (Bridge Construction); non-English full text                        |
| 201 | 3672 | Scopus         | A digital twin-based framework for simulation and monitoring analysis … | No  | Yes | Yes | Yes | Yes | Exclude     | Floating wind turbine DT; energy sector                                             |
| 202 | 3879 | Web of Science | Immersive Technologies-Driven Building Information Modeling (BIM) in t… | Yes | No  | No  | Yes | Yes | Exclude     | ImTs-BIM bibliometric; DT one cluster                                               |
| 203 | 3560 | Scopus         | Digital Twin‐Based Risk Control during Prefabricated Building Hoisting… | Yes | Yes | Yes | Yes | Yes | **Include** | DT+BN risk control for prefab hoisting operations                                   |
| 204 | 3602 | Scopus         | Digital twin-based safety risk coupling of prefabricated building hois… | Yes | Yes | Yes | Yes | Yes | **Include** | DT safety risk coupling of prefab hoisting; Apriori+complex network                 |
| 205 | 3573 | Scopus         | Intelligent tensioning method for prestressed cables based on digital … | Yes | Yes | Yes | Yes | Yes | **Include** | DT+AI intelligent tensioning of prestressed cables; safety evaluation               |
| 206 | 3749 | Scopus         | Digital twin modeling method for construction process of assembled bui… | Yes | Yes | Yes | Yes | No  | Exclude     | Chinese journal (J. Building Structures); non-English                               |
| 207 | 3669 | Scopus         | Digital Twins-Based Impact Response Prediction of Prestressed Steel St… | Yes | Yes | Yes | Yes | Yes | **Include** | DT+ML impact response prediction of prestressed steel structures                    |
| 208 | 3641 | Scopus         | A framework for an indoor safety management system based on digital tw… | Yes | Yes | Yes | Yes | Yes | **Include** | DT indoor safety management; SVM danger classification; stadium case                |
| 209 | 3676 | Scopus         | Guidance Method for Earthquake-damaged Building Reinforcement Integrat… | Yes | Yes | Yes | Yes | No  | Exclude     | Chinese journal (J. Architecture & Civil Eng.); non-English                         |
| 210 | 3969 | Web of Science | Structural safety risk prediction method for terminal building steel r… | Yes | Yes | Yes | Yes | Yes | **Include** | DT safety risk prediction for terminal steel roof construction; 98% stress accuracy |
| 211 | 3952 | Web of Science | Intelligent safety control modeling and construction process control o… | Yes | Yes | Yes | Yes | Yes | **Include** | DT-driven intelligent safety control of large-span steel construction               |
| 212 | 4013 | Web of Science | Research progress and trends of intelligent technology construction in… | Yes | No  | No  | Yes | Yes | Exclude     | CiteSpace review of intelligent construction; DT only core-literature topic         |
| 213 | 3597 | Scopus         | Intelligent Analysis Method for Prestressed Steel Structure Constructi… | Yes | Yes | Yes | Yes | No  | Exclude     | Chinese journal (J. Architecture & Civil Eng.); non-English                         |
| 214 | 3887 | Web of Science | Electrical Safety Enhanced With BIM, SCADA and Digital Twin Integratio… | No  | Yes | Yes | Yes | Yes | Exclude     | MV-LV substation electrical safety; power equipment                                 |
| 215 | 3992 | Web of Science | Developing an integrative framework for digital twin applications in t… | Yes | Yes | No  | Yes | Yes | Exclude     | SLR integrative framework; operational intelligence broadly, DfS/DfQ not core       |
| 216 | 3766 | Scopus         | Automatic Calibration of Structural Damage in Building Information Mod… | Yes | No  | Yes | Yes | Yes | Exclude     | RPA calibration of damage into BIM; no live DT                                      |
| 217 | 4006 | Web of Science | Structural Health Assessment of a Reinforced Concrete Building in Valp… | Yes | No  | Yes | Yes | Yes | Exclude     | Modal identification study; DT as future foundation                                 |
| 218 | 3925 | Web of Science | An open-source GIS app for digitalising bridge inspections and automat… | Yes | No  | Yes | Yes | Yes | Exclude     | GIS app for bridge inspection→BIM; no DT                                            |
| 219 | 3606 | Scopus         | Community Twin Ecosystem for Disaster Resilient Communities             | Yes | Yes | Yes | Yes | Yes | **Include** | Community Twin Ecosystem for disaster resilience; tornado scenarios                 |
| 220 | 3698 | Scopus         | Applications and challenges of digital twin in intelligent constructio… | Yes | Yes | Yes | Yes | No  | Exclude     | Chinese journal (J. Traffic & Transportation Eng.); non-English                     |
| 221 | 3894 | Web of Science | Automating digitalization of engineered slopes to support interactive … | Yes | Yes | Yes | Yes | Yes | **Include** | Automated slope digital models + web DT; slope safety management                    |
| 222 | 3638 | Scopus         | Digital twins for secure thermal energy storage in building             | Yes | Yes | No  | Yes | Yes | Exclude     | Thermal energy storage DT; energy scheduling, safety incidental                     |
| 223 | 3688 | Scopus         | Digital Transformation in Early-Stage MEP Coordination: A Serious Gami… | Yes | No  | Yes | Yes | Yes | Exclude     | Serious-game MEP coordination education; DT linkage future                          |
| 224 | 3995 | Web of Science | Digital Transformation in Early-Stage MEP Coordination: A Serious Gami… | Yes | No  | Yes | Yes | Yes | Exclude     | Duplicate of ID 3688 (WoS copy)                                                     |
| 225 | 3986 | Web of Science | Tunnel performance prediction through degradation inspection and digit… | Yes | Yes | Yes | Yes | Yes | **Include** | Inspection DT for tunnel degradation; serviceability & intervention prediction      |
| 226 | 3965 | Web of Science | Automated procedural modeling for tunnel inspection and digital twin d… | Yes | Yes | Yes | Yes | Yes | **Include** | Automated procedural modeling for tunnel inspection DT; defect detection            |
| 227 | 3805 | Scopus         | Assessing the impact of Modbus/TCP protocol attacks on critical infras… | No  | Yes | No  | Yes | Yes | Exclude     | WWTP cybersecurity testbed; water industrial ICS                                    |
| 228 | 3715 | Scopus         | The Internet of Things for Smart Roads: A Road Map From Present to Fut… | No  | Yes | Yes | Yes | Yes | Exclude     | Smart road IoT/DT for traffic; not built-asset DfS/DfQ                              |
| 229 | 3785 | Scopus         | A Systematic Survey of Digital Twin Applications: Transferring Knowled… | No  | Yes | Yes | Yes | Yes | Exclude     | Automotive/aviation/maritime DT survey; not AECO                                    |
| 230 | 3574 | Scopus         | BIM-Driven Safety: Automated Rule-Based Multihazard Detection and Lega… | Yes | No  | Yes | Yes | Yes | Exclude     | 8D BIM rule-based compliance; static BIM, DT as label                               |
| 231 | 3496 | Scopus         | Roads Infrastructure Digital Twin: Advancing Situational Awareness Thr… | No  | Yes | No  | Yes | Yes | Exclude     | Road situational awareness streaming; vehicular                                     |
| 232 | 3799 | Scopus         | Integrating Advanced Technologies for Environmental Valuation in Legac… | No  | Yes | Yes | Yes | Yes | Exclude     | Mining heritage site environmental DT; not AECO                                     |
| 233 | 3847 | Scopus         | A Hybrid Methodology to Assess Cyber Resilience of IoT in Energy Manag… | No  | Yes | No  | Yes | Yes | Exclude     | CNI cyber-resilience methodology; energy/connected sites                            |
| 234 | 3862 | Scopus         | Reliability Analysis of Micropile-Supported Deep Excavations Using Mul… | Yes | No  | Yes | Yes | Yes | Exclude     | MARS reliability of excavations; DT/BIM as outlook                                  |
| 235 | 3720 | Scopus         | Toward cognitive digital twins using a BIM-GIS asset management system… | Yes | Yes | Yes | Yes | Yes | **Include** | BIM-GIS AMS toward cognitive DTs; fire crowd-simulation safety                      |
| 236 | 3812 | Scopus         | Organising digital twin in the built environment: a systematic review … | Yes | Yes | No  | Yes | Yes | Exclude     | Organisational SR of DT in AEC; use/user perspective, DfS/DfQ not core              |
| 237 | 3622 | Scopus         | Digital Twin Modelling Approach and Optimization Analysis for Safety i… | Yes | Yes | Yes | Yes | No  | Exclude     | Chinese journal (J. Basic Science & Eng.); non-English                              |
| 238 | 4004 | Web of Science | SMAC-based cooperative hyperparameter optimization for occupational ri… | Yes | Yes | Yes | Yes | Yes | **Include** | DT orchestration layer for federated worker-safety AI; occupational risk            |
| 239 | 3944 | Web of Science | Safety monitoring digital twin-based centralized model consolidation m… | Yes | Yes | Yes | Yes | Yes | **Include** | FL-based Safety Monitoring DT for multi-worker safety prediction                    |
| 240 | 4049 | Web of Science | Environmental impacts of standard building renovations: City-level ext… | Yes | Yes | No  | Yes | Yes | Exclude     | Renovation environmental-impact DT; energy/carbon focus                             |
| 241 | 4009 | Web of Science | Image-based acquisition and digital documentation of geometry and cond… | Yes | Yes | Yes | Yes | No  | Exclude     | German journal (Bautechnik); non-English full text                                  |
| 242 | 3890 | Web of Science | A Comprehensive Framework for Integrating Extended Reality into Lifecy… | Yes | No  | Yes | Yes | Yes | Exclude     | XR lifecycle safety framework; BIM/Lean/PtD but no DT                               |
| 243 | 3600 | Scopus         | When BIM Meets MBSE: Building a Semantic Bridge for Infrastructure Dat… | Yes | No  | Yes | Yes | Yes | Exclude     | BIM-MBSE semantic bridge; DT environment only as context                            |
| 244 | 4022 | Web of Science | Data-Driven Piecewise Bivariate Regression for Best-Estimate Natural P… | Yes | No  | Yes | Yes | Yes | Exclude     | Natural-period regression; DT as application context                                |
| 245 | 3922 | Web of Science | Digital twin non-fungible token (DT-NFT): Enabling data ownership in t… | Yes | Yes | No  | Yes | Yes | Exclude     | DT-NFT data ownership; no safety/quality focus                                      |
| 246 | 3512 | Scopus         | Machine learning enhancement of manoeuvring prediction for ship Digita… | No  | Yes | Yes | Yes | Yes | Exclude     | Ship manoeuvring DT; maritime                                                       |
| 247 | 3939 | Web of Science | Construction defects, envelope degradation and lifecycle carbon implic… | Yes | Yes | Yes | Yes | Yes | **Include** | Conceptual DT prototype for defect propagation; construction quality-carbon         |
| 248 | 3508 | Scopus         | Optimising the construction process through digitalisation: Case studi… | Yes | No  | No  | Yes | Yes | Exclude     | Digitalisation case-study review; DT one of many techs                              |
| 249 | 3837 | Scopus         | Use of gaming technology to bring bridge inspection to the office       | Yes | No  | Yes | Yes | Yes | Exclude     | LIDAR+VR bridge inspection; "step towards DTs"                                      |
| 250 | 3743 | Scopus         | Risk Assessment of Underground Utility Tunnel Projects in Q City Using… | Yes | No  | Yes | Yes | Yes | Exclude     | AHP risk assessment; BIM/DT only as smart-O&M factor                                |
| 251 | 3820 | Scopus         | Diagnostic Systems and Complexes for Railways                           | Yes | No  | Yes | Yes | No  | Exclude     | Russian journal (Russian Electrical Eng.); non-English                              |
| 252 | 3871 | Scopus         | Digital twin platform for evaluating thermal bridging effects on aggre… | Yes | Yes | No  | Yes | Yes | Exclude     | Thermal-bridging DT platform; energy performance, no DfS/DfQ                        |
| 253 | 3585 | Scopus         | A REVIEW OF THE APPLICATION OF ONTOLOGIES AND SEMANTIC WEB FOR BUILDIN… | Yes | Yes | Yes | Yes | Yes | **Include** | SLR ontologies/semantic web for BIM-DT construction mgmt incl. safety use case      |
| 254 | 3970 | Web of Science | An Anomaly-Enhanced Digital Twin (AEDT) Model for Intelligent Inspecti… | Yes | Yes | Yes | Yes | Yes | **Include** | Anomaly-enhanced DT for slope infrastructure inspection; defect classification      |
| 255 | 3989 | Web of Science | Enriching geometric digital twins of buildings with small objects by f… | Yes | Yes | Yes | Yes | Yes | **Include** | Enriching geometric DTs with fire-safety objects; condition monitoring              |
| 256 | 4003 | Web of Science | Unlocking the Potential of Digital Twins in Construction: A Systematic… | Yes | Yes | Yes | Yes | Yes | **Include** | Text-mining systematic review of DTs in construction; safety & productivity         |
| 257 | 4021 | Web of Science | Design and Implementation of a Smart IoT Based Building and Town Disas… | Yes | No  | Yes | Yes | Yes | Exclude     | AR-based disaster management; physical-virtual linkage but pre-DT (2018)            |
| 258 | 3764 | Scopus         | Current Benefits of ASCE 75 and its Potential to Affect Digital As-Bui… | Yes | No  | No  | Yes | Yes | Exclude     | ASCE 75 utility as-built standard; DT as data product                               |
| 259 | 3497 | Scopus         | Digital Twin development and implementation for the management of irri… | No  | Yes | No  | Yes | Yes | Exclude     | Irrigation network DT; water/agriculture infrastructure                             |
| 260 | 3755 | Scopus         | ESTIMATING THE SERVICE LIFE OF CONCRETE REINFORCED WITH ADVANCED MATER… | Yes | Yes | Yes | Yes | Yes | **Include** | IoT sensors + DT for concrete service-life & early damage; review                   |
| 261 | 3902 | Web of Science | BIM and TLS Point Cloud Integration for Information Management of Unde… | No  | No  | Yes | Yes | Yes | Exclude     | Underground coal mine BIM+TLS; mining                                               |
| 262 | 3881 | Web of Science | Designing a BIM-enhanced digital twin architecture for construction po… | Yes | Yes | Yes | Yes | Yes | **Include** | BIM-enhanced DT for renovation pollution (health hazard) management                 |
| 263 | 3798 | Scopus         | Optimizing construction site layouts with dynamic multi-objective meth… | Yes | No  | Yes | Yes | Yes | Exclude     | Site layout optimization; hazard risk one objective, no DT                          |
| 264 | 3557 | Scopus         | Risk assessment for modern industry                                     | No  | Yes | Yes | Yes | Yes | Exclude     | Modern-industry risk assessment reflections; manufacturing/energy cases             |
| 265 | 3536 | Scopus         | DInSAR–SBAS satellite monitoring of infrastructures: how temperature a… | Yes | Yes | Yes | Yes | Yes | **Include** | Calibrated 3D DT of bridge for thermal-deformation SHM interpretation               |
| 266 | 4044 | Web of Science | DInSAR-SBAS satellite monitoring of infrastructures: how temperature a… | Yes | Yes | Yes | Yes | Yes | Exclude     | Duplicate of ID 3536 (WoS copy)                                                     |
| 267 | 3882 | Web of Science | Designing Digital Twin with IoT and AI in Warehouse to Support Optimiz… | No  | Yes | Yes | Yes | Yes | Exclude     | ETO manufacturing warehouse DT; factory domain (edge 1)                             |
| 268 | 3614 | Scopus         | CONSTRUCTION OF A DIGITAL TWIN MODEL FOR A SYSTEM THAT MONITORS THE TE… | No  | Yes | Yes | Yes | Yes | Exclude     | Nuclear power unit monitoring DT                                                    |
| 269 | 3710 | Scopus         | Digital Twin Framework for Structural Health Monitoring of Transmissio… | No  | Yes | Yes | Yes | Yes | Exclude     | Transmission tower SHM DT; power infrastructure (edge 2)                            |
| 270 | 3893 | Web of Science | Digital Twin Framework for Structural Health Monitoring of Transmissio… | No  | Yes | Yes | Yes | Yes | Exclude     | Duplicate of ID 3710 (WoS copy); power infrastructure                               |
| 271 | 4000 | Web of Science | LiDAR-Simulated Multimodal and Self-Supervised Contrastive Digital Twi… | Yes | Yes | Yes | Yes | Yes | **Include** | DT point-cloud generation of rail fasteners; infrastructure monitoring safety       |
| 272 | 3627 | Scopus         | Study and Design of Dike Engineering Safety Management System Based on… | Yes | Yes | Yes | Yes | No  | Exclude     | Chinese journal (China Rural Water & Hydropower); non-English                       |
| 273 | 3892 | Web of Science | An IFC-based framework for semantic integration of BIM and mobile crow… | Yes | Yes | Yes | Yes | Yes | **Include** | IFC+MCS real-time evacuation routing; DT-like emergency management                  |
| 274 | 3673 | Scopus         | Digitisation of as-built structures with AI                             | Yes | Yes | Yes | Yes | No  | Exclude     | German journal (Bautechnik); non-English full text                                  |
| 275 | 3663 | Scopus         | Digital Twin Enabled Automated Pin Defect Detection System for Aviatio… | No  | Yes | Yes | Yes | Yes | Exclude     | Aviation connector pin defect DT; aerospace manufacturing                           |
| 276 | 3791 | Scopus         | AI for empowering the construction and development of university labor… | Yes | No  | No  | Yes | No  | Exclude     | Chinese journal (Experimental Tech. & Mgmt); non-English, no DT                     |
| 277 | 4042 | Web of Science | Designing automated digital safety systems for building health monitor… | Yes | Yes | Yes | Yes | Yes | **Include** | Automated digital safety systems for construction site health monitoring            |
| 278 | 3983 | Web of Science | Physics-informed computational framework for assessing the seismic beh… | Yes | Yes | Yes | Yes | Yes | **Include** | BIM+FEM+real-time SHM digital replica of dam; seismic safety                        |
| 279 | 3957 | Web of Science | Internet of Things in construction: trends and adoption insights from … | Yes | No  | No  | Yes | Yes | Exclude     | IoT-in-construction scientometric; DT one theme                                     |
| 280 | 3714 | Scopus         | Well Construction Action Planning and Automation through Finite-Horizo… | No  | Yes | Yes | Yes | Yes | Exclude     | Oil-well construction MDP DT; O&G drilling                                          |
| 281 | 3634 | Scopus         | Digital Twins for Real-Time Scenario Analysis during Well Construction… | No  | Yes | Yes | Yes | Yes | Exclude     | Well construction scenario DT; O&G drilling                                         |
| 282 | 3772 | Scopus         | Intelligent Action Planning for Well Construction Operations Demonstra… | No  | Yes | Yes | Yes | Yes | Exclude     | Well construction RL planning; O&G drilling                                         |
| 283 | 3810 | Scopus         | Digital Twins for Construction Projects—Developing a Risk Systematizat… | Yes | Yes | Yes | Yes | Yes | **Include** | DT risk systematization for construction projects; anomaly detection                |
| 284 | 4047 | Web of Science | Exploring the Adoption of Construction Technologies in Infrastructure … | Yes | No  | No  | Yes | Yes | Exclude     | Tech adoption perceptions vs project data; DT one of many                           |
| 285 | 4052 | Web of Science | Investigating the Correlation and Synergy of Artificial Intelligence T… | Yes | No  | No  | Yes | Yes | Exclude     | AI+tech correlation survey; DT one of 13 technologies                               |
| 286 | 3722 | Scopus         | Stack-AttenLSTM: A surrogate deep learning model for sequential earthq… | Yes | No  | Yes | Yes | Yes | Exclude     | LSTM surrogate for earthquake-flood response; no DT                                 |
| 287 | 4043 | Web of Science | Defect-oriented supportive bridge inspection system featuring building… | Yes | No  | Yes | Yes | Yes | Exclude     | BIM+AR bridge inspection; "heading toward a DT"                                     |
| 288 | 3818 | Scopus         | ITA − AITES tunnelling information modelling − A BIM approach for a su… | Yes | No  | No  | Yes | Yes | Exclude     | ITA-AITES BIM tunnelling guideline; sustainability focus                            |
| 289 | 3900 | Web of Science | ITA - AITES tunnelling information modelling - A BIM approach for a su… | Yes | No  | No  | Yes | Yes | Exclude     | Duplicate of ID 3818 (WoS copy)                                                     |
| 290 | 3914 | Web of Science | Structural Information Modeling                                         | Yes | Yes | Yes | Yes | No  | Exclude     | German journal (Mauerwerk); non-English full text                                   |
| 291 | 3929 | Web of Science | Structural Information Modeling - the digital transformation of buildi… | Yes | Yes | Yes | Yes | No  | Exclude     | German journal (Bautechnik); non-English full text                                  |
| 292 | 3713 | Scopus         | A BIM-Based Digital Twin Framework for Urban Roads: Integrating MMS an… | Yes | Yes | Yes | Yes | Yes | **Include** | BIM-based DT of urban roads; defect detection & predictive maintenance              |
| 293 | 3884 | Web of Science | Mapping the Evolution of 4D BIM in Construction Digitalisation: A Scie… | Yes | No  | No  | Yes | Yes | Exclude     | 4D BIM scientometric; DT one emerging theme                                         |
| 294 | 3532 | Scopus         | Analyzing Research Trends in Smart Construction Safety: A Topic Modeli… | Yes | Yes | Yes | Yes | Yes | **Include** | Topic-modeling review + framework of DT/IoT/big-data for construction safety        |
| 295 | 4040 | Web of Science | Metrics development and modelling the mixed reality and digital twin a… | Yes | Yes | No  | Yes | Yes | Exclude     | MRDT adoption TAM meta-analysis; safety only as outcome context                     |
| 296 | 3880 | Web of Science | BIM and Digital Twin for Developing Convergence Technologies as Future… | Yes | No  | No  | Yes | Yes | Exclude     | BIM+DT convergence roadmap; no DfS/DfQ core                                         |
| 297 | 3633 | Scopus         | Intelligent overall planning model of underground space based on digit… | Yes | Yes | Yes | Yes | Yes | **Include** | DT underground-space planning; BN accident risk & disaster warning                  |
| 298 | 3907 | Web of Science | Digital Twin-Driven Stability Optimization Framework for Large Undergr… | Yes | Yes | Yes | Yes | Yes | **Include** | DT framework for large cavern stability; real-time monitoring & optimization        |
| 299 | 3823 | Scopus         | When Roads Go Underwater: AI-Enhanced Digital Twin-Driven Flood Resili… | Yes | Yes | Yes | Yes | Yes | **Include** | AI-enhanced DT flood resilience of roadways; serviceability & emergency             |
| 300 | 3964 | Web of Science | Reverse digital twin mapping of building envelope anomalies based on U… | Yes | Yes | Yes | Yes | Yes | **Include** | Reverse DT mapping of envelope anomalies; UAV infrared + CNN                        |
| 301 | 3569 | Scopus         | Developing a Comprehensive Diagnostics Technology for the Technical Co… | Yes | No  | Yes | Yes | No  | Exclude     | Russian journal; UAV diagnostics, no DT core, non-English                           |
| 302 | 3966 | Web of Science | The Research on the Construction Method of a Slope Digital Twin Model … | Yes | Yes | Yes | Yes | Yes | **Include** | Surrogate-model-driven slope DT; landslide deformation prediction                   |
| 303 | 3531 | Scopus         | Twinning simulation and model test for construction error assessment o… | Yes | Yes | Yes | Yes | No  | Exclude     | Chinese journal (J. Building Structures); non-English                               |
| 304 | 3997 | Web of Science | Leveraging emerging technologies to address the crisis of aging concre… | Yes | No  | Yes | Yes | Yes | Exclude     | Commentary on aging concrete rehab; DT one of many techs                            |
| 305 | 4033 | Web of Science | A New Benchmark Model for the Automated Detection and Classification o… | Yes | No  | Yes | Yes | Yes | Exclude     | YOLO equipment detection benchmark; DT as future extension                          |
| 306 | 4034 | Web of Science | AI-assisted fibre optic sensing frameworks for automated monitoring of… | Yes | No  | Yes | Yes | Yes | Exclude     | AI+FOS railway SHM review; DT-integrated RL only emerging                           |
| 307 | 3594 | Scopus         | Building a Cad-Native Digital Twin for Ndt and Plm: Workflow, Tools, a… | No  | Yes | Yes | Yes | Yes | Exclude     | Aircraft nacelle NDT CAD-native DT; aerospace                                       |
| 308 | 3932 | Web of Science | Simultaneous Digital Twin: Chaining Climbing-Robot, Defect Segmentatio… | Yes | Yes | Yes | Yes | Yes | **Include** | Climbing-robot + defect segmentation + DT platform for facade inspection            |
| 309 | 3833 | Scopus         | Digital twin-assisted fault diagnosis system for robot joints with ins… | Yes | Yes | Yes | Yes | Yes | **Include** | DT-assisted fault diagnosis of construction robot joints; safety mishaps            |
| 310 | 4001 | Web of Science | Agentic system for construction safety risk assessments using large la… | Yes | No  | Yes | Yes | Yes | Exclude     | LLM+KG safety risk assessment; DT integration future work                           |
| 311 | 3568 | Scopus         | Automatic creation of personalised virtual construction safety trainin… | Yes | Yes | Yes | Yes | Yes | **Include** | DTCS auto-generated VR safety training; BIM+schedule+hazard data                    |
| 312 | 3540 | Scopus         | Track Geometry Prediction Using Three-Dimensional Recurrent Neural Net… | Yes | No  | Yes | Yes | Yes | Exclude     | RNN+BIM co-simulation track prediction; no DT claim                                 |
| 313 | 3768 | Scopus         | Enhancing Urban Heatwave Response Planning via a Graph-Based Digital T… | Yes | Yes | Yes | Yes | Yes | **Include** | Graph-based DT for heatwave risk & first-responder routing; Vienna                  |
| 314 | 3787 | Scopus         | Selected implications of a hyper-connected world on pavement engineeri… | Yes | No  | Yes | Yes | Yes | Exclude     | Hyper-connected pavement concepts; DT mode discussion only                          |
| 315 | 3919 | Web of Science | Development of a digital twin-driven bridge construction safety monito… | Yes | Yes | Yes | Yes | Yes | **Include** | DT-driven bridge construction safety monitoring; Yellow River bridge case           |
| 316 | 4041 | Web of Science | Near Real-Time 3D Reconstruction of Construction Sites Based on Survei… | Yes | No  | Yes | Yes | Yes | Exclude     | 3D reconstruction from surveillance; DT management as beneficiary                   |
| 317 | 3694 | Scopus         | Research on the construction of civil airport safety management system… | Yes | Yes | Yes | Yes | No  | Exclude     | Chinese journal (China Safety Science J.); non-English                              |
| 318 | 3941 | Web of Science | Digital twin of advanced geological conditions in rock tunnel construc… | Yes | Yes | Yes | Yes | Yes | **Include** | DT of geological conditions in rock tunnel construction; risk management            |
| 319 | 3648 | Scopus         | An Enhanced Digital Twin-Driven Fault Diagnosis Approach Based on Deep… | No  | Yes | Yes | Yes | Yes | Exclude     | Marine machinery fault diagnosis DT                                                 |
| 320 | 3994 | Web of Science | Intelligent Risk Prognosis and Control of Foundation Pit Excavation Ba… | Yes | Yes | Yes | Yes | Yes | **Include** | DT intelligent risk prognosis & control of foundation pit excavation                |
| 321 | 3583 | Scopus         | Data and Knowledge-Driven Bridge Digital Twin Modeling for Smart Opera… | Yes | Yes | Yes | Yes | Yes | **Include** | Data+knowledge-driven bridge DT for smart O&M; failure risk prediction              |
| 322 | 3948 | Web of Science | Human-in-the-Loop Digital Twin Modeling for Smart Civil Infrastructure… | Yes | Yes | Yes | Yes | Yes | **Include** | Human-in-the-loop DT for CI O&M; risk sensing/prediction/control                    |
| 323 | 3850 | Scopus         | Data-driven progress prediction in construction: a multi-project portf… | Yes | No  | No  | Yes | Yes | Exclude     | Progress prediction portfolio; DT integration future                                |
| 324 | 3559 | Scopus         | Sensor Acquisition and Allocation for Real-Time Monitoring of Articula… | Yes | Yes | Yes | Yes | Yes | **Include** | Real-time sensor→DT of articulated equipment; struck-by/utility strike prevention   |
| 325 | 3737 | Scopus         | Artificial Intelligence-Powered Digital Twins for Sustainable and Resi… | Yes | Yes | Yes | Yes | No  | Exclude     | German journal (Bauingenieur); non-English full text                                |
| 326 | 3552 | Scopus         | Review of Construction Automation and Robotics Practices in Indonesian… | Yes | No  | No  | Yes | Yes | Exclude     | Automation/robotics adoption in Indonesian SOEs; DT prospect only                   |
| 327 | 3904 | Web of Science | Integration and linking of inspection data in digital bridge models     | Yes | Yes | Yes | Yes | No  | Exclude     | German journal (Bautechnik); non-English full text                                  |
| 328 | 3621 | Scopus         | Relationship between Subcontracting Models and Adoption of Innovative … | Yes | No  | Yes | Yes | Yes | Exclude     | Subcontracting & safety innovation; digitalization broadly, no DT                   |
| 329 | 3946 | Web of Science | Defect Trigger Identification in a Construction Digital Twin Using Qua… | Yes | Yes | Yes | Yes | Yes | **Include** | Defect-trigger identification in construction DT; ontology+linked data quality      |
| 330 | 3834 | Scopus         | Big data in the processes of ensuring the security of critical informa… | No  | Yes | No  | Yes | Yes | Exclude     | Critical information infrastructure cybersecurity; grid DT testbed                  |
| 331 | 3593 | Scopus         | Overall introduction to the framework of BIM-based digital twinning in… | Yes | Yes | Yes | Yes | Yes | **Include** | BIM-based DT framework for OHS decision-making in building construction             |
| 332 | 3935 | Web of Science | Building Digital Twins to Overcome Digitalization Barriers for Automat… | Yes | Yes | Yes | Yes | Yes | **Include** | Building DT platform for site mgmt incl. OHS & quality control domains              |
| 333 | 3878 | Web of Science | A digital twin framework for civil engineering structures               | Yes | Yes | Yes | Yes | Yes | **Include** | Predictive DT for civil structures; DBN updating + maintenance planning             |
| 334 | 3840 | Scopus         | Physical digital twins for ancient stone masonry informed of original … | Yes | Yes | Yes | Yes | Yes | **Include** | Physical DTs of ancient masonry (nuraghi); structural safety assessment             |
| 335 | 3836 | Scopus         | Spatial Insights for Building Resilience: The Territorial Risk Managem… | Yes | Yes | Yes | Yes | Yes | **Include** | TERIMAAS BIM+GIS+IoT multi-hazard framework; flood risk of building                 |
| 336 | 3494 | Scopus         | A scoping review of green Internet of Things in construction and smart… | Yes | No  | No  | Yes | Yes | Exclude     | Green-IoT scoping review; DT future direction only                                  |
| 337 | 3933 | Web of Science | A framework to define, design and construct digital twins in the minin… | No  | Yes | Yes | Yes | Yes | Exclude     | Mining DT framework; not AECO                                                       |
| 338 | 3598 | Scopus         | Autonomy is not enough: why agentic AI in the built environment demand… | Yes | Yes | No  | Yes | Yes | Exclude     | Agentic AI governance; HVAC/energy focus, safety as governance risk                 |
| 339 | 3825 | Scopus         | Yara: An Ocean Virtual Environment for Research and Development of Aut… | No  | Yes | No  | Yes | Yes | Exclude     | Sailing robot virtual environment; maritime                                         |
| 340 | 3920 | Web of Science | A Digital Twin-Driven System for Road Maintenance: Integrating UAVs an… | Yes | Yes | Yes | Yes | Yes | **Include** | UAV+AMR DT for road maintenance; worker safety & inspection                         |
| 341 | 3781 | Scopus         | Disaster Risk Assessment and Analysis of Physical Infrastructure: A Co… | Yes | No  | Yes | Yes | Yes | Exclude     | Disaster risk assessment review; DT one method among many                           |
| 342 | 3697 | Scopus         | Key technology and engineering practice of intelligent rapid heading i… | No  | No  | Yes | Yes | No  | Exclude     | Coal mine heading; Chinese journal, non-English                                     |
| 343 | 4010 | Web of Science | Development and validation of graphics-based digital twin framework fo… | Yes | Yes | Yes | Yes | Yes | **Include** | Graphics-based DT for UAV post-earthquake inspection of high-rises                  |
| 344 | 4019 | Web of Science | Mixed reality and machine learning-guided cable robot framework (MMCR)… | Yes | No  | Yes | Yes | Yes | Exclude     | MR+ML cable robot; no DT component                                                  |
| 345 | 3762 | Scopus         | Reference-free ego-motion compensation for vision-based measurement of… | Yes | No  | Yes | Yes | Yes | Exclude     | Vision deformation measurement; graphics DT only as synthetic env                   |
| 346 | 3562 | Scopus         | AI and Digital Twin for Consumer Electronics in Smart Cities            | No  | Yes | No  | Yes | Yes | Exclude     | Consumer-electronics smart-city DT; traffic GNN                                     |
| 347 | 3985 | Web of Science | Interactive and Immersive Process-Level Digital Twin for Collaborative… | Yes | Yes | Yes | Yes | Yes | **Include** | Immersive process-level DT for human-robot construction; safety supervision         |
| 348 | 3763 | Scopus         | A digital twin integrated smart-liner for visualization monitoring of … | No  | Yes | Yes | Yes | Yes | Exclude     | Oil/gas pipeline smart-liner DT                                                     |
| 349 | 3779 | Scopus         | Enabling Building Information Model-driven human-robot collaborative c… | Yes | Yes | Yes | Yes | Yes | **Include** | Closed-loop DT for BIM-driven human-robot workflows; as-built updating              |
| 350 | 3718 | Scopus         | Detailed transient modeling and FPGA-based real-time digital-twin deve… | No  | Yes | No  | Yes | Yes | Exclude     | Sodium-cooled reactor RTDT; nuclear                                                 |
| 351 | 3783 | Scopus         | Construction of digital twin and parallel intelligent control method f… | No  | Yes | Yes | Yes | No  | Exclude     | Coal mine heading face; Chinese journal, non-English                                |
| 352 | 3895 | Web of Science | Augmenting progress monitoring in soil-foundation construction utilizi… | Yes | No  | No  | Yes | Yes | Exclude     | SOLOv2 progress monitoring; DT as future development                                |
| 353 | 3590 | Scopus         | Design and System Development of Knowledge Graph and Process Planning … | Yes | Yes | Yes | Yes | No  | Exclude     | Chinese journal (Tunnel Construction); non-English                                  |
| 354 | 3891 | Web of Science | Research on the intelligent construction of prefabricated building bas… | Yes | Yes | Yes | Yes | Yes | **Include** | DT for intelligent prefab construction; hoisting, safety, predictive analytics      |
| 355 | 3806 | Scopus         | Research on Management Efficiency and Public Participation in Smart Ci… | Yes | No  | No  | Yes | Yes | Exclude     | BIM-CIM smart city governance; DT not core                                          |
| 356 | 4025 | Web of Science | Using Eye-Tracking to Measure Worker Situation Awareness in Augmented … | Yes | No  | Yes | Yes | Yes | Exclude     | Eye-tracking AR situation awareness; no DT                                          |
| 357 | 3960 | Web of Science | Real-time mixed reality-based visual warning for construction workforc… | Yes | Yes | Yes | Yes | Yes | **Include** | DT+DL+MR real-time visual warning system for worker safety                          |
| 358 | 3988 | Web of Science | Knowledge-data driven digital twin platform: intelligent prediction an… | Yes | Yes | Yes | Yes | Yes | **Include** | Knowledge-data DT platform for tunnel face stability prediction/control             |
| 359 | 3981 | Web of Science | Multisource information fusion for real-time prediction and multiobjec… | Yes | Yes | Yes | Yes | Yes | **Include** | DT framework for slurry shield attitude prediction/optimization; safety & quality   |
| 360 | 3656 | Scopus         | A Novel Method for Tunnel Digital Twin Construction and Virtual-Real F… | Yes | Yes | Yes | Yes | Yes | **Include** | Tunnel DT construction + virtual-real fusion; accident rescue & emergency           |
| 361 | 3530 | Scopus         | Research on Digital Twin Construction and Safety Management Applicatio… | Yes | Yes | Yes | Yes | Yes | **Include** | Inland waterway DT with 3D video fusion; safety management                          |
| 362 | 3843 | Scopus         | Real-time digital twin of autonomous ships based on virtual-physical m… | No  | Yes | Yes | Yes | Yes | Exclude     | Autonomous ship DT; maritime                                                        |
| 363 | 3502 | Scopus         | Auto-constructed PID-based search algorithm for ship parameter identif… | No  | Yes | Yes | Yes | Yes | Exclude     | Ship parameter identification; maritime                                             |
| 364 | 3856 | Scopus         | CommandFence: A Novel Digital-Twin-Based Preventive Framework for Secu… | No  | Yes | Yes | Yes | Yes | Exclude     | Smart home cybersecurity DT; not AECO industry                                      |
| 365 | 3719 | Scopus         | 3D City Modeling on Infrastructure Construction Using Digital Twin      | Yes | Yes | No  | Yes | Yes | Exclude     | City-scale 3D modelling algorithm; efficiency focus (edge 10)                       |
| 366 | 3927 | Web of Science | AIoT-powered building digital twin for smart firefighting and super re… | Yes | Yes | Yes | Yes | Yes | **Include** | AIoT DT for smart firefighting; super real-time fire forecast                       |
| 367 | 3829 | Scopus         | Research on the construction of 5G fully connected mining digital twin… | No  | Yes | Yes | Yes | No  | Exclude     | Open-pit mining 5G DT; Chinese journal, non-English                                 |
| 368 | 3950 | Web of Science | Edge-cloud collaborative digital twin for vibration anomaly detection … | Yes | Yes | Yes | Yes | Yes | **Include** | Edge-cloud DT for high-rise vibration anomaly detection/localization                |
| 369 | 3961 | Web of Science | Digital twin system for deepwater well construction: Enhancing operati… | No  | Yes | Yes | Yes | Yes | Exclude     | Deepwater well construction DT; O&G                                                 |
| 370 | 3849 | Scopus         | A digital twin framework for construction and operation of the radio a… | No  | Yes | Yes | Yes | Yes | Exclude     | Radioactive waste repository DT; nuclear                                            |
| 371 | 3545 | Scopus         | Ensuring construction material provenance using Internet of Things and… | Yes | No  | Yes | Yes | Yes | Exclude     | IoT+blockchain material provenance; DT as prospect                                  |
| 372 | 3896 | Web of Science | Developing a digital twin model for monitoring building structural hea… | Yes | Yes | Yes | Yes | Yes | **Include** | BIM+real-scene 3D DT for building SHM; sensor/data management                       |
| 373 | 3499 | Scopus         | Status and prospects of synergistic development between smart city inf… | No  | No  | No  | Yes | No  | Exclude     | Vehicle-road-cloud review; Chinese journal, non-English                             |
| 374 | 3522 | Scopus         | Geological Perception and Digital Twin of Rock and Machine for TBM Tun… | Yes | Yes | Yes | Yes | No  | Exclude     | Chinese journal (J. Basic Science & Eng.); non-English                              |
| 375 | 3553 | Scopus         | Improvement of Construction Machinery Development Process by Digital T… | No  | Yes | Yes | Yes | Yes | Exclude     | Construction machinery development process; manufacturing DT                        |
| 376 | 3905 | Web of Science | Real-Time Digital Twin-Driven 3D Near-Miss Detection System at Constru… | Yes | Yes | Yes | Yes | Yes | **Include** | Real-time DT 3D near-miss detection at construction sites                           |
| 377 | 3909 | Web of Science | Digital twin-enabled 3D near-misses prediction method based on traject… | Yes | Yes | Yes | Yes | Yes | **Include** | DT 3D near-miss prediction from trajectories/postures; proactive safety             |
| 378 | 3811 | Scopus         | A Big Data-driven Digital Twin Model Method for Building a Shop Floor   | No  | Yes | No  | Yes | No  | Exclude     | Shop-floor manufacturing DT; Chinese journal, non-English                           |
| 379 | 3721 | Scopus         | Digital twin-based framework for multi-objective optimization of shiel… | Yes | Yes | Yes | Yes | Yes | **Include** | DT multi-objective optimization of shield tunneling parameters; safety              |
| 380 | 3547 | Scopus         | CAVTest: A Closed Connected and Automated Vehicles Test Field of Chang… | No  | Yes | Yes | Yes | Yes | Exclude     | CAV test field; automotive testing                                                  |
| 381 | 3649 | Scopus         | Construction of digital twin model of lithium-ion battery for intellig… | No  | Yes | Yes | Yes | No  | Exclude     | Li-ion battery DT; Chinese journal, non-English                                     |
| 382 | 3874 | Web of Science | Design and Validation of a Real-Time Maintenance Monitoring System Usi… | Yes | Yes | Yes | Yes | Yes | **Include** | BIM+DT real-time maintenance monitoring of tunnel; anomaly detection                |
| 383 | 3674 | Scopus         | Current situation and development trend of intelligent unmanned autono… | No  | No  | Yes | Yes | No  | Exclude     | Unmanned excavators review; Chinese journal, non-English                            |
| 384 | 3520 | Scopus         | Related Literature Review 5D Model for Project and Operation/Maintenan… | No  | No  | No  | Yes | Yes | Exclude     | 5D model review for O&G plant remote monitoring                                     |
| 385 | 3576 | Scopus         | Metaverse for the Energy Industry: Technologies, Applications, and Sol… | No  | Yes | Yes | Yes | Yes | Exclude     | Metaverse for energy industry (O&G)                                                 |
| 386 | 3696 | Scopus         | A digital twin approach for tunnel construction safety early warning a… | Yes | Yes | Yes | Yes | Yes | **Include** | DT tunnel construction early warning; collapse predicted, personnel saved           |
| 387 | 3855 | Scopus         | Deep Tabular and Sequential Models for Robust SCADA Cybersecurity Usin… | No  | No  | No  | Yes | Yes | Exclude     | SCADA intrusion detection; DT only future validation                                |
| 388 | 3667 | Scopus         | Topology guided fourier neural operator with decoupled geometric param… | Yes | Yes | Yes | Yes | Yes | **Include** | FNO dam leakage detection for operational DTs; safety monitoring                    |
| 389 | 3518 | Scopus         | Earthwork digital twin for teleoperation of an automated bulldozer in … | Yes | Yes | Yes | Yes | Yes | **Include** | Earthwork DT for bulldozer teleoperation; construction safety                       |
| 390 | 3993 | Web of Science | Intelligent Analysis of Construction Safety of Large Underground Space… | Yes | Yes | Yes | Yes | Yes | **Include** | DT intelligent safety analysis of large underground space construction              |
| 391 | 3757 | Scopus         | Application of BIM technologies based on parametric modeling in the mi… | No  | No  | No  | Yes | No  | Exclude     | Mining BIM parametric modeling; Russian journal, non-English                        |
| 392 | 3628 | Scopus         | Exploration and practice of the digital twin construction for producti… | No  | Yes | Yes | Yes | No  | Exclude     | Deep-sea gas field DT; Chinese journal, non-English                                 |
| 393 | 3539 | Scopus         | A dynamic digital twin-based health monitoring method for steel struct… | Yes | Yes | Yes | Yes | Yes | **Include** | Dynamic DT health monitoring of steel structures; CNN-LSTM+Bayesian                 |
| 394 | 3706 | Scopus         | Quantitative prediction method for safety of old building structures b… | Yes | Yes | Yes | Yes | No  | Exclude     | Chinese journal (China Safety Science J.); non-English                              |
| 395 | 3495 | Scopus         | Digital twin modeling and performance inversion of modular fully assem… | Yes | Yes | Yes | Yes | No  | Exclude     | Chinese journal (J. Building Structures); non-English                               |
| 396 | 3934 | Web of Science | Joint detection PCD-based method for automatic construction of geometr… | Yes | Yes | Yes | Yes | Yes | **Include** | PCD joint detection for geometric DT of cable domes; safety/stability               |
| 397 | 3845 | Scopus         | Three-Dimensional Stratigraphic Structure and Property Collaborative M… | Yes | No  | Yes | Yes | Yes | Exclude     | 3D stratigraphic modeling; urban DT as application context                          |
| 398 | 4035 | Web of Science | Digital Safety Navigation for Tower Crane Climbing Process from a Syst… | Yes | Yes | Yes | Yes | Yes | **Include** | Digital safety navigation for tower crane climbing; SINP platform                   |
| 399 | 4038 | Web of Science | Technology and implementation of safety monitoring system for power gr… | No  | Yes | Yes | Yes | Yes | Exclude     | Power grid construction site video monitoring; power industry                       |
| 400 | 3800 | Scopus         | Construction technology of prefabricated concrete frame with steel con… | Yes | Yes | Yes | Yes | No  | Exclude     | Chinese journal (J. Civil & Environmental Eng.); non-English                        |
| 401 | 3968 | Web of Science | AI-empowered digital twin modeling for high-precision building defect … | Yes | Yes | Yes | Yes | Yes | **Include** | AI+UAV+GeoBIM DT for facade defect management; building health                      |
| 402 | 3928 | Web of Science | Digital Twins for Construction Sites: Concepts, LoD Definition, and Ap… | Yes | Yes | Yes | Yes | Yes | **Include** | DT for construction sites: LoD framework; quality, efficiency, safety               |
| 403 | 3498 | Scopus         | Advanced informatic technologies for intelligent construction: A revie… | Yes | No  | No  | Yes | Yes | Exclude     | Intelligent construction review; DT only future path                                |
| 404 | 3991 | Web of Science | Digital twin-enabled synchronous jacking control of an aerial building… | Yes | Yes | Yes | Yes | Yes | **Include** | DT synchronous jacking control of aerial building machine; structural safety        |
| 405 | 3918 | Web of Science | Research on the Digital Twin System for Rotation Construction Monitori… | Yes | Yes | Yes | Yes | Yes | **Include** | MBSE-designed DT for bridge rotation construction monitoring; risk prediction       |
| 406 | 3681 | Scopus         | A Fixed-Budget Study of Real–Synthetic Data Mixing for PPE Detection i… | Yes | No  | Yes | Yes | Yes | Exclude     | PPE detection data-mixing benchmark; DT only synthetic data source                  |
| 407 | 4015 | Web of Science | A Fixed-Budget Study of Real-Synthetic Data Mixing for PPE Detection i… | Yes | No  | Yes | Yes | Yes | Exclude     | Duplicate of ID 3681 (WoS copy)                                                     |
| 408 | 4017 | Web of Science | From instance segmentation to physical quantification: High-resolution… | Yes | Yes | Yes | Yes | Yes | **Include** | UAV facade defect dataset + as-is DT registration; severity evaluation              |
| 409 | 3711 | Scopus         | Predictive diagnosis of hidden risk for urban lifeline infrastructures… | Yes | Yes | Yes | Yes | Yes | **Include** | DT-driven predictive diagnosis of urban lifeline hidden risks; perspective          |
| 410 | 3682 | Scopus         | A single-spindle monitoring system and its application for intelligent… | No  | Yes | Yes | Yes | No  | Exclude     | Textile spinning monitoring; Chinese journal, non-English                           |
| 411 | 3954 | Web of Science | Digital Twin Evaluation of Environment and Health of Public Toilet Ven… | Yes | Yes | Yes | Yes | Yes | **Include** | DT evaluation of public toilet ventilation; health/safety of IAQ                    |
| 412 | 3515 | Scopus         | Digital twin-enabled anti-collision system for smart construction site… | Yes | Yes | Yes | Yes | Yes | **Include** | DT anti-collision system for smart construction sites; 96% zone prediction          |
| 413 | 3972 | Web of Science | Digital twin-enabled simulation system for NATM tunnel construction pr… | Yes | Yes | Yes | Yes | Yes | **Include** | DT simulation for NATM tunnel construction under uncertainty; safety/schedule       |
| 414 | 3863 | Scopus         | Automatic response prediction in a digital twin framework for regional… | Yes | Yes | Yes | Yes | Yes | **Include** | DT for regional bridges group response prediction; Transformer safety warning       |
| 415 | 3700 | Scopus         | Simulation method of shield-machine empty push through station based o… | Yes | Yes | Yes | Yes | No  | Exclude     | Chinese journal (J. Tsinghua Univ.); non-English                                    |
| 416 | 3923 | Web of Science | An Established Theory of Digital Twin Model for Tunnel Construction Sa… | Yes | Yes | Yes | Yes | Yes | **Include** | DT model theory for tunnel construction safety assessment; settlement prediction    |
| 417 | 4014 | Web of Science | Research on the Construction of Multimodal Large Models and Self-super… | No  | Yes | No  | Yes | Yes | Exclude     | Power equipment perception; power industry                                          |
| 418 | 3943 | Web of Science | Digital Twin-Based Investigation of a Building Collapse Accident        | Yes | Yes | Yes | Yes | Yes | **Include** | DT-based building collapse accident investigation                                   |
| 419 | 3858 | Scopus         | Research on Key Common Technologies in Intelligent Construction of Lon… | Yes | No  | Yes | Yes | No  | Exclude     | Chinese journal (Bridge Construction); non-English                                  |
| 420 | 3773 | Scopus         | The Modelling of Digital Twins Technology in the Construction Process … | Yes | Yes | Yes | Yes | Yes | **Include** | DT modelling of prefab construction process; damage/deformation monitoring          |
| 421 | 4039 | Web of Science | Intelligent Prediction of Prestressed Steel Structure Construction Saf… | Yes | Yes | Yes | Yes | Yes | **Include** | DT+BP NN for prestressed steel construction safety prediction                       |
| 422 | 3564 | Scopus         | A knowledge foundation and prospect review on thermal response of brid… | Yes | No  | Yes | Yes | Yes | Exclude     | Bridge thermal response bibliometric; DT recent trend only                          |
| 423 | 3852 | Scopus         | Enhancing dam safety evaluation using dam digital twins                 | Yes | Yes | Yes | Yes | Yes | **Include** | Dam DT for continuous safety evaluation; IFC data integration + cloud model         |
| 424 | 3703 | Scopus         | Fast electrothermal coupling calculation method for supporting digital… | No  | Yes | Yes | Yes | Yes | Exclude     | Electrical equipment electrothermal DT; power                                       |
| 425 | 3687 | Scopus         | Artificial Intelligence in the Construction Industry: A Comprehensive … | Yes | No  | No  | Yes | Yes | Exclude     | AI-in-construction review; DT one of six techs                                      |
| 426 | 3951 | Web of Science | Digital Twin Construction Method for Monitoring Operation Status of Bu… | Yes | Yes | Yes | Yes | Yes | **Include** | DT monitoring of building machine jacking operation; ANN prediction                 |
| 427 | 3885 | Web of Science | Research on Building Process Optimization Framework Based on BIM-DT     | Yes | Yes | Yes | Yes | Yes | **Include** | BIM-DT building process optimization incl. construction safety; fault diagnosis     |
| 428 | 3875 | Web of Science | Multisensory and BIM-Integrated Digital Twin to Improve Urban Excavati… | Yes | Yes | Yes | Yes | Yes | **Include** | Multisensory BIM-integrated DT for urban excavation safety; collision avoidance     |
| 429 | 3877 | Web of Science | Integration of building information modelling and digital twin in mech… | Yes | Yes | Yes | Yes | Yes | **Include** | BIM+DT integration in mechanized tunnelling; rework reduction, lean                 |

## Included papers (proceed to Step 3 full-text coding)

| # | ID | Slug (atomic note) |
|---|---|---|
| 6 | 3756 | `Ahmad2026.md` |
| 7 | 3978 | `Akanmu2021.md` |
| 13 | 3915 | `Almatared2024.md` |
| 14 | 3668 | `Alvaro2025.md` |
| 15 | 4053 | `Ammar2024.md` |
| 19 | 3842 | `Aragon2025.md` |
| 20 | 4028 | `Araujo2025.md` |
| 21 | 3828 | `Arhrib2026.md` |
| 22 | 3662 | `Armijo2024.md` |
| 23 | 3975 | `Aroquipa2025.md` |
| 24 | 3996 | `Arowoiya2024.md` |
| 28 | 4037 | `Bao2026.md` |
| 35 | 3595 | `Brucherseifer2021.md` |
| 42 | 3658 | `Cervenka2026.md` |
| 44 | 3936 | `Chacon2024.md` |
| 45 | 3795 | `Chan2025.md` |
| 46 | 3998 | `Chang2024-rebar.md` |
| 47 | 3984 | `Chang2026-tunnel.md` |
| 49 | 3911 | `Chen2025-KG.md` |
| 50 | 3953 | `Chen2026-ginpole.md` |
| 61 | 3802 | `Dan2022-bridgesgroup.md` |
| 65 | 3626 | `Delhibabu2026.md` |
| 66 | 3967 | `Deng2025-risk.md` |
| 67 | 4036 | `Deng2025-bridge.md` |
| 68 | 3760 | `Deng2026-llm.md` |
| 72 | 3736 | `Doukari2026.md` |
| 74 | 3906 | `ElDin2022.md` |
| 76 | 4046 | `Ellul2024.md` |
| 78 | 4029 | `Fang2023.md` |
| 84 | 3493 | `Franciosi2024.md` |
| 86 | 3775 | `Gao2025-vibration.md` |
| 88 | 3876 | `Gao2024-bridge.md` |
| 92 | 3979 | `Geng2025-bridgenet.md` |
| 97 | 4005 | `Gonzalez-Boehme2023.md` |
| 100 | 4026 | `Granzner2023.md` |
| 102 | 3577 | `Gu2023.md` |
| 104 | 3977 | `Guo2026-SCP.md` |
| 106 | 3924 | `Guo2025-quality.md` |
| 109 | 3770 | `Ham2020.md` |
| 110 | 3926 | `Han2026-pipeline.md` |
| 111 | 3959 | `Han2025-UAV.md` |
| 112 | 3765 | `Han2026-MiC.md` |
| 115 | 3973 | `Hasan2022.md` |
| 118 | 3813 | `Hekmatnejad2025-scopus.md` |
| 121 | 3558 | `Hong2022-pit.md` |
| 122 | 3886 | `Hong2025-RAM.md` |
| 123 | 3949 | `Hou2026.md` |
| 125 | 3956 | `Hu2026-maturity.md` |
| 128 | 3575 | `Hu2024-SHM.md` |
| 129 | 3666 | `Huang2026-tunnel.md` |
| 137 | 3930 | `Jiang2022-clearance.md` |
| 138 | 3784 | `Jiang2022-archcover.md` |
| 141 | 3605 | `Jiang2023-fire.md` |
| 143 | 3572 | `Jiang2022-crane.md` |
| 144 | 3872 | `Jiang2024-hoisting.md` |
| 148 | 4027 | `Johansen2025.md` |
| 154 | 4024 | `Kamari2022-hurricane.md` |
| 155 | 3644 | `Kamari2022-debris.md` |
| 158 | 3792 | `Kang2025-VR.md` |
| 162 | 3604 | `Kaveh2025.md` |
| 163 | 3517 | `Khajavi2023.md` |
| 165 | 3916 | `Kim2023-piping.md` |
| 167 | 3938 | `Kim2024-heat.md` |
| 168 | 3999 | `Kim2024-fire.md` |
| 176 | 3591 | `Lai2022.md` |
| 178 | 3712 | `Levine2022.md` |
| 181 | 3661 | `Li2024-roof.md` |
| 183 | 3839 | `Li2023-pipeline.md` |
| 185 | 3947 | `Li2021-dredger.md` |
| 194 | 3899 | `Lin2026-cable.md` |
| 195 | 3974 | `Lin2025-WRC.md` |
| 196 | 3945 | `Lin2020-parking.md` |
| 203 | 3560 | `Liu2022-hoisting.md` |
| 204 | 3602 | `Liu2021-hoisting.md` |
| 205 | 3573 | `Liu2020-tensioning.md` |
| 207 | 3669 | `Liu2022-impact.md` |
| 208 | 3641 | `Liu2020-indoor.md` |
| 210 | 3969 | `Liu2025-roof.md` |
| 211 | 3952 | `Liu2025-steel.md` |
| 219 | 3606 | `Luleci2024.md` |
| 221 | 3894 | `Lv2026-slope.md` |
| 225 | 3986 | `Machado2024.md` |
| 226 | 3965 | `Machado2025.md` |
| 235 | 3720 | `Meschini2022.md` |
| 238 | 4004 | `Moe2026-SMAC.md` |
| 239 | 3944 | `Moe2025-SMDT.md` |
| 247 | 3939 | `Okuntade2026.md` |
| 253 | 3585 | `Palihakkara2025.md` |
| 254 | 3970 | `Pan2026-AEDT.md` |
| 255 | 3989 | `Pan2022-enrich.md` |
| 256 | 4003 | `Park2024-review.md` |
| 260 | 3755 | `PerezPerez2026.md` |
| 262 | 3881 | `Pham2026-pollution.md` |
| 265 | 3536 | `Ponzo2024-scopus.md` |
| 271 | 4000 | `Qiu2025.md` |
| 273 | 3892 | `Rashidian2026.md` |
| 277 | 4042 | `Rezaie2025.md` |
| 278 | 3983 | `Rinaldi2025.md` |
| 283 | 3810 | `Salem2023.md` |
| 292 | 3713 | `Scolamiero2026.md` |
| 294 | 3532 | `Seo2025.md` |
| 297 | 3633 | `Shao2022.md` |
| 298 | 3907 | `Sharafat2025-cavern.md` |
| 299 | 3823 | `Shariatfar2026.md` |
| 300 | 3964 | `Shen2026.md` |
| 302 | 3966 | `Shi2026-slope.md` |
| 308 | 3932 | `Song2026-facade.md` |
| 309 | 3833 | `Song2023-robot.md` |
| 311 | 3568 | `Speiser2024.md` |
| 313 | 3768 | `Stergiopoulos2025.md` |
| 315 | 3919 | `Su2025.md` |
| 318 | 3941 | `Sun2025-geology.md` |
| 320 | 3994 | `Sun2023-pit.md` |
| 321 | 3583 | `Sun2025-bridge.md` |
| 322 | 3948 | `Sun2026-HITL.md` |
| 324 | 3559 | `Talmaki2022.md` |
| 329 | 3946 | `Tian2026.md` |
| 331 | 3593 | `Torrecilla-Garcia2021.md` |
| 332 | 3935 | `Torres2024.md` |
| 333 | 3878 | `Torzoni2024.md` |
| 334 | 3840 | `Tran2025.md` |
| 335 | 3836 | `Ugliotti2025.md` |
| 340 | 3920 | `Villaverde2026.md` |
| 343 | 4010 | `Wang2024-GBDT.md` |
| 347 | 3985 | `Wang2021-I2PL.md` |
| 349 | 3779 | `Wang2024-closedloop.md` |
| 354 | 3891 | `Wen2025-prefab.md` |
| 357 | 3960 | `Wu2022-MR.md` |
| 358 | 3988 | `Wu2026-TFS.md` |
| 359 | 3981 | `Wu2024-slurry.md` |
| 360 | 3656 | `Wu2022-tunnel.md` |
| 361 | 3530 | `Wu2021-waterway.md` |
| 366 | 3927 | `Xie2025-fire.md` |
| 368 | 3950 | `Xiong2026.md` |
| 372 | 3896 | `Xu2023-SHM.md` |
| 376 | 3905 | `Yan2025-nearmiss.md` |
| 377 | 3909 | `Yan2026-nearmiss.md` |
| 379 | 3721 | `Yang2026-shield.md` |
| 382 | 3874 | `Yang2025-maintenance.md` |
| 386 | 3696 | `Ye2023-tunnel.md` |
| 388 | 3667 | `Yin2026-dam.md` |
| 389 | 3518 | `You2023.md` |
| 390 | 3993 | `Yu2024-underground.md` |
| 393 | 3539 | `Zeng2025-steel.md` |
| 396 | 3934 | `Zhang2024-cabledome.md` |
| 398 | 4035 | `Zhang2025-crane.md` |
| 401 | 3968 | `Zhang2025-facade.md` |
| 402 | 3928 | `Zhang2022-LoD.md` |
| 404 | 3991 | `Zhang2026-ABM.md` |
| 405 | 3918 | `Zhang2025-MBSE.md` |
| 408 | 4017 | `Zhao2026-CUBIT.md` |
| 409 | 3711 | `Zhao2024-lifeline.md` |
| 411 | 3954 | `Zhao2022-toilet.md` |
| 412 | 3515 | `Zhao2025-anticollision.md` |
| 413 | 3972 | `Zhao2026-NATM.md` |
| 414 | 3863 | `Zhao2025-bridgesgroup.md` |
| 416 | 3923 | `Zhao2022-theory.md` |
| 418 | 3943 | `Zheng2022-collapse.md` |
| 420 | 3773 | `Zhou2021-prefab.md` |
| 421 | 4039 | `Zhu2022-BP.md` |
| 423 | 3852 | `Zhu2023-dam.md` |
| 426 | 3951 | `Zou2024-BMJO.md` |
| 427 | 3885 | `Zhang2024-BIMDT.md` |
| 428 | 3875 | `Liu2023-excavation.md` |
| 429 | 3877 | `Martinez2026.md` |

## Step 3 Deep-Read Coding (pending full text)

| ID   | P   | Q   | R   | U Tier                                                | V   | W   | X   | Z                       | AA             | AB                                          | AC                             | AD                   | AE  | AF                               | AG                                                                                                                                                                                                                                                                                                                  |
| ---- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | ----------------------- | -------------- | ------------------------------------------- | ------------------------------ | -------------------- | --- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 3756 | Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0   | 1   | 0   | Design for Safety (DfS) | None           | Other / Mixed                               | Multi (two or more data types) | Single case study    | 4   | Design for Safety                | Deployed LiDAR+radar+camera fusion validated with RTK-GNSS at real work zone (lane-level accuracy); Predictive DT framework (Digital Shadow + Digital Sibling, TTC/PET conflict metrics, C-V2X warnings) proposed but not implemented — hence Tier 2, AA None.                                                      |
| 3978 | Yes | Yes | Yes | Tier 3 - Digital Twin (bidirectional, two-way)        | 0   | 1   | 1   | Design for Safety (DfS) | Mentioned only | Digital Twin platform (no machine learning) | Multi (two or more data types) | Conceptual (no test) | 3   | BIM-to-Digital-Twin architecture | Perspective paper defining next-gen CPS/DT with explicit two-way mapping and passive/active control; scenarios (teleoperated drywall robot, postural tracking, near-miss prevention) illustrate bidirectional control but nothing implemented; ML training of movement data only suggested.                         |
| 3915 | Yes | Yes | Yes | Tier 3 - Digital Twin (bidirectional, two-way)        | 0   | 0   | 1   | Design for Safety (DfS) | Mentioned only | Digital Twin platform (no machine learning) | Multi (two or more data types) | Conceptual (no test) | 3   | Design for Safety                | Four-layer DT-based fire-safety framework (physical/virtual/application/user-interaction) with explicit feedback "integrated back with the physical building layer for automatic control"; validated only via FM-professional questionnaire, no technical test; AI learning cited from literature, not implemented. |
| 3842 | Yes | Yes | Yes | Tier 1 - Digital Model (static, no live data) | 0 | 0 | 1 | Design for Safety (DfS) | None | Digital Twin platform (no machine learning) | Multi (two or more data types) | Cross-project (multiple real projects) | 3 | Lifecycle / governance | Definition/standardisation position paper (CEN/TC 442/WG 9, ISO); two illustrative DT cases (Bidebieta-Basauri railway station, UPM civil engineering school) are management/visualisation platforms with real-time info integration but no analytics loop or learning; safety only a secondary use case. |
| 3828 | Yes | Yes | Yes | Tier 1 - Digital Model (static, no live data) | 0 | 0 | 1 | Design for Quality (DfQ) | None | Digital Twin platform (no machine learning) | Multi (two or more data types) | Single case study | 4 | Perception / Computer Vision | Serverless SfM/MVS pipeline + PostGIS defect anchors on real inspection datasets; defects as georeferenced 3D anchors support DfQ traceability; authors explicitly position against passive Level-1 twins, but no live link/learning: periodic re-scan workflow. |
| 3662 | Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 0 | 1 | Design for Safety (DfS) | Implemented | Other / Mixed | Single (one data type) | Single case study | 4 | Predictive analytics / decision support | 2-year in-service railway bridge pilot; unsupervised clustering of normal vibration + FEM-calibrated synthetic damage + LightGBM classifier (ROC-AUC 0.9999); periodic retraining of the model on accumulated data = implemented learning loop, but no convergence criterion/metric. |
| 3795 | Yes | Yes | Yes | Tier 2 - Digital Shadow (one-way physical to virtual) | 0 | 0 | 1 | Design for Safety (DfS) | None | Finite Element Method / physics-based | Multi (two or more data types) | Single case study | 4 | Design for Safety | 120-yr heritage RC bridge; ambient vibration + laser displacement monitoring; FE-based DT validated against field data, used for what-if scenarios (overweight vehicles, scour loss); six-phase Incident Response Framework; model is updated/validated, not self-learning. |
| 3911 | Yes | Yes | Yes | Tier 3 - Digital Twin (bidirectional, two-way) | 0 | 1 | 0 | Design for Safety (DfS) | None | Ontology / semantic | Multi (two or more data types) | Single case study | 4 | Predictive analytics / decision support | Tunnel project in China; DT continuously integrates settlement/TBM/structural monitoring; KG rule-based reasoning infers hazards and mitigation; bidirectional DT-KG interaction visualised for decisions; prevention of further structural impact claimed in real emergency. |
| 3953 | Yes | Yes | Yes | Tier 3 - Digital Twin (bidirectional, two-way) | 0 | 1 | 0 | Design for Safety (DfS) | Mentioned only | Other / Mixed | Multi (two or more data types) | Single case study | 4 | Design for Safety | Mobile gin pole (UHV construction): FEM kinetic analysis + TROA-ET surrogate (R2 0.9642) + NSGA-III safety-efficiency optimisation embedded in DT parallel-control architecture; bidirectional 4G/MQTT link (CANopen control commands) on real 110 kV project; safety risk -32.3%; surrogate is offline-trained, no online learning. |
| 3906 | Yes | Yes | Yes | Unclear | 1 | 1 | 1 | Both | None | Digital Twin platform (no machine learning) | Multi (two or more data types) | Conceptual (no test) | 3 | BIM-to-Digital-Twin architecture | SLR (229 pubs) + conceptual DT development framework grounded in ISO 19650; no implementation or experiment; DfS/DfQ appear as application potentials, not demonstrated. |
