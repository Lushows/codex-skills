// PageLoadStagger.jsx — entrada escalonada del hero.
// Deps: framer-motion. Uso: <PageLoadStagger/>. Requiere Tailwind.
import { motion } from "framer-motion";
const container = { hidden: {}, show: { transition: { staggerChildren: 0.12, delayChildren: 0.05 } } };
const item = { hidden: { opacity: 0, y: 24 }, show: { opacity: 1, y: 0, transition: { duration: 0.7, ease: [0.2, 0.8, 0.2, 1] } } };
export default function PageLoadStagger() {
  return (
    <motion.div variants={container} initial="hidden" animate="show" className="mx-auto max-w-2xl px-8 py-24 text-center text-zinc-100">
      <motion.h1 variants={item} className="text-5xl font-semibold tracking-tight leading-[1.05]">Movimiento con intención</motion.h1>
      <motion.p variants={item} className="mt-4 text-zinc-400">Un page-load orquestado vale más que diez microinteracciones dispersas.</motion.p>
      <motion.a variants={item} href="#" className="mt-6 inline-block rounded-full bg-emerald-300 px-6 py-3 font-semibold text-emerald-950">Empezar</motion.a>
    </motion.div>
  );
}