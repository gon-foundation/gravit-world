"""Content of gravit.world in DE / FR / IT / EN.

Facts (names, dates, address) come from Dr. Alex Konviser (2026-10-07) and the
statutes in the Foundation's legal package. German is the legally authoritative
language; the Impressum exists only in DE / FR / IT.

PENDING(...) marks text that must be confirmed before going live; a production
build refuses to run while any remains.
"""


def PENDING(text: str) -> str:
    return f'<span class="pending" data-pending="1">{text}</span>'


SITE_URL = "https://gravit.world"
EMAIL = "web@gravit.world"
EMAIL_SHOWN = "web [at] gravit.world"  # legal notice and privacy: shown, not linked (spam)
CONTACT = '<a href="/contact/">{}</a>'
CONTACT_LABEL = {"de": "Kontaktformular", "fr": "formulaire de contact", "it": "modulo di contatto", "en": "contact form"}
LANGS = ["de", "fr", "it", "en"]
LANG_NAMES = {"de": "Deutsch", "fr": "Français", "it": "Italiano", "en": "English"}
FOUNDED_ISO = "2023-02-12"

# ── board (order as given) ────────────────────────────────────────────────
BOARD = [
    ("konviser", "Dr. Alex Konviser", {
        "de": "Präsident und Vorsitzender des Vorstands", "fr": "Président du comité",
        "it": "Presidente del comitato direttivo", "en": "President and Chair of the Board"}),
    ("neumann", "Alexander Neumann", {
        "de": "Vizepräsident, Mitglied des Vorstands", "fr": "Vice-président, membre du comité",
        "it": "Vicepresidente, membro del comitato direttivo", "en": "Vice President, Board Member"}),
    ("luca", "Alexander Luca", {
        "de": "Vizepräsident, Mitglied des Vorstands", "fr": "Vice-président, membre du comité",
        "it": "Vicepresidente, membro del comitato direttivo", "en": "Vice President, Board Member"}),
    ("schwarzstein", "Walter Schwarzstein", {
        "de": "Vizepräsident, Mitglied des Vorstands", "fr": "Vice-président, membre du comité",
        "it": "Vicepresidente, membro del comitato direttivo", "en": "Vice President, Board Member"}),
]

# ── navigation ────────────────────────────────────────────────────────────
NAV = ["foundation", "people", "governance", "projects", "publications", "news", "contact"]
FOOTER_NAV = ["statutes", "membership", "transparency", "impressum", "privacy"]
LABELS = {
    "foundation": {"de": "Foundation", "fr": "Fondation", "it": "Fondazione", "en": "Foundation"},
    "people": {"de": "Personen", "fr": "Personnes", "it": "Persone", "en": "People"},
    "governance": {"de": "Governance", "fr": "Gouvernance", "it": "Governance", "en": "Governance"},
    "projects": {"de": "Projekte", "fr": "Projets", "it": "Progetti", "en": "Projects"},
    "publications": {"de": "Publikationen", "fr": "Publications", "it": "Pubblicazioni", "en": "Publications"},
    "news": {"de": "Aktuelles", "fr": "Actualités", "it": "Attualità", "en": "News"},
    "contact": {"de": "Kontakt", "fr": "Contact", "it": "Contatto", "en": "Contact"},
    "statutes": {"de": "Statuten", "fr": "Statuts", "it": "Statuto", "en": "Statutes"},
    "membership": {"de": "Mitgliedschaft", "fr": "Adhésion", "it": "Adesione", "en": "Membership"},
    "transparency": {"de": "Transparenz", "fr": "Transparence", "it": "Trasparenza", "en": "Transparency"},
    "impressum": {"de": "Impressum", "fr": "Mentions légales", "it": "Note legali", "en": "Legal notice"},
    "privacy": {"de": "Datenschutz", "fr": "Protection des données", "it": "Protezione dei dati", "en": "Privacy"},
}
COMMON = {
    "legal_form": {"de": "Verein nach Schweizer Recht · Zürich", "fr": "Association de droit suisse · Zurich",
                   "it": "Associazione di diritto svizzero · Zurigo", "en": "Association under Swiss law · Zürich"},
    # same line as on gravit.space, with the Foundation's founding year
    "copyright": {l: "©2023 – 2026 Gravit Open Network Foundation · Gravit Open Network · Gravit Continuum · Gravit Quantum"
                  for l in ["de", "fr", "it", "en"]},
    "from": {"de": "Von", "fr": "De", "it": "Dalla", "en": "From"},
    "to_world": {"de": "in die Welt", "fr": "au reste du monde", "it": "al resto del mondo", "en": "to the rest of the world"},
    "address": {"de": "Dufourstrasse 56<br>8008 Zürich<br>Schweiz", "fr": "Dufourstrasse 56<br>8008 Zurich<br>Suisse",
                "it": "Dufourstrasse 56<br>8008 Zurigo<br>Svizzera", "en": "Dufourstrasse 56<br>8008 Zürich<br>Switzerland"},
    "board": {"de": "Vorstand", "fr": "Comité", "it": "Comitato direttivo", "en": "Board"},
    "german_prevails": {
        "de": "",
        "fr": "Les statuts sont publiés en allemand, seule version juridiquement déterminante.",
        "it": "Lo statuto è pubblicato in tedesco, unica versione giuridicamente determinante.",
        "en": "The statutes are published in German, the legally authoritative version."},
}

# ── home ──────────────────────────────────────────────────────────────────
HOME = {
    "title": "Gravit Open Network Foundation",
    "intro": {
        "de": "Die Gravit Open Network Foundation ist ein unabhängiger, gemeinnütziger Verein mit Sitz in Zürich. "
              "Sie erforscht, entwickelt und fördert offene wissenschaftliche und technische Grundlagen für verifizierbare "
              "Kommunikation, digitales Vertrauen und vertrauenswürdige autonome Systeme.",
        "fr": "La Gravit Open Network Foundation est une association indépendante à but non lucratif dont le siège est à Zurich. "
              "Elle étudie, développe et promeut des bases scientifiques et techniques ouvertes pour une communication vérifiable, "
              "la confiance numérique et des systèmes autonomes dignes de confiance.",
        "it": "La Gravit Open Network Foundation è un'associazione indipendente senza scopo di lucro con sede a Zurigo. "
              "Studia, sviluppa e promuove basi scientifiche e tecniche aperte per una comunicazione verificabile, "
              "la fiducia digitale e sistemi autonomi affidabili.",
        "en": "The Gravit Open Network Foundation is an independent non-profit association based in Zürich. "
              "It researches, develops and promotes open scientific and technical foundations for verifiable "
              "communication, digital trust and trustworthy autonomous systems."},
    "tiles": [
        ("foundation", {"de": "Zweck, Rechtsform und Grundsätze des Vereins.", "fr": "But, forme juridique et principes de l'association.",
                        "it": "Scopo, forma giuridica e principi dell'associazione.", "en": "Purpose, legal form and principles of the association."}),
        ("projects", {"de": "Offene Forschung: Gravit Triad, EES und Verifikation.", "fr": "Recherche ouverte : Gravit Triad, EES et vérification.",
                      "it": "Ricerca aperta: Gravit Triad, EES e verifica.", "en": "Open research: the Gravit Triad, EES and verification."}),
        ("people", {"de": "Der Vorstand der Foundation.", "fr": "Le comité de la fondation.",
                    "it": "Il comitato direttivo della fondazione.", "en": "The Foundation's Board."}),
        ("publications", {"de": "Offene Spezifikationen und Internet-Drafts.", "fr": "Spécifications ouvertes et Internet-Drafts.",
                          "it": "Specifiche aperte e Internet-Draft.", "en": "Open specifications and Internet-Drafts."}),
    ],
}

# ── pages: slug -> {"title": {lang}, "tagline": {lang}, "body": {lang}} ────
PAGES = {}

