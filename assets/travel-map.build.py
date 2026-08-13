import math
LAT0, LON0, P1, P2 = 37.5, -96.0, 29.5, 45.5
r = math.radians
n = 0.5*(math.sin(r(P1))+math.sin(r(P2)))
C = math.cos(r(P1))**2 + 2*n*math.sin(r(P1))
rho0 = math.sqrt(C - 2*n*math.sin(r(LAT0)))/n
def albers(lat, lon):
    th = n*(r(lon)-r(LON0)); rho = math.sqrt(C - 2*n*math.sin(r(lat)))/n
    return rho*math.sin(th), rho*math.cos(th) - rho0   # y flipped for SVG

OUTLINE = [
# Pacific coast, north to south
(48.4,-124.7),(47.4,-124.4),(46.3,-124.1),(44.6,-124.1),(43.3,-124.4),(42.0,-124.2),
(40.4,-124.4),(39.0,-123.7),(38.3,-123.1),(37.8,-122.5),(36.9,-122.0),(36.3,-121.9),
(35.4,-120.9),(34.5,-120.6),(34.0,-118.8),(33.7,-118.4),(33.2,-117.4),(32.5,-117.1),
# Mexico border
(32.7,-114.7),(32.5,-113.3),(31.7,-111.5),(31.3,-111.0),(31.3,-108.2),(31.8,-108.2),
(31.8,-106.5),(30.8,-105.6),(29.8,-104.7),(29.9,-103.3),(29.3,-103.0),(29.8,-102.4),
(29.2,-101.4),(28.4,-100.5),(26.9,-99.5),(26.4,-99.1),(25.9,-97.4),
# Gulf coast
(26.9,-97.4),(27.8,-97.1),(28.4,-96.4),(28.9,-95.4),(29.4,-94.7),(29.7,-93.8),
(29.6,-92.1),(29.5,-91.5),(29.0,-90.2),(29.2,-89.3),(30.0,-89.2),(30.4,-88.4),
(30.2,-87.5),(30.4,-86.6),(29.9,-85.4),(29.7,-84.4),(29.1,-83.1),(28.4,-82.7),
# Florida peninsula
(27.4,-82.6),(26.6,-82.2),(25.9,-81.7),(25.2,-81.1),(25.1,-80.4),(26.2,-80.1),
(27.2,-80.2),(28.4,-80.6),(29.5,-81.1),(30.4,-81.4),
# Atlantic coast, south to north
(31.4,-81.3),(32.0,-80.8),(32.8,-79.9),(33.9,-78.5),(34.6,-77.4),(34.9,-76.3),
(35.2,-75.5),(36.0,-75.7),(36.9,-76.0),(37.9,-75.4),(38.8,-75.1),(39.4,-74.4),
(40.5,-74.0),(41.0,-71.9),(41.5,-71.0),(42.0,-70.1),(42.7,-70.8),(43.1,-70.7),
(43.7,-70.2),(44.1,-69.0),(44.5,-68.0),(44.8,-67.0),
# Northern border
(45.3,-67.8),(47.1,-67.8),(47.4,-69.2),(46.4,-70.3),(45.3,-71.1),(45.0,-71.5),
(45.0,-74.7),(44.3,-76.0),(43.6,-76.4),(43.3,-79.0),(42.9,-78.9),(41.7,-82.5),
(41.9,-83.1),(43.6,-82.5),(45.0,-83.4),(45.8,-84.7),(46.5,-84.5),(46.6,-87.5),
(46.8,-90.4),(46.7,-92.1),(47.4,-90.0),(48.0,-89.6),(48.6,-93.4),(49.0,-95.2),
(49.0,-123.0),
]

CITIES = [
 ("Chicago","IL",41.88,-87.63,8),  ("Dallas","TX",32.78,-96.80,2),
 ("Orlando","FL",28.54,-81.38,2),  ("Las Vegas","NV",36.17,-115.14,2),
 ("Los Angeles","CA",34.05,-118.24,3),   # LAX + Burbank + Ontario, all greater LA
 ("New Orleans","LA",29.95,-90.07,1),("Atlanta","GA",33.75,-84.39,1),
 ("Philadelphia","PA",39.95,-75.17,1),("Salt Lake City","UT",40.76,-111.89,1),
 ("Jacksonville","FL",30.33,-81.66,1),("Fort Lauderdale","FL",26.12,-80.14,1),
 ("Raleigh","NC",35.78,-78.64,1),  ("Tucson","AZ",32.22,-110.97,1),
 ("Phoenix","AZ",33.45,-112.07,1),
]
HOME = (39.74,-104.99)

