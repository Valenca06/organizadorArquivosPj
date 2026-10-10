from pathlib import Path

# Cria pasta isolada para testes
pasta_teste = Path.cwd() / "sandbox_teste"
pasta_teste.mkdir(exist_ok=True)

# 1. Arquivos com conteúdo duplicado
conteudo_dup1 = b"Conteudo identico do arquivo A"
(pasta_teste / "relatorio.txt").write_bytes(conteudo_dup1)
(pasta_teste / "relatorio_copia.txt").write_bytes(conteudo_dup1)
(pasta_teste / "relatorio_final_v2.txt").write_bytes(conteudo_dup1)

conteudo_dup2 = b"Dados da foto identica B"
(pasta_teste / "foto.jpg").write_bytes(conteudo_dup2)
(pasta_teste / "foto_backup.jpg").write_bytes(conteudo_dup2)

# 2. Arquivos diversos (únicos)
(pasta_teste / "documento.pdf").write_bytes(b"Conteudo PDF")
(pasta_teste / "planilha.xlsx").write_bytes(b"Conteudo Excel")
(pasta_teste / "imagem.png").write_bytes(b"Conteudo PNG")
(pasta_teste / "musica.mp3").write_bytes(b"Conteudo MP3")
(pasta_teste / "video.mp4").write_bytes(b"Conteudo MP4")
(pasta_teste / "compactado.zip").write_bytes(b"Conteudo ZIP")
(pasta_teste / "desconhecido.xyz").write_bytes(b"Extensao sem categoria")

print(f"Ambiente de teste criado em: {pasta_teste.resolve()}")
print("Copie o organizador para essa pasta para testar com segurança!")