PAGES["foundation"] = {
    "title": LABELS["foundation"],
    "tagline": COMMON["legal_form"],
    "body": {
        "de": """
<h2>Über die Foundation</h2>
<p>Die Gravit Open Network Foundation ist ein Verein im Sinne von Art. 60 ff. des Schweizerischen Zivilgesetzbuches.
Sie verfolgt ausschliesslich gemeinnützige, wissenschaftliche, technologische und bildungsbezogene Zwecke und ist
unabhängig von politischen Parteien, Behörden, religiösen Organisationen und privaten wirtschaftlichen Einzelinteressen.</p>
<dl class="facts">
  <dt>Rechtsform</dt><dd>Verein nach Schweizer Recht</dd>
  <dt>Sitz</dt><dd>Zürich, Schweiz</dd>
  <dt>Gegründet</dt><dd>12. Februar 2023</dd>
  <dt>Adresse</dt><dd>Dufourstrasse 56, 8008 Zürich</dd>
</dl>
<h2>Zweck</h2>
<p>Zweck des Vereins ist die Erforschung, Entwicklung, Dokumentation und Förderung offener wissenschaftlicher und
technologischer Grundlagen für verifizierbare Kommunikation, digitale Vertrauenssysteme, verteilte Systeme, künstliche
Intelligenz, autonome Systeme, sichere digitale Infrastruktur und unabhängige Verifikation. Die Foundation fördert
insbesondere unabhängige und reproduzierbare Forschung, offene Protokolle und Standards, freie Software,
wissenschaftliche Bildungsarbeit und internationale Zusammenarbeit.</p>
<h2>Grundsätze</h2>
<ul>
  <li><strong>Gemeinnützig:</strong> keine Erwerbs- oder Selbsthilfezwecke; alle Mittel sind unwiderruflich dem Zweck gewidmet.</li>
  <li><strong>Unabhängig:</strong> Zusammenarbeit nur, wenn sie dem Zweck dient und die Unabhängigkeit wahrt.</li>
  <li><strong>Offen:</strong> Forschungsergebnisse, Spezifikationen und Software werden möglichst öffentlich zugänglich gemacht.</li>
  <li><strong>Transparent:</strong> nachvollziehbare Dokumentation von Tätigkeit, Governance und Entscheidungen.</li>
</ul>""",
        "fr": """
<h2>À propos de la fondation</h2>
<p>La Gravit Open Network Foundation est une association au sens des art. 60 ss du Code civil suisse. Elle poursuit
exclusivement des buts d'utilité publique, scientifiques, technologiques et éducatifs, et est indépendante des partis
politiques, des autorités, des organisations religieuses et des intérêts économiques privés particuliers.</p>
<dl class="facts">
  <dt>Forme juridique</dt><dd>Association de droit suisse</dd>
  <dt>Siège</dt><dd>Zurich, Suisse</dd>
  <dt>Fondée le</dt><dd>12 février 2023</dd>
  <dt>Adresse</dt><dd>Dufourstrasse 56, 8008 Zurich</dd>
</dl>
<h2>But</h2>
<p>L'association a pour but la recherche, le développement, la documentation et la promotion de bases scientifiques et
technologiques ouvertes pour la communication vérifiable, les systèmes de confiance numérique, les systèmes distribués,
l'intelligence artificielle, les systèmes autonomes, les infrastructures numériques sûres et la vérification indépendante.
Elle encourage notamment la recherche indépendante et reproductible, les protocoles et standards ouverts, les logiciels
libres, la formation scientifique et la coopération internationale.</p>
<h2>Principes</h2>
<ul>
  <li><strong>Utilité publique :</strong> aucun but lucratif ni d'entraide ; tous les moyens sont affectés irrévocablement au but.</li>
  <li><strong>Indépendance :</strong> coopérations uniquement si elles servent le but et préservent l'indépendance.</li>
  <li><strong>Ouverture :</strong> résultats de recherche, spécifications et logiciels rendus publics dans la mesure du possible.</li>
  <li><strong>Transparence :</strong> documentation traçable des activités, de la gouvernance et des décisions.</li>
</ul>""",
        "it": """
<h2>La fondazione</h2>
<p>La Gravit Open Network Foundation è un'associazione ai sensi degli art. 60 segg. del Codice civile svizzero. Persegue
esclusivamente scopi di pubblica utilità, scientifici, tecnologici e formativi ed è indipendente da partiti politici,
autorità, organizzazioni religiose e singoli interessi economici privati.</p>
<dl class="facts">
  <dt>Forma giuridica</dt><dd>Associazione di diritto svizzero</dd>
  <dt>Sede</dt><dd>Zurigo, Svizzera</dd>
  <dt>Fondata il</dt><dd>12 febbraio 2023</dd>
  <dt>Indirizzo</dt><dd>Dufourstrasse 56, 8008 Zurigo</dd>
</dl>
<h2>Scopo</h2>
<p>Scopo dell'associazione è la ricerca, lo sviluppo, la documentazione e la promozione di basi scientifiche e
tecnologiche aperte per la comunicazione verificabile, i sistemi di fiducia digitale, i sistemi distribuiti,
l'intelligenza artificiale, i sistemi autonomi, le infrastrutture digitali sicure e la verifica indipendente. Promuove in
particolare la ricerca indipendente e riproducibile, protocolli e standard aperti, il software libero, la formazione
scientifica e la cooperazione internazionale.</p>
<h2>Principi</h2>
<ul>
  <li><strong>Pubblica utilità:</strong> nessuno scopo di lucro o di mutuo aiuto; tutti i mezzi sono destinati irrevocabilmente allo scopo.</li>
  <li><strong>Indipendenza:</strong> collaborazioni solo se servono lo scopo e ne preservano l'indipendenza.</li>
  <li><strong>Apertura:</strong> risultati di ricerca, specifiche e software resi pubblici per quanto possibile.</li>
  <li><strong>Trasparenza:</strong> documentazione tracciabile di attività, governance e decisioni.</li>
</ul>""",
        "en": """
<h2>About the Foundation</h2>
<p>The Gravit Open Network Foundation is an association under Articles 60 et seq. of the Swiss Civil Code. It pursues
exclusively non-profit, scientific, technological and educational purposes and is independent of political parties,
public authorities, religious organisations and individual private economic interests.</p>
<dl class="facts">
  <dt>Legal form</dt><dd>Association under Swiss law (Verein)</dd>
  <dt>Seat</dt><dd>Zürich, Switzerland</dd>
  <dt>Founded</dt><dd>12 February 2023</dd>
  <dt>Address</dt><dd>Dufourstrasse 56, 8008 Zürich</dd>
</dl>
<h2>Purpose</h2>
<p>The association researches, develops, documents and promotes open scientific and technological foundations for
verifiable communication, digital trust systems, distributed systems, artificial intelligence, autonomous systems,
secure digital infrastructure and independent verification. In particular it supports independent and reproducible
research, open protocols and standards, free software, scientific education and international cooperation.</p>
<h2>Principles</h2>
<ul>
  <li><strong>Non-profit:</strong> no commercial or mutual-benefit purposes; all funds are irrevocably dedicated to the purpose.</li>
  <li><strong>Independent:</strong> cooperation only where it serves the purpose and preserves independence.</li>
  <li><strong>Open:</strong> research results, specifications and software are made public wherever possible.</li>
  <li><strong>Transparent:</strong> traceable documentation of activities, governance and decisions.</li>
</ul>"""},
}

PAGES["people"] = {
    "title": LABELS["people"],
    "tagline": {"de": "Vorstand", "fr": "Comité", "it": "Comitato direttivo", "en": "Board"},
    "body": {l: "{board}" for l in LANGS},
}

