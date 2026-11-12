SKIN="#B87A52"; SKIN_SH="#9A6240"; HAIR="#4A2C20"; HAIR_HI="#6B4330"
BK="#26262E"; BK2="#1E1E25"; BK_HI="#3B3B47"; GOLD="#E8C46A"
ORANGE="#F28C28"

AURA_FORCA='''<g id="aura-forca"{d}>
<ellipse cx="120" cy="116" rx="94" ry="100" fill="#F9C784" opacity="0.35"/>
<ellipse cx="120" cy="116" rx="80" ry="86" fill="#F4A259" opacity="0.45"/>
<ellipse cx="120" cy="116" rx="80" ry="86" fill="none" stroke="#F28C28" stroke-width="3" opacity="0.85"/>
</g>'''
AURA_NORMAL='''<g id="aura-normal"{d}>
<ellipse cx="120" cy="116" rx="86" ry="92" fill="#EEF0F4" opacity="0.45"/>
<ellipse cx="120" cy="116" rx="86" ry="92" fill="none" stroke="#D5DAE3" stroke-width="2"/>
</g>'''

P='style="fill:var(--poder)"'
PS='style="stroke:var(--poder)"'
BODY=f'''<g id="personagem">
<ellipse cx="120" cy="228" rx="54" ry="7" fill="{HAIR}" opacity="0.18"/>
<ellipse cx="120" cy="162" rx="44" ry="15" fill="{BK}"/>
<ellipse cx="62" cy="178" rx="32" ry="18" fill="{BK}"/>
<ellipse cx="178" cy="178" rx="32" ry="18" fill="{BK}"/>
<ellipse cx="100" cy="190" rx="40" ry="11" transform="rotate(-8 100 190)" fill="{BK2}" stroke="{BK_HI}" stroke-width="1.5"/>
<ellipse cx="140" cy="190" rx="40" ry="11" transform="rotate(8 140 190)" fill="{BK2}" stroke="{BK_HI}" stroke-width="1.5"/>
<ellipse cx="96" cy="187" rx="13" ry="6" fill="{SKIN}"/>
<ellipse cx="144" cy="187" rx="13" ry="6" fill="{SKIN}"/>
<circle cx="86" cy="184" r="2" fill="{SKIN}"/><circle cx="90" cy="182" r="2" fill="{SKIN}"/><circle cx="154" cy="184" r="2" fill="{SKIN}"/><circle cx="150" cy="182" r="2" fill="{SKIN}"/>
<path d="M84 98Q84 88 98 86L142 86Q156 88 156 98L150 156L90 156Z" fill="{BK}"/>
<polyline points="100,110 120,126 140,110" fill="none" stroke-width="7" stroke-linejoin="miter" {PS}/>
<path d="M88 100Q62 128 52 168" stroke="{BK}" stroke-width="16" stroke-linecap="round" fill="none"/>
<path d="M152 100Q178 128 188 168" stroke="{BK}" stroke-width="16" stroke-linecap="round" fill="none"/>
<path d="M64.2 134.4L60 143.6" stroke-width="16" fill="none" {PS}/>
<path d="M175.8 134.4L180 143.6" stroke-width="16" fill="none" {PS}/>
<circle cx="51" cy="172" r="7.5" fill="{SKIN}"/><circle cx="189" cy="172" r="7.5" fill="{SKIN}"/>
<circle cx="47" cy="168" r="3" fill="none" stroke="{SKIN_SH}" stroke-width="1.4"/><circle cx="193" cy="168" r="3" fill="none" stroke="{SKIN_SH}" stroke-width="1.4"/>
<rect x="112" y="68" width="16" height="16" fill="{SKIN_SH}"/>
<path d="M102 82h36v9q-18 7-36 0z" fill="{BK2}"/>
<g fill="{HAIR}"><circle cx="98" cy="46" r="12"/><circle cx="142" cy="46" r="12"/><circle cx="104" cy="32" r="12"/><circle cx="120" cy="26" r="13"/><circle cx="136" cy="32" r="12"/><circle cx="96" cy="60" r="9"/><circle cx="144" cy="60" r="9"/></g>
<ellipse cx="120" cy="52" rx="22" ry="25" fill="{SKIN}"/>
<ellipse cx="97.5" cy="57" rx="3.5" ry="5" fill="{SKIN}"/><ellipse cx="142.5" cy="57" rx="3.5" ry="5" fill="{SKIN}"/>
<circle cx="97.5" cy="63" r="1.7" fill="{GOLD}"/><circle cx="142.5" cy="63" r="1.7" fill="{GOLD}"/>
<g fill="{HAIR}"><circle cx="108" cy="40" r="8"/><circle cx="120" cy="37" r="8"/><circle cx="132" cy="40" r="8"/><circle cx="100" cy="48" r="6"/><circle cx="140" cy="48" r="6"/></g>
<g fill="{HAIR_HI}"><circle cx="104" cy="35" r="2.4"/><circle cx="124" cy="31" r="2.4"/><circle cx="138" cy="38" r="2.2"/><circle cx="100" cy="44" r="2"/></g>
FACE
</g>'''