# label placement: dx, dy, anchor  (hand-tuned where dots crowd)
PLACE = {
 "Chicago":(11,4,"start"), "Dallas":(10,4,"start"), "Orlando":(11,4,"start"),
 "Las Vegas":(-11,4,"end"), "Los Angeles":(-11,4,"end"), "New Orleans":(0,20,"middle"),
 "Atlanta":(11,4,"start"), "Philadelphia":(11,4,"start"), "Salt Lake City":(-11,4,"end"),
 "Jacksonville":(11,-2,"start"), "Fort Lauderdale":(11,8,"start"), "Raleigh":(11,4,"start"),
 "Tucson":(0,20,"middle"), "Phoenix":(-11,0,"end"),
}

pts=[albers(la,lo) for la,lo in OUTLINE]
cpt=[albers(c[2],c[3]) for c in CITIES]
minx=min(p[0] for p in pts+cpt); maxx=max(p[0] for p in pts+cpt)
miny=min(p[1] for p in pts+cpt); maxy=max(p[1] for p in pts+cpt)

W,PAD = 1000, 58
s = (W-2*PAD)/(maxx-minx)
H = (maxy-miny)*s + 2*PAD
offx = PAD - minx*s; offy = PAD - miny*s
def xy(la,lo):
    x,y=albers(la,lo); return x*s+offx, y*s+offy

outline=" ".join(f"{'M' if i==0 else 'L'}{xy(la,lo)[0]:.1f},{xy(la,lo)[1]:.1f}"
                 for i,(la,lo) in enumerate(OUTLINE))+" Z"
hx,hy = xy(*HOME)
arcs=dots=labels=""
for name,st,lat,lon,trips in sorted(CITIES,key=lambda c:-c[4]):
    x,y = xy(lat,lon)
    dx,dy = x-hx, y-hy; L=math.hypot(dx,dy) or 1
    bow=min(42,L*0.15)
    cx,cy = (hx+x)/2 - dy/L*bow, (hy+y)/2 + dx/L*bow
    arcs += f'<path d="M{hx:.1f},{hy:.1f} Q{cx:.1f},{cy:.1f} {x:.1f},{y:.1f}"/>'
    rad = 4.5 + min(trips,8)*0.7
    dots += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{rad:.1f}"><title>{name}, {st} - {trips} trip{"s" if trips>1 else ""} in 2025</title></circle>'
    ldx,ldy,anc = PLACE[name]
    labels += f'<text x="{x+ldx:.1f}" y="{y+ldy:.1f}" text-anchor="{anc}">{name}</text>'

svg=f'''<svg viewBox="0 0 {W:.0f} {H:.0f}" xmlns="http://www.w3.org/2000/svg" class="travel-map" role="img"
     aria-label="Map of the United States showing the 14 metro areas Event Video Pros travelled to for events in 2025, with routes radiating from Denver, Colorado.">
  <style>
    .travel-map .land{{fill:#F2F4F8;stroke:#DDE2EA;stroke-width:1.2;stroke-linejoin:round}}
    .travel-map .arcs path{{fill:none;stroke:#4C5A99;stroke-width:1.4;opacity:.38;stroke-linecap:round}}
    .travel-map .dots circle{{fill:#4C5A99;opacity:.92}}
    .travel-map .home{{fill:#C19A36}}
    .travel-map .home-halo{{fill:#C19A36;opacity:.2}}
    .travel-map .home-label{{font:800 12px Inter,system-ui,sans-serif;fill:#A8842C;letter-spacing:.12em}}
    .travel-map .labels text{{font:600 12.5px Inter,system-ui,sans-serif;fill:#2E2E2E}}
    @media (max-width:640px){{
      .travel-map .labels text{{font-size:17px}}
      .travel-map .home-label{{font-size:16px}}
    }}
  </style>
  <path class="land" d="{outline}" fill="#F2F4F8" stroke="#DDE2EA" stroke-width="1.2"/>
  <g class="arcs" fill="none" stroke="#4C5A99" stroke-width="1.4" opacity="0.38" stroke-linecap="round">{arcs}</g>
  <g class="dots" fill="#4C5A99" opacity="0.92">{dots}</g>
  <circle class="home-halo" cx="{hx:.1f}" cy="{hy:.1f}" r="16" fill="#C19A36" opacity="0.2"/>
  <circle class="home" cx="{hx:.1f}" cy="{hy:.1f}" r="7" fill="#C19A36"/>
  <text class="home-label" x="{hx:.1f}" y="{hy-24:.1f}" text-anchor="middle" fill="#A8842C" font-family="Inter,system-ui,sans-serif" font-size="12" font-weight="800" letter-spacing="1.4">DENVER</text>
  <g class="labels" fill="#2E2E2E" font-family="Inter,system-ui,sans-serif" font-size="12.5" font-weight="600">{labels}</g>
</svg>'''
open('map.svg','w').write(svg)
print(f"wrote map.svg  viewBox 0 0 {W:.0f} {H:.0f}")