PAGES["governance"] = {
    "title": LABELS["governance"],
    "tagline": {"de": "Wie die Foundation geführt wird", "fr": "Comment la fondation est dirigée",
                "it": "Come è guidata la fondazione", "en": "How the Foundation is run"},
    "body": {
        "de": """
<h2>Vereinsversammlung</h2>
<p>Oberstes Organ. Sie tagt mindestens einmal jährlich und entscheidet unter anderem über Statuten, Wahl des Vorstands,
Jahresbericht, Jahresrechnung, Budget und Auflösung. Statutenänderungen erfordern eine Zweidrittelmehrheit.</p>
<h2>Vorstand</h2>
<p>Leitungs- und Verwaltungsorgan aus mindestens zwei Personen, gewählt für zwei Jahre. Er führt die laufenden Geschäfte,
verwaltet das Vereinsvermögen und vertritt den Verein. Präsident ist Dr. Alex Konviser.</p>
<h2>Zeichnungsberechtigung</h2>
<p>Rechtlich verbindliche Verpflichtungen erfordern die Kollektivunterschrift zu zweien.</p>
<h2>Interessenkonflikte</h2>
<p>Interessenkonflikte sind offenzulegen; betroffene Personen nehmen an Beratung und Beschluss nicht teil. Geschäfte mit
Vorstandsmitgliedern erfolgen zu marktüblichen und transparenten Bedingungen.</p>
<h2>Vergütung und Spesen</h2>
<p>Der Vorstand ist grundsätzlich ehrenamtlich tätig. Ersetzt werden effektive, belegte Auslagen. Eine angemessene
Vergütung für besondere Leistungen ist nur nach Vergütungsreglement und ohne Mitwirkung der betroffenen Person möglich.</p>
<h2>Rechnungswesen</h2>
<p>Das Geschäftsjahr entspricht dem Kalenderjahr. Die Jahresrechnung wird der Vereinsversammlung zur Genehmigung vorgelegt.</p>""",
        "fr": """
<h2>Assemblée générale</h2>
<p>Organe suprême. Elle se réunit au moins une fois par an et décide notamment des statuts, de l'élection du comité, du
rapport annuel, des comptes, du budget et de la dissolution. Les modifications statutaires requièrent une majorité des deux tiers.</p>
<h2>Comité</h2>
<p>Organe de direction et d'administration d'au moins deux personnes, élues pour deux ans. Il gère les affaires
courantes, administre le patrimoine et représente l'association. Le président est Dr. Alex Konviser.</p>
<h2>Pouvoir de signature</h2>
<p>Les engagements juridiquement contraignants requièrent la signature collective à deux.</p>
<h2>Conflits d'intérêts</h2>
<p>Les conflits d'intérêts doivent être déclarés ; les personnes concernées ne participent ni aux délibérations ni aux
décisions. Les transactions avec des membres du comité se font à des conditions usuelles et transparentes.</p>
<h2>Rémunération et frais</h2>
<p>Le comité agit en principe bénévolement. Les frais effectifs et justifiés sont remboursés. Une rémunération appropriée
pour des prestations particulières n'est possible que selon le règlement de rémunération et sans la participation de la personne concernée.</p>
<h2>Comptabilité</h2>
<p>L'exercice correspond à l'année civile. Les comptes annuels sont soumis à l'approbation de l'assemblée générale.</p>""",
        "it": """
<h2>Assemblea dei soci</h2>
<p>Organo supremo. Si riunisce almeno una volta all'anno e decide tra l'altro su statuto, elezione del comitato, rapporto
annuale, conti, budget e scioglimento. Le modifiche statutarie richiedono una maggioranza dei due terzi.</p>
<h2>Comitato direttivo</h2>
<p>Organo di direzione e amministrazione di almeno due persone, elette per due anni. Gestisce gli affari correnti,
amministra il patrimonio e rappresenta l'associazione. Il presidente è il Dr. Alex Konviser.</p>
<h2>Diritto di firma</h2>
<p>Gli impegni giuridicamente vincolanti richiedono la firma collettiva a due.</p>
<h2>Conflitti di interesse</h2>
<p>I conflitti di interesse devono essere dichiarati; le persone interessate non partecipano a deliberazioni e decisioni.
Le transazioni con membri del comitato avvengono a condizioni usuali e trasparenti.</p>
<h2>Retribuzione e spese</h2>
<p>Il comitato opera di principio a titolo onorifico. Sono rimborsate le spese effettive e documentate. Una retribuzione
adeguata per prestazioni particolari è possibile solo secondo il regolamento delle retribuzioni e senza la partecipazione della persona interessata.</p>
<h2>Contabilità</h2>
<p>L'esercizio corrisponde all'anno civile. I conti annuali sono sottoposti all'approvazione dell'assemblea dei soci.</p>""",
        "en": """
<h2>General Assembly</h2>
<p>The supreme body. It meets at least once a year and decides, among other things, on the statutes, the election of
the Board, the annual report and accounts, the budget and dissolution. Amending the statutes requires a two-thirds majority.</p>
<h2>Board</h2>
<p>The management body of at least two members, elected for two years. It runs day-to-day business, manages the
association's assets and represents it. The President is Dr. Alex Konviser.</p>
<h2>Signing authority</h2>
<p>Legally binding commitments require the joint signature of two authorised persons.</p>
<h2>Conflicts of interest</h2>
<p>Conflicts of interest must be disclosed; those concerned take no part in deliberation or decision. Transactions with
Board members are made on arm's-length, transparent terms.</p>
<h2>Remuneration and expenses</h2>
<p>Board members serve on an honorary basis. Actual, documented expenses are reimbursed. Reasonable remuneration for
special services is possible only under the remuneration regulation and without the participation of the person concerned.</p>
<h2>Accounts</h2>
<p>The financial year is the calendar year. The annual accounts are submitted to the General Assembly for approval.</p>"""},
}

PAGES["statutes"] = {
    "title": LABELS["statutes"],
    # new version; replaces the original statutes adopted at the founding assembly of 12 Feb 2023
    "tagline": {"de": "Fassung vom 7. Oktober 2026", "fr": "Version du 7 octobre 2026",
                "it": "Versione del 7 ottobre 2026", "en": "Version of 7 October 2026"},
    # body is generated from STATUTEN_DE (German only, authoritative)
    "body": {l: "{statutes}" for l in LANGS},
}

OVERVIEW_EN = """
<p>Gravit Open Network is a distributed system designed to establish verifiable trust and semantic clarity in
environments where artificial intelligence operates autonomously and at scale.</p>
<p>The core of the system is Epistemic Execution Systems (EES), a formal standard in which every unit of knowledge is
inseparable from its origin, its reasoning trajectory, and the conditions of its formation. Knowledge is preserved as a
complete epistemic structure that can be independently replayed, audited, and validated. Verification is treated as a
system-level primitive rather than an external step.</p>
<p>The architecture is implemented as the Gravit Triad. The <strong>Gravit Open Network</strong> layer provides secure
communication between AI agents. The <strong>Gravit Continuum</strong> serves as a semantic verification environment
where independent validators evaluate logic and factual consistency; outputs are not accepted by default and must
withstand adversarial conditions and conflicting interpretations. Only knowledge that remains stable under pressure
becomes a verifiable state. The <strong>Gravit Quantum</strong> layer enables high-dimensional reasoning through
integrated computational models.</p>
<p>Truth is not declared but continuously validated. Gravit is designed with a people-first constraint: every decision
and knowledge state can be traced and verified. The Gravit Open Network is currently in testnet, with mainnet planned
for Q4 2026.</p>"""

OVERVIEW = {
    "en": OVERVIEW_EN,
    "de": """
<p>Gravit Open Network ist ein verteiltes System, das verifizierbares Vertrauen und semantische Klarheit dort schaffen
soll, wo künstliche Intelligenz autonom und in grossem Massstab arbeitet.</p>
<p>Kern des Systems sind Epistemic Execution Systems (EES), ein formaler Standard, bei dem jede Wissenseinheit untrennbar
mit ihrer Herkunft, ihrem Begründungsweg und den Bedingungen ihrer Entstehung verbunden bleibt. Wissen wird als
vollständige epistemische Struktur bewahrt, die unabhängig nachvollzogen, geprüft und validiert werden kann. Verifikation
ist ein Grundbaustein des Systems und kein nachgelagerter Schritt.</p>
<p>Umgesetzt wird dies in der Gravit Triad. Die Ebene <strong>Gravit Open Network</strong> ermöglicht sichere
Kommunikation zwischen KI-Agenten. <strong>Gravit Continuum</strong> ist eine Umgebung für semantische Verifikation, in der
unabhängige Validatoren Logik und sachliche Konsistenz prüfen; Ergebnisse gelten nicht automatisch als akzeptiert und
müssen widersprüchlichen Bedingungen standhalten. Nur Wissen, das unter Druck stabil bleibt, wird zu einem verifizierbaren
Zustand. <strong>Gravit Quantum</strong> ermöglicht hochdimensionales Schliessen durch integrierte Rechenmodelle.</p>
<p>Wahrheit wird nicht erklärt, sondern fortlaufend überprüft. Gravit folgt dem Grundsatz «der Mensch zuerst»: Jede
Entscheidung und jeder Wissenszustand ist nachvollziehbar und überprüfbar. Das Gravit Open Network befindet sich im
Testnetz; das Hauptnetz ist für das vierte Quartal 2026 geplant.</p>""",
    "fr": """
<p>Gravit Open Network est un système distribué conçu pour établir une confiance vérifiable et une clarté sémantique là
où l'intelligence artificielle opère de manière autonome et à grande échelle.</p>
<p>Au cœur du système se trouvent les Epistemic Execution Systems (EES), un standard formel dans lequel chaque unité de
connaissance reste indissociable de son origine, de son raisonnement et des conditions de sa formation. La connaissance
est conservée comme une structure épistémique complète, qui peut être rejouée, auditée et validée de manière
indépendante. La vérification est une primitive du système et non une étape externe.</p>
<p>L'architecture est mise en œuvre dans la Gravit Triad. La couche <strong>Gravit Open Network</strong> assure une
communication sûre entre agents d'IA. <strong>Gravit Continuum</strong> est un environnement de vérification sémantique où
des validateurs indépendants évaluent la logique et la cohérence factuelle ; aucun résultat n'est accepté par défaut et
chacun doit résister à des conditions adverses. Seule une connaissance qui reste stable sous pression devient un état
vérifiable. <strong>Gravit Quantum</strong> permet un raisonnement de haute dimension par des modèles de calcul intégrés.</p>
<p>La vérité n'est pas déclarée, elle est validée en continu. Gravit place l'humain au premier plan : chaque décision et
chaque état de connaissance sont traçables et vérifiables. Le Gravit Open Network est actuellement en testnet ; le
mainnet est prévu pour le quatrième trimestre 2026.</p>""",
    "it": """
<p>Gravit Open Network è un sistema distribuito pensato per creare fiducia verificabile e chiarezza semantica dove
l'intelligenza artificiale opera in modo autonomo e su larga scala.</p>
<p>Il cuore del sistema sono gli Epistemic Execution Systems (EES), uno standard formale in cui ogni unità di conoscenza
resta inseparabile dalla sua origine, dal suo percorso di ragionamento e dalle condizioni in cui si è formata. La
conoscenza è conservata come struttura epistemica completa, che può essere ripercorsa, verificata e convalidata in modo
indipendente. La verifica è una primitiva del sistema e non un passaggio esterno.</p>
<p>L'architettura è realizzata nella Gravit Triad. Il livello <strong>Gravit Open Network</strong> garantisce una
comunicazione sicura tra agenti di IA. <strong>Gravit Continuum</strong> è un ambiente di verifica semantica in cui
validatori indipendenti valutano logica e coerenza fattuale; nessun risultato è accettato per impostazione predefinita e
ognuno deve resistere a condizioni avverse. Solo la conoscenza che rimane stabile sotto pressione diventa uno stato
verificabile. <strong>Gravit Quantum</strong> consente un ragionamento ad alta dimensionalità tramite modelli di calcolo integrati.</p>
<p>La verità non viene dichiarata, ma convalidata continuamente. Gravit mette al primo posto le persone: ogni decisione e
ogni stato di conoscenza sono tracciabili e verificabili. Il Gravit Open Network è attualmente in testnet; la mainnet è
prevista per il quarto trimestre 2026.</p>""",
}

