# Component resources

Where to get implementation building blocks, and when each source fits. Names only. Code always comes from the
official source at install time.

## UI foundations (use before effects)
| Resource | Use when | Notes |
|---|---|---|
| The project's own components | Always first | Extend, don't duplicate |
| shadcn/ui | React + Tailwind projects needing accessible primitives you own | Copy-in components on Radix; theme via its CSS variables |
| Radix UI / React Aria | Custom-styled accessible primitives | Headless; full keyboard/ARIA patterns |
| Headless UI | Tailwind projects, small set | |
| MUI, Chakra, Mantine | Already in the project | Style via the theme API |
| Native elements | Always viable | `<dialog>`, `<details>`, `popover` attribute, native form controls |

## Icons
Lucide · Phosphor · Heroicons · Tabler · Material Symbols · Remix Icon. Pick one per project. Real brand logos come
from the brand's press kit or Simple Icons (check the trademark terms).

## React Bits catalogue (snapshot: commit a30a9da, 2026-11-26; about 215 components)
Use the rules in `motion/react-bits-guidelines.md`. These are the components with a plausible product purpose, by
the need they serve. Everything else is decorative and needs a strong reason.

**Text, for a hero headline entrance or one emphasis moment** (pick one per page):
SplitText, BlurText, TextType, RotatingText (one rotating word, at most 3 options), ScrollReveal, ScrollFloat,
ShinyText (sparingly), CountUp (real numbers only), DecryptedText (dev or security products), VariableProximity,
TextPressure (Experience), CurvedLoop, ScrollVelocity (marquee, needs pause), FallingText, ASCIIText, GlitchText
(gaming only), GradientText (avoid: gradient text is a slop signal).

**Animations, for feedback or a signature interaction:**
AnimatedContent / FadeContent (single entrances, not every section), Magnet (one CTA), ClickSpark (playful
products), GlareHover, StarBorder / ElectricBorder (one highlighted item), LogoLoop (real logos, with pause),
ImageTrail / PixelTransition (portfolios), GradualBlur (scroll-edge fade), ScrollExpand (a media reveal moment),
cursor effects (BlobCursor, SplashCursor, TargetCursor, GhostCursor: Experience surfaces only, `aria-hidden`).

**Components, for structure and navigation:**
Dock, CardNav, StaggeredMenu, FlowingMenu, BubbleMenu, GooeyNav, PillNav (pills≠off), Stepper (real multi-step
flows), Counter, AnimatedList (real lists), Masonry (galleries), CircularGallery / DomeGallery / FlyingPosters
(Experience), Carousel / DepthCarousel (only when browsing a set is the task, no autoplay), SpotlightCard /
PixelCard / TiltedCard / ProfileCard (card effects: respect `containers`; avoid tilt by default), MagicBento
(avoid under containers=none), ModelViewer / Lanyard / FluidGlass (3D, `ambitious` only).

**Micro, for small interface details** (usually dependency-light; check each one):
SquishSwitch, SpringCheck, JellyRadio, HoldButton (destructive confirm), SlideCommit, SwipeRow, SwipeToast,
StatusMark, LatticeLoader, PeekRating, PromptBar (AI input), ElasticSlider, GlideSelect, WarmTooltip, FlipCard.
These still have to meet accessibility requirements: verify the keyboard and ARIA behaviour of each.

**Backgrounds, at most one per page, tech/software/gaming/Experience only, with a static fallback:**
Restrained: DotGrid, Grainient, Silk, Threads, SoftAurora, LineWaves, Topography, ShapeGrid, GridMotion.
Loud (needs a concept): Aurora, Galaxy, Hyperspeed, LiquidEther, Plasma, Prism, Particles, Ballpit, Iridescence,
LetterGlitch, FaultyTerminal, PixelBlast, LightRays, Beams.

The catalogue changes often. Confirm the current name and flavour at https://reactbits.dev before installing.
React Bits Pro (paid) exists. Don't recommend it unprompted.

## Real-product reference catalogues
UIZZE (uizze.com: about 800k real web and iOS screens, free search API, paid MCP). Example DESIGN.md libraries
(albemala/design-md-library: 14 category systems; brand style libraries). Use these for structural lessons, not copying.