FELIZ='''<g id="rosto-feliz"{d}>
<path d="M104 50q5-3 11-1M125 49q6-2 11 1" stroke="#4A2C20" stroke-width="1.8" stroke-linecap="round" fill="none"/>
<path d="M105 56q5 4 10 0M125 56q5 4 10 0" stroke="#3A241B" stroke-width="1.9" stroke-linecap="round" fill="none"/>
<path d="M119 60q-2 4 1 5" stroke="#9A6240" stroke-width="1.5" stroke-linecap="round" fill="none"/>
<path d="M112 69q8 5 16 0" stroke="#7A3B2E" stroke-width="1.9" stroke-linecap="round" fill="none"/>
<circle cx="104" cy="64" r="3.5" fill="#E58E7A" opacity="0.4"/><circle cx="136" cy="64" r="3.5" fill="#E58E7A" opacity="0.4"/>
</g>'''
TRISTE='''<g id="rosto-triste"{d}>
<path d="M104 52L115 48M125 48L136 52" stroke="#4A2C20" stroke-width="1.8" stroke-linecap="round" fill="none"/>
<path d="M105 58q5-3 10 0M125 58q5-3 10 0" stroke="#3A241B" stroke-width="1.9" stroke-linecap="round" fill="none"/>
<path d="M119 60q-2 4 1 5" stroke="#9A6240" stroke-width="1.5" stroke-linecap="round" fill="none"/>
<path d="M112 72q8-5 16 0" stroke="#7A3B2E" stroke-width="1.9" stroke-linecap="round" fill="none"/>
<path d="M137 61q3 4 0 7q-3-3 0-7z" fill="#8FC1E8"/>
</g>'''

def svg(inner, poder=ORANGE, w=240, h=240, bg=None):
    b=f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ''
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" style="--poder:{poder}">{b}\n{inner}\n</svg>\n'

def fig(aura='forca', face='feliz', modular=False):
    hide=' style="display:none"'
    if modular:
        a=AURA_FORCA.format(d='')+AURA_NORMAL.format(d=hide)
        f=FELIZ.format(d='')+TRISTE.format(d=hide)
    else:
        a=(AURA_FORCA if aura=='forca' else AURA_NORMAL).format(d='')
        f=(FELIZ if face=='feliz' else TRISTE).format(d='')
    return a+BODY.replace('FACE',f)

if __name__=='__main__':
    open('sanira_frente_forca.svg','w').write(svg(fig('forca','feliz'),ORANGE))
    open('sanira_frente_sem_forca.svg','w').write(svg(fig('normal','feliz'),'#5B8DEF'))
    open('sanira_frente_triste.svg','w').write(svg(fig('forca','triste'),ORANGE))
    open('sanira_frente_modular.svg','w').write(svg(fig(modular=True),ORANGE))
    prev=f'<g>{fig("forca","feliz")}</g>'
    # prévia 3 estados lado a lado
    parts=[(fig('forca','feliz'),ORANGE),(fig('normal','feliz'),'#5B8DEF'),(fig('forca','triste'),ORANGE)]
    inner=''.join(f'<g transform="translate({i*250+5},0)" style="--poder:{c}">{s}</g>' for i,(s,c) in enumerate(parts))
    open('sanira_frente_previa.svg','w').write(svg(inner,ORANGE,760,240,"#F5EFE3"))
    print('ok')