PROJECT_LIST = {
    "de": """
<h2>Laufende Projekte</h2>
<ul>
  <li><strong>Epistemic Execution Systems (EES)</strong> – formaler Standard für nachvollziehbares, überprüfbares Wissen. Status: in Entwicklung.</li>
  <li><strong>Offene Standardisierung</strong> – Spezifikationen als IETF Internet-Drafts (siehe <a href="../publications/">Publikationen</a>).</li>
  <li><strong>Referenzimplementierung</strong> – quelloffener Verifier, der die Regeln reproduzierbar umsetzt und gemeinsam mit Testvektoren geprüft wird.</li>
</ul>
<p class="note">Technische Details und Code: <a href="https://gravit.space">gravit.space</a> · Gravit Verifier: <a href="https://gravitverifier.space">gravitverifier.space</a></p>""",
    "fr": """
<h2>Projets en cours</h2>
<ul>
  <li><strong>Epistemic Execution Systems (EES)</strong> – standard formel pour une connaissance traçable et vérifiable. Statut : en développement.</li>
  <li><strong>Standardisation ouverte</strong> – spécifications sous forme d'Internet-Drafts de l'IETF (voir <a href="../publications/">Publications</a>).</li>
  <li><strong>Implémentation de référence</strong> – vérificateur open source appliquant les règles de façon reproductible, contrôlé par des vecteurs de test.</li>
</ul>
<p class="note">Détails techniques et code : <a href="https://gravit.space">gravit.space</a> · Gravit Verifier: <a href="https://gravitverifier.space">gravitverifier.space</a></p>""",
    "it": """
<h2>Progetti in corso</h2>
<ul>
  <li><strong>Epistemic Execution Systems (EES)</strong> – standard formale per una conoscenza tracciabile e verificabile. Stato: in sviluppo.</li>
  <li><strong>Standardizzazione aperta</strong> – specifiche come Internet-Draft dell'IETF (vedi <a href="../publications/">Pubblicazioni</a>).</li>
  <li><strong>Implementazione di riferimento</strong> – verificatore open source che applica le regole in modo riproducibile, controllato con vettori di test.</li>
</ul>
<p class="note">Dettagli tecnici e codice: <a href="https://gravit.space">gravit.space</a> · Gravit Verifier: <a href="https://gravitverifier.space">gravitverifier.space</a></p>""",
    "en": """
<h2>Current projects</h2>
<ul>
  <li><strong>Epistemic Execution Systems (EES)</strong> – a formal standard for traceable, verifiable knowledge. Status: in development.</li>
  <li><strong>Open standardisation</strong> – specifications published as IETF Internet-Drafts (see <a href="../publications/">Publications</a>).</li>
  <li><strong>Reference implementation</strong> – an open-source verifier that applies the rules reproducibly, checked against shared test vectors.</li>
</ul>
<p class="note">Technical details and code: <a href="https://gravit.space">gravit.space</a> · Gravit Verifier: <a href="https://gravitverifier.space">gravitverifier.space</a></p>""",
}

PAGES["projects"] = {
    "title": LABELS["projects"],
    "tagline": {"de": "Gravit Triad", "fr": "Gravit Triad", "it": "Gravit Triad", "en": "The Gravit Triad"},
    "body": {l: OVERVIEW[l] + PROJECT_LIST[l] for l in LANGS},
}

# Each publication links to the exact published version (not the generic document page),
# plus parallel publications (e.g. the Foundation's LinkedIn post) when there is one.
IETF = "https://datatracker.ietf.org/doc"
ARCHIVE = "https://www.ietf.org/archive/id"
LINKEDIN = {  # the Foundation's LinkedIn posts (tracking parameters removed)
    "gevp-04": "https://www.linkedin.com/posts/gravit-open-network_github-gravitopennetworkgravitnet-canonical-activity-7487139690001760256-bX3I",
    "testnet": "https://www.linkedin.com/posts/gravit-open-network_gravit-verifiableintelligence-gravotcore-activity-7488256075712880641-ZfMD",
    "gevp-06": "https://www.linkedin.com/posts/gravit-open-network_gravitopennetwork-ietf-gevp-activity-7490842551374024704-miMX",
    "two-track": "https://www.linkedin.com/posts/gravit-open-network_euaiact-ietf-gevp-activity-7501247819274616832-p609",
}
DRAFTS = [
    # (date, title, name, current rev, all revs oldest first, {rev: {label: url}} parallel publications)
    ("2026-10-13", "GEVP – Gravit Epistemic Verification Protocol", "draft-gravit-gevp", "09",
     ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09"],
     {"04": {"LinkedIn": LINKEDIN["gevp-04"]}, "06": {"LinkedIn": LINKEDIN["gevp-06"]},
      "07": {"LinkedIn": LINKEDIN["two-track"]}}),
    ("2026-08-09", "VEDS – Verifiable Epistemic Decision Standard", "draft-gravit-verifiable-epistemic-decision", "00",
     ["00"], {"00": {"LinkedIn": LINKEDIN["two-track"]}}),
    ("2026-07-21", "VCP – Verifiable Convergence Protocol (superseded: renamed GEVP to avoid a name collision with draft-kamimura-scitt-vcp)", "draft-gravit-vcp", "01", ["00", "01"], {}),
]
CODE = [
    ("Gravit Grover", "https://github.com/gravit-open-network-foundation/gravit-grover"),
    ("Gravit Verifier", "https://github.com/gravit-open-network-foundation/verifier"),
]
EARLIER = {"de": "Frühere Fassungen", "fr": "Versions antérieures", "it": "Versioni precedenti", "en": "Earlier versions"}
CODE_TEXT = {"de": "Quellcode", "fr": "Code source", "it": "Codice sorgente", "en": "Source code"}


def draft_links(name, rev, extra):
    """Direct links to one published draft version: datatracker page, full text, parallel posts."""
    links = [(f"{name}-{rev}", f"{IETF}/{name}/{rev}/"), ("HTML", f"{ARCHIVE}/{name}-{rev}.html"),
             ("TXT", f"{ARCHIVE}/{name}-{rev}.txt")] + list(extra.items())
    return " · ".join(f'<a href="{u}">{t}</a>' for t, u in links)


RFC_GOAL = {
    "de": "<strong>Unser Ziel: die Veröffentlichung von GEVP als RFC.</strong>",
    "fr": "<strong>Notre objectif : la publication de GEVP en tant que RFC.</strong>",
    "it": "<strong>Il nostro obiettivo: la pubblicazione di GEVP come RFC.</strong>",
    "en": "<strong>Our goal: publication of GEVP as an RFC.</strong>",
}
PUB_TEXT = {
    "de": ("Internet-Drafts", "Internet-Drafts sind Einzeleinreichungen; sie sind nicht von der IETF verabschiedet und haben im Standardisierungsprozess keinen formellen Status."),
    "fr": ("Internet-Drafts", "Les Internet-Drafts sont des soumissions individuelles ; ils ne sont pas approuvés par l'IETF et n'ont pas de statut formel dans le processus de normalisation."),
    "it": ("Internet-Draft", "Gli Internet-Draft sono contributi individuali; non sono approvati dall'IETF e non hanno uno status formale nel processo di standardizzazione."),
    "en": ("Internet-Drafts", "Internet-Drafts are individual submissions; they are not endorsed by the IETF and have no formal standing in the IETF standards process."),
}
def revisions_html(lang, name, current, revs, posts):
    earlier = [r for r in revs if r != current]
    if not earlier:
        return ""
    return (f'<div class="links">{EARLIER[lang]}: ' + " · ".join(
        f'<a href="{IETF}/{name}/{r}/">-{r}</a>'
        + "".join(f' (<a href="{u}">{t}</a>)' for t, u in posts.get(r, {}).items())
        for r in reversed(earlier)) + "</div>")


PAGES["publications"] = {
    "title": LABELS["publications"],
    "tagline": {"de": "Offene Spezifikationen", "fr": "Spécifications ouvertes", "it": "Specifiche aperte", "en": "Open specifications"},
    "body": {l: f"<h2>{PUB_TEXT[l][0]}</h2>\n<ul class=\"entries\">\n" + "".join(
        f'<li><div class="date">{d}</div><div class="title">{t}</div>'
        f'<div class="links">{draft_links(n, r, p.get(r, {}))}</div>{revisions_html(l, n, r, rs, p)}</li>\n'
        for d, t, n, r, rs, p in DRAFTS) + f"</ul>\n<p>{RFC_GOAL[l]}</p>\n<p class=\"note\">{PUB_TEXT[l][1]}</p>"
        + f"\n<h2>{CODE_TEXT[l]}</h2>\n<ul>" + "".join(f'<li><a href="{u}">{t}</a></li>' for t, u in CODE) + "</ul>"
        for l in LANGS},
}

