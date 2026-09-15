// ScrollReveal.jsx — revela su contenido al entrar en viewport.
// Deps: framer-motion. Uso: <ScrollReveal><Card/></ScrollReveal>. Requiere Tailwind.
import { motion } from "framer-motion";

export default function ScrollReveal({ children, delay = 0, y = 32 }) {
  return (
    <motion.div
      initial={{ opacity: 0, y }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, margin: "-10%" }}
      transition={{ duration: 0.6, ease: [0.2, 0.8, 0.2, 1], delay }}
    >
      {children}
    </motion.div>
  );
}