# News / activities: newest first. Add entries here; they appear on News and Home.
NEWS = [
    ("2026-10-13", {"de": "GEVP-09 veröffentlicht: vollständige Spezifikation", "fr": "Publication de GEVP-09 : spécification complète",
                    "it": "Pubblicato GEVP-09: specifica completa", "en": "GEVP-09 published: a complete specification"},
     {"de": "Revision 09 beschreibt das Protokoll so genau wie die Referenzimplementierung v0.6.0: Format und Signatur der Belege, das signierte Ergebnis (wahr, falsch, kein Urteil), das Register mit Schwellenwert der Root-Schlüssel, die reproduzierbare Entscheidung und signierte Quittungen für die Prüfung ohne Vertrauen in den Dienst. Unser Ziel: die Veröffentlichung als RFC.",
      "fr": "La révision 09 décrit le protocole aussi précisément que l'implémentation de référence v0.6.0 : format et signature des preuves, résultat signé (vrai, faux, sans verdict), registre accepté sous un seuil de clés racines, décision reproductible et reçus signés permettant un audit sans faire confiance au service. Notre objectif : la publication en tant que RFC.",
      "it": "La revisione 09 descrive il protocollo con la stessa precisione dell'implementazione di riferimento v0.6.0: formato e firma delle prove, risultato firmato (vero, falso, nessun verdetto), registro accettato sotto una soglia di chiavi radice, decisione riproducibile e ricevute firmate per un audit senza fidarsi del servizio. Il nostro obiettivo: la pubblicazione come RFC.",
      "en": "Revision 09 specifies the protocol as precisely as the reference implementation v0.6.0: the format and signature of evidence records, the signed result (true, false, no verdict), a registry accepted under a threshold of root keys, a reproducible decision record and signed receipts that let an auditor check decisions without trusting the service. Our goal: publication as an RFC."},
     draft_links("draft-gravit-gevp", "09", {})),
    ("2026-10-12", {"de": "GEVP-08 veröffentlicht: Korrektur", "fr": "Publication de GEVP-08 : correction",
                    "it": "Pubblicato GEVP-08: correzione", "en": "GEVP-08 published: a correction"},
     {"de": "Revision 08 ersetzt die nicht reproduzierbaren Kalibrierungszahlen früherer Fassungen durch reproduzierbare Ergebnisse; der Schwellenwert 0,73 wird nicht mehr empfohlen. Die früheren Zahlen bleiben dokumentiert.",
      "fr": "La révision 08 remplace les chiffres de calibrage non reproductibles des versions antérieures par des résultats reproductibles ; le seuil de 0,73 n'est plus recommandé. Les anciens chiffres restent documentés.",
      "it": "La revisione 08 sostituisce i dati di calibrazione non riproducibili delle versioni precedenti con risultati riproducibili; la soglia 0,73 non è più raccomandata. I dati precedenti restano documentati.",
      "en": "Revision 08 replaces the unreproducible calibration figures of earlier revisions with reproducible results; the 0.73 threshold is no longer recommended. The earlier figures remain on record."},
     draft_links("draft-gravit-gevp", "08", {})),
    ("2026-09-03", {"de": "Zwei-Spur-Architektur: GEVP-07 und VEDS-00", "fr": "Architecture à deux voies : GEVP-07 et VEDS-00",
                    "it": "Architettura a due binari: GEVP-07 e VEDS-00", "en": "Two-track architecture: GEVP-07 and VEDS-00"},
     {"de": "GEVP beschreibt, wie verifiziert wird; VEDS, was eine verifizierte Entscheidung garantieren muss – mit Bezug auf Art. 50 EU AI Act.",
      "fr": "GEVP décrit comment vérifier ; VEDS, ce qu'une décision vérifiée doit garantir – en lien avec l'art. 50 de l'AI Act de l'UE.",
      "it": "GEVP descrive come verificare; VEDS, che cosa deve garantire una decisione verificata – con riferimento all'art. 50 dell'AI Act UE.",
      "en": "GEVP describes how to verify; VEDS what a verified decision must guarantee – with reference to Art. 50 of the EU AI Act."},
     f'<a href="{LINKEDIN["two-track"]}">LinkedIn</a>'),
    ("2026-08-12", {"de": "GEVP-07 veröffentlicht", "fr": "Publication de GEVP-07", "it": "Pubblicato GEVP-07", "en": "GEVP-07 published"},
     {"de": "Revision 07 des Gravit Epistemic Verification Protocol als IETF Internet-Draft.",
      "fr": "Révision 07 du Gravit Epistemic Verification Protocol publiée comme Internet-Draft de l'IETF.",
      "it": "Revisione 07 del Gravit Epistemic Verification Protocol pubblicata come Internet-Draft dell'IETF.",
      "en": "Revision 07 of the Gravit Epistemic Verification Protocol published as an IETF Internet-Draft."}, draft_links("draft-gravit-gevp", "07", {})),
    ("2026-08-09", {"de": "VEDS-00 veröffentlicht", "fr": "Publication de VEDS-00", "it": "Pubblicato VEDS-00", "en": "VEDS-00 published"},
     {"de": "Erste Fassung des Standards für verifizierbare epistemische Entscheidungen als IETF Internet-Draft.",
      "fr": "Première version du standard de décision épistémique vérifiable publiée comme Internet-Draft de l'IETF.",
      "it": "Prima versione dello standard per decisioni epistemiche verificabili pubblicata come Internet-Draft dell'IETF.",
      "en": "First version of the verifiable epistemic decision standard published as an IETF Internet-Draft."}, draft_links("draft-gravit-verifiable-epistemic-decision", "00", {})),
    ("2026-08-05", {"de": "GEVP-06 veröffentlicht", "fr": "Publication de GEVP-06", "it": "Pubblicato GEVP-06", "en": "GEVP-06 published"},
     {"de": "Revision 06 des Gravit Epistemic Verification Protocol als IETF Internet-Draft.",
      "fr": "Révision 06 du Gravit Epistemic Verification Protocol publiée comme Internet-Draft de l'IETF.",
      "it": "Revisione 06 del Gravit Epistemic Verification Protocol pubblicata come Internet-Draft dell'IETF.",
      "en": "Revision 06 of the Gravit Epistemic Verification Protocol published as an IETF Internet-Draft."},
     draft_links("draft-gravit-gevp", "06", {"LinkedIn": LINKEDIN["gevp-06"]})),
    ("2026-07-29", {"de": "Öffentliches Testnet von Gravit Core angekündigt", "fr": "Annonce du testnet public de Gravit Core",
                    "it": "Annunciato il testnet pubblico di Gravit Core", "en": "Public testnet of Gravit Core announced"},
     {"de": "Ankündigung des öffentlichen Testnets (gestartet am 25.07.2026).",
      "fr": "Annonce du testnet public (lancé le 25.07.2026).",
      "it": "Annuncio del testnet pubblico (avviato il 25.07.2026).",
      "en": "Announcement of the public testnet (launched on 25 July 2026)."},
     f'<a href="{LINKEDIN["testnet"]}">LinkedIn</a>'),
    ("2026-07-24", {"de": "GEVP-04 veröffentlicht", "fr": "Publication de GEVP-04", "it": "Pubblicato GEVP-04", "en": "GEVP-04 published"},
     {"de": "Revision 04 des Gravit Epistemic Verification Protocol als IETF Internet-Draft.",
      "fr": "Révision 04 du Gravit Epistemic Verification Protocol publiée comme Internet-Draft de l'IETF.",
      "it": "Revisione 04 del Gravit Epistemic Verification Protocol pubblicata come Internet-Draft dell'IETF.",
      "en": "Revision 04 of the Gravit Epistemic Verification Protocol published as an IETF Internet-Draft."},
     draft_links("draft-gravit-gevp", "04", {"LinkedIn": LINKEDIN["gevp-04"]})),
    ("2026-07-21", {"de": "VCP-01 veröffentlicht", "fr": "Publication de VCP-01", "it": "Pubblicato VCP-01", "en": "VCP-01 published"},
     {"de": "Revision 01 des Verifiable Convergence Protocol als IETF Internet-Draft.",
      "fr": "Révision 01 du Verifiable Convergence Protocol publiée comme Internet-Draft de l'IETF.",
      "it": "Revisione 01 del Verifiable Convergence Protocol pubblicata come Internet-Draft dell'IETF.",
      "en": "Revision 01 of the Verifiable Convergence Protocol published as an IETF Internet-Draft."}, draft_links("draft-gravit-vcp", "01", {})),
]
PAGES["news"] = {
    "title": LABELS["news"],
    "tagline": {"de": "Tätigkeiten und Veranstaltungen", "fr": "Activités et événements", "it": "Attività ed eventi", "en": "Activities and events"},
    "body": {l: "{news}" for l in LANGS},
}

PAGES["membership"] = {
    "title": LABELS["membership"],
    "tagline": {"de": "Mitglied werden", "fr": "Devenir membre", "it": "Diventare membro", "en": "Becoming a member"},
    "body": {
        "de": f"""<p>Mitglied können natürliche und juristische Personen werden, die den Zweck des Vereins unterstützen.
Über die Aufnahme entscheidet der Vorstand. Jedes Mitglied hat in der Vereinsversammlung eine Stimme.</p>
<p>Der Austritt ist jederzeit durch schriftliche Erklärung an den Vorstand möglich. Ein Ausschluss ist nur bei erheblichem
Verstoss gegen Zweck oder Pflichten und nach Anhörung möglich. Mitglieder haben keinen Anspruch auf das Vereinsvermögen.</p>
<p>Aufnahmegesuche über das <a href="/contact/">Kontaktformular</a></p>""",
        "fr": f"""<p>Peuvent devenir membres les personnes physiques et morales qui soutiennent le but de l'association.
Le comité décide de l'admission. Chaque membre dispose d'une voix à l'assemblée générale.</p>
<p>La démission est possible en tout temps par déclaration écrite au comité. Une exclusion n'est possible qu'en cas de
violation grave du but ou des obligations, après audition. Les membres n'ont aucun droit sur le patrimoine de l'association.</p>
<p>Demandes d'admission : par le <a href="/contact/">formulaire de contact</a></p>""",
        "it": f"""<p>Possono diventare membri le persone fisiche e giuridiche che sostengono lo scopo dell'associazione.
Il comitato decide sull'ammissione. Ogni membro dispone di un voto nell'assemblea dei soci.</p>
<p>Il recesso è possibile in ogni momento con dichiarazione scritta al comitato. L'esclusione è possibile solo in caso di
grave violazione dello scopo o degli obblighi, previa audizione. I membri non hanno diritti sul patrimonio dell'associazione.</p>
<p>Domande di ammissione: tramite il <a href="/contact/">modulo di contatto</a></p>""",
        "en": f"""<p>Natural and legal persons who support the association's purpose may become members. The Board decides on
admission. Each member has one vote at the General Assembly.</p>
<p>Members may resign at any time by written notice to the Board. Exclusion is possible only for serious breaches of the
purpose or duties, after a hearing. Members have no claim on the association's assets.</p>
<p>Applications through the <a href="/contact/">contact form</a></p>"""},
}

PAGES["transparency"] = {
    "title": LABELS["transparency"],
    "tagline": {"de": "Nachvollziehbarkeit", "fr": "Traçabilité", "it": "Tracciabilità", "en": "Accountability"},
    "body": {
        "de": """<ul>
<li>Die Statuten und die Grundsätze der Governance sind öffentlich.</li>
<li>Nach jedem Geschäftsjahr wird ein Tätigkeitsbericht veröffentlicht.</li>
<li>Sämtliche Mittel sind unwiderruflich dem gemeinnützigen Zweck gewidmet; Ausschüttungen an Mitglieder, Gründer oder Vorstand sind ausgeschlossen.</li>
<li>Interessenkonflikte werden offengelegt; Vergütungen und Spesen sind reglementiert und werden dokumentiert.</li>
<li>Bei Auflösung geht das verbleibende Vermögen an eine steuerbefreite Institution in der Schweiz mit gleichem oder ähnlichem Zweck.</li>
</ul>
<h2 id="standards">Sicherheit und Standards</h2>
<p>Unsere Werkzeuge beruhen auf offenen, veröffentlichten Standards. Wir sagen genau, welche, und wie weit wir sind. Nichts davon ist eine Zertifizierung.</p>
<ul>
<li><strong>In Gebrauch:</strong> Signaturen Ed25519 (RFC 8032); Fingerabdrücke SHA-256 und SHA3-256 (FIPS 180-4, FIPS 202); öffentliches Belegprotokoll mit Merkle-Bäumen (RFC 9162); Zeitstempel von drei unabhängigen Stellen (RFC 3161); Verbindungen mit dem postquantensicheren Schlüsselaustausch ML-KEM (NIST FIPS 203).</li>
<li><strong>In Arbeit:</strong> postquantensichere Signaturen ML-DSA (NIST FIPS 204) als zweite Signatur neben Ed25519.</li>
<li><strong>Geplant:</strong> hashbasierte Signaturen SLH-DSA (NIST FIPS 205) für langlebige Nachweise.</li>
</ul>
<p>Signaturen von heute müssen noch in Jahrzehnten prüfbar sein. Deshalb stellen wir schrittweise und mit öffentlichen Testvektoren auf die neuen Standards des NIST um. Unsere Protokolle sind Internet-Drafts bei der IETF; die Arbeit des NIST zu postquantensicherer Kryptografie und zur Sicherheit von KI-Agenten verfolgen wir und werden uns an öffentlichen Konsultationen beteiligen. Wir sind mit dem NIST nicht verbunden und werden von ihm nicht empfohlen. Aktueller Stand: <a href="https://gravitverifier.space/#standards">gravitverifier.space</a>.</p>""",
        "fr": """<ul>
<li>Les statuts et les principes de gouvernance sont publics.</li>
<li>Un rapport d'activité est publié après chaque exercice.</li>
<li>Tous les moyens sont affectés irrévocablement au but d'utilité publique ; aucune distribution aux membres, fondateurs ou membres du comité.</li>
<li>Les conflits d'intérêts sont déclarés ; rémunérations et frais sont réglementés et documentés.</li>
<li>En cas de dissolution, le patrimoine restant revient à une institution suisse exonérée d'impôt ayant un but identique ou similaire.</li>
</ul>
<h2 id="standards">Sécurité et normes</h2>
<p>Nos outils reposent sur des normes ouvertes et publiées. Nous disons exactement lesquelles, et où nous en sommes. Rien de ceci n'est une certification.</p>
<ul>
<li><strong>En usage :</strong> signatures Ed25519 (RFC 8032) ; empreintes SHA-256 et SHA3-256 (FIPS 180-4, FIPS 202) ; journal public des reçus en arbres de Merkle (RFC 9162) ; horodatage par trois autorités indépendantes (RFC 3161) ; connexions avec l'échange de clés post quantique ML-KEM (NIST FIPS 203).</li>
<li><strong>En cours :</strong> signatures post quantiques ML-DSA (NIST FIPS 204), en seconde signature à côté d'Ed25519.</li>
<li><strong>Prévu :</strong> signatures fondées sur le hachage SLH-DSA (NIST FIPS 205) pour les preuves à long terme.</li>
</ul>
<p>Les signatures d'aujourd'hui doivent rester vérifiables dans des décennies. Nous passons donc pas à pas, avec des vecteurs de test publics, aux nouvelles normes du NIST. Nos protocoles sont des Internet-Drafts à l'IETF ; nous suivons les travaux du NIST sur la cryptographie post quantique et la sécurité des agents d'IA et participerons à ses consultations publiques. Nous ne sommes ni liés au NIST ni recommandés par lui. État actuel : <a href="https://gravitverifier.space/#standards">gravitverifier.space</a>.</p>""",
        "it": """<ul>
<li>Lo statuto e i principi di governance sono pubblici.</li>
<li>Dopo ogni esercizio viene pubblicato un rapporto di attività.</li>
<li>Tutti i mezzi sono destinati irrevocabilmente allo scopo di pubblica utilità; nessuna distribuzione a membri, fondatori o membri del comitato.</li>
<li>I conflitti di interesse sono dichiarati; retribuzioni e spese sono regolamentate e documentate.</li>
<li>In caso di scioglimento il patrimonio residuo va a un'istituzione svizzera esente da imposte con scopo uguale o simile.</li>
</ul>
<h2 id="standards">Sicurezza e standard</h2>
<p>I nostri strumenti si basano su standard aperti e pubblicati. Diciamo esattamente quali, e a che punto siamo. Nulla di ciò è una certificazione.</p>
<ul>
<li><strong>In uso:</strong> firme Ed25519 (RFC 8032); impronte SHA-256 e SHA3-256 (FIPS 180-4, FIPS 202); registro pubblico delle ricevute con alberi di Merkle (RFC 9162); marche temporali di tre autorità indipendenti (RFC 3161); connessioni con lo scambio di chiavi post quantistico ML-KEM (NIST FIPS 203).</li>
<li><strong>In corso:</strong> firme post quantistiche ML-DSA (NIST FIPS 204) come seconda firma accanto a Ed25519.</li>
<li><strong>Previsto:</strong> firme basate su hash SLH-DSA (NIST FIPS 205) per prove a lungo termine.</li>
</ul>
<p>Le firme di oggi devono restare verificabili per decenni. Per questo passiamo gradualmente, con vettori di test pubblici, ai nuovi standard del NIST. I nostri protocolli sono Internet-Draft presso l'IETF; seguiamo il lavoro del NIST sulla crittografia post quantistica e sulla sicurezza degli agenti di IA e parteciperemo alle sue consultazioni pubbliche. Non siamo affiliati al NIST né da esso raccomandati. Stato attuale: <a href="https://gravitverifier.space/#standards">gravitverifier.space</a>.</p>""",
        "en": """<ul>
<li>The statutes and governance principles are public.</li>
<li>An activity report is published after each financial year.</li>
<li>All funds are irrevocably dedicated to the non-profit purpose; no distributions to members, founders or Board members.</li>
<li>Conflicts of interest are disclosed; remuneration and expenses are regulated and documented.</li>
<li>On dissolution, remaining assets go to a tax-exempt Swiss institution with the same or a similar purpose.</li>
</ul>
<h2 id="standards">Security and standards</h2>
<p>Our tools build on open, published standards. We say exactly which ones, and how far we are. Nothing here is a certification.</p>
<ul>
<li><strong>In use:</strong> Ed25519 signatures (RFC 8032); SHA-256 and SHA3-256 fingerprints (FIPS 180-4, FIPS 202); a public receipt log with Merkle trees (RFC 9162); timestamps from three independent authorities (RFC 3161); connections with the post quantum key exchange ML-KEM (NIST FIPS 203).</li>
<li><strong>In progress:</strong> post quantum signatures ML-DSA (NIST FIPS 204) as a second signature next to Ed25519.</li>
<li><strong>Planned:</strong> hash based signatures SLH-DSA (NIST FIPS 205) for long term proofs.</li>
</ul>
<p>Signatures made today must still be checkable in decades. So we are moving to NIST's new standards step by step, with public test vectors. Our protocols are Internet-Drafts at the IETF; we follow NIST's work on post quantum cryptography and on the security of AI agents and will take part in its public comment periods. We are not affiliated with or endorsed by NIST. Live status: <a href="https://gravitverifier.space/#standards">gravitverifier.space</a>.</p>"""},
}

PAGES["contact"] = {
    "title": LABELS["contact"],
    "tagline": {"de": "Gravit Open Network Foundation", "fr": "Gravit Open Network Foundation",
                "it": "Gravit Open Network Foundation", "en": "Gravit Open Network Foundation"},
    "body": {l: f'<p>{COMMON["address"][l]}</p>\n<p><a href="/contact/">{CONTACT_LABEL[l]}</a></p>' for l in LANGS},
}

IMPRESSUM = {
    "de": ("Verein nach Schweizer Recht", "Sitz", "Zürich, Schweiz", "Rechtsdomizil", "Vertretung", "Vorstand",
           "Kontakt", "Web", "Verantwortlich für den Inhalt"),
    "fr": ("Association de droit suisse", "Siège", "Zurich, Suisse", "Domicile juridique", "Représentation", "Comité",
           "Contact", "Site Internet", "Responsable du contenu"),
    "it": ("Associazione di diritto svizzero", "Sede", "Zurigo, Svizzera", "Domicilio legale", "Rappresentanza",
           "Comitato direttivo", "Contatto", "Sito web", "Responsabile dei contenuti"),
}


def impressum_body(l):
    form, sitz_l, sitz, dom_l, rep_l, board_l, k_l, w_l, r_l = IMPRESSUM[l]
    names = "<br>".join(n for _, n, _ in BOARD)
    return f"""<p><strong>Gravit Open Network Foundation</strong><br>{form}</p>
<dl class="facts">
  <dt>{sitz_l}</dt><dd>{sitz}</dd>
  <dt>{dom_l}</dt><dd>{COMMON["address"][l]}</dd>
  <dt>{rep_l}</dt><dd>{names}<br><em>{board_l}</em></dd>
  <dt>{k_l}</dt><dd>{EMAIL_SHOWN} · <a href="/contact/">{CONTACT_LABEL[l]}</a></dd>
  <dt>{w_l}</dt><dd>https://gravit.world</dd>
  <dt>{r_l}</dt><dd>Gravit Open Network Foundation, Dr. Alex Konviser</dd>
</dl>"""


PAGES["impressum"] = {
    "title": LABELS["impressum"],
    "tagline": COMMON["legal_form"],
    "langs": ["de", "fr", "it"],  # Impressum only in the three Swiss languages
    "body": {l: impressum_body(l) for l in ["de", "fr", "it"]},
}

PAGES["privacy"] = {
    "title": LABELS["privacy"],
    "tagline": {"de": "Datenschutzerklärung", "fr": "Déclaration de protection des données",
                "it": "Informativa sulla protezione dei dati", "en": "Privacy notice"},
    "body": {
        "de": f"""<p>Verantwortlich: Gravit Open Network Foundation, Dufourstrasse 56, 8008 Zürich, {EMAIL_SHOWN}.</p>
<h2>Besuch der Website</h2>
<p>Die Website wird bei Hostpoint AG in der Schweiz betrieben. Beim Aufruf speichert der Server technisch notwendige Daten
(IP-Adresse, Datum und Uhrzeit, aufgerufene Seite, Browsertyp) in Protokolldateien, um den Betrieb und die Sicherheit zu
gewährleisten. Diese Daten werden nicht mit anderen Daten zusammengeführt und nach kurzer Zeit gelöscht.</p>
<p>Die Website verwendet keine Cookies, kein Tracking, keine Analysedienste und bindet keine Inhalte Dritter ein.</p>
<h2>Kontakt per E-Mail</h2>
<p>Wenn Sie uns schreiben, verwenden wir Ihre Angaben nur zur Bearbeitung Ihrer Anfrage.</p>
<h2>Ihre Rechte</h2>
<p>Nach dem Schweizer Datenschutzgesetz (DSG) können Sie Auskunft über Ihre Daten verlangen sowie deren Berichtigung oder
Löschung. Wenden Sie sich dazu an die oben genannte Adresse.</p>""",
        "fr": f"""<p>Responsable : Gravit Open Network Foundation, Dufourstrasse 56, 8008 Zurich, {EMAIL_SHOWN}.</p>
<h2>Consultation du site</h2>
<p>Le site est hébergé par Hostpoint AG en Suisse. Lors de chaque consultation, le serveur enregistre des données techniquement
nécessaires (adresse IP, date et heure, page consultée, type de navigateur) dans des fichiers journaux, afin d'assurer le
fonctionnement et la sécurité. Ces données ne sont pas combinées avec d'autres données et sont supprimées après une courte durée.</p>
<p>Le site n'utilise ni cookies, ni suivi, ni services d'analyse, et n'intègre aucun contenu de tiers.</p>
<h2>Contact par e-mail</h2>
<p>Si vous nous écrivez, vos données sont utilisées uniquement pour traiter votre demande.</p>
<h2>Vos droits</h2>
<p>Selon la loi suisse sur la protection des données (LPD), vous pouvez demander l'accès à vos données ainsi que leur
rectification ou leur effacement en vous adressant à l'adresse ci-dessus.</p>""",
        "it": f"""<p>Titolare: Gravit Open Network Foundation, Dufourstrasse 56, 8008 Zurigo, {EMAIL_SHOWN}.</p>
<h2>Visita del sito</h2>
<p>Il sito è ospitato da Hostpoint AG in Svizzera. A ogni accesso il server registra dati tecnicamente necessari (indirizzo
IP, data e ora, pagina visitata, tipo di browser) in file di log, per garantirne il funzionamento e la sicurezza. Questi dati
non vengono combinati con altri dati e sono cancellati dopo breve tempo.</p>
<p>Il sito non utilizza cookie, tracciamento o servizi di analisi e non integra contenuti di terzi.</p>
<h2>Contatto via e-mail</h2>
<p>Se ci scrive, i suoi dati sono usati solo per evadere la richiesta.</p>
<h2>I suoi diritti</h2>
<p>In base alla legge svizzera sulla protezione dei dati (LPD) può chiedere l'accesso ai suoi dati, nonché la loro rettifica
o cancellazione, scrivendo all'indirizzo sopra indicato.</p>""",
        "en": f"""<p>Controller: Gravit Open Network Foundation, Dufourstrasse 56, 8008 Zürich, Switzerland, {EMAIL_SHOWN}.</p>
<h2>Visiting this website</h2>
<p>The website is hosted by Hostpoint AG in Switzerland. On each visit the server stores technically necessary data (IP
address, date and time, page requested, browser type) in log files to keep the site running and secure. This data is not
combined with other data and is deleted after a short period.</p>
<p>The website uses no cookies, no tracking and no analytics, and embeds no third-party content.</p>
<h2>Contacting us by e-mail</h2>
<p>If you write to us, we use your details only to handle your request.</p>
<h2>Your rights</h2>
<p>Under the Swiss Federal Act on Data Protection (FADP) you may request access to, correction or deletion of your data
by writing to the address above.</p>"""},
}

# ── principle (home page, under the intro) ───────────────────────────────
GROVER = "https://github.com/gravit-open-network-foundation/gravit-grover"
HISTORY_KEEPER = "https://github.com/gravit-open-network-foundation/gravitnet/blob/main/specs/history-keeper.md"
PRINCIPLE = {
    "de": {
        "title": "Verifikation",
        "lead": "Seit mehr als zweihundert Jahren ist Verifikation der entscheidende Faktor des Fortschritts – "
                "in Wissenschaft, Recht und Finanzwesen und heute in der künstlichen Intelligenz.",
        "body": f'In Gravit Open Network trägt jedes Ereignis einen Zeitstempel. Der <a href="{HISTORY_KEEPER}">History Keeper</a> '
                "bewahrt jedes Ereignis in einem Protokoll, das nur ergänzt und von niemandem umgeschrieben werden kann. "
                f'Ereignisse werden nach ihren Parametern klassifiziert (<a href="{GROVER}">Gower-Ähnlichkeit</a>), konsistente '
                f'Hypothesen werden verstärkt (nach dem Vorbild des <a href="{GROVER}">Grover-Algorithmus</a>), und durch die '
                "Konvergenz unabhängiger Belege wird als Wahrheit festgestellt, was der Verifikation standhält. Wie Gödel gezeigt hat, "
                "kann kein hinreichend mächtiges formales System jede in ihm formulierbare Wahrheit beweisen – deshalb wird Wahrheit "
                "nie einfach erklärt, sondern durch Verifikation fortlaufend erhalten.",
        "truth": "Jeder hat seine eigene Sicht der Dinge. Die Wahrheit ist eine.",
        "quote": "Ein Symbol lässt sich leicht auf Hochglanz polieren. Geschichte lässt sich nicht auslöschen.",
        "method": 'Wir arbeiten so, wie wir es erklären. In unserer eigenen Forschung – in Laborumgebungen, auf der Suche nach tragfähigen Theorien und nach der Konvergenz unterschiedlicher Faktoren – wenden wir genau die Methoden an, die wir vorschlagen, und keine anderen: Jedes Ergebnis trägt seinen Zeitstempel und seine Geschichte, und jede Aussage muss durch Code reproduzierbar sein. So prüfen wir an uns selbst, was wir der Menschheit anbieten.',
        "verify": 'Jeder muss jederzeit selbst überprüfen können, was wir bewiesen, begründet und veröffentlicht haben – ohne uns zu fragen und ohne uns vertrauen zu müssen.',
        "amodei": 'Denselben Gedanken – unabhängige Überprüfung durch Dritte – formuliert Dario Amodei, CEO von Anthropic, in <a href="https://darioamodei.com/post/we-must-pace-the-frontier"><em>We Must Pace the Frontier</em></a> (September 2026): „it seems vital to have a neutral third party who can actually see the details“ – „the public deserves to know what is going on.“',
        "purpose": "Unser Ziel ist es, gemeinsam mit unseren Mitstreitern bleibende Werte für künftige Generationen zu schaffen. "
                   "Weil wir es erklären, sind wir verpflichtet, es zu erfüllen.",
    },
    "fr": {
        "title": "Vérification",
        "lead": "Depuis plus de deux cents ans, la vérification est le facteur décisif du progrès – "
                "dans la science, le droit, la finance et aujourd'hui l'intelligence artificielle.",
        "body": f'Dans Gravit Open Network, chaque événement porte un horodatage. Le <a href="{HISTORY_KEEPER}">History Keeper</a> '
                "conserve chaque événement dans un registre que l'on peut seulement compléter et que personne ne peut réécrire. "
                f'Les événements sont classés selon leurs paramètres (<a href="{GROVER}">similarité de Gower</a>), les hypothèses '
                f'cohérentes sont amplifiées (sur le modèle de l\'<a href="{GROVER}">algorithme de Grover</a>) et, par la convergence '
                "de preuves indépendantes, ce qui résiste à la vérification est établi comme vérité. Comme l'a montré Gödel, aucun "
                "système formel suffisamment puissant ne peut démontrer toutes les vérités qu'il peut exprimer : c'est pourquoi la "
                "vérité n'est jamais simplement déclarée, mais maintenue en permanence par la vérification.",
        "truth": "Chacun a sa propre version des faits. La vérité est une.",
        "quote": "Un symbole se polit facilement jusqu'à briller. L'histoire ne peut pas être effacée.",
        "method": "Nous travaillons comme nous le déclarons. Dans notre propre recherche – dans des environnements de laboratoire, en quête de théories solides et de convergences entre différents facteurs – nous appliquons exactement les méthodes que nous proposons, et aucune autre : chaque résultat porte son horodatage et son histoire, et chaque affirmation doit être reproductible par le code. Ainsi, nous éprouvons sur nous-mêmes ce que nous proposons à l'humanité.",
        "verify": 'Chacun doit pouvoir vérifier à tout moment, par lui-même, ce que nous avons démontré, justifié et publié – sans nous le demander et sans devoir nous faire confiance.',
        "amodei": 'La même idée – la vérification indépendante par un tiers – est formulée par Dario Amodei, CEO d\'Anthropic, dans <a href="https://darioamodei.com/post/we-must-pace-the-frontier"><em>We Must Pace the Frontier</em></a> (septembre 2026) : « it seems vital to have a neutral third party who can actually see the details » – « the public deserves to know what is going on. »',
        "purpose": "Notre but, avec nos compagnons de route, est de créer une valeur durable pour les générations futures. "
                   "Parce que nous le déclarons, nous sommes tenus de l'accomplir.",
    },
    "it": {
        "title": "Verifica",
        "lead": "Da oltre duecento anni la verifica è il fattore decisivo del progresso – "
                "nella scienza, nel diritto, nella finanza e oggi nell'intelligenza artificiale.",
        "body": f'In Gravit Open Network ogni evento porta una marca temporale. Il modulo <a href="{HISTORY_KEEPER}">History Keeper</a> '
                "conserva ogni evento in un registro che può essere solo integrato e che nessuno può riscrivere. "
                f'Gli eventi sono classificati secondo i loro parametri (<a href="{GROVER}">similarità di Gower</a>), le ipotesi '
                f'coerenti vengono amplificate (sul modello dell\'<a href="{GROVER}">algoritmo di Grover</a>) e, attraverso la '
                "convergenza di prove indipendenti, ciò che resiste alla verifica viene stabilito come verità. Come ha mostrato Gödel, "
                "nessun sistema formale sufficientemente potente può dimostrare tutte le verità che può esprimere: per questo la verità "
                "non viene mai semplicemente dichiarata, ma mantenuta costantemente dalla verifica.",
        "truth": "Ognuno ha la propria versione dei fatti. La verità è una sola.",
        "quote": "Un simbolo si lucida facilmente fino a farlo brillare. La storia non si può cancellare.",
        "method": "Lavoriamo come dichiariamo. Nella nostra ricerca – in ambienti di laboratorio, alla ricerca di teorie solide e di convergenze tra fattori diversi – applichiamo esattamente i metodi che proponiamo, e nessun altro: ogni risultato porta la sua marca temporale e la sua storia, e ogni affermazione deve essere riproducibile dal codice. Così verifichiamo su noi stessi ciò che proponiamo all'umanità.",
        "verify": 'Chiunque deve poter verificare in qualsiasi momento, da sé, ciò che abbiamo dimostrato, motivato e pubblicato – senza chiederlo a noi e senza doverci dare fiducia.',
        "amodei": 'La stessa idea – la verifica indipendente da parte di terzi – è formulata da Dario Amodei, CEO di Anthropic, in <a href="https://darioamodei.com/post/we-must-pace-the-frontier"><em>We Must Pace the Frontier</em></a> (settembre 2026): «it seems vital to have a neutral third party who can actually see the details» – «the public deserves to know what is going on.»',
        "purpose": "Il nostro scopo, insieme ai nostri compagni di strada, è creare un valore duraturo per le generazioni future. "
                   "Poiché lo dichiariamo, siamo tenuti a realizzarlo.",
    },
    "en": {
        "title": "Verification",
        "lead": "For more than two hundred years, verification has been the decisive factor of progress – "
                "in science, law, finance and now in artificial intelligence.",
        "body": f'In Gravit Open Network every event carries a timestamp. The <a href="{HISTORY_KEEPER}">History Keeper</a> '
                "preserves every event in an append-only record that no one can rewrite. "
                f'Events are classified by their parameters (<a href="{GROVER}">Gower similarity</a>), consistent hypotheses are '
                f'amplified (inspired by <a href="{GROVER}">Grover\'s algorithm</a>), and through the convergence of independent '
                "evidence what withstands verification is established as truth. As Gödel showed, no sufficiently powerful formal "
                "system can prove every truth it can express – which is why truth is never simply declared, but continuously "
                "maintained by verification.",
        "truth": "Everyone has their own version of the facts. The truth is one.",
        "quote": "A symbol can easily be polished to a shine. History cannot be erased.",
        "method": 'We work the way we declare. In our own research – in laboratory sandboxes, in the search for sound theories and for convergence between different factors – we use exactly the methods we propose, and no others: every result carries its timestamp and its history, and every claim must be reproducible by code. In this way we test on ourselves what we offer to humanity.',
        "verify": 'Anyone, at any time, must be able to verify independently what we have proven, justified and published – without asking us and without having to trust us.',
        "amodei": 'The same idea – independent verification by a third party – is set out by Dario Amodei, CEO of Anthropic, in <a href="https://darioamodei.com/post/we-must-pace-the-frontier"><em>We Must Pace the Frontier</em></a> (September 2026): “it seems vital to have a neutral third party who can actually see the details” – “the public deserves to know what is going on.”',
        "purpose": "Our purpose, together with our fellow founders, is to create lasting value for future generations. "
                   "Because we declare it, we are bound to deliver it.",
    },
}
